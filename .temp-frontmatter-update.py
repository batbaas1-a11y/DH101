from pathlib import Path

rules = []
for path in Path('makes').glob('*.md'):
    if path.name in ['index.md']:
        continue
    rules.append((path, 'make'))
for path in Path('reflections').glob('*.md'):
    rules.append((path, 'default'))

for path, layout in rules:
    text = path.read_text(encoding='utf-8')
    if text.startswith('---'):
        continue
    front = f"---\ntitle: {path.stem.replace('-', ' ').title()}\nlayout: {layout}\n---\n\n"
    path.write_text(front + text, encoding='utf-8')
    print(f'Updated {path}')
