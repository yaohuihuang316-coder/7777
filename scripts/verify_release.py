"""Read-only integrity and frozen-row consistency checks; standard library only."""
from pathlib import Path
import hashlib,json,subprocess,sys,math

ROOT=Path(__file__).resolve().parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def main():
    manifest=read(ROOT/'MANIFEST.sha256.json')
    for relative,obj in manifest['files'].items():
        path=ROOT/relative
        assert path.is_file(),relative
        assert hashlib.sha256(path.read_bytes()).hexdigest()==obj['sha256'],relative
    ev=ROOT/'data/evidence'
    check=subprocess.run([sys.executable,str(ev/'verify_evidence.py')],capture_output=True,text=True,encoding='utf-8')
    assert check.returncode==0,check.stdout+check.stderr
    pairs=read(ev/'E01_selection_175_pairs.json')['per_query']
    plot=read(ROOT/'data/figures/plot_data_frozen.json')
    plotted=plot['figure2']['query_rows']
    index={r['query_id']:r for r in pairs};assert len(index)==len(pairs)==len(plotted)==175
    compared=0
    for row in plotted:
        for key,value in row.items():assert value==index[row['query_id']][key],(row['query_id'],key);compared+=1
    assert sum(r['same_context'] for r in plotted)==54
    case=read(ev/'E05_real_case_two_positions.json')
    assert all('user_prompt' not in r['record'] for r in case['raw_quality_records'])
    context=read(ev/'E05b_actual_context_excerpt.json')
    assert all('actual_context_excerpt' not in r for r in context['rows'])
    derivation=read(ROOT/'docs/public_derivation.json');assert len(derivation['redacted_fields'])==4
    prediction=read(ev/'E02_prediction_175.json')
    assert prediction['n_queries']==175 and prediction['n_positions']==700
    assert plot['figureS1']['prediction']['M0_MAE']==prediction['err_M0_mean']
    assert plot['figureS1']['prediction']['M1_MAE']==prediction['err_M1_mean']
    rag=read(ev/'E04_RAGTruth32_statistics.json')
    assert rag['primary']['N']==32 and rag['methods']['joint']['evaluable']==25
    assert rag['primary']['two_sided_exact_McNemar_p']==.21875
    print(json.dumps({'status':'PASS','release_files_hashed':len(manifest['files']),'query_rows':175,'field_equalities':compared,'same_C':54,'prediction_positions':700,'RAGTruth_used_groups':32,'public_redacted_fields':4,'new_statistical_tests':0,'model_calls':0,'writes':0}))
    print(check.stdout.strip())
if __name__=='__main__':main()
