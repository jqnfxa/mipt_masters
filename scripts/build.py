#!/usr/bin/env python3
"""Build the MIPT FPMI study book.

Usage:
    python scripts/build.py            # both book-ru.pdf and book-en.pdf
    python scripts/build.py book-ru    # Russian edition only
    python scripts/build.py book-en    # English edition only
    python scripts/build.py chapters   # each chapter standalone (both langs)
    python scripts/build.py all        # books + chapters
    python scripts/build.py clean      # remove build/

Requirements:
    - latexmk
    - pdflatex
    - biber
    - LaTeX packages: babel-russian, cyrillic, biblatex, biblatex-gost,
      subfiles, cleveref, hyperref, mathtools, tikz, microtype.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BUILD = REPO / "build"

BOOKS = ("book-ru", "book-en")


def _latex_env() -> dict[str, str]:
    """Add the repo root to TEX/BIB input search paths so that subfile chapter
    builds (cwd != repo root) and master book builds both find shared
    resources like literature.bib and preamble.tex.

    The trailing colon is kpathsea's way of saying "and also the defaults".
    """
    env = os.environ.copy()
    root = f"{REPO}{os.pathsep}"
    for var in ("BIBINPUTS", "TEXINPUTS", "BSTINPUTS"):
        env[var] = root + env.get(var, "")
    return env


def latexmk(target: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "latexmk",
        "-pdf",
        "-interaction=nonstopmode",
        "-file-line-error",
        f"-outdir={outdir}",
        target.name,
    ]
    print(f"$ (cd {target.parent.relative_to(REPO)} && {' '.join(cmd)})")
    subprocess.run(cmd, cwd=target.parent, env=_latex_env(), check=True)
    return outdir / (target.stem + ".pdf")


def build_book(name: str) -> Path:
    pdf = latexmk(REPO / f"{name}.tex", BUILD)
    print(f"\n[{name}] {pdf.relative_to(REPO)}")
    return pdf


def discover_chapters() -> list[Path]:
    chapters: list[Path] = []
    for root in ("core", "electives"):
        chapters.extend(sorted((REPO / root).rglob("chapter-*.tex")))
    return chapters


def build_chapters() -> list[Path]:
    pdfs: list[Path] = []
    for ch in discover_chapters():
        rel = ch.parent.relative_to(REPO)
        outdir = BUILD / "chapters" / rel
        pdfs.append(latexmk(ch, outdir))
    print(f"\n[chapters] built {len(pdfs)} chapter(s)")
    for p in pdfs:
        print(f"  - {p.relative_to(REPO)}")
    return pdfs


def clean() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
        print(f"removed {BUILD.relative_to(REPO)}/")
    else:
        print("nothing to clean")


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="book",
        choices=("book", *BOOKS, "chapters", "all", "clean"),
    )
    args = parser.parse_args()

    if args.target == "clean":
        clean()
        return 0
    if args.target in ("chapters", "all"):
        build_chapters()
    if args.target == "book" or args.target == "all":
        for b in BOOKS:
            build_book(b)
    elif args.target in BOOKS:
        build_book(args.target)
    print(f"\noutputs in {BUILD.relative_to(REPO)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
