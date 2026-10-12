"""Compact manuscript figures guided by four user-provided reference papers.
All numbers are frozen observations; no model execution or statistical testing.
Every execution requires a new --attempt name; existing artifacts are never replaced.
"""
import sys, argparse, json, hashlib, io
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle, FancyArrowPatch, Patch
from PIL import Image
from layout_check import require_matplotlib_panel_alignment
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'data/figures/plot_data_frozen.json'
CASE_SOURCE=ROOT/'data/evidence/E05_real_case_two_positions.json'
D=json.loads(SOURCE.read_text(encoding='utf8'));CASE=json.loads(CASE_SOURCE.read_text(encoding='utf8'))
Q=D['figure2']['query_rows'];assert len(Q)==175 and sum(q['same_context'] for q in Q)==54
assert CASE['old_paired_difference']==.1 and CASE['restored_paired_difference']==0
F03=[a for a in CASE['aspects'] if a['support']=='supported'];assert len(F03)==1
assert F03[0]['weight']==.2 and F03[0]['restored_completion']==.5 and F03[0]['old_completion'] is None
from matplotlib import font_manager
CHART_FONT='Arial' if any(f.name=='Arial' for f in font_manager.fontManager.ttflist) else 'DejaVu Sans'
BLUE='#315B75';BLACK='#202020';GRAY='#777777';LIGHT='#D7D7D7';OLD='#777777'
WIDTH_MM=180
plt.rcParams.update({'font.family':CHART_FONT,'font.size':9,'axes.labelsize':9,'axes.linewidth':.7,
 'xtick.labelsize':8,'ytick.labelsize':8,'text.color':BLACK,'axes.labelcolor':BLACK,
 'svg.fonttype':'none','pdf.fonttype':42,'ps.fonttype':42,'savefig.facecolor':'white',
 'figure.facecolor':'white','lines.linewidth':.8})
def text(ax,x,y,s,size=9,ha='center',va='center',weight='normal',color=BLACK):
    return ax.text(x,y,s,transform=ax.transAxes,fontsize=size,ha=ha,va=va,fontweight=weight,color=color,linespacing=1.18)
def panel(ax,letter,title):
    off=11/(ax.figure.get_figwidth()*72*ax.get_position().width)
    y=1+8/(ax.figure.get_figheight()*72*ax.get_position().height)
    text(ax,-off,y,letter,ha='left',va='bottom',weight='bold',size=9)
    text(ax,0,y,title,ha='left',va='bottom',size=9)
    ax.spines[['top','right']].set_visible(False);ax.tick_params(length=3,width=.6)
def blank(ax):ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(ax,x,y,w,h,label,color=BLACK):
    ax.add_patch(Rectangle((x,y),w,h,fill=False,edgecolor=color,lw=.7,transform=ax.transAxes))
    text(ax,x+w/2,y+h/2,label,color=color)
def arrow(ax,start,end,dashed=False):
    ax.add_patch(FancyArrowPatch(start,end,transform=ax.transAxes,arrowstyle='->',mutation_scale=8,lw=.7,
        color=BLACK,linestyle='--' if dashed else '-'))
def save(fig,stem,out,qa):
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig,json_out=qa/(stem+'_alignment.json'),overlay_svg=qa/(stem+'_alignment.svg'),
        tolerance_pt=1.5,gutter_tolerance_pt=1.5,require_panel_labels=True,strict=True)
    for ext in ['.pdf','.svg','.png']:
        p=out/(stem+ext);assert not p.exists()
        fig.savefig(p,dpi=300,bbox_inches=None)
    buffer=io.BytesIO();fig.savefig(buffer,format='png',dpi=600,bbox_inches=None);buffer.seek(0)
    with Image.open(buffer) as im:im.convert('RGB').save(out/(stem+'.tiff'),compression='tiff_lzw',dpi=(600,600))
    plt.close(fig)

def figure1(out,qa):
    fig=plt.figure(figsize=(WIDTH_MM/25.4,100/25.4))
    gs=fig.add_gridspec(3,1,left=.065,right=.98,bottom=.06,top=.90,hspace=.72,height_ratios=[1,1.35,.65])
    a,b,c=[fig.add_subplot(gs[i]) for i in range(3)]
    for ax in [a,b,c]:blank(ax)
    panel(a,'a','Content objects')
    labels=['Query','Candidate\ndocs','Selected\nfragments','Input C','Answer A','Claims']
    xs=[i*.173 for i in range(6)]
    for x,label in zip(xs,labels):box(a,x,.25,.133,.58,label,BLUE if label in ['Input C','Answer A'] else BLACK)
    for x in xs[:-1]:arrow(a,(x+.136,.54),(x+.170,.54))
    panel(b,'b','Measurement records')
    box(b,0,.60,.36,.30,'Content owner');box(b,0,.05,.36,.30,'Query × condition')
    box(b,.66,.32,.34,.30,'Evaluation record',BLUE)
    arrow(b,(.37,.75),(.65,.53),True);arrow(b,(.37,.20),(.65,.41))
    text(b,.51,.84,'Reuse',size=8.5);text(b,.51,.12,'Association',size=8.5)
    panel(c,'c','Evaluation relations')
    for x,title,relation in [(1/6,'Fidelity (F)','A ↔ claim'),(.5,'Support (S)','C ↔ claim'),(5/6,'Coverage','A ↔ aspect')]:
        text(c,x,.69,title,weight='bold');text(c,x,.27,relation)
    save(fig,'Figure_1_Provenance',out,qa)

def figure2(out,qa):
    fig=plt.figure(figsize=(WIDTH_MM/25.4,118/25.4))
    gs=fig.add_gridspec(2,2,left=.10,right=.97,bottom=.07,top=.86,wspace=.35,hspace=.90,height_ratios=[1,.30])
    a=fig.add_subplot(gs[0,0]);b=fig.add_subplot(gs[0,1]);c=fig.add_subplot(gs[1,:])
    panel(a,'a','Corrected Δa3')
    a.axhline(0,color=LIGHT,lw=.6,zorder=0);a.axvline(0,color=LIGHT,lw=.6,zorder=0)
    a.plot([-.65,1.05],[-.65,1.05],color='#AAAAAA',ls='--',lw=.7,zorder=0)
    for same,col,m in [(False,BLUE,'o'),(True,OLD,'s')]:
        rows=[q for q in Q if bool(q['same_context'])==same]
        a.scatter([q['delta_original_a3'] for q in rows],[q['delta_repaired_a3'] for q in rows],s=16,c=col,marker=m,
                  alpha=.65,edgecolors='white',linewidths=.25,zorder=3)
    a.set(xlim=(-.65,1.05),ylim=(-.65,1.05),xlabel='Original Δa3')
    a.set_xticks([-.5,0,.5,1]);a.set_yticks([-.5,0,.5,1])
    a.legend(handles=[Line2D([],[],color=BLUE,marker='o',ls='',label='Different C'),Line2D([],[],color=OLD,marker='s',ls='',label='Same C')],
        loc='upper left',bbox_to_anchor=(-.04,-.28),ncol=2,frameon=False,fontsize=8,handletextpad=.25,columnspacing=1)
    panel(b,'b','Group means')
    for y,sample,label in zip([2,1,0],['all_175','same_context_54','changed_context_121'],['All (175)','Same C (54)','Different C (121)']):
        old=next(r['delta_a3'] for r in D['figure2']['summaries'] if r['sample']==sample and r['version']=='original_a3')
        new=next(r['delta_a3'] for r in D['figure2']['summaries'] if r['sample']==sample and r['version']=='repaired_a3')
        b.plot([old,new],[y,y],c='#AAAAAA',lw=.8,zorder=1);b.scatter(old,y,s=25,c=OLD,marker='s',zorder=2);b.scatter(new,y,s=25,c=BLUE,zorder=3)
        b.text(.001,y+.29,label,fontsize=8.2)
        b.text(.177,y-.25,f'{old:+.4f} → {new:+.4f}',fontsize=7.8,ha='right',va='center')
    b.axvline(0,color=LIGHT,lw=.6,zorder=0);b.set(xlim=(-.025,.18),ylim=(-.5,2.7),xlabel='Mean Δa3')
    b.set_yticks([]);b.set_xticks([0,.05,.1,.15]);b.spines['left'].set_visible(False)
    b.legend(handles=[Line2D([],[],color=OLD,marker='s',ls='',label='Original'),Line2D([],[],color=BLUE,marker='o',ls='',label='Corrected')],
        loc='upper left',bbox_to_anchor=(-.04,-.28),ncol=2,frameon=False,fontsize=8,handletextpad=.25,columnspacing=1)
    blank(c);panel(c,'c','Record attribution')
    for x,s in [(0,'Shared payload'),(.38,'Missing completion'),(.83,'a3 = 1*')]:text(c,x,.82,s,ha='left',size=9)
    arrow(c,(.24,.82),(.34,.82));arrow(c,(.70,.82),(.80,.82))
    text(c,0,.15,'38/700 positions: 37 Selection + 1 Hybrid',ha='left',size=8.5)
    save(fig,'Figure_2_Correction',out,qa)

def figure3(out,qa):
    fig=plt.figure(figsize=(WIDTH_MM/25.4,90/25.4))
    gs=fig.add_gridspec(2,1,left=.065,right=.98,bottom=.08,top=.88,hspace=.56,height_ratios=[.67,1])
    a,b=[fig.add_subplot(gs[i]) for i in range(2)]
    for ax in [a,b]:blank(ax)
    panel(a,'a','Shared objects')
    for x,label,key in [(1/6,'Context C','actual_context_sha256'),(.5,'Answer A','answer_sha256'),(5/6,'Payload','quality_payload_sha256')]:
        text(a,x,.85,label,size=8.5);text(a,x,.56,CASE[key][:12],size=8.5,color=BLUE)
    text(a,.18,.10,'Hybrid',weight='bold');text(a,.82,.10,'Selection',weight='bold')
    arrow(a,(.65,.10),(.35,.10),True);text(a,.5,.26,'shared_with',size=8)
    panel(b,'b','Position-level scoring')
    cols=[0,.40,.64,.86]
    for x,s in zip(cols,['Position','Completion','a3','Contribution']):text(b,x,.94,s,ha='left' if x==0 else 'center',weight='bold',size=8.5)
    b.plot([0,1],[.82,.82],lw=.7,c=BLACK,transform=b.transAxes)
    rows=[('Hybrid','0.5','0.5','0.2 × 0.5 = 0.10'),('Selection: old','NULL → 1','1.0','0.2 × 1.0 = 0.20'),('Selection: corrected','0.5','0.5','0.2 × 0.5 = 0.10')]
    for y,row in zip([.69,.45,.21],rows):
        for x,s in zip(cols,row):text(b,x,y,s,ha='left' if x==0 else 'center',size=8.5)
        b.plot([0,1],[y-.11,y-.11],lw=.45,c='#AAAAAA',transform=b.transAxes)
    text(b,.5,-.10,'Selection − Hybrid: +0.10 → 0.00',size=9,weight='bold')
    save(fig,'Figure_3_Real_Case',out,qa)

def figure4(out,qa):
    fig=plt.figure(figsize=(WIDTH_MM/25.4,100/25.4))
    gs=fig.add_gridspec(2,1,left=.10,right=.97,bottom=.08,top=.85,hspace=.86,height_ratios=[1,.7])
    a,b=[fig.add_subplot(gs[i]) for i in range(2)]
    panel(a,'a','Legacy aspect labels')
    left=0
    for count,col in [(77,BLUE),(33,GRAY),(86,LIGHT)]:
        w=count/196*100;a.barh(1,w,left=left,height=.35,color=col,edgecolor='white',lw=1)
        a.text(left+w/2,1,str(count),ha='center',va='center',fontsize=9,color=BLACK if col==LIGHT else 'white');left+=w
    a.barh(0,70,height=.35,color=BLUE);a.barh(0,30,left=70,height=.35,color=GRAY,edgecolor='white',lw=1)
    a.text(35,0,'77 (70%)',ha='center',va='center',color='white',fontsize=9);a.text(85,0,'33',ha='center',va='center',color='white',fontsize=9)
    a.text(0,1.34,'All records (n = 196)',fontsize=8.5);a.text(0,.34,'Old unsupported (n = 110)',fontsize=8.5)
    a.set(xlim=(0,100),ylim=(-.42,1.62),xlabel='Share (%)');a.set_yticks([]);a.set_xticks([0,25,50,75,100]);a.spines['left'].set_visible(False)
    fig.legend(handles=[Patch(facecolor=BLUE,label='Omitted'),Patch(facecolor=GRAY,label='Other unsupported'),Patch(facecolor=LIGHT,label='Other labels')],
        loc='upper center',bbox_to_anchor=(.54,.995),ncol=3,frameon=False,fontsize=8,columnspacing=1.5,handlelength=1)
    blank(b);panel(b,'b','Reference reconstruction')
    b.plot([0,1],[.94,.94],lw=.6,c=BLACK,transform=b.transAxes)
    for y,label,n in [(.78,'Nonempty records',119),(.47,'Fixed excerpts',91),(.16,'Matched natural-F reference',0)]:
        text(b,.02,y,label,ha='left',size=9);text(b,.88,y,str(n),ha='right',size=9,color=BLUE)
    b.plot([0,1],[.00,.00],lw=.6,c=BLACK,transform=b.transAxes)
    save(fig,'Figure_4_Reference_Migration',out,qa)

def figure5(out,qa):
    fig=plt.figure(figsize=(WIDTH_MM/25.4,112/25.4))
    gs=fig.add_gridspec(3,1,left=.13,right=.97,bottom=.18,top=.90,hspace=.75)
    axes=[fig.add_subplot(gs[i]) for i in range(3)]
    specs=[('a','Reference-positive (n = 6)',[(6,0,0),(6,0,0)]),('b','Reference-negative (n = 26)',[(7,19,0),(11,8,7)]),('c','All groups (n = 32)',[(13,19,0),(17,8,7)])]
    for i,(ax,(letter,title,bars)) in enumerate(zip(axes,specs)):
        panel(ax,letter,title)
        for y,counts in zip([1,0],bars):
            n=sum(counts);left=0
            for count,col in zip(counts,[BLUE,GRAY,LIGHT]):
                if not count:continue
                w=count/n*100;ax.barh(y,w,left=left,height=.45,color=col,edgecolor='white',lw=.8)
                ax.text(left+w/2,y,('U: '+str(count)) if col==LIGHT else str(count),ha='center',va='center',fontsize=8.5,color=BLACK if col==LIGHT else 'white');left+=w
        ax.set(xlim=(0,100),ylim=(-.5,1.5));ax.set_yticks([1,0],['Split','Joint']);ax.spines['left'].set_visible(False)
        ax.set_xticks([0,25,50,75,100])
        if i==2:ax.set_xlabel('Share (%)')
    fig.legend(handles=[Patch(facecolor=BLUE,label='Correct'),Patch(facecolor=GRAY,label='Incorrect'),Patch(facecolor=LIGHT,label='Unknown (U)')],
        loc='lower center',bbox_to_anchor=(.54,.01),ncol=3,frameon=False,fontsize=8.5,handlelength=1.2,columnspacing=2)
    save(fig,'Figure_5_RAGTruth_Coverage',out,qa)

def figures1(out,qa):
    fig=plt.figure(figsize=(WIDTH_MM/25.4,120/25.4))
    gs=fig.add_gridspec(3,1,left=.25,right=.96,bottom=.12,top=.90,hspace=.85)
    a,b,c=[fig.add_subplot(gs[i]) for i in range(3)]
    panel(a,'a','Ranking reversals')
    counts=[r['reversals'] for r in D['figureS1']['association_comparisons']]
    a.barh([2,1,0],counts,height=.48,color=BLUE);a.set_yticks([2,1,0],['BM25 / Hybrid','Dense / Hybrid','BM25 / Dense'])
    a.set(xlim=(0,42),xlabel='Query count')
    for y,n in zip([2,1,0],counts):a.text(n+.6,y,str(n),va='center',fontsize=8.5)
    panel(b,'b','Process-feature prediction')
    vals=[D['figureS1']['prediction'][k] for k in ['M0_MAE','M1_MAE']]
    for y,v,col in zip([1,0],vals,[GRAY,BLUE]):b.scatter(v,y,s=28,c=col);b.text(v-.008,y,f'{v:.6f}',ha='right',va='center',fontsize=8.5)
    b.set_yticks([1,0],['M0','M1']);b.set(xlim=(0,.3),ylim=(-.55,1.55),xlabel='MAE')
    panel(c,'c','Corrected input selection')
    value=D['figureS1']['selection']['delta_a3'];c.axvline(0,color=LIGHT,lw=.7,zorder=0);c.scatter(value,0,s=30,c=BLUE)
    c.set(xlim=(-.01,.01),ylim=(-1,1),xlabel='Mean Δa3');c.set_xticks([-.01,-.005,0,.005,.01]);c.set_yticks([]);c.spines['left'].set_visible(False)
    c.text(value,-.50,f'{value:.6f}',ha='center',va='center',fontsize=8.5)
    save(fig,'Figure_S1_Process_Limits_Corrected',out,qa)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--attempt',required=True);args=p.parse_args()
    out=ROOT/args.attempt/'figures';qa=ROOT/args.attempt/'qa';out.mkdir(parents=True,exist_ok=False);qa.mkdir()
    for fn in [figure1,figure2,figure3,figure4,figure5,figures1]:fn(out,qa)
    with (qa/'source_contract.json').open('x',encoding='utf8') as f:json.dump({'frozen_data_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'case_source_sha256':hashlib.sha256(CASE_SOURCE.read_bytes()).hexdigest(),'records':175,'same_C':54,'new_tests':0,'API':0,
        'source_rows_dropped':0,'jitter':False,'chart_font':CHART_FONT,'reference_font_claim':'No exact raster font inference',
        'notes':'Explanations/denominators/p-values moved to captions; unchanged frozen scientific meanings.'},f,indent=2)
    print(out)
