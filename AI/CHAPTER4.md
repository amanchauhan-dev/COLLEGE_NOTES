# **4 Inference in First Order Logic**

## **4.1 Introduction**

=> **Inference** means deriving new sentences from existing facts and rules.

=> In first-order logic, inference is more powerful than propositional logic because it uses variables, predicates and quantifiers.

### Example

```text
∀x Human(x) => Mortal(x)
Human(Socrates)
Therefore Mortal(Socrates)
```

## **4.2 Propositional vs First Order Inference**

| Propositional Inference | First Order Inference |
|---|---|
| Works with whole propositions | Works with objects, predicates and variables |
| No variables or quantifiers | Uses variables and quantifiers |
| Less expressive | More expressive |
| Example: `P => Q` | Example: `∀x Human(x) => Mortal(x)` |
| Simpler inference | Needs substitution and unification |

=> FOL inference often converts quantified rules into usable instances.

## **4.3 Soundness and Completeness**

### Soundness

=> An inference procedure is **sound** if every sentence it derives is logically correct.

```text
If KB ⊢ alpha, then KB |= alpha
```

=> It never proves a false conclusion from true premises.

### Completeness

=> An inference procedure is **complete** if it can derive every sentence that logically follows from the knowledge base.

```text
If KB |= alpha, then KB ⊢ alpha
```

=> It can find all valid conclusions.

## **4.4 Inference Rules**

### Modus Ponens

```text
P
P => Q
Therefore Q
```

=> Example:

```text
Rain
Rain => WetRoad
Therefore WetRoad
```

### Modus Tollens

```text
P => Q
¬Q
Therefore ¬P
```

=> Example:

```text
Rain => WetRoad
¬WetRoad
Therefore ¬Rain
```

### Universal Instantiation

```text
∀x Human(x) => Mortal(x)
Human(John) => Mortal(John)
```

### Existential Instantiation

```text
∃x Student(x)
Student(A)
```

=> A new constant `A` is introduced.

## **4.5 Substitution**

=> **Substitution** replaces variables by terms.

### Example

```text
Likes(x, Mango)
Substitution: {x/Ravi}
Result: Likes(Ravi, Mango)
```

=> Substitution is written using theta `θ`.

```text
θ = {x/Ravi, y/Mango}
```

## **4.6 Unification**

=> **Unification** is the process of finding a substitution that makes two logical expressions identical.

=> The substitution produced is called a **unifier**.

=> The most general useful substitution is called **Most General Unifier (MGU)**.

### Purpose

1. Match facts with rules.
2. Apply inference rules in FOL.
3. Support resolution, forward chaining and backward chaining.
4. Find variable bindings that make predicates identical.

### Example

```text
Knows(John, x)
Knows(y, Mother(y))
```

=> To unify, set:

```text
y = John
x = Mother(John)
```

=> MGU:

```text
{y/John, x/Mother(John)}
```

### Unification failure

```text
test(11), test(y)
```

=> MGU is `{y/11}`.

```text
P(x), Q(x)
```

=> Fails because predicate names are different.

## **4.7 Forward Chaining**

=> **Forward chaining** is a data-driven inference method.

=> It starts from known facts and applies rules to derive new facts until the goal is reached.

### Rule form

```text
Premise1 ∧ Premise2 ∧ ... => Conclusion
```

### Algorithm

```text
1. Start with known facts in KB.
2. Find rules whose premises match known facts.
3. Infer the conclusions of those rules.
4. Add new conclusions to KB.
5. Repeat until query is proved or no new fact can be inferred.
```

### Example

```text
Facts: Human(Socrates)
Rule:  Human(x) => Mortal(x)
Infer: Mortal(Socrates)
```

### Advantages

1. Good when many facts are available.
2. Useful for monitoring and diagnosis.
3. Can derive all possible conclusions.

## **4.8 Backward Chaining**

=> **Backward chaining** is a goal-driven inference method.

=> It starts with a query and works backward to prove required facts.

### Algorithm

```text
1. Start with goal/query.
2. Find a rule whose conclusion matches the goal.
3. Make rule premises subgoals.
4. Prove each subgoal from facts or other rules.
5. If all subgoals are proved, goal is proved.
```

### Example

```text
Goal: Mortal(Socrates)
Rule: Human(x) => Mortal(x)
Subgoal: Human(Socrates)
Fact: Human(Socrates)
Therefore Mortal(Socrates)
```

### Advantages

1. Good for answering specific queries.
2. Avoids deriving unrelated facts.
3. Used in Prolog and expert systems.

## **4.9 Forward Chaining vs Backward Chaining**

| Forward Chaining | Backward Chaining |
|---|---|
| Data-driven | Goal-driven |
| Starts from facts | Starts from query |
| Derives all possible facts | Proves only required goal |
| Useful when many conclusions are needed | Useful for specific questions |
| May infer irrelevant facts | More focused |
| Example: diagnosis from symptoms | Example: proving a theorem |

## **4.10 Choosing Forward or Backward Search Direction**

### Use forward chaining when

1. Many initial facts are available.
2. We want to know all possible conclusions.
3. Data arrives continuously.
4. Number of possible goals is large.

### Use backward chaining when

1. Goal/query is known.
2. Number of possible goals is small.
3. We only need to prove one conclusion.
4. Rules naturally work backward from goal to facts.

## **4.11 Resolution in First Order Logic**

=> **Resolution** is a rule of inference used to prove a statement by contradiction.

=> It is complete for first-order logic when used with proper conversion to clause form.

### Resolution rule

```text
(A ∨ B)
(¬B ∨ C)
---------
(A ∨ C)
```

### Steps for FOL resolution

1. Convert all sentences to first-order logic.
2. Remove implications.
3. Move negation inward.
4. Standardize variables.
5. Remove existential quantifiers using Skolemization.
6. Drop universal quantifiers.
7. Convert to CNF.
8. Negate the query and add it to KB.
9. Apply unification and resolution.
10. If empty clause is derived, query is proved.

## **4.12 Example: Prove West is Criminal**

### Knowledge

1. It is a crime for an American to sell weapons to hostile nations.
2. All missiles were sold to Nono by West.
3. Nono is an enemy of America.
4. Enemies of America are hostile.
5. Nono has missiles.
6. Missiles are weapons.
7. West is an American.

### FOL representation

```text
∀x∀y∀z American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) => Criminal(x)
∀x Missile(x) ∧ Owns(Nono,x) => Sells(West,x,Nono)
Enemy(Nono, America)
∀x Enemy(x, America) => Hostile(x)
∃x Missile(x) ∧ Owns(Nono,x)
∀x Missile(x) => Weapon(x)
American(West)
```

### Proof idea

=> From `∃x Missile(x) ∧ Owns(Nono,x)`, assume a missile `M1`.

```text
Missile(M1)
Owns(Nono, M1)
```

=> Since missiles are weapons:

```text
Weapon(M1)
```

=> Since West sold Nono's missile to Nono:

```text
Sells(West, M1, Nono)
```

=> Since Nono is enemy of America:

```text
Hostile(Nono)
```

=> Since West is American and sold a weapon to a hostile nation:

```text
Criminal(West)
```

=> Therefore, by resolution, **West is criminal** is proved.

## **4.13 Example: Backward Chaining to Prove John Likes Peanuts**

### Knowledge

```text
∀x Food(x) => Likes(John,x)
Food(Apples)
Food(Chicken)
∀x∀y Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
Eats(Bill, Peanuts)
¬KilledBy(Bill, Peanuts)
∀x Eats(Bill,x) => Eats(Sue,x)
```

### Goal

```text
Likes(John, Peanuts)
```

### Backward proof

1. To prove `Likes(John, Peanuts)`, use:

```text
Food(x) => Likes(John,x)
```

=> Subgoal:

```text
Food(Peanuts)
```

2. To prove `Food(Peanuts)`, use:

```text
Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
```

=> Subgoals:

```text
Eats(Bill, Peanuts)
¬KilledBy(Bill, Peanuts)
```

3. Both subgoals are facts.

=> Therefore:

```text
Food(Peanuts)
Likes(John, Peanuts)
```

## **4.14 Example: Resolution to Find Food Vinod/Sue Eats**

=> If Sachin/Bill eats peanuts and is not killed by peanuts, then peanuts are food.

=> If Vinod/Sue eats everything Sachin/Bill eats, then Vinod/Sue eats peanuts.

```text
Eats(Sachin, Peanuts)
∀x Eats(Sachin,x) => Eats(Vinod,x)
```

=> Therefore:

```text
Eats(Vinod, Peanuts)
```

=> If the question asks what food Vinod eats, answer:

```text
Peanuts
```

## **4.15 Exam Short Questions**

### 1. Define inference.

=> Inference is the process of deriving new facts or conclusions from existing facts and rules.

### 2. Differentiate propositional and first-order inference.

=> Propositional inference works on whole true/false statements, while first-order inference works with predicates, variables, objects and quantifiers.

### 3. Define soundness and completeness.

=> Soundness means every derived conclusion is correct. Completeness means every logically valid conclusion can be derived.

### 4. Define unification.

=> Unification is the process of finding substitutions that make two predicate logic expressions identical.

### 5. What is MGU?

=> MGU stands for Most General Unifier, the most general substitution that unifies two expressions.

### 6. State purpose of unification.

=> Unification is used to match facts with rules during resolution, forward chaining and backward chaining.

### 7. Define forward chaining.

=> Forward chaining is data-driven reasoning that starts from known facts and applies rules to derive new facts.

### 8. Define backward chaining.

=> Backward chaining is goal-driven reasoning that starts from a query and works backward to prove required facts.

### 9. Differentiate forward and backward chaining.

=> Forward chaining starts from facts and derives conclusions; backward chaining starts from the goal and proves its subgoals.

### 10. What factors decide forward or backward search?

=> Number of facts, number of goals, branching factor, whether all conclusions are needed, and whether the query is already known.

### 11. Explain Modus Ponens.

```text
P
P => Q
Therefore Q
```

=> If `P` is true and `P` implies `Q`, then `Q` is true.

### 12. Explain Modus Tollens.

```text
P => Q
¬Q
Therefore ¬P
```

=> If `P` implies `Q` and `Q` is false, then `P` is false.

### 13. Define resolution.

=> Resolution is an inference rule that derives a new clause by eliminating complementary literals from two clauses.

### 14. List steps of FOL resolution.

=> Convert to FOL, remove implications, move negation inward, standardize variables, Skolemize, drop universal quantifiers, convert to CNF, negate query, and apply resolution.

### 15. Prove West is criminal.

=> West is American, Nono is hostile, missiles are weapons, and West sold missiles to Nono. Therefore, by the rule "American selling weapons to hostile nation is criminal", `Criminal(West)` is proved.
