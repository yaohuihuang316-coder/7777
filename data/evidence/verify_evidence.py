from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parent
def load(n): return json.loads((R/n).read_text(encoding="utf-8"))
m=load("MANIFEST.json")
for f in m["files"]:
 p=R/f["file"]
 assert p.resolve().is_relative_to(R.resolve()),f["file"]
 assert hashlib.sha256(p.read_bytes()).hexdigest()==f["sha256"],f["file"]
a=load("E01_selection_175_pairs.json")["per_query"]
ids={x["query_id"] for x in a}
assert len(a)==len(ids)==175 and sum(x["same_context"] for x in a)==54
b=load("E02_prediction_175.json")
assert len(b["rows"])==700 and {x["query_id"] for x in b["per_query"]}==ids
assert all(x["query_id"] in ids for x in b["rows"])
assert len({x["delta_repaired_a3"] for x in a})>1
assert len({x["d_i"] for x in b["per_query"]})>1
c=load("E04b_RAGTruth32_decisions.json")["rows"]
assert len(c)==len({x["id"] for x in c})==len({x["source_group"] for x in c})==32
assert all(x["split_endpoint"] in [0,1,None] and x["joint_endpoint"] in [0,1,None] for x in c)
f=load("E03_macroF1_primary312.json")
assert f["n_rows_primary"]==312 and f["n_positions_primary"]==84
assert f["support"]["per_class"]["uncertain"]["f1"]==0
c=load("E05_real_case_two_positions.json")
assert len(c["raw_quality_records"])==2
assert c["actual_context_sha256"]==c["raw_quality_records"][0]["record"]["context_sha256"]==c["raw_quality_records"][1]["record"]["context_sha256"]
assert c["answer_sha256"]==c["raw_quality_records"][0]["record"]["answer_sha256"]==c["raw_quality_records"][1]["record"]["answer_sha256"]
print("PASS: file digests, 175-query membership, 700 positions, 32 used groups and case identities; read-only, no network, no new tests")
