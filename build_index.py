# Kleiner Helfer, um einen „schönen“ Index auf GitHub Pages zu generieren.

import pathlib

cwd = pathlib.Path.cwd()

md_files = sorted(file.relative_to(cwd) for file in cwd.rglob('*.md'))
md_files = [str(f).replace(".tex.md", "") for f in md_files]
md_files = [f for f in md_files if not f.startswith('gh-pages-bundle/')]


out = ''
out += '# Altklausuren\n\n'
out += '\n'.join([f'- [{x}]({x})' for x in md_files])

print(out)
