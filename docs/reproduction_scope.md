# Reproduction scope

| Layer | Included | Limit |
|---|---|---|
| File integrity | SHA-256 manifest and read-only verification | A hash proves identity, not semantic validity |
| Frozen selection results | 175 paired rows and original/repaired summaries | Corrected p is already stored post hoc; no new hypothesis test |
| Worked assignment case | Parsed records, shared-owner relation, aspect weights/completion and original identifiers | Four raw-text fields removed in the public derivative; full-context hash cannot be reconstructed from metadata |
| Prediction | Existing query/position outputs and model feature definitions | Full retraining pipeline and all fitted coefficients are not supplied; do not claim retraining reproduction |
| Human calibration | Existing 312-aspect aggregate/confusion data and migration counts | Private raw annotations and matched natural-F semantic gold are not provided |
| Independent public-reference check | 32 already-used group identifiers, predictions and frozen statistics | Six positives and abstention constrain inference; not natural-F gold |
| Models/inputs | Existing request parameters, prompts, schemas, input budget units and versions | Provider weights and historical responses cannot be regenerated exactly by this archive |
| Figures | Current six figures, frozen numerical inputs and relative-path plotting | Font/rendering metadata can differ across installations |

No reserved semantic records, new model calls, new calibration or new significance tests were used to prepare this release. The initial offline verification checks existing arithmetic and identity relations; it does not validate automatic judgments against new human labels. Historical null/missing fields remain historical data unless the documented public text-only derivation applies.
