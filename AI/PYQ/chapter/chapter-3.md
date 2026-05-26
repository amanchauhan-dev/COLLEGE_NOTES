# **Chapter 3: Logical Agent & First Order Logic - PYQ Solutions**

## **Q.1 Translate the given sentences into predicate logic. [04]**

### Repeated PYQ entries

```text
Consider the following sentences:
1. Rama likes all kinds of vegetarian food.
2. Oranges are food.
3. Mutton is food.
4. Anything anyone eats and is not killed by is food.
5. Likex eats peanuts and is still alive.
6. Lovex eats everything Likex eats.
Translate these sentences into formulas in Predicate Logic.
[04] [3 Time] [Winter 2025]

OR

Translate these sentences into formulas in predicate logic.
1. John likes all kinds of food.
2. Apples are food.
3. Chicken is food.
4. Anything anyone eats and isn't killed-by is food.
5. Bill eats peanuts and is still alive.
6. Sue eats everything Bill eats.
[04] [Winter 2024]

OR

Describe following facts into predicate logic form.
1. Every child loves Santa.
2. Everyone who loves Santa loves any reindeer.
3. Rudolph is a reindeer, and Rudolph has a red nose.
[03] [Winter 2022]
```

### Answer

### Set 1: Rama, Likex and Lovex

```text
1. ∀x VegetarianFood(x) => Likes(Rama, x)
2. Food(Oranges)
3. Food(Mutton)
4. ∀x∀y Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
5. Eats(Likex, Peanuts) ∧ Alive(Likex)
6. ∀x Eats(Likex, x) => Eats(Lovex, x)
```

### Set 2: John, Bill and Sue

```text
1. ∀x Food(x) => Likes(John, x)
2. Food(Apples)
3. Food(Chicken)
4. ∀x∀y Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
5. Eats(Bill, Peanuts) ∧ Alive(Bill)
6. ∀x Eats(Bill, x) => Eats(Sue, x)
```

### Set 3: Santa and Rudolph

```text
1. ∀x Child(x) => Loves(x, Santa)
2. ∀x∀y Loves(x, Santa) ∧ Reindeer(y) => Loves(x, y)
3. Reindeer(Rudolph) ∧ RedNose(Rudolph)
```

## **Q.2 Convert `P <=> (Q ∨ R)` to CNF. [03]**

### Repeated PYQ entries

```text
Convert the logical statement P <=> (Q V R) to CNF(conjunctive normal form).
[03] [3 Time] [Winter 2025]

OR

Convert the logical statement P <=> (Q V R) to conjunctive normal form.
[03] [Summer 2024]

OR

Convert the logical statement to conjunctive normal form.
[04] [Winter 2022]
```

### Answer

```text
P <=> (Q ∨ R)
= (P => (Q ∨ R)) ∧ ((Q ∨ R) => P)
= (¬P ∨ Q ∨ R) ∧ (¬(Q ∨ R) ∨ P)
= (¬P ∨ Q ∨ R) ∧ ((¬Q ∧ ¬R) ∨ P)
= (¬P ∨ Q ∨ R) ∧ (P ∨ ¬Q) ∧ (P ∨ ¬R)
```

=> Final CNF:

```text
(¬P ∨ Q ∨ R) ∧ (P ∨ ¬Q) ∧ (P ∨ ¬R)
```

## **Q.3 Convert the given food statements to CNF. [03]**

### Repeated PYQ entries

```text
Convert the logical statement to conjunctive normal form:
1. Ravi likes all kind of food
2. Apples and chicken are food
3. Anything anyone eats and is not killed is food.
[03] [Summer 2024]
```

### Answer

### Predicate logic form

```text
1. ∀x Food(x) => Likes(Ravi,x)
2. Food(Apples) ∧ Food(Chicken)
3. ∀x∀y Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
```

### CNF clauses

```text
1. ¬Food(x) ∨ Likes(Ravi,x)
2. Food(Apples)
3. Food(Chicken)
4. ¬Eats(x,y) ∨ KilledBy(x,y) ∨ Food(y)
```

## **Q.4 Explain tautology and contradiction with example. [03]**

### Repeated PYQ entries

```text
Explain tautology and contradiction with example.
[03] [2 Time] [Summer 2025]

OR

Explain tautology and contradiction in propositional logic.
[03] [Winter 2023]
```

### Answer

=> **Tautology** is a logical formula that is always true for every truth assignment.

```text
P ∨ ¬P
```

=> **Contradiction** is a logical formula that is always false for every truth assignment.

```text
P ∧ ¬P
```

| P | ¬P | P ∨ ¬P | P ∧ ¬P |
|---|---|---|---|
| T | F | T | F |
| F | T | T | F |

## **Q.5 Differentiate propositional logic and predicate logic. [03/04]**

### Repeated PYQ entries

```text
Differentiate propositional logic and predicate logic.
[03] [4 Time] [Winter 2025]

OR

Explain advantages of first-order predicate logic over propositional logic.
[03] [Winter 2023]

OR

Differentiate propositional logic and predicate logic.
[04] [Summer 2023]

OR

Differentiate propositional logic and predicate logic.
[03] [Winter 2022]
```

### Answer

| Propositional Logic | Predicate Logic |
|---|---|
| Represents complete statements as symbols | Represents objects, properties and relations |
| No variables | Uses variables |
| No quantifiers | Uses `∀` and `∃` |
| Less expressive | More expressive |
| Example: `P => Q` | Example: `∀x Human(x) => Mortal(x)` |
| Large number of facts may be needed | General rules can be written compactly |

=> Predicate logic is more powerful because it can represent relations and general rules.

## **Q.6 Give four examples of facts difficult to represent in predicate logic. [04]**

### Repeated PYQ entries

```text
Give four examples of facts difficult to represent in predicate logic.
[04] [Winter 2025]
```

### Answer

1. **Uncertain facts**

=> Example: "It will probably rain tomorrow."

2. **Vague facts**

=> Example: "Ramesh is tall."

3. **Default facts with exceptions**

=> Example: "Birds normally fly, but penguins do not."

4. **Temporal facts**

=> Example: "Ravi was in class before lunch and in lab after lunch."

5. **Beliefs and intentions**

=> Example: "John believes that the exam is easy."

=> These facts are hard because predicate logic is mainly exact, symbolic and truth-based.

## **Q.7 Define knowledge-based agent in AI. [03/07]**

### Repeated PYQ entries

```text
Define knowledge-based agent in AI.
[03] [3 Time] [Winter 2024]

OR

What is knowledge-based agent in AI? Discuss architecture of AI.
[07] [Summer 2024]

OR

Define knowledge-based agent in AI.
[03] [Winter 2021]
```

### Answer

=> **Knowledge-based agent** is an intelligent agent that stores knowledge about the world and uses inference to derive new facts and choose actions.

### Architecture

```text
Environment -> Sensors -> Percepts -> Knowledge Base
                                      |
                                      v
                                Inference Engine
                                      |
                                      v
Environment <- Actuators <- Actions <- Agent
```

### Components

1. **Knowledge base**

=> Stores facts and rules.

2. **Inference engine**

=> Derives new facts from stored knowledge.

3. **TELL**

=> Adds new percepts into the KB.

4. **ASK**

=> Queries the KB to decide action.

5. **Action selection**

=> Uses inferred knowledge to choose the best action.

=> For 3 marks, write definition and components. For 7 marks, include architecture diagram and TELL/ASK explanation.

## **Q.8 Explain Wumpus World problem. [03/07]**

### Repeated PYQ entries

```text
Explain Wumpus world problem.
[03] [4 Time] [Winter 2024]

OR

What is wampus world? Explain in detail.
[07] [Summer 2025]

OR

Explain Wumpus world problem.
[03] [Summer 2024]

OR

Discuss the Wampus World problem in brief.
[03] [Winter 2023]

OR

What is wampus world? Explain in detail.
[07] [Winter 2022]
```

### Answer

=> **Wumpus World** is a 4x4 grid environment used to study knowledge-based logical agents.

=> The agent must find gold, avoid pits and avoid the Wumpus.

### Elements

| Element | Meaning |
|---|---|
| Agent | Searches for gold |
| Wumpus | Monster that kills the agent |
| Pit | Dangerous square |
| Gold | Goal object |

### Percepts

| Percept | Meaning |
|---|---|
| Stench | Wumpus is nearby |
| Breeze | Pit is nearby |
| Glitter | Gold is in current square |
| Bump | Wall hit |
| Scream | Wumpus is killed |

### Actions

1. Move forward.
2. Turn left/right.
3. Grab gold.
4. Shoot arrow.
5. Climb out.

=> The agent uses logic to infer safe squares. For example, if there is no breeze and no stench at `(1,1)`, adjacent squares are safe.

## **Q.9 Explain universal and existential quantifiers with example. [03/04]**

### Repeated PYQ entries

```text
Explain universal and existential quantifiers with example.
[04] [2 Time] [Winter 2023]

OR

Explain Quantifier.
[03] [Summer 2022]
```

### Answer

=> Quantifiers specify how variables are used in first-order logic.

### Universal quantifier

=> `∀` means "for all".

```text
∀x Human(x) => Mortal(x)
```

=> Meaning: All humans are mortal.

### Existential quantifier

=> `∃` means "there exists".

```text
∃x Student(x) ∧ Smart(x)
```

=> Meaning: There exists at least one student who is smart.

## **Q.10 Discuss logical connectives in propositional logic. [03]**

### Repeated PYQ entries

```text
Discuss various logical connectives in propositional logic.
[03] [2 Time] [Winter 2023]

OR

Explain propositional logic.
[03] [Summer 2022]
```

### Answer

=> **Propositional logic** represents facts using propositions that are true or false.

### Logical connectives

| Symbol | Name | Meaning |
|---|---|---|
| `¬P` | NOT | Negation |
| `P ∧ Q` | AND | True if both are true |
| `P ∨ Q` | OR | True if at least one is true |
| `P => Q` | Implication | If P then Q |
| `P <=> Q` | Biconditional | P iff Q |

### Example

```text
P: It is raining
Q: Road is wet
P => Q: If it is raining, road is wet
```

## **Q.11 Differentiate declarative and procedural knowledge. [04]**

### Repeated PYQ entries

```text
Differentiate declarative and procedural knowledge.
[04] [Summer 2022]
```

### Answer

| Declarative Knowledge | Procedural Knowledge |
|---|---|
| Describes facts | Describes how to do tasks |
| "Knowing that" | "Knowing how" |
| Stored as logic, facts or relations | Stored as procedures, rules or programs |
| Easier to modify facts | Changes may require procedure changes |
| Example: `Food(Apple)` | Example: steps to solve a puzzle |

## **Q.12 Show using truth table: `¬(P ∧ Q) ≡ (¬P ∨ ¬Q)`. [03]**

### Repeated PYQ entries

```text
Show using truth table: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q).
[03] [Winter 2021]
```

### Answer

| P | Q | P ∧ Q | ¬(P ∧ Q) | ¬P | ¬Q | ¬P ∨ ¬Q |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

=> The columns of `¬(P ∧ Q)` and `¬P ∨ ¬Q` are identical.

=> Therefore:

```text
¬(P ∧ Q) ≡ (¬P ∨ ¬Q)
```
