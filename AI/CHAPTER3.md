# **3 Logical Agents**

## **3.1 Knowledge-Based Agents**

=> **Knowledge-based agent** is an intelligent agent that stores knowledge about the world and uses inference to derive new facts and choose actions.

=> It contains a **knowledge base (KB)** and an **inference mechanism**.

### Main components

| Component | Meaning |
|---|---|
| **Knowledge Base** | Stores facts and rules |
| **Inference Engine** | Derives new facts from existing knowledge |
| **Percepts** | Information received from environment |
| **Actions** | Decisions made by the agent |

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

### TELL and ASK

1. **TELL**

=> Adds new percepts/facts into the knowledge base.

2. **ASK**

=> Queries the knowledge base to decide what action should be taken.

### Knowledge-based agent program

```text
1. TELL the knowledge base what the agent perceives.
2. ASK the knowledge base what action should be performed.
3. TELL the knowledge base which action was selected.
4. Return the action.
```

## **3.2 Wumpus World**

=> **Wumpus World** is a classic AI environment used to study logical reasoning and knowledge-based agents.

=> It is usually a 4x4 grid containing an agent, a Wumpus, pits and gold.

### Objects

| Object | Meaning |
|---|---|
| **Agent** | Moves in the world and searches for gold |
| **Wumpus** | Monster that kills the agent if entered |
| **Pit** | Dangerous square; agent dies if it falls |
| **Gold** | Goal object to be collected |

### Percepts

| Percept | Meaning |
|---|---|
| **Stench** | Wumpus is in an adjacent square |
| **Breeze** | Pit is in an adjacent square |
| **Glitter** | Gold is in current square |
| **Bump** | Agent hits wall |
| **Scream** | Wumpus is killed |

### Actions

1. Move forward.
2. Turn left.
3. Turn right.
4. Grab gold.
5. Shoot arrow.
6. Climb out.

### Example rules

```text
Breeze(x,y) => Pit is in an adjacent square.
Stench(x,y) => Wumpus is in an adjacent square.
No breeze and no stench => adjacent squares are safe.
```

### Importance

1. It shows reasoning under partial information.
2. It uses propositional logic for safe movement.
3. It demonstrates inference from percepts.
4. It is a standard example of a knowledge-based agent.

## **3.3 Logic in AI**

=> **Logic** is a formal language used to represent facts and reason about them.

=> Logic has two important parts:

| Part | Meaning |
|---|---|
| **Syntax** | Rules for writing valid sentences |
| **Semantics** | Meaning/truth of sentences |

### Important terms

| Term | Meaning |
|---|---|
| **Sentence** | Statement in logic |
| **Model** | Possible world in which a sentence may be true or false |
| **Entailment** | `KB |= alpha` means alpha logically follows from KB |
| **Inference** | Process of deriving new sentences |

## **3.4 Propositional Logic**

=> **Propositional logic** represents knowledge using propositions that are either true or false.

=> It does not describe internal structure of objects.

### Examples

```text
P: It is raining.
Q: Road is wet.
P => Q: If it is raining, then road is wet.
```

### Logical connectives

| Symbol | Name | Meaning |
|---|---|---|
| `¬P` | NOT | True when P is false |
| `P ∧ Q` | AND | True when both P and Q are true |
| `P ∨ Q` | OR | True when at least one is true |
| `P => Q` | Implication | If P then Q |
| `P <=> Q` | Biconditional | P if and only if Q |

### Tautology and contradiction

=> **Tautology** is a formula that is true in every interpretation.

```text
P ∨ ¬P
```

=> **Contradiction** is a formula that is false in every interpretation.

```text
P ∧ ¬P
```

## **3.5 Truth Table**

=> A truth table checks truth values of a logical expression for all combinations of propositions.

### De Morgan's law

```text
¬(P ∧ Q) ≡ (¬P ∨ ¬Q)
```

| P | Q | P ∧ Q | ¬(P ∧ Q) | ¬P | ¬Q | ¬P ∨ ¬Q |
|---|---|---|---|---|---|---|
| T | T | T | F | F | F | F |
| T | F | F | T | F | T | T |
| F | T | F | T | T | F | T |
| F | F | F | T | T | T | T |

=> Since both columns are same, the two expressions are logically equivalent.

## **3.6 Propositional Theorem Proving**

=> **Theorem proving** derives a sentence from a knowledge base using inference rules.

### Common inference rule: Modus Ponens

```text
P
P => Q
Therefore Q
```

### Resolution rule

```text
(A ∨ B), (¬B ∨ C)
----------------
(A ∨ C)
```

=> Resolution is widely used after converting sentences to CNF.

## **3.7 Conjunctive Normal Form (CNF)**

=> **CNF** is a conjunction of clauses where each clause is a disjunction of literals.

### Example

```text
(P ∨ Q) ∧ (¬R ∨ S)
```

### Steps to convert to CNF

1. Remove biconditional:

```text
A <=> B becomes (A => B) ∧ (B => A)
```

2. Remove implication:

```text
A => B becomes ¬A ∨ B
```

3. Move NOT inward using De Morgan's laws.
4. Distribute OR over AND.

### Example: Convert `P <=> (Q ∨ R)` to CNF

```text
P <=> (Q ∨ R)
= (P => (Q ∨ R)) ∧ ((Q ∨ R) => P)
= (¬P ∨ Q ∨ R) ∧ (¬(Q ∨ R) ∨ P)
= (¬P ∨ Q ∨ R) ∧ ((¬Q ∧ ¬R) ∨ P)
= (¬P ∨ Q ∨ R) ∧ (P ∨ ¬Q) ∧ (P ∨ ¬R)
```

## **3.8 Effective Propositional Model Checking**

=> **Model checking** verifies whether a sentence is true in all models where the knowledge base is true.

```text
KB |= alpha
```

=> This means every model that satisfies `KB` also satisfies `alpha`.

### Truth-table entailment

1. Generate all possible truth assignments.
2. Check models where KB is true.
3. If query is true in all such models, KB entails query.

### Limitation

=> If there are `n` symbols, model checking may require `2^n` models.

## **3.9 Agents Based on Propositional Logic**

=> A propositional logic agent stores rules and facts as propositional sentences.

=> It uses inference to choose safe and goal-directed actions.

### Example from Wumpus World

```text
¬Breeze(1,1) => ¬Pit(1,2) ∧ ¬Pit(2,1)
¬Stench(1,1) => ¬Wumpus(1,2) ∧ ¬Wumpus(2,1)
```

=> From these rules, the agent can infer that adjacent squares are safe.

## **3.10 First Order Logic**

=> **First Order Logic (FOL)** represents objects, properties and relations more clearly than propositional logic.

=> It uses predicates, variables, constants, functions and quantifiers.

### Basic elements

| Element | Meaning | Example |
|---|---|---|
| **Constant** | Specific object | `John`, `Rama` |
| **Variable** | Object placeholder | `x`, `y` |
| **Predicate** | Relation/property | `Food(x)`, `Likes(John,x)` |
| **Function** | Maps object to object | `Mother(x)` |
| **Quantifier** | Scope of variables | `∀`, `∃` |

## **3.11 Syntax and Semantics of FOL**

### Atomic sentence

```text
Predicate(term1, term2, ...)
```

=> Example:

```text
Likes(John, Apple)
Food(Apple)
```

### Universal quantifier

=> `∀x` means "for all x".

```text
∀x Human(x) => Mortal(x)
```

### Existential quantifier

=> `∃x` means "there exists x".

```text
∃x Student(x) ∧ Smart(x)
```

## **3.12 Using First Order Logic**

=> FOL is used to represent general facts and rules.

### Examples

1. Every child loves Santa:

```text
∀x Child(x) => Loves(x, Santa)
```

2. All food is liked by John:

```text
∀x Food(x) => Likes(John, x)
```

3. Bill eats peanuts:

```text
Eats(Bill, Peanuts)
```

### Advantages over propositional logic

1. Can represent objects and relations.
2. Can use variables.
3. Can express general rules using quantifiers.
4. More compact than propositional logic.

## **3.13 Declarative and Procedural Knowledge**

| Declarative Knowledge | Procedural Knowledge |
|---|---|
| Describes facts and truths | Describes how to perform actions |
| "Knowing that" | "Knowing how" |
| Easy to modify facts | Often embedded in procedures |
| Used in logic and databases | Used in production rules/programs |
| Example: `Food(Apple)` | Example: steps to diagnose disease |

## **3.14 Facts Difficult to Represent in Predicate Logic**

=> Predicate logic is powerful but some facts are difficult to represent naturally.

### Examples

1. **Uncertain facts**

=> "It will probably rain tomorrow."

2. **Vague facts**

=> "Ramesh is tall."

3. **Default facts with exceptions**

=> "Birds normally fly, but penguins do not."

4. **Temporal facts**

=> "Aman was in class before lunch and in lab after lunch."

5. **Beliefs and intentions**

=> "Ravi believes that the exam is easy."

## **3.15 Exam Short Questions**

### 1. Define knowledge-based agent.

=> A knowledge-based agent stores facts and rules in a knowledge base and uses inference to choose actions.

### 2. What are TELL and ASK?

=> TELL adds facts to the knowledge base, while ASK queries the knowledge base for answers or actions.

### 3. Explain Wumpus World.

=> Wumpus World is a grid environment where an agent uses logical inference to find gold while avoiding pits and the Wumpus.

### 4. List Wumpus World percepts.

=> Stench, breeze, glitter, bump and scream.

### 5. Define propositional logic.

=> Propositional logic represents knowledge using propositions that are either true or false.

### 6. List logical connectives.

=> NOT, AND, OR, implication and biconditional.

### 7. Define tautology and contradiction.

=> A tautology is always true, while a contradiction is always false.

### 8. What is CNF?

=> CNF is a conjunction of clauses where each clause is a disjunction of literals.

### 9. Convert `P <=> (Q ∨ R)` into CNF.

```text
(¬P ∨ Q ∨ R) ∧ (P ∨ ¬Q) ∧ (P ∨ ¬R)
```

### 10. Define model checking.

=> Model checking verifies whether a query is true in every model where the knowledge base is true.

### 11. Define first-order logic.

=> First-order logic represents objects, properties, relations, variables and quantifiers.

### 12. List elements of FOL.

=> Constants, variables, predicates, functions, connectives and quantifiers.

### 13. Explain universal and existential quantifiers.

=> Universal quantifier `∀` means "for all"; existential quantifier `∃` means "there exists".

### 14. Differentiate propositional logic and predicate logic.

=> Propositional logic treats whole statements as symbols, while predicate logic represents objects, relations and general rules using variables and quantifiers.

### 15. Differentiate declarative and procedural knowledge.

=> Declarative knowledge states facts, while procedural knowledge describes how to perform actions.
