# **Chapter 6: Probabilistic Reasoning - PYQ Solutions**

## **Q.1 Discuss Bayesian network and its applications. [03/04/07]**

### Repeated PYQ entries

```text
Discuss Bayesian network and its two applications.
[03] [5 Time] [Winter 2025]

OR

Discuss Bayesian network and its application.
[04] [Summer 2025]

OR

Discuss Bayesian network and its application.
[07] [Winter 2024]

OR

Discuss Bayesian network and its applications.
[04] [Summer 2024, Summer 2023]

OR

Discuss Bayesian network and its applications.
[04] [Summer 2022, Winter 2021]
```

### Answer

=> A **Bayesian Network** is a graphical model used to represent probabilistic relationships among random variables.

=> It is a **directed acyclic graph (DAG)**.

### Components

| Component | Meaning |
|---|---|
| Nodes | Random variables |
| Directed edges | Direct dependency |
| CPT | Conditional Probability Table for each node |

### Example

```text
Burglary      Earthquake
    \          /
      Alarm
      /   \
JohnCalls  MaryCalls
```

=> Burglary and Earthquake can cause Alarm.

=> Alarm can cause John and Mary to call.

### Semantics

=> Bayesian network represents full joint distribution as:

```text
P(x1, x2, ..., xn) = product P(xi | Parents(Xi))
```

=> For the above example:

```text
P(B,E,A,J,M) = P(B)P(E)P(A | B,E)P(J | A)P(M | A)
```

### Applications

1. **Medical diagnosis**

=> Calculates probability of disease from symptoms and test results.

2. **Fault diagnosis**

=> Finds likely cause of machine or system failure.

3. **Spam filtering**

=> Estimates whether an email is spam based on words.

4. **Weather prediction**

=> Predicts weather from uncertain variables.

### Advantages

1. Represents uncertain knowledge clearly.
2. Reduces storage compared to full joint distribution.
3. Supports probabilistic inference.
4. Shows dependencies visually.

## **Q.2 Explain inference in Bayesian networks using an appropriate example. [07]**

### Repeated PYQ entries

```text
Explain inference in Bayesian networks using an appropriate example.
[07] [Winter 2023]
```

### Answer

=> **Inference in Bayesian networks** means computing posterior probability of query variables given evidence.

### Query form

```text
P(Query | Evidence)
```

### Example network

```text
Burglary      Earthquake
    \          /
      Alarm
      /   \
JohnCalls  MaryCalls
```

### Example query

```text
P(Burglary | JohnCalls=true, MaryCalls=true)
```

=> We want to know probability of burglary when both John and Mary call.

### Joint distribution

```text
P(B,E,A,J,M) = P(B)P(E)P(A | B,E)P(J | A)P(M | A)
```

### Inference by enumeration

=> Hidden variables are summed out.

```text
P(B | j,m) = alpha P(B,j,m)
```

```text
P(B | j,m) = alpha sum_e sum_a P(B)P(e)P(a | B,e)P(j | a)P(m | a)
```

=> `alpha` is a normalization constant used to make probabilities sum to 1.

### Exact inference methods

1. Inference by enumeration.
2. Variable elimination.
3. Belief propagation for tree-like networks.

### Approximate inference methods

1. Prior sampling.
2. Rejection sampling.
3. Likelihood weighting.
4. Gibbs sampling.

=> Bayesian network inference is useful because it updates belief when new evidence is observed.

## **Q.3 What is Maximum a Posteriori (MAP) learning in Bayesian learning? Explain. [04]**

### Repeated PYQ entries

```text
What is Maximum a Posteriori (MAP) learning in Bayesian learning? Explain.
[04] [Winter 2022]
```

### Answer

=> **Maximum A Posteriori (MAP)** learning selects the hypothesis that has the highest posterior probability after observing data.

### Formula

```text
h_MAP = argmax_h P(h | D)
```

Using Bayes theorem:

```text
P(h | D) = P(D | h)P(h) / P(D)
```

=> Since `P(D)` is same for all hypotheses:

```text
h_MAP = argmax_h P(D | h)P(h)
```

### Meaning of terms

| Term | Meaning |
|---|---|
| `h` | Hypothesis |
| `D` | Observed data |
| `P(h)` | Prior probability |
| `P(D | h)` | Likelihood |
| `P(h | D)` | Posterior probability |

### MAP vs Maximum Likelihood

| MAP Learning | Maximum Likelihood |
|---|---|
| Uses prior and data | Uses only data |
| Maximizes `P(D | h)P(h)` | Maximizes `P(D | h)` |
| Better when prior knowledge is available | Useful when no prior is used |

=> MAP learning is important because it combines previous belief with observed evidence.
