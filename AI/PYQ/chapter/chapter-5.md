# **Chapter 5: Uncertainty - PYQ Solutions**

## **Q.1 Compare monotonic and non-monotonic reasoning. [03]**

### Repeated PYQ entries

```text
Compare monotonic and non-monotonic reasoning.
[03] [Winter 2025]
```

### Answer

| Monotonic Reasoning | Non-Monotonic Reasoning |
|---|---|
| Adding new facts never invalidates old conclusions | Adding new facts may invalidate old conclusions |
| Suitable for mathematical logic | Suitable for common-sense reasoning |
| Does not handle exceptions well | Handles exceptions |
| Knowledge only increases | Beliefs may change |
| Example: theorem proving | Example: birds normally fly, but penguins do not |

=> In AI, non-monotonic reasoning is useful because real-world knowledge often has exceptions.

## **Q.2 Explain ambiguity in the sentence about glasses and sherry. [04]**

### Repeated PYQ entries

```text
Consider the sentence: The old man's glasses were filled with sherry. What information is
necessary to choose the correct meaning for the word "glasses"? What information suggests the
incorrect meaning?
[04] [Winter 2025]
```

### Answer

=> The word **glasses** is ambiguous.

=> It may mean:

1. Drinking glasses.
2. Spectacles worn for eyesight.

### Correct meaning

=> In this sentence, **glasses** means drinking glasses.

### Information supporting correct meaning

1. **Filled with sherry**

=> Sherry is a drink, and drinks are poured into drinking glasses.

2. **Container relation**

=> A drinking glass can be filled with liquid.

3. **Plural usage**

=> Many drinking glasses can be filled at the same time.

### Information suggesting incorrect meaning

1. **Old man**

=> Old people often wear spectacles.

2. **Word glasses**

=> In common usage, glasses can mean spectacles.

=> The correct interpretation is selected using context and background knowledge.

## **Q.3 Describe axioms of probability theory. [03/04]**

### Repeated PYQ entries

```text
Describe axioms of probability theory.
[04] [4 Time] [Summer 2025, Winter 2024]

OR

Describe axioms of probability theory.
[03] [Summer 2024]

OR

Describe axioms of probability theory.
[04] [Winter 2022]
```

### Answer

=> Probability theory follows basic axioms used for reasoning under uncertainty.

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

=> If A and B are mutually exclusive:

```text
P(A ∨ B) = P(A) + P(B)
```

=> General form:

```text
P(A ∨ B) = P(A) + P(B) - P(A ∧ B)
```

### Derived rule

```text
P(¬A) = 1 - P(A)
```

=> These axioms ensure probability values remain logically consistent.

## **Q.4 Discuss Bayes theorem. [03/04]**

### Repeated PYQ entries

```text
Discuss Bayes theorem.
[03] [4 Time] [Winter 2024]

OR

Discuss Bayes theorem.
[04] [Summer 2023]

OR

Discuss Bayes theorem.
[03] [Summer 2022, Winter 2021]
```

### Answer

=> **Bayes theorem** is used to compute posterior probability of a hypothesis after observing evidence.

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

=> If a medical test is positive, Bayes theorem calculates the probability that the patient actually has the disease.

## **Q.5 Explain unconditional and conditional probability with examples. [03]**

### Repeated PYQ entries

```text
Explain unconditional and conditional probability with examples.
[03] [Winter 2023]
```

### Answer

### Unconditional probability

=> It is the probability of an event without any extra condition.

```text
P(Rain)
```

=> Example: Probability of rain today is `0.30`.

### Conditional probability

=> It is the probability of an event when another event is already known.

```text
P(A | B) = P(A ∧ B) / P(B)
```

=> Example:

```text
P(Rain | Cloudy)
```

=> This means probability of rain given that the sky is cloudy.

## **Q.6 Explain inference using full joint distribution with example. [04]**

### Repeated PYQ entries

```text
Explain inference using full joint distribution in uncertainty using an appropriate example.
[04] [2 Time] [Winter 2023]

OR

Write inference using full joint distributions with example.
[04] [Winter 2021]
```

### Answer

=> A **full joint distribution** lists probabilities for all combinations of values of all random variables.

### Example

| Toothache | Cavity | Probability |
|---|---|---|
| true | true | 0.108 |
| true | false | 0.012 |
| false | true | 0.072 |
| false | false | 0.808 |

### Find `P(Cavity)`

```text
P(Cavity) = P(Toothache, Cavity) + P(¬Toothache, Cavity)
P(Cavity) = 0.108 + 0.072
P(Cavity) = 0.180
```

### Find `P(Cavity | Toothache)`

```text
P(Cavity | Toothache) = P(Cavity ∧ Toothache) / P(Toothache)
P(Toothache) = 0.108 + 0.012 = 0.120
P(Cavity | Toothache) = 0.108 / 0.120 = 0.9
```

=> Full joint distribution can answer any probability query, but it becomes large for many variables.

## **Q.7 Calculate `P(King | Face)` from a deck of cards. [04]**

### Repeated PYQ entries

```text
From a standard deck of playing cards, a single card is drawn. The probability that the card is king
is 4/52, then calculate posterior probability P(King|Face), which means the drawn face card is a
king card.
[04] [Winter 2021]
```

### Answer

=> Total cards = 52.

=> Kings = 4.

=> Face cards = Jack, Queen, King of each suit = 12.

=> Every king is a face card.

### Calculation

```text
P(King | Face) = P(King ∧ Face) / P(Face)

P(King ∧ Face) = P(King) = 4/52
P(Face) = 12/52

P(King | Face) = (4/52) / (12/52)
               = 4/12
               = 1/3
```

=> Posterior probability is:

```text
P(King | Face) = 1/3
```
