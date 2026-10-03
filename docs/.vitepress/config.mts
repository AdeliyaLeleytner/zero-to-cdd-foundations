import { defineConfig } from 'vitepress'

// The primary deliverable is the repository. This optional renderer uses the
// same Markdown files, following the layout of datawhalechina/zero-to-sglang.
export default defineConfig({
  title: 'zero-to-cdd-foundations',
  lang: 'ru-RU',
  srcDir: '..',
  srcExclude: ['*.md', '**/WRITING_TEMPLATE.md', 'docs/**', '.github/**', '.review/**', 'references/**', 'tests/**', 'node_modules/**'],
  rewrites: (id) => id.replace(/^course-material\/ru\//, 'ru/').replace(/^community\/ru\//, 'ru/community/'),
  // Source-only links (Python files, root README, contributor template) remain
  // valid repository links and are checked by scripts/check_chapters.py.
  ignoreDeadLinks: true,
  markdown: { math: true },
  themeConfig: {
    nav: [{ text: 'Программа', link: '/ru/' }],
    sidebar: [
      { text: 'Part 0 — Перед началом', items: [
        { text: 'Как учиться', link: '/ru/part0/Part0-Learning-and-Open-Science' },
        { text: 'Окружение', link: '/ru/part0/Part0-Environment-Setup' }
      ] },
      { text: 'Part I — Основы', items: [
        { text: '1. От болезни к молекуле', link: '/ru/part1/Chapter1_From-Disease-to-Molecule' },
        { text: '2. Как читать молекулу', link: '/ru/part1/Chapter2_Reading-Molecules' },
        { text: '3. Белок в движении', link: '/ru/part1/Chapter3_Proteins-in-Motion' },
        { text: '4. Что значит «связывается»', link: '/ru/part1/Chapter4_Molecular-Binding' }
      ] },
      { text: 'Part II — Практика', items: [
        { text: '1. Молекулярная идентичность', link: '/ru/part2/Chapter1_Molecular-Identity' },
        { text: '2. Модель связывания', link: '/ru/part2/Chapter2_Binding-Model' }
      ] },
      { text: 'Дальнейшая работа', items: [
        { text: 'Part III — Инструменты и данные', link: '/ru/part3/' },
        { text: 'Part IV — Самостоятельная работа', link: '/ru/part4/' },
        { text: 'Материалы сообщества', link: '/ru/community/' }
      ] }
    ],
    outline: { level: [2,3], label: 'В этой главе' },
    search: { provider: 'local' },
    docFooter: { prev: 'Назад', next: 'Дальше' }
  }
})
