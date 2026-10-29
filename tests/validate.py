"""Structural checks only; these do not prove model compliance."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
catalog_path = root / '.agents/plugins/marketplace.json'
assert catalog_path.is_file(), 'Missing installable plugin marketplace'
catalog = json.loads(catalog_path.read_text())
assert catalog['name'] == 'universal-lever'
assert len(catalog['plugins']) == 1
listing = catalog['plugins'][0]
assert listing['name'] == 'universal-lever'
assert listing['policy'] == {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}
source = listing['source']
assert source['source'] == 'local'
assert source['path'].startswith('./') and '..' not in Path(source['path']).parts
plugin = (root / source['path']).resolve()
assert plugin.is_relative_to(root) and plugin.is_dir()
manifest = json.loads((plugin / 'plugin.json').read_text())
compatibility = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
assert manifest['name'] == compatibility['name'] == listing['name']
assert manifest['version'] == compatibility['version']
assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
assert compatibility['skills'] == './skills/'
assert manifest['license'] == 'MIT'
assert manifest['extensions']['com.openai']['interface'] == compatibility['interface']
assert manifest['extensions']['com.openai']['requires_local_executor'] is True
assert compatibility['requires_local_executor'] is True
assert (plugin / 'LICENSE').read_bytes() == (root / 'LICENSE').read_bytes()
skill = plugin / 'skills/universal-lever'
assert list(plugin.glob('skills/*/SKILL.md')) == [skill / 'SKILL.md']
entry = (skill / 'SKILL.md').read_text()
assert entry.startswith('---\nname: universal-lever\ndescription: Use when ')
assert len(entry.split('---', 2)[1]) < 1024
assert len(entry.split()) < 1500
checked = 0
for path in skill.rglob('*.md'):
    body = path.read_text()
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
        assert not re.match(r'https?://', target), (path, target)
        assert (path.parent / target.split('#')[0]).is_file(), (path, target)
        assert (path.parent / target.split('#')[0]).resolve().is_relative_to(plugin)
        checked += 1
    for forbidden in ['gh pr ', 'github/', '~/.copilot', 'create_automation', 'copilot plugin']:
        assert forbidden not in body, (path, forbidden)
for phrase in ['inconclusive', 'A/A', 'ACTED', 'NOOP', 'BLOCKED', 'authority']:
    assert phrase in entry, phrase
assert (root / 'LICENSE').read_text().startswith('MIT License')
for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', (root / 'README.md').read_text()):
    if not target.startswith(('https://', '#')):
        assert (root / target).exists(), target
print(f'PASS: marketplace resolution, manifests, one skill, {checked} self-contained links, portable contracts and MIT license')
