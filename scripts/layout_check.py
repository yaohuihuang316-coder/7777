"""Project-written lightweight layout check; no third-party skill code copied."""
import json
from itertools import combinations
from pathlib import Path

def require_matplotlib_panel_alignment(fig,json_out=None,overlay_svg=None,tolerance_pt=1.5,gutter_tolerance_pt=1.5,require_panel_labels=True,strict=True):
    fig.canvas.draw()
    width,height=fig.get_size_inches()*72
    axes=fig.axes;panels=[];findings=[]
    for i,ax in enumerate(axes):
        b=ax.get_position();rect=[b.x0*width,b.y0*height,b.x1*width,b.y1*height]
        labels=[t.get_text() for t in ax.texts if t.get_text() in list('abcdef')]
        if require_panel_labels and len(labels)!=1:findings.append({'axis':i,'reason':'Expected one panel label'})
        if any(v<-.01 for v in rect) or rect[2]>width+.01 or rect[3]>height+.01:findings.append({'axis':i,'reason':'Panel outside canvas'})
        panels.append({'axis':i,'bbox_pt':rect,'labels':labels})
    comparisons=0
    for a,b in combinations(panels,2):
        x0,y0,x1,y1=a['bbox_pt'];u0,v0,u1,v1=b['bbox_pt']
        if abs(y0-v0)<tolerance_pt and abs(y1-v1)<tolerance_pt:
            comparisons+=1
            if abs((x1-x0)-(u1-u0))>tolerance_pt:findings.append({'axes':[a['axis'],b['axis']],'reason':'Unequal width within row'})
    report={'tool':'project lightweight layout check','not_original_production_skill_audit':True,'panels':panels,'comparisons':comparisons,'findings':findings,'verdict':'FAIL' if findings else 'PASS','tolerance_pt':tolerance_pt}
    if json_out:
        with Path(json_out).open('x',encoding='utf-8') as f:json.dump(report,f,indent=2)
    if strict and findings:raise ValueError(report)
    return report
