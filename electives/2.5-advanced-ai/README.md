# 2.5. Advanced Artificial Intelligence Methods

**RU:** Продвинутые методы искусственного интеллекта

Modern deep-learning topics: optimization (momentum / Nesterov, ADAM), batch-size effects, Transformer attention and decoder-only architectures, large-scale training (FlashAttention, FSDP, ZeRO, tensor parallelism), data quality and distribution shift, fine-tuning (LoRA / QLoRA, catastrophic forgetting), reinforcement learning (Bellman, Actor–Critic, off- vs on-policy), LLM hallucinations.

**Prerequisites:** [1.4 Intro to AI](../../core/1.4-intro-ai/), [2.4 Convex Optimization](../2.4-convex-optimization/) is highly recommended.

**Best fit for:** ML / DL / LLM-research kafedras.

## Topics (per program)

1. Метод оптимизации с импульсом и его интерпретация как физической динамики. Отличия Nesterov Momentum. Ограничения и нестабильности методов.
2. Определение batch size. Влияние размера batch size и величины градиентного шума на обобщение. Связь batch size и learning rate. Размер batch size при fine-tuning LLM. Влияние batch size на обобщение в задачах классификации, генерации и RL.
3. Shortcut solutions в больших моделях и методы их обнаружения. Методы интерпретации моделей для выявления shortcut solutions.
4. Механизмы внимания в Transformer. Causal и bidirectional attention: различия и области применения. Causal attention: масштабирование и потоковая генерация.
5. Архитектура Transformer decoder-only: особенности и сравнение с encoder–decoder.
6. Методы оптимизации обучения LLM: FlashAttention, FSDP, ZeRO, tensor parallelism.
7. Качество обучающих данных. Проблемы несбалансированных и неоднородных обучающих корпусов. Distribution shift.
8. Феномен Catastrophic forgetting в LLM. Причины и последствия возникновения при fine-tuning. Методы предотвращения.
9. Отличия LoRA и QLoRA.
10. Обучение с подкреплением. Уравнения Беллмана и их свойства, ошибки критика и их влияние на обучение актора в Actor–Critic, отличия off-policy и on-policy методов и проблемы стабильности off-policy.
11. Галлюцинации в LLM. Методы уменьшения галлюцинаций и проверки фактической точности в LLM.

## Suggested study order

- **Optimization (1–3):** momentum & Nesterov → batch size effects → shortcut solutions and interpretation.
- **Transformer architecture (4–5):** attention mechanisms → decoder-only.
- **Training at scale (6, 7):** FlashAttention / FSDP / ZeRO / tensor parallelism → data quality / distribution shift.
- **Fine-tuning (8, 9):** catastrophic forgetting → LoRA / QLoRA.
- **RL (10):** Bellman → Actor–Critic → off-/on-policy.
- **LLM reliability (11):** hallucinations and mitigation.

## Recommended literature

- Goodfellow I., Bengio Y., Courville A. *Deep Learning*. MIT Press, 2016.
- Sutton R.S., Barto A.G. *Reinforcement Learning: An Introduction*. MIT Press, 2nd ed., 2018.
- Vaswani A. et al. "Attention is All You Need." NeurIPS, 2017.
- Sebastian Ruder. "An Overview of Gradient Descent Optimization Algorithms." arXiv:1609.04747.
- Christiano et al. "Deep Reinforcement Learning from Human Preferences." NeurIPS, 2017.
