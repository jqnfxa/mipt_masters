# 1.1. Mathematical Analysis and Linear Algebra

> Russian version: [README.ru.md](README.ru.md).

The foundational block. Linear algebra (matrices, vector spaces, operators,
quadratic forms) and calculus (differentiation in one and several variables,
series, Fourier analysis). Prerequisite for **every** other section,
especially probability theory (1.2), ML (1.4), and convex optimization (2.4).

## Topics (per program)

The full ticket descriptions below are translated from
[программа.pdf](../../программа.pdf). Each ticket is one `.tex` file under
[`ru/`](ru/) (Russian) and [`en/`](en/) (English); the slug is stable
across languages.

### Linear algebra

| # | File slug | Topic |
|---|-----------|-------|
| 1 | `01-systems-gauss` | Systems of linear equations. Rectangular matrices. Reduction to row echelon form. Gaussian elimination. |
| 2 | `02-rank` | Linear dependence and rank. Main lemma on linear dependence; basis and rank of a system of rows (columns). Rank of a matrix. Compatibility / definiteness criterion in terms of ranks. Fundamental system of solutions of a homogeneous linear system. |
| 3 | `03-matrix-operations` | Operations on matrices and their properties. Rank of a product. Determinant of a product of square matrices. Inverse matrix: explicit form and via elementary row operations. |
| 4 | `04-vector-spaces` | Vector space, basis, dimension. Coordinate transformations. Subspaces as solution sets of homogeneous linear systems. Dimension of sum and intersection. Direct sum: basis and dimension. |
| 5 | `05-linear-maps` | Linear maps and operators. Image and kernel and the relation between their dimensions. Dual space and dual bases. Change of matrix under a change of basis. |
| 6 | `06-eigenvalues` | Eigenvectors and eigenvalues. Eigenspaces and their linear independence. Diagonalizability criterion. Self-adjoint operator on a finite-dimensional Euclidean space; properties of eigenvalues / eigenvectors. |
| 7 | `07-quadratic-forms` | Bilinear forms and their matrices; transformation under a change of basis. Quadratic forms. Lagrange's reduction to canonical form. Positive (negative) definiteness conditions. Sylvester's criterion. |

### Calculus

| # | File slug | Topic |
|---|-----------|-------|
| 8 | `08-series` | Numerical and functional series. Convergence tests (d'Alembert, Cauchy, integral, Leibniz). Absolutely / conditionally convergent series. |
| 9 | `09-derivatives-taylor` | Differentiation of functions. Derivative for finding extrema. Taylor's formula. |
| 10 | `10-multivariable` | Functions of several variables. Partial derivatives. Gradient and its geometric meaning. Gradient descent. |
| 11 | `11-conditional-extrema` | Constrained extrema. Method of Lagrange multipliers; necessary and sufficient conditions. |
| 12 | `12-fourier-series` | Riemann's oscillation theorem. Trigonometric Fourier series. Conditions for pointwise / uniform convergence. |
| 13 | `13-fourier-transform` | Fourier transform of an absolutely integrable function and its properties. Fourier transform of a derivative; derivative of a Fourier transform. |

## Suggested study order

- **Linear algebra (topics 1–7):** in order — each topic builds on the previous.
- **Calculus (topics 8–13):** in order; multivariable (10–11) needs
  single-variable (9) first; Fourier (12–13) closes the chapter.

## Recommended literature

Cite via the keys in [`../../literature.bib`](../../literature.bib).

- **Иванов Г.Е.** *Лекции по математическому анализу.* МФТИ, 2011.
- **Беклемишев Д.В.** *Курс аналитической геометрии и линейной алгебры.* 2025.
- **Винберг Э.Б.** *Курс алгебры.* МЦНМО, 1999/2018.
- **Кострикин А.И.** *Введение в алгебру, ч. I, II.* Физматлит, 2000.
- **Курош А.Г.** *Курс высшей алгебры.* Наука, 1975.
- **Сборник задач по алгебре** под ред. А.И. Кострикина. МЦНМО, 2009.
- **Зорич В.А.** *Математический анализ I, II.* Наука, 1981/1984.
- **Кудрявцев Л.Д.** *Курс математического анализа* (3 тома).
- **Демидович Б.П.** *Сборник задач и упражнений по математическому анализу.* АСТ, 2007.
