"""Exercise the documented local Git path in a disposable repo; no remote/model needed."""
from pathlib import Path
import subprocess
import tempfile


def git(cwd, *args):
    return subprocess.run(['git', '-C', str(cwd), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


with tempfile.TemporaryDirectory(prefix='lever-local-') as tmp:
    root = Path(tmp)
    repo = root / 'project'
    repo.mkdir()
    git(repo, 'init', '-b', 'main')
    git(repo, 'config', 'user.name', 'Local smoke test')
    git(repo, 'config', 'user.email', 'test@example.invalid')
    source = repo / 'value.txt'
    source.write_text('baseline\n')
    git(repo, 'add', 'value.txt')
    git(repo, 'commit', '-m', 'baseline')
    base = git(repo, 'rev-parse', 'HEAD')
    candidate = root / 'candidate'
    git(repo, 'worktree', 'add', '-b', 'lever/test', str(candidate), base)
    # A worker writes only in its assigned worktree.
    (candidate / 'value.txt').write_text('candidate\n')
    assert source.read_text() == 'baseline\n'
    assert git(repo, 'status', '--porcelain') == ''
    git(candidate, 'add', 'value.txt')
    git(candidate, 'commit', '-m', 'candidate')
    head = git(candidate, 'rev-parse', 'HEAD')
    git(repo, 'cherry-pick', head)
    assert source.read_text() == 'candidate\n'
    # HEAD alone must not stand for dirty state, and isolation omits dirty inputs.
    source.write_text('user edit\n')
    (repo / 'untracked.txt').write_text('user untracked work\n')
    status = git(repo, 'status', '--porcelain')
    assert 'value.txt' in status and '?? untracked.txt' in status
    assert (candidate / 'value.txt').read_text() == 'candidate\n'
    assert not (candidate / 'untracked.txt').exists()
    # Only remove the clean worktree created by this test, never force cleanup.
    assert git(candidate, 'status', '--porcelain') == ''
    git(repo, 'worktree', 'remove', str(candidate))
    assert source.read_text() == 'user edit\n'
    assert (repo / 'untracked.txt').read_text() == 'user untracked work\n'
    assert git(repo, 'remote') == ''
    print('PASS: isolated local worktree, commit integration, dirty/untracked preservation, clean cleanup; no remote')
