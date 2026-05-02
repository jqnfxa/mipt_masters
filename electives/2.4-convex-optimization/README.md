# 2.4. Convex Analysis, Optimization Theory and Optimal Control

**RU:** Выпуклый анализ, теория оптимизации и методы оптимального управления

Convex sets and functions, support / Legendre–Fenchel duality, subdifferential calculus, KKT conditions, linear-programming duality, calculus of variations, Pontryagin's maximum principle, gradient / Newton / stochastic methods, non-convex optimization.

**Prerequisites:** [1.1 Calculus and Linear Algebra](../../core/1.1-calculus-linalg/) (gradients, eigenvalues, multi-variable calculus).

**Best fit for:** optimization, applied-math, ML kafedras.

## Topics (per program)

1. Определение и топологические свойства выпуклых множеств. Операция с выпуклыми множествами. Выпуклые комбинации. Теоремы Каратеодори, Радона, Хелли.
2. Опорные функции и их свойства.
3. Выпуклые функции и их свойства. Критерий выпуклости дифференцируемой функции.
4. Преобразование Лежандра–Юнга–Фенхеля. Теорема Фенхеля–Моро.
5. Субдифференциал выпуклой функции и его связь с производной по направлению.
6. Теорема Моро-Рокафеллара. Теорема Дубовицкого–Милютина о субдифференциале максимума.
7. Теорема Куна-Таккера для задач выпуклого программирования.
8. Теорема двойственности для задач линейного программирования.
9. Задачи вариационного исчисления. Уравнение Эйлера. Первые интегралы уравнения Эйлера. Условия Вейерштрасса, Лежандра и Якоби. Уравнение Якоби. Условия Вейерштрасса–Эрдмана.
10. Задачи оптимального управления. Принцип максимума Понтрягина.
11. Точечно-множественные отображения и их свойства (замкнутость, полунепрерывность сверху и снизу). Теорема Какутани.
12. Невыпуклая оптимизация. Примеры трудных задач невыпуклой оптимизации. Условие Поляка-Лоясиевича, глобальная сходимость градиентного спуска для невыпуклых задач.
13. Переход к двойственной задаче. Уменьшение размерности задачи в случае выпуклости и сепарабельности функционала.
14. Метод условного градиента (Франк-Вульфа). Примеры множеств, на которых легко минимизировать линейный функционал. Скорость сходимости.
15. Метод Ньютона. Аффинная инвариантность. Самосогласованные функции.
16. Метод множителей Лагранжа, условия ККТ, условие Слейтера.
17. Стохастическая оптимизация. Минибатчинг и распараллеливание.
18. Решение обратных задач методом градиентного спуска. Учёт ограничений с помощью ввода множителей Лагранжа.

> Note: the program PDF concatenates topics 12 and 13 together. They are split here for clarity.

## Suggested study order

- **Convex sets and functions (1–6):** sets and Helly/Radon/Carathéodory → support functions → convex functions → Legendre–Fenchel → subdifferential → Moreau–Rockafellar.
- **Optimality conditions and duality (7–8, 13, 16):** KKT → LP duality → general dual problem → Lagrangian / Slater.
- **Calculus of variations and optimal control (9–11):** Euler equation → Pontryagin's maximum principle → set-valued maps and Kakutani.
- **Algorithms (12, 14, 15, 17, 18):** non-convex (PL condition) → Frank–Wolfe → Newton → SGD / minibatching → inverse problems.

## Recommended literature

- Гасников А.В. Современные методы оптимизации. 2-е изд., 2021.
- Воронцова Е.В. Выпуклая оптимизация, 2021.
- Магарил-Ильяев Г.Г., Тихомиров В.М. Выпуклый анализ и его приложения. УРСС, 2003.
- Арутюнов А.В., Магарил-Ильяев Г.Г., Тихомиров В.М. Принцип максимума Понтрягина. Доказательство и приложения. Факториал Пресс, 2006.
- Boyd S., Vandenberghe L. *Convex Optimization*. Cambridge University Press, 2004.
