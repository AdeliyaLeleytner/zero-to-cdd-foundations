"""Check scientific invariants and completeness of the two current editions."""
from pathlib import Path
import re
import json

root=Path(__file__).resolve().parents[1]
errors=[];pairs=0

def math_fragments(text):
    return [re.sub(r'\s+','',a or b) for a,b in re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',text)]

def no_code(text):return re.sub(r'```[\s\S]*?```','',text)

def headings(text):
    return re.findall(r'^(#{1,3}) (?:(?:Глава|Chapter) )?(\d+(?:\.\d+)?)',no_code(text),re.M)

for ru in sorted((root/'course-material/ru').rglob('*.md')):
    eng=root/'course-material/eng'/ru.relative_to(root/'course-material/ru')
    if not eng.exists():errors.append(f'Missing English file: {eng.relative_to(root)}');continue
    if not ru.name.startswith('Chapter'):continue
    pairs+=1
    a,b=ru.read_text(),eng.read_text()
    if headings(a)!=headings(b):errors.append(f'{eng.name}: section numbering differs')
    if math_fragments(a)!=math_fragments(b):errors.append(f'{eng.name}: mathematical expressions differ')
    for name,pattern in [('exercises',r'^(\d+)\. '),('figures',r'<img src="([^"]+)"')]:
        if re.findall(pattern,no_code(a),re.M)!=re.findall(pattern,no_code(b),re.M):errors.append(f'{eng.name}: {name} differ')
    urls=lambda s:re.findall(r'https?://[^\s>)]+',s)
    if urls(a)!=urls(b):errors.append(f'{eng.name}: external references differ')
    if a.count('★')!=b.count('★'):errors.append(f'{eng.name}: extension exercises differ')

for folder in [root/'course-material/eng',root/'community/eng']:
    for p in folder.rglob('*'):
        if p.suffix not in ['.md','.svg','.py','.json']:continue
        text=p.read_text().replace('Русский','')
        if re.search('[А-Яа-яЁё]',text):errors.append(f'{p.relative_to(root)}: untranslated Cyrillic text')
        if p.suffix=='.md' and re.search(r'\]\([^)]*(?:course-material|community)/ru/',text):errors.append(f'{p.relative_to(root)}: link to Russian instructional material')

ru_figures=json.loads((root/'course-material/ru/part1/images/provenance.json').read_text())
eng_figures=json.loads((root/'course-material/eng/part1/images/provenance.json').read_text())
for key in ['occupancy','kinetics']:
    if ru_figures[key]!=eng_figures[key]:errors.append(f'Figure parameters differ: {key}')
if [m['smiles'] for m in ru_figures['molecules']] != [m['smiles'] for m in eng_figures['molecules']]:
    errors.append('Molecular drawings use different SMILES')
ru_answers=(root/'community/ru/Exercise-Discussions.md').read_text()
eng_answers=(root/'community/eng/Exercise-Discussions.md').read_text()
if math_fragments(ru_answers)!=math_fragments(eng_answers):errors.append('Exercise-discussion equations differ')

readme=(root/'README.md').read_text()
if re.search(r'\]\((?:course-material|community)/ru/',readme):errors.append('English README points to Russian lessons')

if errors:raise SystemExit('\n'.join(errors))
print(f'{pairs} chapter pairs match in sections, equations, exercise numbering, figures and external references.')
print('English text, diagrams and Python output contain no untranslated Russian; English README routes to English lessons.')
