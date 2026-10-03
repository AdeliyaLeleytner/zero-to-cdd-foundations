# English Edition: Translation Check

Date: 2026-10-03. The English edition translates the currently written Russian material. Planned chapters remain planned.

## Scope

- Four complete theory chapters, retaining section order, derivations, examples, tables, exercises, captions, and references.
- Two practical chapters and two onboarding pages.
- English exercise discussions, contribution guidelines, writing template, and navigation pages.
- Seven figures regenerated with English labels from the shared generator; curve parameters and molecular SMILES are unchanged.
- English copies of both Python practicals, including descriptions and printed output.
- The English README points to English material; the Russian README retains Russian chapter links. The optional Markdown renderer supports both editions without a custom application interface.

## Checks

- `check_chapters.py --all`: 12 chapters and 134 local links checked.
- `check_translations.py`: six chapter pairs match in numbered sections, equations, exercise numbers, figures, extension questions, and external references. Answer equations, figure parameters, and molecular SMILES also match. No untranslated Cyrillic remains in English teaching files, apart from the intentional language-switch label.
- Ten unit tests passed under Python 3.12: the same physical and graph checks run against both language versions.
- Both English command-line practicals ran successfully.
- All seven English figures were rendered and visually inspected.
- The optional documentation build passed. No site was launched or published for this translation.

## Independent Reading

Claude Fable 5 compared the four theory chapter pairs in consultation `20261003T073228Z-61f0119a`. It recommended small wording clarifications and identified that “rate constant for approach to equilibrium” is more precise than the original Russian “rate.” The Russian extension question was updated to the same precise wording. Equations are unchanged.

The advisor's infrastructure observations reflected an incomplete or inaccurate file inventory during ongoing work; final file existence, links, code, and diagrams were checked directly. Its advice is not evidence of experimental reproduction or learner outcomes.
