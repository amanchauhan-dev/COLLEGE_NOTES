# **Chapter 4: Inference in First Order Logic - PYQ Solutions**

## **Q.1 Define Soundness and Completeness in propositional logic. [03]**

### Repeated PYQ entries

```text
Define Soundness and Completeness in propositional logic.
[03] [3 Time] [Winter 2025, Summer 2025]

OR

Define Soundness and Completeness in propositional logic.
[03] [Winter 2021]
```

### Answer

=> **Soundness** means an inference procedure derives only logically correct conclusions.

```text
If KB ⊢ alpha, then KB |= alpha
```

=> It never proves a false statement from true premises.

=> **Completeness** means an inference procedure can derive every sentence that logically follows from the knowledge base.

```text
If KB |= alpha, then KB ⊢ alpha
```

=> A sound and complete system is both correct and powerful enough to prove all valid conclusions.

## **Q.2 State the purpose of unification in predicate logic. [03/04]**

### Repeated PYQ entries

```text
State the purpose of unification in predicate logic.
[03] [5 Time] [Winter 2025, Winter 2021]

OR

Explain Unification.
[03] [Summer 2025]

OR

Perform the unification of atomic sentences. Find the most general unifier.
1. p(b, X, f(g(Z))) and p(Z, f(Y), f(Y)).
2. test(11), test(y)
[04] [Summer 2024]

OR

Explain the concept of unification in first order predicate logic with an appropriate example.
[03] [Winter 2023]

OR

Perform the unification of following atomic sentences. Find the most general unifier.
1. Knows(John, x); Knows(y, Mother(y))
2. Q(a, g(x, a), f(y)), Q(a, g(f(b), a), x)
[03] [Winter 2022]

OR

Perform the unification of atomic sentences. Find the most general unifier.
1. p(b, X, f(g(Z))) and p(Z, f(Y), f(Y)).
2. test(11), test(y)
[03] [Winter 2022]

OR

Explain Unification.
[03] [Summer 2022, Summer 2023]
```

### Answer

=> **Unification** is the process of finding a substitution that makes two predicate logic expressions identical.

=> The best general substitution is called **Most General Unifier (MGU)**.

### Purpose

1. Match facts with rules.
2. Apply inference rules.
3. Support resolution.
4. Support forward and backward chaining.

### Examples

1. `Knows(John, x)` and `Knows(y, Mother(y))`

```text
MGU = {y/John, x/Mother(John)}
```

2. `test(11)` and `test(y)`

```text
MGU = {y/11}
```

3. `p(b, X, f(g(Z)))` and `p(Z, f(Y), f(Y))`

```text
Z = b
X = f(Y)
f(g(Z)) = f(Y) => Y = g(Z) = g(b)

MGU = {Z/b, Y/g(b), X/f(g(b))}
```

4. `Q(a, g(x,a), f(y))` and `Q(a, g(f(b),a), x)`

```text
x = f(b)
f(y) = x = f(b) => y = b

MGU = {x/f(b), y/b}
```

## **Q.3 Differentiate forward chaining and backward chaining. [04/07]**

### Repeated PYQ entries

```text
Differentiate forward chaining and backward chaining.
[04] [4 Time] [Summer 2025]

OR

Explain Forward and Backward Chaining with example.
[07] [Winter 2024]

OR

Explain forward and backward reasoning with example.
[07] [Summer 2023]

OR

Differentiate forward chaining and backward chaining.
[04] [Summer 2022]

OR

Explain forward and backward reasoning with example.
[07] [Winter 2021]
```

### Answer

| Forward Chaining | Backward Chaining |
|---|---|
| Data-driven | Goal-driven |
| Starts from known facts | Starts from query |
| Applies rules to derive new facts | Finds rules that can prove goal |
| May infer irrelevant facts | More focused |
| Useful when many facts are available | Useful for specific query |
| Example: monitoring system | Example: Prolog query |

### Forward chaining example

```text
Fact: Human(Socrates)
Rule: Human(x) => Mortal(x)
Infer: Mortal(Socrates)
```

### Backward chaining example

```text
Goal: Mortal(Socrates)
Rule: Human(x) => Mortal(x)
Subgoal: Human(Socrates)
Fact: Human(Socrates)
Goal proved.
```

## **Q.4 What factors determine forward or backward search direction? [04]**

### Repeated PYQ entries

```text
What factors determine forward or backward search direction?
[04] [2 Time] [Winter 2025]

OR

Explain backward search procedure with example.
[04] [Winter 2023]
```

### Answer

### Factors

1. **Number of initial facts**

=> If many facts are available, forward chaining is suitable.

2. **Number of goals**

=> If goal is specific and known, backward chaining is suitable.

3. **Branching factor**

=> Choose direction that produces fewer branches.

4. **Need for all conclusions or one conclusion**

=> Forward chaining is useful for all conclusions; backward chaining is useful for one query.

5. **Availability of data**

=> If data arrives continuously, forward chaining is better.

### Backward search example

```text
Goal: Criminal(West)
Rule: American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) => Criminal(x)
Subgoals: American(West), Weapon(y), Sells(West,y,z), Hostile(z)
```

=> The system proves each subgoal to prove the original goal.

## **Q.5 Explain Modus Ponens and Modus Tollens inference rules with example. [07]**

### Repeated PYQ entries

```text
Explain Modes Ponens and Modes Tollens inference rules with an appropriate example.
[07] [3 Time] [Summer 2025]

OR

Explain Modes Ponens and Modes Tollens inference rules with an appropriate example.
[07] [Winter 2023]

OR

Explain Modus Ponens inference rule with example.
[04] [Winter 2022]
```

### Answer

### Modus Ponens

=> If `P` is true and `P => Q` is true, then `Q` can be inferred.

```text
P
P => Q
Therefore Q
```

### Example

```text
Rain
Rain => WetRoad
Therefore WetRoad
```

### Modus Tollens

=> If `P => Q` is true and `Q` is false, then `P` must be false.

```text
P => Q
¬Q
Therefore ¬P
```

### Example

```text
Rain => WetRoad
¬WetRoad
Therefore ¬Rain
```

### Difference

| Modus Ponens | Modus Tollens |
|---|---|
| Confirms consequent using antecedent | Denies antecedent using denied consequent |
| Uses `P` and `P => Q` | Uses `¬Q` and `P => Q` |
| Concludes `Q` | Concludes `¬P` |

## **Q.6 Prove "West is criminal" using resolution. [07]**

### Repeated PYQ entries

```text
Translate following sentences to predicate logic and prove that "West is criminal" using resolution.
1. It is a crime for an American to sell weapons to hostile nations.
2. All the missiles were sold to Nono by West.
3. The country Nono is an enemy of America.
4. An enemy of America counts as hostile.
5. Nono has some missiles.
6. Missiles are weapons.
7. West is an American.
[07] [5 Time] [Summer 2025, Winter 2022]

OR

Explain the use of resolution in first order predicate logic using an appropriate example.
[07] [Winter 2023]

OR

Consider the following sentences:
- Raj likes all kinds of food.
- Apples are food.
- Anything anyone eats and isn't killed by is food.
- Sachin eats peanuts and is still alive.
- Vinod eats everything Sachin eats.
Attempt following:
i. Translate these sentences into formulas in predicate logic
ii. Use resolution to answer the question, "What food does Vinod eat?"
[07] [Winter 2021, Summer 2022]
```

### Answer

### FOL representation

```text
1. ∀x∀y∀z American(x) ∧ Weapon(y) ∧ Sells(x,y,z) ∧ Hostile(z) => Criminal(x)
2. ∀x Missile(x) ∧ Owns(Nono,x) => Sells(West,x,Nono)
3. Enemy(Nono, America)
4. ∀x Enemy(x, America) => Hostile(x)
5. ∃x Missile(x) ∧ Owns(Nono,x)
6. ∀x Missile(x) => Weapon(x)
7. American(West)
```

### CNF clauses

```text
1. ¬American(x) ∨ ¬Weapon(y) ∨ ¬Sells(x,y,z) ∨ ¬Hostile(z) ∨ Criminal(x)
2. ¬Missile(x) ∨ ¬Owns(Nono,x) ∨ Sells(West,x,Nono)
3. Enemy(Nono, America)
4. ¬Enemy(x, America) ∨ Hostile(x)
5. Missile(M1)
6. Owns(Nono, M1)
7. ¬Missile(x) ∨ Weapon(x)
8. American(West)
9. ¬Criminal(West)        // negated query
```

### Resolution proof

```text
From 5 and 7:
Weapon(M1)

From 5, 6 and 2:
Sells(West, M1, Nono)

From 3 and 4:
Hostile(Nono)

Use clause 1 with:
x = West, y = M1, z = Nono

American(West), Weapon(M1), Sells(West,M1,Nono), Hostile(Nono)
=> Criminal(West)

Criminal(West) resolves with ¬Criminal(West)
=> Empty clause
```

=> Therefore, **West is criminal** is proved by contradiction.

### Vinod food answer

```text
Eats(Sachin, Peanuts)
∀x Eats(Sachin,x) => Eats(Vinod,x)
```

=> Therefore:

```text
Eats(Vinod, Peanuts)
```

=> Vinod eats **peanuts**.

## **Q.7 Translate sentences and prove "Scrooge is not a child." [07]**

### Repeated PYQ entries

```text
Translate following sentences to predicate logic and prove that "Scrooge is not a child."
1. Every child loves Santa.
2. Everyone who loves Santa loves any reindeer.
3. Rudolph is a reindeer, and Rudolph has a red nose.
4. Anything which has a red nose is weird or is a clown.
5. No reindeer is a clown.
6. Scrooge does not love anything which is weird.
[07] [Summer 2024]
```

### Answer

### FOL representation

```text
1. ∀x Child(x) => Loves(x, Santa)
2. ∀x∀y Loves(x, Santa) ∧ Reindeer(y) => Loves(x, y)
3. Reindeer(Rudolph) ∧ RedNose(Rudolph)
4. ∀x RedNose(x) => Weird(x) ∨ Clown(x)
5. ∀x Reindeer(x) => ¬Clown(x)
6. ∀x Weird(x) => ¬Loves(Scrooge, x)
```

### Proof

=> From `Reindeer(Rudolph)` and `RedNose(Rudolph)`.

=> From rule 4:

```text
Weird(Rudolph) ∨ Clown(Rudolph)
```

=> From rule 5 and `Reindeer(Rudolph)`:

```text
¬Clown(Rudolph)
```

=> Therefore:

```text
Weird(Rudolph)
```

=> From rule 6:

```text
¬Loves(Scrooge, Rudolph)
```

=> Assume opposite of required conclusion:

```text
Child(Scrooge)
```

=> From rule 1:

```text
Loves(Scrooge, Santa)
```

=> From rule 2 and `Reindeer(Rudolph)`:

```text
Loves(Scrooge, Rudolph)
```

=> This contradicts:

```text
¬Loves(Scrooge, Rudolph)
```

=> Therefore:

```text
¬Child(Scrooge)
```

=> Hence, **Scrooge is not a child**.

## **Q.8 Prove John likes peanuts using backward chaining. [07]**

### Repeated PYQ entries

```text
Consider the following sentences:
- John likes all kinds of food.
- Apples are food.
- Chicken is food.
- Anything anyone eats and isn't killed by is food.
- Bill eats peanuts and is still alive.
- Sue eats everything Bill eats.
(i) Translate these sentences into formulas in predicate logic.
(ii) Prove that John likes peanuts using backward chaining.
[07] [2 Time] [Summer 2023]

OR

Translate following sentences to predicate logic and prove that John likes peanuts using backward
chaining.
1. John like all kinds of food.
2. Apples are food.
3. Chicken is food.
4. Anything anyone eats and isn't killed by is food.
5. Bill eats peanuts and is still alive.
6. Sue eats everything Bill eats.
[07] [Winter 2022]
```

### Answer

### Predicate logic

```text
1. ∀x Food(x) => Likes(John,x)
2. Food(Apples)
3. Food(Chicken)
4. ∀x∀y Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
5. Eats(Bill, Peanuts) ∧ ¬KilledBy(Bill, Peanuts)
6. ∀x Eats(Bill,x) => Eats(Sue,x)
```

### Goal

```text
Likes(John, Peanuts)
```

### Backward chaining

1. To prove `Likes(John, Peanuts)`, use rule:

```text
Food(x) => Likes(John,x)
```

=> Substitution:

```text
x = Peanuts
```

=> New subgoal:

```text
Food(Peanuts)
```

2. To prove `Food(Peanuts)`, use:

```text
Eats(x,y) ∧ ¬KilledBy(x,y) => Food(y)
```

=> Substitution:

```text
x = Bill, y = Peanuts
```

=> New subgoals:

```text
Eats(Bill, Peanuts)
¬KilledBy(Bill, Peanuts)
```

3. Both are given facts.

=> Therefore:

```text
Food(Peanuts)
Likes(John, Peanuts)
```

=> Hence, John likes peanuts.
