# Pull Request Requirements

A change should help readers understand the material or reproduce a result. Describe the problem and what the change improves.

## Text and Figures

- Follow the [chapter template](../../course-material/eng/WRITING_TEMPLATE.md).
- Check terminology, notation, units, and transitions between sections.
- Provide an appropriate source for a new factual claim.
- Store figures in the relevant part's `images/` directory and include the source or generation script.
- Keep questions and exercises at the end of a chapter; place answers separately.

## Code and Checks

From the repository root, run:

```sh
python3 scripts/check_chapters.py --all
python3 -m unittest discover -s tests
```

When changing a calculation, provide the command and expected result. When reorganizing directories, check links in the README and chapters. For changes to the optional documentation renderer, also run `pnpm build`.

## Describing a Change

State the problem addressed, what was checked, and any remaining limits. Do not present running a teaching model as reproducing a scientific experiment. Reflect chapter additions, merges, and reordering in the README syllabus before changing the files.
