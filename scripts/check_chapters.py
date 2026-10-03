"""Validate repository-readable chapters and local links. No network required."""
from pathlib import Path
from html.parser import HTMLParser
import argparse
import re

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--all',action='store_true',help='Check all authored material')
parser.add_argument('files',nargs='*')
args=parser.parse_args()
files=[root/p for p in args.files] if args.files else [*sorted(root.glob('README*.md')),*sorted((root/'course-material').rglob('*.md')),*sorted((root/'community').rglob('*.md'))]
files=[p for p in files if p.name!='WRITING_TEMPLATE.md']
errors=[];links=0;chapter_count=0
class AssetParser(HTMLParser):
    def __init__(self):super().__init__();self.targets=[];self.bad_alt=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='img':
            if not a.get('alt','').strip():self.bad_alt=True
            if a.get('src'):self.targets.append(a['src'])
        if tag=='a' and a.get('href'):self.targets.append(a['href'])
for p in files:
    content=p.read_text()
    if content.count('```')%2:errors.append(f'{p.name}: unbalanced fences')
    clean=re.sub(r'```[\s\S]*?```','',content)
    clean=re.sub(r'\$\$[\s\S]*?\$\$','',clean)
    clean=re.sub(r'\$[^$\n]*\$','',clean)
    assets=AssetParser();assets.feed(clean)
    targets=re.findall(r'\]\(([^)]+)\)',clean)+assets.targets
    for target in targets:
        if '://' in target or target.startswith('#'):continue
        links+=1
        if not (p.parent/target.split('#')[0]).exists():errors.append(f'{p.name}: missing {target}')
    if p.name.startswith('Chapter'):
        chapter_count+=1
        if len(re.findall(r'^# ',clean,re.M))!=1:errors.append(f'{p.name}: expected one H1')
        english = 'eng' in p.relative_to(root).parts
        markers = ['## 1. Learning Objectives', '## References and Further Reading'] if english else ['## 1. Чему вы научитесь','## Источники и дальнейшее чтение']
        for marker in markers:
            if marker not in content:errors.append(f'{p.name}: missing {marker}')
        summary = r'^## \d+\. Summary and Exercises' if english else r'^## \d+\. Итоги и задачи'
        if not re.search(summary,content,re.M):errors.append(f'{p.name}: missing exercises')
        numbers=[int(x) for x in re.findall(r'^## (\d+)\.',content,re.M)]
        if numbers!=list(range(1,len(numbers)+1)):errors.append(f'{p.name}: non-sequential H2 numbering')
        if '<BindingExplorer' in content or '<ClientOnly' in content:errors.append(f'{p.name}: frontend-only content')
        if assets.bad_alt:errors.append(f'{p.name}: image missing alt text')
        if p.parent.name=='part1' and '<img ' not in content:errors.append(f'{p.name}: no reference-style figure')
if errors:raise SystemExit('\n'.join(errors))
print(f'Checked {chapter_count} chapters and {links} local links; static Markdown structure OK.')
