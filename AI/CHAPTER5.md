# **5 Uncertainty**

## **5.1 Acting Under Uncertainty**

=> In many real-world problems, an agent cannot know all facts with complete certainty.

=> Sensors may be noisy, data may be incomplete, and actions may have unpredictable results.

=> Therefore, an intelligent agent must reason using **degrees of belief** instead of only true/false logic.

### Sources of uncertainty

1. **Partial observability**

=> The agent cannot see the complete state of the world.

2. **Noisy sensors**

=> Sensor readings may be inaccurate.

3. **Uncertain action effects**

=> The same action may produce different results.

4. **Incomplete knowledge**

=> Some required facts may be missing.

5. **Ambiguous language**

=> Same word or sentence may have more than one meaning.

### Example

=> A medical diagnosis system may know that fever and cough are present, but it cannot be fully certain whether the patient has flu, malaria or another disease.

## **5.2 Monotonic and Non-Monotonic Reasoning**

### Monotonic reasoning

=> In monotonic reasoning, adding new facts to the knowledge base never invalidates old conclusions.

```text
If KB entails alpha, then KB + new facts also entails alpha.
```

### Non-monotonic reasoning

=> In non-monotonic reasoning, adding new facts may invalidate previous conclusions.

### Comparison

| Monotonic Reasoning | Non-Monotonic Reasoning |
|---|---|
| Conclusions never decrease after adding facts | Conclusions may change after adding facts |
| Suitable for mathematical logic | Suitable for common-sense reasoning |
| No exceptions | Handles exceptions |
| Example: theorem proving | Example: birds normally fly, but penguins do not |

### Example

```text
Bird(Tweety) => Flies(Tweety)
Penguin(Tweety) => ¬Flies(Tweety)
```

=> Initially, Tweety may be assumed to fly. After learning Tweety is a penguin, the conclusion changes.

## **5.3 Ambiguity Under Uncertainty**

=> Natural language often contains ambiguous words.

=> Correct meaning depends on surrounding context and background knowledge.

### Example

```text
The old man's glasses were filled with sherry.
```

### Correct meaning

=> Here, **glasses** means drinking glasses, not spectacles.

### Information needed to choose correct meaning

1. **Filled with sherry**

=> Sherry is a drink, so it is normally poured into drinking glasses.

2. **Plural object**

=> Several drinking glasses can be filled.

3. **Semantic compatibility**

=> A container can be filled with liquid.

### Information suggesting incorrect meaning

1. **Old man**

=> Old people commonly wear spectacles.

2. **Word glasses**

=> The word can also mean spectacles.

=> The final interpretation is chosen using context and probability.

## **5.4 Basic Probability Notation**

=> Probability is used to represent uncertainty numerically.

=> Probability values always lie between 0 and 1.

```text
0 <= P(A) <= 1
```

### Important notation

| Notation | Meaning |
|---|---|
| `P(A)` | Probability of event A |
| `P(¬A)` | Probability that A does not occur |
| `P(A ∧ B)` | Probability that both A and B occur |
| `P(A ∨ B)` | Probability that A or B occurs |
| `P(A | B)` | Probability of A given B |
| `P(A,B)` | Joint probability of A and B |

### Random variable

=> A random variable represents an uncertain quantity.

```text
Weather = {Sunny, Rainy, Cloudy}
```

## **5.5 Unconditional and Conditional Probability**

### Unconditional probability

=> **Unconditional probability** is the probability of an event without considering any extra information.

```text
P(Rain)
```

=> Example: Probability that it rains today is 0.30.

### Conditional probability

=> **Conditional probability** is the probability of an event given that another event is known.

```text
P(A | B) = P(A ∧ B) / P(B)
```

=> Example:

```text
P(Rain | Cloudy)
```

=> This means probability of rain when it is already known that the sky is cloudy.

## **5.6 Axioms of Probability**

=> Probability theory is based on three main axioms.

### Axiom 1: Non-negativity

```text
P(A) >= 0
```

=> Probability of any event cannot be negative.

### Axiom 2: Normalization

```text
P(True) = 1
P(False) = 0
```

=> A certain event has probability 1 and an impossible event has probability 0.

### Axiom 3: Additivity

=> For mutually exclusive events A and B:

```text
P(A ∨ B) = P(A) + P(B)
```

=> General addition rule:

```text
P(A ∨ B) = P(A) + P(B) - P(A ∧ B)
```

### Useful derived rules

1. Complement rule:

```text
P(¬A) = 1 - P(A)
```

2. Product rule:

```text
P(A ∧ B) = P(A | B)P(B)
```

3. Chain rule:

```text
P(A,B,C) = P(A | B,C)P(B | C)P(C)
```

## **5.7 Bayes Theorem**

=> **Bayes theorem** is used to calculate the probability of a cause when evidence is known.

### Formula

```text
P(H | E) = P(E | H)P(H) / P(E)
```

| Term | Meaning |
|---|---|
| `H` | Hypothesis |
| `E` | Evidence |
| `P(H)` | Prior probability |
| `P(E | H)` | Likelihood |
| `P(H | E)` | Posterior probability |

### Expanded form

```text
P(H | E) = P(E | H)P(H) / [P(E | H)P(H) + P(E | ¬H)P(¬H)]
```

### Example

=> If a disease is rare but a test is positive, Bayes theorem helps calculate the actual probability that the patient has the disease.

## **5.8 Inference Using Full Joint Distribution**

=> A **full joint distribution** gives probabilities for every possible combination of values of all random variables.

### Example variables

```text
Toothache, Cavity
```

### Full joint distribution

| Toothache | Cavity | Probability |
|---|---|---|
| true | true | 0.108 |
| true | false | 0.012 |
| false | true | 0.072 |
| false | false | 0.808 |

### Query example

=> Find probability of cavity:

```text
P(Cavity) = P(Toothache, Cavity) + P(¬Toothache, Cavity)
P(Cavity) = 0.108 + 0.072 = 0.180
```

### Conditional query

=> Find probability of cavity given toothache:

```text
P(Cavity | Toothache) = P(Cavity ∧ Toothache) / P(Toothache)
P(Toothache) = 0.108 + 0.012 = 0.120
P(Cavity | Toothache) = 0.108 / 0.120 = 0.9
```

=> Thus, full joint distribution can answer any probability query, but it becomes very large as variables increase.

## **5.9 Posterior Probability Example**

=> A standard deck has 52 cards.

=> Number of kings = 4.

=> Number of face cards = 12.

=> All kings are face cards.

### Find `P(King | Face)`

```text
P(King | Face) = P(King ∧ Face) / P(Face)
P(King ∧ Face) = P(King) = 4/52
P(Face) = 12/52

P(King | Face) = (4/52) / (12/52)
               = 4/12
               = 1/3
```

=> Posterior probability is `1/3`.

## **5.10 Exam Short Questions**

### 1. What is uncertainty in AI?

=> Uncertainty means the agent does not have complete or exact knowledge about the world, action effects or evidence.

### 2. Why does an agent need probability?

=> An agent needs probability to make rational decisions when knowledge is incomplete, noisy or uncertain.

### 3. Compare monotonic and non-monotonic reasoning.

=> In monotonic reasoning, new facts do not invalidate old conclusions. In non-monotonic reasoning, new facts can change previous conclusions.

### 4. Define unconditional probability.

=> Unconditional probability is the probability of an event without considering extra evidence.

```text
P(A)
```

### 5. Define conditional probability.

=> Conditional probability is the probability of event A when event B is already known.

```text
P(A | B) = P(A ∧ B) / P(B)
```

### 6. State axioms of probability.

=> Probabilities are non-negative, certain event has probability 1, impossible event has probability 0, and mutually exclusive events satisfy `P(A ∨ B)=P(A)+P(B)`.

### 7. Write Bayes theorem.

```text
P(H | E) = P(E | H)P(H) / P(E)
```

### 8. Define prior probability.

=> Prior probability is the probability assigned before observing new evidence.

### 9. Define posterior probability.

=> Posterior probability is the updated probability after observing evidence.

### 10. What is full joint distribution?

=> Full joint distribution gives probabilities for every possible combination of values of all random variables.

### 11. How is inference performed using full joint distribution?

=> Inference is performed by summing probabilities of relevant rows and normalizing when conditional probability is required.

### 12. Calculate `P(King | Face)` for a deck of cards.

```text
P(King | Face) = (4/52) / (12/52) = 4/12 = 1/3
```
