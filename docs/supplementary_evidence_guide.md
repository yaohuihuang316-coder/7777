# Supplementary Evidence: measurement provenance audit

Accompanies “Measurement provenance and warranted claims in reasoning intensive retrieval”

## S1. Scope and relationship to the article

This supplement accompanies the current manuscript and Figures 1–5 and Supplementary Figure S1. It maps the claims to the existing frozen evidence. This 19-file public derivative removes four raw-text fields from E05/E05b and updates README/MANIFEST; the private submission archive remains unchanged; the current figures and captions have been checked against those same records. Changes in presentation do not constitute new experiments or independent replications.

The repository data/evidence directory supplies the 19 public evidence members and an updated network-free verification manifest. docs/public_derivation.json maps pre-public and public digests. The private Supplementary_Evidence.zip and its ASCII serialization are not redistributed because they retain underlying raw text. Numerical results are unchanged.

## S2. Record correction and input selection (Figure 2; Table II)

E01 contains 175 paired query differences: 54 share identical actual contexts and 121 have differing contexts. The historical mean Selection-minus-Hybrid a3 difference was +0.045277230705802134. The original primary-family raw p=.0006 is recorded in E01b; the separately stored historical reproduction p=.0002 in E01 is a different calculation record, and neither restores the withdrawn result.

The corrected mean is −0.004213064713064714, with stored post hoc p=.6471. E01c records 38 affected measurement positions among 700, comprising 37 Selection and one Hybrid. This correction withdraws the historical advantage. The post hoc comparison does not establish equivalence or validated human answer utility.

## S3. Worked record-assignment case (Figure 3)

E05 and E05b document brightpro:biology:11 using retained hashes, parsed quality records and context metadata; raw user_prompt and actual_context_excerpt text is omitted from this public release. Hybrid and Selection shared a context, answer and quality payload. The supported aspect had normalized weight .2 and recorded completion .5. Missing completion in the Selection position invoked a fallback of 1, producing .2 rather than .1; restoring the archived value returned .1 and the paired difference changed from +.1 to zero.

E10 contains the historical scoring and assignment code excerpts. The worked case is an inspection of archived records and automatic judgments, not a fresh semantic adjudication or a representative effect-size estimate. The fallback shown in the figure applies to supported aspects with absent completion, not every missing value.

## S4. Defined-zero macro-F1 (Table II)

E03 describes 84 primary positions and 312 aspect records. Historical macro-F1 .8725 excluded a defined zero class. The corrected displayed macro-F1 is .5817 (stored cross-check .581658). F1=2TP/(2TP+FP+FN) includes zero when its denominator is positive; only a zero denominator is undefined. The historical route_E null field and corrected primary per-class zero are different artifact meanings. The diagnostic 14-position/57-aspect aggregate is excluded.

## S5. Human-reference migration (Figure 4)

E12 records 196 original A/B aspect-label rows, including 77 not-mentioned omissions. These omissions are 77/110 of the old unsupported category; they are not 77 verified unsupported factual assertions. Separately, 119 nonempty original annotation records map to 91 fixed excerpts. These counts concern different objects and denominators. The matched natural-F human reference count is zero, meaning natural claim-fidelity accuracy remains unverified.

## S6. Public-reference evaluation and abstention (Figure 5)

E04 and E04b contain the frozen 32 used RAGTruth groups, with one response per group and six positive references. Positive denotes reference hallucination or an unsupported assertion. Split decisions: TP6/FP19/TN7/FN0, unknown0. Joint decisions: TP6/FP8/TN11/FN0, unknown7; all unknowns are reference-negative.

Conditional F1 values are .3870967741935484 and .6 at coverages 32/32 and 25/32. Full-sample correct decisions are 13/32 and 17/32. Exact McNemar p=.21875 compares paired correct endpoint decisions over all 32 groups; it is not a test of conditional F1. These results establish neither stable superiority nor equivalence. The lower bound under unresolved outcomes differs from the reported conditional score.

## S7. Distinct descriptive, predictive and selection endpoints (Figure S1)

E11 supplies 19/34/22 query-level ranking reversals among the same 175 queries and their separate nDCG@10–a3 difference associations. The association p values do not test the reversal counts. E02 records matched-target MAEs .2613426761128884 and .2597422701046936; the stored reduction is .00160040600819482 with p=.4442. E01 supplies the corrected input-selection endpoint. The endpoints share queries and are not independent replications.

The supplement supports measurement inspection. Automatic labels are not treated as human semantic gold, the public support-proxy evaluation does not validate natural F, and the retained negative findings are not claims that all possible methods are ineffective.

## S8. Evidence file index

### E01_selection_175_pairs.json

175 paired query records, original and repaired summaries; Figure 2.

### E01b_historical_primary_family.json

Original primary-family inference record; withdrawn result only.

### E01c_affected_position_counts.json

38 affected positions and condition allocation; Figure 2c.

### E02_prediction_175.json

Frozen matched-target prediction results; Figure S1b.

### E03_macroF1_primary312.json

84-position/312-aspect primary comparison and defined-zero correction; Table II.

### E04_RAGTruth32_statistics.json

Confusion counts, coverage and stored paired endpoint test; Figure 5.

### E04b_RAGTruth32_decisions.json

The 32 already used group/response identifiers and endpoint decisions.

### E05_real_case_two_positions.json

Parsed quality payload and position-assignment case; two raw user_prompt fields omitted publicly; Figure 3.

### E05b_actual_context_excerpt.json

Actual context hash, length, offsets and budget metadata for the worked case; original excerpt text omitted publicly.

### E06_retrieval_and_analysis_config.json

Data and code revisions, retrieval and historical budget configurations.

## S8. Evidence file index (continued)

### E07_checker_prompts.json

Existing checker prompts, preserved as data rather than new instructions.

### E08_checker_schemas.json

Existing checker output contracts and endpoint fields.

### E09_claim_extractor_contract.json

Claim extraction contract and its measurement scope.

### E10_historical_code_excerpts.txt

Historical implementation excerpts, with limitations documented in README.

### E11_association_statistics.json

Association summaries and ranking reversals; Figure S1a.

### E12_reference_migration_counts.json

Original aspect labels and fixed-excerpt migration counts; Figure 4.

### MANIFEST.json

Member hashes, source lineage and explicit extraction/mapping scope.

### README.md

Evidence reading order, boundaries, rights and verification instructions.

### verify_evidence.py

Read-only, standard-library verification; no network or model requests.

## S9. Verification and exclusions

To verify this public derivative, run python data/evidence/verify_evidence.py from the repository root using Python 3. The script checks the local files and identities without changing them, contacting a service, or performing new inference. The manifest excludes its own digest. Original archive-relative source paths and historical hashes document lineage; source files are needed separately to verify upstream hashes.

This public derivative additionally excludes raw user_prompt and actual_context_excerpt text. It excludes the 494 retained Bright-Pro queries, 118 unused RAGTruth groups, credentials, private reviewer names/signatures and raw RAGTruth human spans/answer text. It is not a complete experiment regeneration repository. No blanket redistribution licence is newly granted. The historical constant-difference shortcut in E10 is not a validated general statistical routine; the included 175-query vectors did not use that branch.
