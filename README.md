# Measurement provenance in reasoning-intensive retrieval

Public research artifacts accompanying **Measurement provenance and warranted claims in reasoning intensive retrieval**. This release corresponds to manuscript/figures v5, integrated submission package v6, and the already frozen study results.

## Start here

```sh
python scripts/verify_release.py
python data/evidence/verify_evidence.py
```

Python 3 standard library is sufficient for verification. The commands make no model requests and perform no new significance tests. Run them from the repository root. The second command also works from another working directory because it resolves paths from its own file.

| Directory | Content |
|---|---|
| `data/evidence/` | 19-file public derivative: 175 paired query results, 700 prediction positions, 312-aspect metric audit, 32 already-used RAGTruth decisions, case metadata, configuration, prompts, contracts, lineage and verification |
| `data/figures/` | Frozen plotting inputs; every one of the 175 query observations retained |
| `figures/` | Current Figure 1–5 and S1, each in PNG/PDF/SVG/600-dpi TIFF |
| `scripts/` | Portable figure rendering, layout checks and read-only release verification |
| `docs/` | Current captions, Tables I/II, evidence guide, public-derivative record and reproduction boundaries |
| `third_party_licenses/` | Existing Bright-Pro, RAGTruth and RAGAs licence texts; scope is explained in RIGHTS.md |

## What can be checked

- The selection-proxy correction across 175 queries: same C 54, different C 121; 38 affected positions of 700. The historical positive-effect interpretation is withdrawn.
- The archived biology:11 assignment mechanism, parsed completion and score restoration, using retained hashes and records.
- Defined-zero macro-F1 in the separate 84-position/312-aspect primary audit.
- Reference migration, conditional F1/coverage and correct-decision counts in the 32 already-used public-reference groups.
- The frozen numbers underlying all six current figures.

These are **inspection and deterministic consistency artifacts**, not an end-to-end model-experiment reproduction repository. See [reproduction scope](docs/reproduction_scope.md) and the [evidence guide](docs/supplementary_evidence_guide.md).

## Public derivative

The public copy removes two `user_prompt` fields containing underlying question/reference/answer text and two `actual_context_excerpt` fields containing source-document text. Numerical results, hashes, position identities, lengths, offsets and budgets are retained. The local submission archive was not edited. Public and pre-public digests are mapped in [public_derivation.json](docs/public_derivation.json); do not claim all 19 public files are byte-identical to the submission archive.

The 494 retained Bright-Pro queries and 118 unused RAGTruth groups are excluded, as are credentials, private reviewer information, ethics documents, editorial letters and the full source corpora. Retained-data counts are bookkeeping metadata, not released semantic records. The unpublished full manuscript is not needed for these artifact checks and is not included here.

## Render the figures (optional)

```sh
python -m pip install -r requirements-figures.txt
python scripts/draw_figures.py --attempt outputs/local_render_01
```

Each attempt must use a new directory; the script refuses to overwrite outputs. It reads only the frozen published inputs. Arial is used when installed, otherwise DejaVu Sans; font fallback can change visual appearance. The repository layout checker is a small, project-written structural check, **not** a redistributed copy of the original production audit tool. Published figures remain the exact v5 deliverables; local PDF/SVG metadata and fonts need not reproduce byte-identical files.

## Citation and rights

Use `CITATION.cff` for this artifact and cite the underlying Bright-Pro/RAGTruth sources separately. No DOI or published-article status is claimed. [RIGHTS.md](RIGHTS.md) distinguishes project artifacts from upstream source rights; public access does not create a new blanket licence.
