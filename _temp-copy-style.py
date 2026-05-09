from pathlib import Path
source = Path('assets/style.css')
if source.exists():
    dest = Path('style.css')
    dest.write_text(source.read_text(encoding='utf-8'), encoding='utf-8')
    print('Copied style.css to root')
else:
    print('Source style.css not found')
