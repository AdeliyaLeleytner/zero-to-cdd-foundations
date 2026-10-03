# Sources and Verification Limits

Source review: 2026-10-03. This record documents provenance; it does not claim full peer review or reproduction of every cited study. The English edition preserves the scientific content of the Russian source. [Russian record](SOURCES_ru.md).

| Source | Role in the course | What was checked |
| --- | --- | --- |
| zero-to-sglang, SHA `2577007cc326f17651c41f6a886906deaa7e3088` | Teaching organization | The KV-cache chapter, parts of the inference chapter, the architecture chapter, and writing template were read. Text and images were not copied. |
| Druker et al., 1996, DOI `10.1038/nm0596-561` | Brief ABL → cellular growth example in Chapter 1 | Bibliography and author abstract through PubMed/orx, plus the publisher page. No claim of full-paper reading or experimental reproduction. |
| Nagar et al., 2002, PMID `12154025` | ABL structure and imatinib | Author abstract and primary structure entry 1IEP. Numerical comparisons reported in the paper are not imported into the course. |
| RCSB PDB 1IEP | Precise identity of the structural object | Mus musculus, c-ABL kinase domain, STI, X-ray diffraction, 2.10 Å. It is not presented as full-length human BCR–ABL. |
| Weininger, 1988, DOI `10.1021/ci00057a005` | Historical SMILES reference | Original paper metadata; current structure examples checked with RDKit. No full-text analysis of this paper has been performed. |
| Anfinsen, 1973, DOI `10.1126/science.181.4096.223` | Historical introduction to folding | PubMed metadata and bibliographic connection to the Nobel Lecture. NobelPrize.org/PDF access returned 403. Retained for further reading; no quantitative data taken from it. |
| Monod, Wyman & Changeux, 1965, DOI `10.1016/S0022-2836(65)80285-6` | Conformational states and allostery | PubMed metadata and the original PDF from an NYU university archive. Introduction and model assumptions read. The theory is not treated as covering every allosteric mechanism. |
| Jarmoskaite et al., 2020, DOI `10.7554/eLife.57264`, PMC7452723 | Equilibrium, concentration regimes, and kinetics | Open full text obtained through Europe PMC. Sections on equilibration time and depletion of a binding component read. Biological experiments were not reproduced. |
| RDKit Getting Started | Molecular drawings | Official documentation and actual figure generation with RDKit 2026.03.6. SMILES for all six molecular drawings are recorded in each edition's figure provenance file. |
| McMurry / OpenStax, Acid and Base Strength | Background on acidity and pKa | Relevant textbook section read. Exercise pKa values were chosen as hypothetical examples; source figures and exercises were not copied. |
| Harvard HMX, MIT–Harvard PPDD, Stanford CS279 | Subject map and teaching organization | Public syllabi checked earlier in the same project. A detailed comparison is maintained in the umbrella repository. |

## Figures and Calculations

The seven SVGs in each edition were created for this course. Conceptual diagrams are schematic. The Newman projections show specified 180° and 60° butane dihedrals, not calculated energies. Curves come from analytical equations with hypothetical parameters, not measurements. Molecular drawings are generated from explicit SMILES.

The shared generator is `scripts/render_figures.py`. Use `--language eng`, `--language ru`, or `--language all`. The versions, molecule definitions, and parameters are recorded in `course-material/<language>/part1/images/provenance.json`. PNG versions are previews; chapters use SVGs.

Exercises, discussions, and calculations are original. They do not reproduce Stanford/MIT or zero-to-sglang assignments. Properties of real drugs are not inferred from the illustrative plots.
