# Before You Learn: Environment Setup

The theory chapters can be read directly in the repository. The two completed practical exercises need only Python 3.10 or newer; they require no third-party Python libraries, GPU, or data downloads.

## 1. Check Python

Run these commands from the repository root:

```sh
python3 --version
python3 course-material/eng/part2/code/identity.py
python3 course-material/eng/part2/code/binding.py
```

The first program shows that renumbering atoms preserves a graph, while changing connectivity can change the molecule. The second reproduces the binding calculations. If `python3` is unavailable, install a supported Python version from the [official website](https://www.python.org/downloads/).

## 2. Check the Materials

```sh
python3 scripts/check_chapters.py --all
python3 -m unittest discover -s tests
```

These commands check local links, chapter structure, and scientifically meaningful properties of the learning code. They should finish without errors. These checks support independent study; they do not measure a reader's understanding.

## 3. Reproduce the Figures

The generated SVGs are already included beside the chapters in `course-material/eng/part1/images/`. If needed, regenerate them using [uv](https://docs.astral.sh/uv/):

```sh
uv run --no-project scripts/render_figures.py --language eng
```

Library versions are pinned in the script. Molecular drawings are generated from explicit SMILES, and the plots show analytical models with hypothetical parameters.

## 4. Continue

Open [Chapter 1](../part1/Chapter1_From-Disease-to-Molecule.md). Before running the code for a practical exercise, read its explanation and make your own prediction.
