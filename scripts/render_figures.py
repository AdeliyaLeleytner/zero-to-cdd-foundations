# /// script
# requires-python = ">=3.11,<3.14"
# dependencies = ["matplotlib==3.11.2", "rdkit==2026.3.6"]
# ///
"""Original teaching figures. Curves are analytic models, not measurements.

Run: uv run --no-project scripts/render_figures.py
No external molecule or experimental dataset is downloaded.
"""
from pathlib import Path
import html
import json
import math
import re
import sys
import argparse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from rdkit import Chem, rdBase
from rdkit.Chem.Draw import rdMolDraw2D

ROOT = Path(__file__).resolve().parents[1]
LANGUAGE = 'ru'
EN_LABELS = json.loads((ROOT/'scripts/figure_labels_en.json').read_text())
OUT = ROOT/'course-material/ru/part1/images'
OUT.mkdir(parents=True, exist_ok=True)
TEAL, INK, MUTED, ORANGE = '#187b73', '#243746', '#586b7a', '#b96a35'


def tr(value):
    if LANGUAGE == 'eng':
        if re.search('[А-Яа-яЁё]', value) and value not in EN_LABELS:
            raise ValueError(f'Missing English figure label: {value}')
        return EN_LABELS.get(value, value)
    return value


def text(x,y,value,size=22,color=INK,anchor='middle',weight='400'):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{html.escape(tr(value))}</text>'


def box(x,y,w,h,title,detail):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#f0f6f5" stroke="#c9ddda"/>'
        +text(x+w/2,y+34,title,23,TEAL,weight='600')+text(x+w/2,y+65,detail,17,MUTED))


def arrow(x1,y1,x2,y2,dashed=False):
    return f'<path d="M{x1},{y1} L{x2},{y2}" fill="none" stroke="{MUTED}" stroke-width="2" marker-end="url(#arrow)" '+('stroke-dasharray="6 5"' if dashed else '')+'/>'


def save_svg(name,body,height,title):
    source=f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img">
<title>{html.escape(tr(title))}</title>
<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8" fill="{MUTED}"/></marker></defs>
<rect width="760" height="{height}" rx="12" fill="white"/>{body}</svg>'''
    (OUT/name).write_text(source)


def schematics():
    stages=[('Вещество в среде','Где находится молекула?'),('Доступ к мишени','Какая концентрация доступна?'),('Взаимодействие','Образуется ли комплекс?'),('Изменение функции','Что меняется в работе системы?')]
    body=''
    for i,(title,detail) in enumerate(stages):
        y=24+i*120
        body+=box(110,y,540,90,title,detail)
        if i<3:body+=arrow(380,y+94,380,y+113)
    save_svg('01-effect-chain.svg',body,494,'От вещества к изменению функции')

    body=box(40,35,300,90,'Гипотеза','Какое изменение нужно?')
    body+=box(420,35,300,90,'Молекулы','Что проверим?')
    body+=box(420,205,300,90,'Эксперимент','Что наблюдаем?')
    body+=box(40,205,300,90,'Объяснение','Что мы узнали?')
    body+=arrow(348,80,408,80)+arrow(570,135,570,194)+arrow(410,250,350,250)+arrow(190,196,190,136,True)
    body+=text(380,354,'Следующий раунд может изменить и молекулу, и гипотезу.',19,MUTED)
    save_svg('01-discovery-cycle.svg',body,390,'Итеративная логика drug discovery')

    body=text(380,42,'Химическая цепь → набор состояний → функция',24,TEAL,weight='600')
    body+=box(100,75,560,86,'Последовательность','… A — G — S — K — L — …')
    body+=arrow(380,169,380,198)
    # Stylized states are deliberately abstract, not claimed protein coordinates.
    body+='<path d="M160 255 C90 195 255 185 235 263 C210 337 107 286 174 245 C246 209 255 328 160 306" fill="none" stroke="#187b73" stroke-width="9" stroke-linecap="round"/>'
    body+='<path d="M545 215 C628 208 655 279 596 300 C530 333 495 281 555 263 C614 242 644 339 541 334" fill="none" stroke="#6d8493" stroke-width="9" stroke-linecap="round"/>'
    body+=arrow(300,262,455,262)+arrow(455,280,300,280)
    body+=text(190,363,'Состояние 1',21)+text(570,363,'Состояние 2',21)
    body+=text(380,404,'Вероятности зависят от среды и партнёров.',19,MUTED)
    body+=arrow(380,420,380,449)
    body+=box(100,462,560,90,'Функция','Реакция, сигнал, транспорт или другая работа')
    save_svg('03-sequence-function.svg',body,575,'Белок как система пространственных состояний')


def molecules():
    groups=[
      ('Одинаковый состав · разная связность',[('CCO','Этанол'),('COC','Диметиловый эфир')]),
      ('Одинаковая связность · разная конфигурация',[('C[C@H](O)C(=O)O','Энантиомер 1'),('C[C@@H](O)C(=O)O','Энантиомер 2')]),
      ('Протонирование · меняется заряд',[('CC(=O)O','Уксусная кислота'),('CC(=O)[O-]','Ацетат')])
    ]
    body=''; manifest=[]
    for row,(title,pairs) in enumerate(groups):
        base=20+row*225
        body+=text(380,base+22,title,21,TEAL,weight='600')
        if row:body+=f'<line x1="40" x2="720" y1="{base-15}" y2="{base-15}" stroke="#dce5e8"/>'
        for col,(smiles,label) in enumerate(pairs):
            mol=Chem.MolFromSmiles(smiles)
            assert mol is not None
            draw=rdMolDraw2D.MolDraw2DSVG(310,135)
            draw.drawOptions().padding=.12
            rdMolDraw2D.PrepareAndDrawMolecule(draw,mol)
            draw.FinishDrawing()
            svg=draw.GetDrawingText()
            inner=re.search(r'<svg[\s\S]*?>([\s\S]*)</svg>',svg).group(1)
            body+=f'<g transform="translate({45+360*col},{base+38})">{inner}</g>'
            body+=text(200+360*col,base+199,label,19)
            manifest.append({'smiles':smiles,'label':tr(label)})
    save_svg('02-molecular-changes.svg',body,705,'Три разных типа изменений молекулы')
    return manifest


def conformers():
    body=text(380,40,'Бутан: взгляд вдоль центральной связи C–C',23,TEAL,weight='600')
    for cx,rotation,title in [(205,180,'anti · 180°'),(555,60,'gauche · 60°')]:
        cy=192
        body+=f'<circle cx="{cx}" cy="{cy}" r="38" fill="none" stroke="#7b8c98" stroke-width="2.5"/>'
        # Front methyl at -90 degrees; back methyl differs by the dihedral.
        for back in [True,False]:
            offset=rotation if back else 0
            for i,angle in enumerate([-90+offset,30+offset,150+offset]):
                a=math.radians(angle)
                r1=38 if back else 0
                x1,y1=cx+r1*math.cos(a),cy+r1*math.sin(a)
                x2,y2=cx+86*math.cos(a),cy+86*math.sin(a)
                color='#7b8c98' if back else INK
                body+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="3"/>'
                body+=text(cx+112*math.cos(a),cy+112*math.sin(a)+7,'CH₃' if i==0 else 'H',23,color)
        body+=f'<circle cx="{cx}" cy="{cy}" r="6" fill="{INK}"/>'
        body+=text(cx,354,title,22,TEAL,weight='600')
    body+=text(380,400,'Связность и состав сохраняются. Меняется внутренний поворот.',18,MUTED)
    save_svg('02-conformers.svg',body,430,'Конформации бутана: anti и gauche')


def curves():
    plt.rcParams.update({'font.family':'sans-serif','font.sans-serif':['Arial','DejaVu Sans','Helvetica'],'font.size':12,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':INK,'text.color':INK,'xtick.color':MUTED,'ytick.color':MUTED,'svg.fonttype':'none','svg.hashsalt':'cdd-foundations-v1','axes.grid':True,'grid.alpha':.17})
    concentrations=[10**(-1+i*5/300) for i in range(301)]
    fig,ax=plt.subplots(figsize=(7.6,4.4),layout='constrained')
    for kd,color,style in [(1,TEAL,'-'),(10,'#416a96','--'),(100,ORANGE,'-.')]:
        ax.plot(concentrations,[l/(kd+l) for l in concentrations],color=color,lw=2.4,ls=style,label=f'Kd = {kd} nM')
        ax.scatter([kd],[.5],s=30,color=color,zorder=3)
    ax.set(xscale='log',xlabel=tr('Свободный лиганд [L], nM'),ylabel=tr('Доля занятого белка, θ'),ylim=(0,1.03),xlim=(.1,10000))
    ax.legend(frameon=False,loc='lower right')
    fig.savefig(OUT/'04-occupancy.svg',metadata={'Date':None,'Description':'Analytic educational model, no measurements.'})
    fig.savefig(OUT/'04-occupancy.png',dpi=160)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(7.6,4.4),layout='constrained')
    times=list(range(0,1501,5))
    for koff,color,style in [(.01,TEAL,'-'),(.001,ORANGE,'--')]:
        ax.plot(times,[math.exp(-koff*t) for t in times],color=color,lw=2.4,ls=style,label=f'koff = {koff:g} 1/s; τ = {1/koff:g} s')
    ax.set(xlabel=tr('Время после удаления лиганда, s'),ylabel=tr('Доля исходных комплексов'),xlim=(0,1500),ylim=(0,1.03))
    ax.legend(frameon=False)
    fig.savefig(OUT/'04-kinetics.svg',metadata={'Date':None,'Description':'Analytic dissociation without rebinding; educational parameters.'})
    fig.savefig(OUT/'04-kinetics.png',dpi=160)
    plt.close(fig)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', choices=['ru', 'eng', 'all'], default='ru')
    args = parser.parse_args()
    for LANGUAGE in (['ru', 'eng'] if args.language == 'all' else [args.language]):
        OUT = ROOT / 'course-material' / LANGUAGE / 'part1/images'
        OUT.mkdir(parents=True, exist_ok=True)
        schematics(); molecules_manifest=molecules(); conformers(); curves()
        (OUT/'provenance.json').write_text(json.dumps({'kind':'original teaching figures','language':LANGUAGE,'rdkit':rdBase.rdkitVersion,'matplotlib':matplotlib.__version__,'molecules':molecules_manifest,'occupancy':{'model':'L/(Kd+L)','kd_nM':[1,10,100],'data_type':'analytical, hypothetical parameters'},'kinetics':{'model':'exp(-koff*t)','koff_per_s':[.01,.001],'data_type':'analytical, no rebinding'}},ensure_ascii=False,indent=2)+'\n')
        for svg_path in OUT.glob('*.svg'):
            svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
        print('Rendered 7 original SVG figures and 2 PNG previews.')
