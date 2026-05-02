# 1.4. Introduction to Artificial Intelligence

**RU:** Введение в искусственный интеллект

Classical machine learning (regression, classification, clustering, dimensionality reduction), model evaluation, gradient-based optimization, and the basic neural-network families (MLP, RNN/LSTM, CNN).

**Prerequisites:** [1.1 Calculus and Linear Algebra](../1.1-calculus-linalg/) for gradients and matrix algebra; [1.2 Probability and Statistics](../1.2-probability-stats/) for likelihood, MSE, distributions.

## Topics (per program)

1. Основные понятия (выборка, модель, функция потерь) и постановки задач машинного обучения. Примеры прикладных задач.
2. Задача регрессии. Линейная регрессия. Аналитическое решение МНК. Метрики качества регрессии: MSE, MAE, R².
3. Регуляризация: L1 и L2. Причины использования, свойства, интерпретация.
4. Задача классификации: метрики качества классификации. Метод максимального правдоподобия.
5. Логистическая регрессия.
6. Задача кластеризации: k-means, DBSCAN. Метрики качества кластеризации.
7. Задача понижения размерности: PCA, T-SNE.
8. Оценка качества моделей. Переобучение. Отложенная выборка, ее недостатки. Оценка полного скользящего контроля. Кросс-валидация. Leave-one-out.
9. Градиентные методы оптимизации в машинном обучении. Оптимизатор ADAM.
10. Понятие нейронной сети. Многослойный перцептрон. Метод обратного распространения ошибки. Функции активации.
11. Рекуррентные нейронные сети. Обратное распространение через слой RNN.
12. Проблема исчезающего градиента и ее решение. LSTM.
13. Сверточные нейронные сети. Свертка матриц. Сверточный слой, обратное распространение через него.

> Note: the program PDF numbers two consecutive items as «1.» under topics 11–12. They are restored to 11 (RNN) and 12 (vanishing gradient / LSTM) here.

## Suggested study order

- **Setup (1, 8):** problem framing → overfitting / cross-validation.
- **Regression (2, 3):** linear regression / OLS → L1/L2 regularization.
- **Classification (4, 5):** metrics + MLE → logistic regression.
- **Unsupervised (6, 7):** clustering → dimensionality reduction.
- **Optimization & nets (9–13):** SGD/ADAM → MLP + backprop → RNN → LSTM → CNN.

## Recommended literature

- Воронцов К.В. Машинное обучение, курс лекций. <http://www.machinelearning.ru/wiki/>
- Mohammed J. Zaki, Wagner Meira Jr. *Data Mining and Analysis*. Cambridge University Press, 2014. <http://www.dataminingbook.info/pmwiki.php/Main/BookDownload>
- Boris Mirkin. *Core Concepts in Data Analysis*, 2010.
- Boyd S., Vandenberghe L. *Convex Optimization*.
- Dekking F.M. et al. *A Modern Introduction to Probability and Statistics*.
