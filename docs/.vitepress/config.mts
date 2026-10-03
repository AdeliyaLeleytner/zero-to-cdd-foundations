import { defineConfig } from 'vitepress'

const sections = [
  { title: ['Part 0 — Before you learn', 'Part 0 — Перед началом'], items: [
    ['Learning and open science', 'Как учиться', 'part0/Part0-Learning-and-Open-Science'],
    ['Environment setup', 'Окружение', 'part0/Part0-Environment-Setup']
  ] },
  { title: ['Part I — Foundations', 'Part I — Основы'], items: [
    ['1. From disease to molecule', '1. От болезни к молекуле', 'part1/Chapter1_From-Disease-to-Molecule'],
    ['2. Reading molecules', '2. Как читать молекулу', 'part1/Chapter2_Reading-Molecules'],
    ['3. Proteins in motion', '3. Белок в движении', 'part1/Chapter3_Proteins-in-Motion'],
    ['4. Molecular binding', '4. Что значит «связывается»', 'part1/Chapter4_Molecular-Binding']
  ] },
  { title: ['Part II — Practical work', 'Part II — Практика'], items: [
    ['1. Molecular identity', '1. Молекулярная идентичность', 'part2/Chapter1_Molecular-Identity'],
    ['2. A binding model', '2. Модель связывания', 'part2/Chapter2_Binding-Model']
  ] },
  { title: ['Further work', 'Дальнейшая работа'], items: [
    ['Part III — Tools and data', 'Part III — Инструменты и данные', 'part3/'],
    ['Part IV — Independent work', 'Part IV — Самостоятельная работа', 'part4/'],
    ['Community', 'Материалы сообщества', 'community/']
  ] }
]
const sidebar = (language: string, column: number) => sections.map(section => ({
  text: section.title[column],
  items: section.items.map(item => ({ text: item[column], link: `/${language}/${item[2]}` }))
}))

// Optional renderer; the repository's Markdown remains the primary material.
export default defineConfig({
  title: 'zero-to-cdd-foundations',
  lang: 'en',
  srcDir: '..',
  srcExclude: ['*.md', '**/WRITING_TEMPLATE.md', 'docs/**', '.github/**', '.review/**', 'references/**', 'tests/**', 'node_modules/**'],
  rewrites: id => id.replace(/^course-material\/(eng|ru)\//, '$1/').replace(/^community\/(eng|ru)\//, '$1/community/'),
  // Source-only links are validated by scripts/check_chapters.py.
  ignoreDeadLinks: true,
  markdown: { math: true },
  locales: {
    eng: {
      label: 'English', lang: 'en', link: '/eng/',
      themeConfig: {
        nav: [{text: 'Syllabus', link: '/eng/'}], sidebar: sidebar('eng', 0),
        outlineTitle: 'On this page', docFooter: {prev: 'Previous', next: 'Next'}
      }
    },
    ru: {
      label: 'Русский', lang: 'ru-RU', link: '/ru/',
      themeConfig: {
        nav: [{text: 'Программа', link: '/ru/'}], sidebar: sidebar('ru', 1),
        outlineTitle: 'В этой главе', docFooter: {prev: 'Назад', next: 'Дальше'}
      }
    }
  },
  themeConfig: { i18nRouting: false, outline: {level: [2,3]}, search: {provider: 'local'} }
})
