<div align="center">
  <h1>zero-to-cdd-foundations</h1>
  <p>
    <a href="../../README.md"><img src="https://img.shields.io/badge/English-2563eb?style=for-the-badge" alt="English"></a>
    <a href="../../README_ru.md"><img src="https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-6b7280?style=for-the-badge" alt="Русский"></a>
  </p>
</div>

### From molecular structure to the foundations of Computational Drug Discovery

A hands-on course: understand molecules, proteins, and binding; work through simple computational models; then explore real research data and tools.

> **Course status:** Part 0, Chapters 1–4 of Part I, and two practical chapters in Part II are written. The remaining material is under development. **All currently written chapters are available in English and Russian.** This repository overview is available in [English](../../README.md) and [Русский](../../README_ru.md).

## About

Computational drug discovery begins with understanding the problem. What do we want to change in a biological system? Which properties of a molecule determine its behavior? What does an experiment measure, and what question does a model's prediction answer?

The first part of this course builds a coherent picture: from the drug discovery problem and chemical structure to proteins, binding equilibria, and experimental measurements. In the second part, you work with small implementations and examine how their assumptions shape the results. Later sections connect these models to real data and research tools.

This is Volume 0 of the **Computational Drug Discovery** series. Subsequent repositories will cover Target Discovery, Hit Discovery, Structure-Based Drug Design, Target Deconvolution, and Lead Optimization.

## What you will learn

- Read molecular structures and distinguish connectivity, stereochemistry, conformations, and protonation states.
- Connect a protein's structure and conformational states to its function.
- Derive simple binding models and explain their numerical results.
- Distinguish experimental observations, computational predictions, and scientific conclusions.
- Work with data and code so that others can reproduce your results.

## Prerequisites

- **Mathematics:** school-level algebra. Logarithms and the meaning of a derivative are explained where needed.
- **Programming:** basic Python for the practical chapters. You can read Part I without running code.
- **Chemistry and biology:** core concepts are introduced throughout the course.
- **Hardware:** the completed practical exercises run on CPU and require no third-party Python libraries.

## Syllabus

Status legend: ✅ written and technically checked · 🚧 planned. This first edition has not yet been piloted with a group of learners. **The links below open the English edition.**

| Chapter | Key content | Status |
| --- | --- | --- |
| **Part 0 — Before you learn** | | |
| [0.1 Learning and participating in an open course](part0/Part0-Learning-and-Open-Science.md) | Working with explanations, sources, and exercises | ✅ |
| [0.2 Environment setup](part0/Part0-Environment-Setup.md) | Python, first runs, and checks | ✅ |
| **Part I — Foundations** | | |
| [1. From disease to molecule](part1/Chapter1_From-Disease-to-Molecule.md) | Targets, hits, and leads; computation and experiment | ✅ |
| [2. Reading molecules](part1/Chapter2_Reading-Molecules.md) | Bonds, shape, stereochemistry, charge, and environment | ✅ |
| [3. Proteins in motion](part1/Chapter3_Proteins-in-Motion.md) | Sequence, structure, states, and function | ✅ |
| [4. What does “binding” mean?](part1/Chapter4_Molecular-Binding.md) | Kd, occupancy, free energy, and kinetics | ✅ |
| 5. What does an experiment measure? | Assays, dose–response, Kd / Ki / IC50 / EC50 | 🚧 |
| 6. Molecules and proteins as data | SMILES, graphs, fingerprints, PDB, and identifiers | 🚧 |
| 7. What can a computational model tell us? | Physical and ML models, baselines, and prediction evaluation | 🚧 |
| **Part II — Working through models yourself** | | |
| [1. Molecular identity](part2/Chapter1_Molecular-Identity.md) | Graphs, atom labels, and renumbering | ✅ |
| [2. A binding model](part2/Chapter2_Binding-Model.md) | Occupancy, mass balance, energy, and complex lifetime | ✅ |
| 3. Your first research analysis | Structures and measurements → reproducible analysis | 🚧 |
| **Part III — Exploring real tools** | | |
| 1. How RDKit represents a molecule | Connecting the models you have learned to a real toolkit | 🚧 |
| 2. Reading structural and biochemical data | From a PDB entry and an assay to a testable question | 🚧 |
| **Part IV — Independent work and contributions** | | |
| 1. Reproduction and research reporting | Checking results and explaining the next decision | 🚧 |
| [2. Making corrections and opening a pull request](../../community/eng/PR_requirement.md) | Sources, text revisions, and code checks | ✅ |

## Quick start

Open [Chapter 1](part1/Chapter1_From-Disease-to-Molecule.md). The core material is readable directly in Markdown, including figures, equations, references, and exercises.

Run the practical exercises from the repository root:

```sh
python3 course-material/eng/part2/code/identity.py
python3 course-material/eng/part2/code/binding.py
```

## Learning path

1. Read Part I to understand the subject and the meaning of the models.
2. Work through the available practical chapters in Part II: predict the result, run the code, and explain what you observe.
3. As Part III becomes available, connect the learning models to real tools and data.
4. Complete an independent analysis and document it so another reader can reproduce it.

## Project structure

```text
zero-to-cdd-foundations/
├── course-material/
│   ├── ru/                    # Russian edition (same layout)
│   └── eng/                   # English edition
│       ├── part0/              # Before you learn
│       ├── part1/              # Foundations; figures in images/
│       ├── part2/              # Practical chapters; Python source in code/
│       ├── part3/              # Real data and tools — planned
│       ├── part4/              # Independent work — planned
│       └── WRITING_TEMPLATE.md
├── community/                 # English and Russian exercise discussions and guidelines
├── docs/.vitepress/            # Optional Markdown renderer
├── scripts/                   # Chapter checks and figure generation
├── tests/                     # Checks for the learning code
├── references/                # Sources and verification records
├── .github/workflows/          # CI
├── README.md                  # English overview (default)
├── README_ru.md               # Russian overview
├── package.json
└── pnpm-lock.yaml
```

## Contributing

Corrections to explanations, sources, figures, and code are welcome. Before editing a chapter, read the [writing template](WRITING_TEMPLATE.md) and the [PR requirements](../../community/eng/PR_requirement.md).

Run these checks from the repository root:

```sh
python3 scripts/check_chapters.py --all
python3 -m unittest discover -s tests
```

[Exercise discussions](../../community/eng/Exercise-Discussions.md) are separate from the chapters. Use them to check your reasoning after attempting the exercises yourself.

## Optional documentation build

As in the reference repository, VitePress renders the source Markdown files. You do not need the site to read the course or run the exercises. This optional build requires Node.js 20+ and pnpm 10.21.0:

```sh
pnpm install --frozen-lockfile
pnpm build
```

## Sources and provenance

The structure and organization follow [datawhalechina/zero-to-sglang](https://github.com/datawhalechina/zero-to-sglang). The text, exercises, and figures in this course are original. Each chapter includes references; [SOURCES.md](../../references/SOURCES.md) records what has been checked and the limits of that verification.

This is currently a local Git repository. Its public address and release license have not yet been chosen; no placeholder GitHub or Colab links are presented as working resources.
