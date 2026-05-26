# **7 Game Playing and Planning**

## **7.1 Game Playing in AI**

=> Game playing is an important AI problem because games require search, decision making, opponent modeling and optimal move selection.

=> Most exam questions focus on two-player, zero-sum, perfect-information games such as chess, tic-tac-toe and checkers.

### Game characteristics

| Characteristic | Meaning |
|---|---|
| **Two-player** | MAX and MIN players alternate moves |
| **Zero-sum** | One player's gain is the other player's loss |
| **Perfect information** | Complete game state is visible |
| **Deterministic** | No random element in state transition |

### Important terms

| Term | Meaning |
|---|---|
| **MAX** | Player trying to maximize utility |
| **MIN** | Opponent trying to minimize utility |
| **Game tree** | Tree of possible moves |
| **Terminal state** | End of game |
| **Utility value** | Score assigned to terminal state |
| **Evaluation function** | Estimate of utility for non-terminal state |

## **7.2 Minimax Algorithm**

=> **Minimax** is a decision procedure for two-player games.

=> It assumes that both players play optimally.

=> MAX chooses the move with maximum value, while MIN chooses the move with minimum value.

### Minimax idea

```text
MAX level: choose maximum child value.
MIN level: choose minimum child value.
```

### Algorithm

```text
MINIMAX(state):
1. If state is terminal, return utility(state).
2. If player is MAX:
      return max value of MINIMAX(successors).
3. If player is MIN:
      return min value of MINIMAX(successors).
```

### Example

```text
             MAX
          /   |   \
        MIN  MIN  MIN
       / \   / \   / \
      3  5  2  9  1  4
```

=> MIN values:

```text
min(3,5)=3
min(2,9)=2
min(1,4)=1
```

=> MAX selects:

```text
max(3,2,1)=3
```

=> Best move is the first branch.

### Depth-first nature

=> Minimax is normally implemented as depth-first search because it recursively explores one branch before another.

## **7.3 Alpha-Beta Pruning**

=> **Alpha-beta pruning** is an optimization of minimax.

=> It removes branches that cannot affect the final minimax decision.

=> It gives the same result as minimax but expands fewer nodes.

### Alpha and beta

| Symbol | Meaning |
|---|---|
| **Alpha (`α`)** | Best value found so far for MAX |
| **Beta (`β`)** | Best value found so far for MIN |

### Cutoff condition

```text
If alpha >= beta, prune remaining branches.
```

### Algorithm

```text
ALPHA-BETA(state, alpha, beta):
1. If terminal, return utility(state).
2. If MAX node:
      value = -infinity
      for each child:
          value = max(value, ALPHA-BETA(child, alpha, beta))
          alpha = max(alpha, value)
          if alpha >= beta: break
      return value
3. If MIN node:
      value = +infinity
      for each child:
          value = min(value, ALPHA-BETA(child, alpha, beta))
          beta = min(beta, value)
          if alpha >= beta: break
      return value
```

### Example

```text
             MAX
           /     \
         MIN     MIN
        /  \     /  \
       3    5   2    9
```

=> Left MIN gives `min(3,5)=3`, so MAX has `alpha=3`.

=> In right MIN, first child gives `2`, so `beta=2`.

=> Since `alpha >= beta` i.e. `3 >= 2`, remaining child `9` is pruned.

## **7.4 Refinements in Game Search**

=> Game trees are very large, so refinements improve practical performance.

### Important refinements

1. **Cutoff test**

=> Stop search at fixed depth instead of terminal state.

2. **Evaluation function**

=> Estimate value of non-terminal state.

3. **Move ordering**

=> Explore promising moves first to improve alpha-beta pruning.

4. **Iterative deepening**

=> Search repeatedly with increasing depth limits.

5. **Transposition table**

=> Store already evaluated positions to avoid repeated work.

## **7.5 Iterative Deepening Search**

=> **Iterative Deepening Search (IDS)** repeatedly performs depth-limited search with increasing depth.

```text
Depth limit: 0, 1, 2, 3, ...
```

### Algorithm

```text
for depth = 0 to infinity:
    result = DEPTH-LIMITED-SEARCH(initial, depth)
    if result is solution:
        return result
```

### Advantages

1. Complete like BFS for finite branching.
2. Uses low memory like DFS.
3. Finds shallowest solution when step cost is equal.
4. Useful in game playing because it can return best move found before time limit.

### Comparison

| Feature | BFS | DFS | IDS |
|---|---|---|---|
| Complete | Yes | No in infinite space | Yes |
| Memory | High | Low | Low |
| Finds shallow solution | Yes | No guarantee | Yes |

## **7.6 Blocks World**

=> Blocks World is a planning domain where blocks are arranged on a table and must be moved to reach a goal arrangement.

### Predicates

| Predicate | Meaning |
|---|---|
| `On(x,y)` | Block x is on block y |
| `OnTable(x)` | Block x is on table |
| `Clear(x)` | Nothing is on x |
| `Holding(x)` | Robot arm holds x |
| `ArmEmpty` | Robot arm is empty |

### Operators

1. `Pickup(x)`
2. `Putdown(x)`
3. `Stack(x,y)`
4. `Unstack(x,y)`

### Example

```text
Initial: OnTable(A), OnTable(B), Clear(A), Clear(B), ArmEmpty
Goal:    On(A,B)
```

=> Plan:

```text
Pickup(A)
Stack(A,B)
```

## **7.7 Components of Planning System**

=> A planning system finds a sequence of actions that transforms the initial state into the goal state.

### Main components

| Component | Meaning |
|---|---|
| **Initial state** | Starting facts |
| **Goal state** | Desired facts |
| **Operators/actions** | Actions available to the agent |
| **Preconditions** | Conditions required before action |
| **Effects** | Changes caused by action |
| **Planner/search control** | Mechanism that builds the plan |

### Operator example

```text
Action: Pickup(A)
Precondition: OnTable(A), Clear(A), ArmEmpty
Effect: Holding(A), ¬OnTable(A), ¬ArmEmpty
```

## **7.8 Goal Stack Planning**

=> **Goal Stack Planning (GSP)** is a planning technique that uses a stack to manage goals and actions.

=> It works backward from the goal and pushes unsatisfied goals and required actions onto a stack.

### Basic idea

```text
1. Push goal on stack.
2. If top of stack is already true, pop it.
3. If top is an unsatisfied goal, choose an action that achieves it.
4. Push action and its preconditions.
5. When preconditions are true, execute action.
6. Continue until stack is empty.
```

### Example

```text
Initial state:
OnTable(A), OnTable(B), Clear(A), Clear(B), ArmEmpty

Goal state:
On(A,B)
```

### Plan

```text
Pickup(A)
Stack(A,B)
```

=> `Pickup(A)` is needed to hold A, and `Stack(A,B)` achieves `On(A,B)`.

## **7.9 Nonlinear Planning Using Constraint Posting**

=> **Nonlinear planning** does not require actions to be totally ordered from the beginning.

=> It creates a partial-order plan and adds ordering constraints only when necessary.

### Constraint posting

=> Constraint posting means adding restrictions to keep the plan valid.

### Types of constraints

1. **Ordering constraint**

```text
Action A before Action B
```

2. **Causal link**

```text
Action A achieves condition P for Action B
```

3. **Threat resolution**

=> If an action threatens a causal link, add ordering constraints to avoid conflict.

### Advantages

1. Avoids unnecessary ordering.
2. Allows independent subgoals to be planned separately.
3. More flexible than linear planning.

## **7.10 Hierarchical Planning**

=> **Hierarchical planning** solves a problem by first creating a high-level abstract plan and then refining it into detailed actions.

### Levels

1. **High-level plan**

=> General tasks.

2. **Intermediate plan**

=> Subtasks.

3. **Primitive actions**

=> Direct executable actions.

### Example

```text
Goal: Travel to college

High-level plan:
Go to college

Refinement:
Reach bus stop -> Take bus -> Walk to classroom
```

### Advantages

1. Reduces search complexity.
2. Easier to understand plans.
3. Supports abstraction.
4. Useful for large planning problems.

## **7.11 Reactive Systems**

=> Reactive systems select actions based on the current situation instead of building a complete plan in advance.

=> They are useful in dynamic environments where plans may fail quickly.

### Characteristics

1. Fast response.
2. No long planning phase.
3. Uses condition-action rules.
4. Suitable for real-time control.

### Example

```text
IF obstacle ahead THEN turn left
IF battery low THEN go to charger
```

## **7.12 Other Planning Techniques**

### 1. Forward state-space planning

=> Starts from initial state and applies actions until goal is reached.

### 2. Backward state-space planning

=> Starts from goal and works backward to required initial conditions.

### 3. Partial-order planning

=> Orders only those actions that must be ordered.

### 4. Conditional planning

=> Creates branches for different possible outcomes.

### 5. Planning with heuristics

=> Uses heuristic estimates to choose promising actions.

## **7.13 Exam Short Questions**

### 1. Define minimax algorithm.

=> Minimax is a game-playing algorithm where MAX chooses the move with maximum utility and MIN chooses the move with minimum utility.

### 2. What are MAX and MIN players?

=> MAX is the player trying to maximize the game value, while MIN is the opponent trying to minimize it.

### 3. Define alpha-beta pruning.

=> Alpha-beta pruning is an optimization of minimax that removes branches that cannot affect the final decision.

### 4. What is alpha cutoff?

=> Alpha cutoff occurs when a MIN node finds a value less than or equal to MAX's current alpha value, so remaining branches are pruned.

### 5. What is beta cutoff?

=> Beta cutoff occurs when a MAX node finds a value greater than or equal to MIN's current beta value, so remaining branches are pruned.

### 6. List game search refinements.

=> Cutoff test, evaluation function, move ordering, iterative deepening and transposition tables.

### 7. Define iterative deepening search.

=> Iterative deepening search repeatedly performs depth-limited search with increasing depth limits until the goal is found.

### 8. What is Blocks World?

=> Blocks World is a planning domain where blocks are moved and stacked to reach a goal arrangement.

### 9. List components of planning system.

=> Initial state, goal state, actions, preconditions, effects and planner/search control.

### 10. Define goal stack planning.

=> Goal stack planning uses a stack to manage goals, subgoals and actions while constructing a plan.

### 11. What is nonlinear planning?

=> Nonlinear planning builds a partial-order plan and orders actions only when required by constraints.

### 12. Define hierarchical planning.

=> Hierarchical planning creates an abstract high-level plan and refines it into detailed executable actions.

### 13. What are reactive systems?

=> Reactive systems choose actions directly from the current situation using condition-action rules instead of complete preplanning.

### 14. List planning techniques.

=> Forward planning, backward planning, partial-order planning, conditional planning, hierarchical planning and heuristic planning.
