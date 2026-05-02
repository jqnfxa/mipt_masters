# MIPT FPMI Master's Entrance Prep

Open-source textbook for preparing for the MIPT FPMI master's entrance exam
in **Applied Mathematics and Informatics** (Прикладная математика и
информатика). Maintained collaboratively by the cohort.

The book is built with LaTeX from per-chapter `.tex` files and a shared
BibTeX bibliography. There are two parallel editions:

- **`book-ru.pdf`** — Russian edition (canonical; mirrors the official
  exam program).
- **`book-en.pdf`** — English edition.

Anyone can improve the material: open the `.tex` file you want, edit it,
send a PR.

## Repository layout

| Path | Purpose |
|------|---------|
| [`book-ru.tex`](book-ru.tex), [`book-en.tex`](book-en.tex) | Master documents, one per language. |
| [`preamble.tex`](preamble.tex) | Shared packages, math macros, theorem environments. |
| [`literature.bib`](literature.bib) | Shared BibTeX bibliography (GOST style). |
| [`core/`](core/) | Mandatory "core block" of the program (1.1–1.4). |
| [`electives/`](electives/) | Elective blocks (2.1–2.6); pick two for the exam. |
| [`images/`](images/) | Shared figures. |
| [`scripts/build.py`](scripts/build.py) | Build the books (and per-chapter PDFs). |
| [`plan.md`](plan.md) | Phased study plan. |
| [`программа.pdf`](программа.pdf) | Official exam program (canonical, in Russian). |

Each chapter lives under `<core|electives>/<id>-<slug>/`:

```
core/1.1-calculus-linalg/
├── README.md           # English description (setup-style doc)
├── README.ru.md        # Russian description (mirror of README.md)
├── chapter-ru.tex      # Russian glue: \chapter{...} + \input{ru/...}
├── chapter-en.tex      # English glue: \chapter{...} + \input{en/...}
├── ru/
│   ├── 01-systems-gauss.tex   # ticket 1, Russian
│   ├── 02-rank.tex
│   └── ...
├── en/
│   ├── 01-systems-gauss.tex   # ticket 1, English
│   └── ...
└── images/             # chapter-specific figures
```

The slug (`01-systems-gauss`) is stable across languages; only the prose
inside the file differs.

## Building

### Dependencies

- TeX Live (or MiKTeX) with packages `babel-russian`, `cyrillic`,
  `biblatex`, `biblatex-gost`, `subfiles`, `cleveref`, `hyperref`,
  `mathtools`, `tikz`, `microtype`.
- `latexmk`, `biber` (the biblatex backend).
- Python ≥ 3.9 (for the build script).

On Ubuntu / Debian (minimal):

```sh
sudo apt install \
    texlive-latex-recommended texlive-latex-extra texlive-bibtex-extra \
    texlive-lang-cyrillic texlive-science \
    latexmk biber python3
```

Or one shot (everything, ~6 GB): `sudo apt install texlive-full`.

### Commands

```sh
python scripts/build.py            # both book-ru.pdf and book-en.pdf
python scripts/build.py book-ru    # Russian edition only
python scripts/build.py book-en    # English edition only
python scripts/build.py chapters   # each chapter standalone (both langs)
python scripts/build.py all        # books + chapters
python scripts/build.py clean      # remove build/
```

Output PDFs land in `build/` (gitignored).

## Contributing

### Filling in a topic

1. Open the topic file you want, e.g.
   [`core/1.1-calculus-linalg/ru/01-systems-gauss.tex`](core/1.1-calculus-linalg/ru/01-systems-gauss.tex)
   for Russian, or its `en/` sibling for English.
2. Replace the `% TODO` markers under the three subsections:
   - **Theory** (Теория) — definitions and statements of theorems.
   - **Proofs** (Доказательства) — proofs of the key theorems.
   - **Examples** (Примеры) — worked examples and problems.
3. If you cite a source, add a BibTeX entry to
   [`literature.bib`](literature.bib) and use `\cite{key}`.
4. Update the parallel-language file when appropriate.

### Adding a new chapter

1. Create `<core|electives>/<id>-<slug>/`.
2. Mirror the existing layout: `chapter-ru.tex`, `chapter-en.tex`,
   `ru/`, `en/`, `images/`.
3. Uncomment the corresponding `\subfile{...}` line in
   [`book-ru.tex`](book-ru.tex) and [`book-en.tex`](book-en.tex).

## Conventions

### Mathematics

- **Strict notation.** Use the macros defined in
  [`preamble.tex`](preamble.tex): `\R`, `\C`, `\Z`, `\rank`, `\im`,
  `\E`, `\Prob`, `\T` (transpose), etc. If you need a new one, add it
  to the preamble — don't redefine locally.
- **Theorem environments** (`theorem`, `lemma`, `proposition`,
  `corollary`, `definition`, `example`, `problem`, `remark`, `proof`)
  are localized via babel and number consecutively within a chapter.

### Cross-references

- Bibliography: `\cite{IvanovAnalysis2011}`.
- To theorems / sections: `\cref{thm:gauss}`, `\Cref{sec:1.1.01-systems-gauss}`.

### Files

- Encoding: UTF-8.
- Topic files are named `NN-slug.tex` (two-digit ticket number + short
  English slug, kebab-case). The slug is stable across languages.
- **Internal `.tex` files (preamble, build setup) and root docs are in
  English** — they are tooling, not content. Per-section READMEs ship
  as a pair: `README.md` (English) and `README.ru.md` (Russian).

## License

CC BY-SA 4.0 (proposed; confirm before reuse).
