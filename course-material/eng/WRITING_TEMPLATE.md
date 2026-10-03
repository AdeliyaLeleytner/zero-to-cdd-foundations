# Chapter Writing Template

Reference version of zero-to-sglang: `2577007cc326f17651c41f6a886906deaa7e3088`; structure rechecked on 2026-10-03.

This repository follows the organization of [zero-to-sglang](https://github.com/datawhalechina/zero-to-sglang): a README syllabus, chapters in `course-material/<language>/partN`, figures beside chapters, and questions and references at the end. English material is in `eng/`; Russian material is in `ru/`. Do not mark an unwritten translation as complete.

## Opening

After a single H1 heading, write one or two connected paragraphs introducing the subject question, motivation, and link to the previous topic. Then state the learning objectives. A list of terms does not replace an introduction.

## Explanatory Order

Question → intuitive picture or diagram → mechanism → equation with definitions → worked example → new problem. Use connected prose. Explain a term before relying on it.

## Structure

```markdown
# Chapter N. Title

The subject question and connection to the previous chapter.

## 1. Learning Objectives

A short list of observable learning outcomes.

## 2. Main Explanation

Connected prose.

### 2.1 First Step

Mechanism, diagram, definitions, and example.

## 3. Summary and Exercises

### 3.1 Summary

What the reader now understands.

### 3.2 Exercises

1. An explanation question.
2. An application problem.
3. ★ A research extension.

## References and Further Reading

- A source link and a short explanation of its role.
```

Number H2 headings consecutively. H3 headings include their parent section number. The final references section is unnumbered. Let the topic determine the structure; the number of sections is not fixed.

## Files and Figures

Name chapter files `ChapterN_English-Title.md`. A code walkthrough may use the `_code.md` suffix. Store figures in `partN/images/` and include them with a relative path, alt text, and caption:

```html
<div align="center">
  <img src="./images/example.svg" alt="An informative description" width="800">
  <p><em>Figure 1. What the diagram shows and how to read it.</em></p>
</div>
```

The entire chapter must be readable in GitHub Markdown. Understanding the material must not require Vue components or a separate application. The optional renderer in `docs/.vitepress/` uses the same source files.

## Numbers and Sources

Explain each equation's quantities, units, assumptions, and a worked example. Clearly distinguish hypothetical teaching values from measurements. Explain the ideas contributed by landmark papers; bibliographic verification must not be presented as full-text reading or reproduction.

## Closing and Checks

Place questions and exercises at the end, followed by references. Answers belong in separate community material. Update the README syllabus before changing chapter numbering or organization.

```sh
python3 scripts/check_chapters.py --all
```

Link checks supplement reading and running examples. Do not copy licenses, authorship, institutional affiliations, or verification claims from the reference repository.

## Keeping Editions Aligned

Preserve section order, equations, numerical examples, sources, and exercise requirements when translating. Write natural English without summarizing away explanations or adding scientific claims. Translate figure labels and reader-facing program output as well as prose. Check both editions when changing shared content.
