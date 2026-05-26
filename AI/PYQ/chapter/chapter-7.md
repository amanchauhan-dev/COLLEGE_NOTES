# **Chapter 7: Game Playing Overview & Example Domain - PYQ Solutions**

## **Q.1 Explain goal stack planning in brief. [03/04]**

### Repeated PYQ entries

```text
Explain goal stack planning in brief.
[04] [5 Time] [Winter 2025]

OR

What is goal stack planning? Give example of initial state and goal state in goal stack planning
using some predicates.
[03-04] [Summer 2025, Summer 2024, Winter 2022]

OR

Discuss Goal Stack Planning.
[04] [Summer 2023, Summer 2022]
```

### Answer

=> **Goal Stack Planning (GSP)** is a planning technique that uses a stack to manage goals, subgoals and actions.

=> It works backward from the goal and chooses actions that can satisfy unsatisfied goals.

### Basic steps

```text
1. Push goal on stack.
2. If top goal is already true, pop it.
3. If top goal is unsatisfied, choose an action that achieves it.
4. Push the action and its preconditions.
5. When preconditions are true, execute the action.
6. Continue until stack becomes empty.
```

### Example using predicates

```text
Initial state:
OnTable(A), OnTable(B), Clear(A), Clear(B), ArmEmpty

Goal state:
On(A,B)
```

### Required actions

```text
Pickup(A)
Stack(A,B)
```

### Explanation

=> To achieve `On(A,B)`, the planner needs action `Stack(A,B)`.

=> `Stack(A,B)` requires `Holding(A)` and `Clear(B)`.

=> `Holding(A)` is achieved by `Pickup(A)`.

=> Therefore, final plan is:

```text
Pickup(A) -> Stack(A,B)
```

## **Q.2 Explain alpha-beta pruning in Minimax procedure with example. [03/04/07]**

### Repeated PYQ entries

```text
Explain alpha-beta pruning in Minimax procedure for game playing with example.
[07] [5 Time] [Winter 2025]

OR

Explain the Alpha-Beta Cutoffs Procedure in Game Playing.
[04] [Winter 2024]

OR

Explain Alpha-Beta Cut-off method.
[03] [Summer 2024]

OR

Explain the alpha-beta pruning algorithm in game-playing using an appropriate example.
[07] [Winter 2023]

OR

Explain Alpha-Beta cutoff procedure in game playing with example.
[07] [Summer 2023]

OR

Explain Alpha-Beta cutoff procedure in game playing with example.
[07] [Summer 2022]
```

### Answer

=> **Alpha-beta pruning** is an optimization of the minimax algorithm.

=> It prunes branches that cannot affect the final decision.

=> It returns the same move as minimax but searches fewer nodes.

### Meaning of alpha and beta

| Symbol | Meaning |
|---|---|
| `α` alpha | Best value found so far for MAX |
| `β` beta | Best value found so far for MIN |

### Cutoff condition

```text
If α >= β, stop exploring that branch.
```

### Algorithm

```text
1. Start with alpha = -infinity and beta = +infinity.
2. At MAX node, update alpha with maximum value found.
3. At MIN node, update beta with minimum value found.
4. If alpha >= beta, prune remaining children.
5. Continue until root value is found.
```

### Example

```text
             MAX
           /     \
         MIN     MIN
        /  \     /  \
       3    5   2    9
```

=> Left MIN node:

```text
min(3,5) = 3
```

=> MAX now has:

```text
alpha = 3
```

=> Right MIN node first child gives:

```text
beta = 2
```

=> Since:

```text
alpha >= beta
3 >= 2
```

=> Remaining child `9` is pruned.

### Advantages

1. Produces same answer as minimax.
2. Reduces number of nodes searched.
3. Allows deeper search in same time.
4. Works best with good move ordering.

## **Q.3 Show alpha-beta cutoff in minimax by drawing game tree. [07]**

### Repeated PYQ entries

```text
Show the alpha-beta cutoff in min-max algorithm by drawing suitable game tree.
[07] [2 Time] [Winter 2022]

OR

Compute with minimax the value of the root of the tree, then say which is the most convenient
move for MIN. Also tell with reason which parts of the tree are not generated if alpha-beta pruning
is performed.

                           MIN
                            O
          ┌─────────────────┼─────────────────┬─────────────────┐
          │                 │                 │                 │
         MAX               MAX               MAX               MAX
          O                 O                 O                 O
        /   \             /   \             /   \             /   \
       9    -7          11     4          -8    -9          -2    12
[07] [Winter 2021]
```

### Answer

### Minimax calculation

=> Root is a MIN node.

=> Each child is a MAX node.

```text
MAX1 = max(9, -7)  = 9
MAX2 = max(11, 4)  = 11
MAX3 = max(-8,-9)  = -8
MAX4 = max(-2,12)  = 12
```

=> Root MIN value:

```text
min(9, 11, -8, 12) = -8
```

=> Most convenient move for MIN is the third branch because it gives value `-8`.

### Alpha-beta pruning explanation

=> At root MIN, after first child, beta becomes `9`.

=> Second MAX child sees first value `11`.

=> Since MAX already has value `11`, which is greater than root beta `9`, the remaining child `4` need not be checked.

=> Fourth MAX child may also get pruned depending on traversal after root beta becomes `-8`.

### Tree with values

```text
                           MIN = -8
              /          /          \          \
          MAX=9      MAX=11      MAX=-8     MAX=12
          /  \        /  \        /  \       /  \
         9   -7      11  4      -8  -9     -2  12
```

=> Alpha-beta pruning avoids expanding branches that cannot improve the final MIN decision.

## **Q.4 Explain Minimax procedure for game playing with example. [03/04/07]**

### Repeated PYQ entries

```text
Explain Minimax procedure for game playing with any example.
[07] [5 Time] [Winter 2025, Summer 2025, Summer 2022]

OR

Explain the MiniMax procedure in a two-player game with an appropriate example.
[07-03] [Winter 2024, Winter 2023]

OR

Is the minimax procedure a depth-first or breadth-first search procedure? Explain.
[04] [Summer 2023]
```

### Answer

=> **Minimax** is a game-playing algorithm used in two-player games.

=> It assumes both players play optimally.

=> MAX tries to maximize utility, while MIN tries to minimize utility.

### Algorithm

```text
1. Generate game tree up to terminal state or cutoff depth.
2. Assign utility values to terminal states.
3. At MAX level, choose maximum child value.
4. At MIN level, choose minimum child value.
5. Propagate values upward to the root.
6. Choose move with best root value.
```

### Example

```text
             MAX
          /   |   \
        MIN  MIN  MIN
       / \   / \   / \
      3  5  2  9  1  4
```

### Calculation

```text
MIN1 = min(3,5) = 3
MIN2 = min(2,9) = 2
MIN3 = min(1,4) = 1

MAX = max(3,2,1) = 3
```

=> MAX selects the first branch.

### DFS or BFS?

=> Minimax is normally implemented as **depth-first search** because it recursively explores a path down to terminal/cutoff depth and then backs up values.

=> It can be drawn as a tree, but implementation is depth-first.

## **Q.5 Explain components of planning system. [03]**

### Repeated PYQ entries

```text
Explain components of planning system.
[03] [Winter 2024]
```

### Answer

=> A planning system creates a sequence of actions to transform an initial state into a goal state.

### Components

| Component | Meaning |
|---|---|
| Initial state | Starting facts |
| Goal state | Desired facts |
| Operators/actions | Possible actions |
| Preconditions | Conditions needed before action |
| Effects | Changes caused by action |
| Planner | Search/control mechanism that builds plan |

### Example

```text
Action: Pickup(A)
Precondition: OnTable(A), Clear(A), ArmEmpty
Effect: Holding(A), ¬OnTable(A), ¬ArmEmpty
```

## **Q.6 Discuss Iterative Deepening Search. [07]**

### Repeated PYQ entries

```text
Discuss Iterative Deepening search.
[07] [2 Time] [Winter 2024]

OR

Discuss Iterative Deepening search.
[07] [Winter 2021]
```

### Answer

=> **Iterative Deepening Search (IDS)** repeatedly applies depth-limited search with increasing depth limits.

```text
Depth limits: 0, 1, 2, 3, ...
```

### Algorithm

```text
for depth = 0 to infinity:
    result = DepthLimitedSearch(initial, depth)
    if result is solution:
        return result
```

### Working

1. First search only depth 0.
2. If goal is not found, search depth 1.
3. Continue increasing depth.
4. Stop when goal is found.

### Advantages

1. Complete if branching factor is finite.
2. Uses low memory like DFS.
3. Finds shallowest solution like BFS when step costs are equal.
4. Useful when depth of solution is unknown.
5. Useful in game playing with time limits.

### Comparison

| Feature | BFS | DFS | IDS |
|---|---|---|---|
| Complete | Yes | No in infinite depth | Yes |
| Memory | High | Low | Low |
| Finds shallowest goal | Yes | No guarantee | Yes |

=> IDS repeats some nodes, but this overhead is usually acceptable because most nodes are at deepest level.

## **Q.7 Explain Hierarchical Planning. [03/04]**

### Repeated PYQ entries

```text
Explain Hierarchical Planning.
[03] [4 Time] [Winter 2024, Summer 2024]

OR

Explain Hierarchical Planning.
[04] [Summer 2023, Summer 2022]
```

### Answer

=> **Hierarchical planning** solves a planning problem using different levels of abstraction.

=> First, a high-level plan is created. Then it is refined into detailed subplans and primitive actions.

### Levels

1. **Abstract plan**

=> Contains general tasks.

2. **Refined plan**

=> Breaks general tasks into subtasks.

3. **Primitive actions**

=> Final executable actions.

### Example

```text
Goal: Travel to college

High-level plan:
Go to college

Refined plan:
Reach bus stop -> Take bus -> Walk to classroom
```

### Advantages

1. Reduces search complexity.
2. Handles large problems easily.
3. Makes plans easier to understand.
4. Allows reuse of abstract plans.
