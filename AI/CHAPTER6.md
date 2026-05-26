# **6 Probabilistic Reasoning**

## **6.1 Introduction**

=> **Probabilistic reasoning** is reasoning with uncertain knowledge using probability theory.

=> It helps an AI system make decisions when facts are incomplete, noisy or uncertain.

### Example

=> A medical diagnosis system may reason about disease using symptoms, test reports and prior disease probability.

## **6.2 Representing Knowledge in an Uncertain Domain**

=> In uncertain domains, simple true/false logic is not enough.

=> We represent belief using probabilities.

### Requirements

1. Represent random variables.
2. Represent dependencies between variables.
3. Store probability values compactly.
4. Perform inference from evidence.

### Example random variables

```text
Burglary = {true, false}
Earthquake = {true, false}
Alarm = {true, false}
JohnCalls = {true, false}
MaryCalls = {true, false}
```

## **6.3 Bayesian Network**

=> A **Bayesian Network** is a graphical model that represents probabilistic relationships among variables.

=> It is a directed acyclic graph (DAG).

### Components

| Component | Meaning |
|---|---|
| **Nodes** | Random variables |
| **Directed edges** | Direct dependency between variables |
| **Conditional Probability Table (CPT)** | Probability of each node given its parents |

### Example

```text
Burglary      Earthquake
    \          /
      Alarm
      /   \
JohnCalls  MaryCalls
```

### Meaning

=> Burglary and Earthquake can cause Alarm.

=> Alarm can cause John and Mary to call.

## **6.4 Semantics of Bayesian Networks**

=> A Bayesian network represents the full joint distribution compactly.

=> Each variable is conditionally independent of its non-descendants given its parents.

### Joint distribution formula

```text
P(x1, x2, ..., xn) = product P(xi | Parents(Xi))
```

### Example

For the burglary network:

```text
P(B,E,A,J,M) = P(B)P(E)P(A | B,E)P(J | A)P(M | A)
```

=> This compact factorization avoids storing every full joint probability separately.

## **6.5 Efficient Representation of Conditional Distribution**

=> A full joint table grows exponentially with number of variables.

=> Bayesian networks reduce storage by using local CPTs.

### Storage comparison

| Representation | Storage |
|---|---|
| Full joint distribution for `n` Boolean variables | `2^n - 1` independent values |
| Bayesian network | Depends on number of parents per node |

### Boolean CPT size

=> If a Boolean node has `k` Boolean parents, its CPT needs:

```text
2^k
```

probability values.

### Advantages

1. Compact representation.
2. Clear dependency structure.
3. Supports efficient inference.
4. Easier to update local probabilities.

## **6.6 Exact Inference in Bayesian Networks**

=> **Exact inference** computes exact posterior probabilities from a Bayesian network.

### Query form

```text
P(Query | Evidence)
```

### Example

```text
P(Burglary | JohnCalls=true, MaryCalls=true)
```

### Common exact inference methods

1. **Inference by enumeration**

=> Sums over hidden variables using the joint distribution.

2. **Variable elimination**

=> Reorders computation and removes hidden variables one by one.

3. **Belief propagation**

=> Efficient for tree-structured networks.

### Inference by enumeration

```text
P(X | e) = alpha P(X, e)
```

=> `alpha` is a normalization constant.

### Example idea

=> To compute `P(Burglary | JohnCalls, MaryCalls)`, sum over hidden variables Earthquake and Alarm.

```text
P(B | j,m) = alpha sum_e sum_a P(B)P(e)P(a | B,e)P(j | a)P(m | a)
```

## **6.7 Approximate Inference in Bayesian Networks**

=> Exact inference may be expensive for large networks.

=> **Approximate inference** estimates probabilities using sampling.

### Common approximate methods

1. **Prior sampling**

=> Generate samples from the network according to topological order.

2. **Rejection sampling**

=> Reject samples that do not match the evidence.

3. **Likelihood weighting**

=> Fix evidence variables and weight samples by likelihood of evidence.

4. **Gibbs sampling**

=> Repeatedly resample non-evidence variables conditioned on current values of other variables.

### Advantages

1. Useful for large networks.
2. Avoids complete enumeration.
3. Accuracy improves with more samples.

### Limitations

1. Gives approximate answer, not exact.
2. May require many samples.
3. Rare evidence can make sampling inefficient.

## **6.8 Applications of Bayesian Networks**

### 1. Medical diagnosis

=> Diseases, symptoms and test results are represented as random variables.

=> The network calculates probability of disease given symptoms.

### 2. Fault diagnosis

=> Used to detect likely causes of machine or system failure.

### 3. Spam filtering

=> Uses word occurrences to estimate whether an email is spam.

### 4. Weather prediction

=> Uses uncertain variables such as humidity, pressure and wind.

### 5. Risk analysis

=> Used in finance, safety systems and decision support.

## **6.9 Maximum A Posteriori (MAP) Learning**

=> **Maximum A Posteriori (MAP)** learning chooses the hypothesis that is most probable after observing the data.

### Formula

```text
h_MAP = argmax_h P(h | D)
```

Using Bayes theorem:

```text
h_MAP = argmax_h P(D | h)P(h)
```

| Term | Meaning |
|---|---|
| `h` | Hypothesis |
| `D` | Observed data |
| `P(h)` | Prior probability of hypothesis |
| `P(D | h)` | Likelihood of data given hypothesis |
| `P(h | D)` | Posterior probability |

### MAP vs Maximum Likelihood

| MAP Learning | Maximum Likelihood |
|---|---|
| Uses prior and data | Uses only data likelihood |
| Maximizes `P(D | h)P(h)` | Maximizes `P(D | h)` |
| Better when prior knowledge is useful | Useful when no prior is assumed |

## **6.10 Exam Short Questions**

### 1. Define probabilistic reasoning.

=> Probabilistic reasoning is reasoning with uncertain knowledge using probability theory.

### 2. What is Bayesian network?

=> A Bayesian network is a directed acyclic graph that represents probabilistic dependencies among random variables.

### 3. List components of Bayesian network.

=> Nodes, directed edges and conditional probability tables are the main components.

### 4. What is conditional probability table?

=> A CPT stores the probability of each value of a variable for every combination of its parent values.

### 5. State semantics of Bayesian networks.

=> Each node is conditionally independent of its non-descendants given its parents.

### 6. Write Bayesian network joint distribution formula.

```text
P(x1, x2, ..., xn) = product P(xi | Parents(Xi))
```

### 7. Why are Bayesian networks compact?

=> They store local conditional probabilities instead of the complete full joint distribution.

### 8. Define exact inference.

=> Exact inference computes exact posterior probabilities from a Bayesian network.

### 9. Define approximate inference.

=> Approximate inference estimates probabilities using sampling when exact computation is expensive.

### 10. List approximate inference methods.

=> Prior sampling, rejection sampling, likelihood weighting and Gibbs sampling.

### 11. Give applications of Bayesian networks.

=> Medical diagnosis, fault diagnosis, spam filtering, weather prediction and risk analysis.

### 12. Define MAP learning.

=> MAP learning selects the hypothesis with maximum posterior probability after observing data.

```text
h_MAP = argmax_h P(h | D)
```
