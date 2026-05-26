# **Chapter 2: Problems, State Space Search & Heuristic Search Techniques - PYQ Solutions**

## **Q.1 Give an example of a problem for which breadth-first search would work better than depth-first search. [04]**

### Repeated PYQ entries

```text
Give an example of a problem for which breadth-first search would work better than depth-first
search.
[04] [2 Time] [Winter 2025]

OR

Compare Breadth First Search and Depth First Search.
[04] [Winter 2021]
```

### Answer

=> **Breadth First Search (BFS)** expands nodes level by level from the root.

=> **Depth First Search (DFS)** expands one path deeply before backtracking.

### Example where BFS is better

=> Finding the shortest path in an unweighted graph is a case where BFS works better than DFS.

```text
        A
      / | \
     B  C  D
    /      |
   E       G
```

=> If the goal is `D`, BFS explores `A, B, C, D` and finds the shallow goal quickly.

=> DFS may go from `A -> B -> E` first and waste time before finding `D`.

### Comparison

| Point | BFS | DFS |
|---|---|---|
| Search order | Level by level | Deepest path first |
| Data structure | Queue | Stack / recursion |
| Completeness | Complete for finite branching | Not complete in infinite spaces |
| Optimality | Optimal when step costs are equal | Not optimal |
| Memory | Requires more memory | Requires less memory |
| Best use | Shortest path in unweighted graph | Memory-limited search |

=> Thus, BFS is better when the solution is shallow or shortest path is required.

## **Q.2 Differentiate between Best First Search and Breadth First Search. [04]**

### Repeated PYQ entries

```text
Differentiate between best first search and breadth first search.
[04] [Summer 2025]
```

### Answer

| Breadth First Search | Best First Search |
|---|---|
| It is an uninformed search. | It is an informed heuristic search. |
| It expands the shallowest node first. | It expands the most promising node first. |
| It uses a FIFO queue. | It uses a priority queue. |
| It does not use heuristic value. | It uses heuristic function `h(n)`. |
| It is complete for finite branching factor. | Completeness depends on implementation and search space. |
| It is optimal when all step costs are equal. | It is not always optimal. |
| It may expand many unnecessary nodes. | It reduces search using domain knowledge. |

=> BFS is useful for shortest path in unweighted graphs, while Best First Search is useful when a good heuristic is available.

## **Q.3 Describe how the branch-and-bound technique could be used to find the shortest solution to a water jug problem. [07]**

### Repeated PYQ entries

```text
Describe how the branch-and-bound technique could be used to find the shortest solution to a
water jug problem.
[07] [4 Time] [Winter 2025]

OR

Solve and suggest the appropriate strategy for the following water-jug problem. You are given two
jugs of capacity having 8 liters and 5 liters. There are no measuring markers on jugs. You have to
obtain exact 4 liters of water into 8 liters jug.
[04] [Summer 2025]

OR

Explain Water Jug Problem with example.
[07] [Winter 2024]

OR

Explain state space search representation using water-jug problem.
[04] [Winter 2023]

OR

Solve and suggest the appropriate strategy for the following water-jug problem. You are given two
jugs of capacity having 8 liters and 5 liters. There are no measuring markers on jugs. You have to
obtain exact 4 liters of water into 8 liters jug.
[04] [Winter 2022]
```

### Answer

=> In the water jug problem, states show the amount of water in each jug.

=> For two jugs of capacity 8 liters and 5 liters, a state is written as:

```text
(x, y)
```

=> `x` = water in 8-liter jug, `y` = water in 5-liter jug.

=> Initial state: `(0,0)`

=> Goal state: `(4,y)`, meaning 8-liter jug must contain exactly 4 liters.

### Operators

1. Fill 8-liter jug.
2. Fill 5-liter jug.
3. Empty 8-liter jug.
4. Empty 5-liter jug.
5. Pour 8-liter jug into 5-liter jug.
6. Pour 5-liter jug into 8-liter jug.

### Branch-and-bound idea

=> Branch-and-bound expands the least-cost partial solution first.

=> Here, cost can be taken as number of operations.

=> If a generated path is longer than the best solution already found, it is not expanded further.

### Solution path

```text
(0,0)  -> Fill 5-liter jug
(0,5)  -> Pour 5 into 8
(5,0)  -> Fill 5-liter jug
(5,5)  -> Pour 5 into 8 until 8 is full
(8,2)  -> Empty 8-liter jug
(0,2)  -> Pour 2 into 8
(2,0)  -> Fill 5-liter jug
(2,5)  -> Pour 5 into 8 until 8 is full
(7,0)  -> Fill 5-liter jug
(7,5)  -> Pour 5 into 8 until 8 is full
(8,4)  -> Empty 8-liter jug
(0,4)  -> Pour 4 into 8
(4,0)  -> Goal reached
```

=> The final state `(4,0)` contains exactly 4 liters in the 8-liter jug.

### For 4 marks

=> Write state representation, operators, initial state, goal state and the solution path.

## **Q.4 Explain the A* search algorithm using an appropriate example. [07]**

### Repeated PYQ entries

```text
Explain the A* search algorithm using an appropriate example.
[07] [4 Time] [Summer 2025]

OR

Explain A* algorithm. What happens if h' underestimates h and overestimates h?
[07] [Winter 2024]

OR

Explain the A* search algorithm using an appropriate example.
[07] [Winter 2023]

OR

Explain A* algorithm.
[07] [Summer 2023]

OR

Explain A * algorithm in detail.
[07] [Summer 2022]
```

### Answer

=> **A\* search** is an informed search algorithm that selects the node with minimum estimated total cost.

### Evaluation function

```text
f(n) = g(n) + h(n)
```

| Term | Meaning |
|---|---|
| `g(n)` | Actual cost from start node to node `n` |
| `h(n)` | Estimated cost from node `n` to goal |
| `f(n)` | Estimated total cost of solution through node `n` |

### Algorithm

```text
1. Put start node in OPEN list.
2. Calculate f(n) = g(n) + h(n).
3. Select node with minimum f(n).
4. If selected node is goal, return solution path.
5. Otherwise expand it and generate successors.
6. Calculate g, h and f for each successor.
7. Put expanded node in CLOSED list.
8. Repeat until goal is found or OPEN becomes empty.
```

### Example

```text
Node    g(n)    h(n)    f(n)
A       0       10      10
B       4        6      10
C       3        8      11
D       7        2       9
G       9        0       9
```

=> A* selects the node having the lowest `f(n)`.

=> If `D` and `G` have lowest `f`, A* expands them before nodes with larger `f`.

### Effect of heuristic

| Condition | Effect |
|---|---|
| `h(n)` underestimates true cost | A* remains optimal but may expand more nodes |
| `h(n)` equals true cost | A* directly follows optimal path |
| `h(n)` overestimates true cost | A* may become faster but optimality is not guaranteed |

=> A heuristic that never overestimates true cost is called **admissible heuristic**.

=> A* is complete and optimal when the heuristic is admissible and step costs are positive.

## **Q.5 Apply A* algorithm to 8-puzzle or graph problem. [07]**

### Repeated PYQ entries

```text
Consider the following initial and goal configuration for 8-puzzle problem. Draw the search tree
for initial three iterations of A* algorithm to reach from initial state to goal state. Assume suitable
heuristic function for the same.
[07] [2 Time] [Winter 2025]

Initial State                 Goal State

+---+---+---+                 +---+---+---+
|   | 1 | 2 |                 | 1 | 2 | 3 |
+---+---+---+                 +---+---+---+
| 3 | 4 | 5 |                 | 8 |   | 4 |
+---+---+---+                 +---+---+---+
| 6 | 7 | 8 |                 | 7 | 6 | 5 |
+---+---+---+                 +---+---+---+

OR

Consider the graph. The numbers written on edges represent distance between nodes. The numbers
written on nodes represent heuristic value. Find the most cost-effective path from A to J using A*.
[07] [Summer 2024]

OR

Consider the following initial and goal state configuration of 8-puzzle problem. Apply A*
algorithm to reach from initial state to goal state by drawing search tree and show the solution.
Consider number of misplaced tiles as a heuristic function.
[07] [Winter 2022]
```

### Answer

=> In 8-puzzle, A* uses:

```text
f(n) = g(n) + h(n)
```

=> `g(n)` = number of moves from initial state.

=> `h(n)` = number of misplaced tiles or Manhattan distance.

### Winter 2022 8-puzzle solution using misplaced tile heuristic

```text
Initial State                 Goal State
+---+---+---+                 +---+---+---+
| 2 | 8 | 3 |                 | 1 | 2 | 3 |
+---+---+---+                 +---+---+---+
| 1 | 6 | 4 |                 | 8 |   | 4 |
+---+---+---+                 +---+---+---+
| 7 |   | 5 |                 | 7 | 6 | 5 |
+---+---+---+                 +---+---+---+
```

### Solution path

```text
Move blank Up:
2 8 3      2 8 3
1 6 4  ->  1   4
7   5      7 6 5

Move blank Up:
2 8 3      2   3
1   4  ->  1 8 4
7 6 5      7 6 5

Move blank Left:
2   3        2 3
1 8 4  ->  1 8 4
7 6 5      7 6 5

Move blank Down:
  2 3      1 2 3
1 8 4  ->    8 4
7 6 5      7 6 5

Move blank Right:
1 2 3      1 2 3
  8 4  ->  8   4
7 6 5      7 6 5
```

=> Goal is reached in 5 moves.

### A* graph answer method

=> For graph questions, prepare table using:

```text
f(n) = g(n) + h(n)
```

=> Select the OPEN node with minimum `f(n)` at every step.

=> For the given A-to-J graph, one cost-effective path is:

```text
A -> F -> D -> C -> E -> J
Cost = 3 + 1 + 1 + 5 + 5 = 15
```

=> Another path with same cost may also be possible depending on tie-breaking.

### For initial three iterations

=> Show start node, generate successors, calculate `g`, `h`, `f`, and expand the node with smallest `f`.

## **Q.6 Explain AO* algorithm with example. [07]**

### Repeated PYQ entries

```text
Explain AO * algorithm with example.
[07] [Winter 2025]

OR

Explain AO* algorithm.
[07] [Summer 2023]
```

### Answer

=> **AO\*** is a heuristic search algorithm used on AND-OR graphs.

=> It finds the best solution graph by considering both alternative choices and required subproblems.

### AND-OR meaning

| Node | Meaning |
|---|---|
| **OR node** | Any one child solution is enough |
| **AND node** | All selected child subproblems must be solved |

### AO* algorithm

```text
1. Start with initial node.
2. Follow currently marked best arcs.
3. Select a non-terminal tip node.
4. Expand the selected node.
5. Assign heuristic values to new nodes.
6. Update cost values backward to ancestors.
7. Mark the best child or best child set.
8. Stop when start node is solved.
```

### Cost calculation

```text
OR node cost  = minimum cost among children
AND node cost = sum of costs of all required children
```

### Example

```text
        A
      /   \
   B(OR) C(AND)
   / \    / \
  D   E  F   G
```

=> If `B` is OR, solving either `D` or `E` solves `B`.

=> If `C` is AND, both `F` and `G` must be solved.

=> AO* repeatedly updates costs and marks the best solution graph.

## **Q.7 Explain AND-OR graphs. [03]**

### Repeated PYQ entries

```text
Explain AND-OR graphs.
[03] [Summer 2022]

OR

Explain AND-OR graphs.
[03] [Summer 2023]
```

### Answer

=> An **AND-OR graph** is used to represent problem reduction.

=> A complex problem is divided into subproblems.

### Types of nodes

1. **OR node**

=> The parent is solved if any one child is solved.

2. **AND node**

=> The parent is solved only if all required children are solved.

### Diagram

```text
        A
      /   \
    B(OR) C(AND)
    / \    / \
   D   E  F   G
```

=> `B` can be solved by `D` or `E`, but `C` requires both `F` and `G`.

## **Q.8 Solve the Crypt Arithmetic problem. [07]**

### Repeated PYQ entries

```text
Solve the following Crypt Arithmetic problem.
   DONALD
+  GERALD
__________
  ROBERT
[07] [3 Time] [Winter 2025]

OR

Solve the following Cryptarithmetic Problem.
   SEND
+  MORE
_______
  MONEY
[07] [Summer 2023, Summer 2022]
```

### Answer

=> In cryptarithmetic, each letter represents a unique digit.

=> Leading letters cannot be zero.

### DONALD + GERALD = ROBERT

```text
Mapping:
D=5, O=2, N=6, A=4, L=8, G=1, E=9, R=7, B=3, T=0

  DONALD = 526485
  GERALD = 197485
  ROBERT = 723970
```

### Verification

```text
  526485
+ 197485
--------
  723970
```

=> Hence, `DONALD + GERALD = ROBERT` is satisfied.

### SEND + MORE = MONEY

```text
Mapping:
S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2

  SEND  = 9567
  MORE  = 1085
  MONEY = 10652
```

### Verification

```text
  9567
+ 1085
------
 10652
```

## **Q.9 Explain the state space search with the use of 8 puzzle problem. [07]**

### Repeated PYQ entries

```text
Explain the state space search with the use of 8 puzzle problem.
[07] [2 Time] [Summer 2025]

OR

Explain the State space search with the use of 8 Puzzle Problem.
[07] [Summer 2022]
```

### Answer

=> 8-puzzle is a standard state space search problem.

=> It contains 8 numbered tiles and one blank space on a 3x3 board.

### State representation

=> A state is a particular arrangement of tiles.

```text
+---+---+---+
| 2 | 8 | 3 |
+---+---+---+
| 1 | 6 | 4 |
+---+---+---+
| 7 |   | 5 |
+---+---+---+
```

### Initial state and goal state

=> Initial state is the given starting arrangement.

=> Goal state is the required final arrangement.

### Operators

1. Move blank up.
2. Move blank down.
3. Move blank left.
4. Move blank right.

### Goal test

=> Check whether current tile arrangement matches the goal arrangement.

### Path cost

=> Usually each move has cost 1, so path cost is number of moves.

### Search tree

```text
Initial State
   |
Apply blank moves
   |
Generated states
   |
Continue until Goal State
```

=> Search algorithms like BFS, DFS or A* can be used to find a path from initial state to goal state.

## **Q.10 Explain: Local maximum, Plateau and Ridge. [03]**

### Repeated PYQ entries

```text
Explain: (i) Local maximum (ii) Plateau (iii) Ridge.
[03] [4 Time] [Summer 2025, Winter 2024]

OR

Define term: Plateau, Ridge.
[03] [Summer 2024, Summer 2023]

OR

Explain Local Maximum, Plateau and Ridge.
[03] [Summer 2022]
```

### Answer

1. **Local maximum**

=> A local maximum is a state that is better than all its neighboring states but is not the best global solution.

=> Hill climbing may stop here incorrectly.

2. **Plateau**

=> A plateau is a flat area where neighboring states have the same heuristic value.

=> The algorithm cannot decide which direction is better.

3. **Ridge**

=> A ridge is a narrow path toward the goal where direct moves do not improve the heuristic immediately.

=> Hill climbing may fail because it requires sideways or indirect moves.

## **Q.11 What is Hill Climbing algorithm? Discuss cases where Hill Climbing fails. [04]**

### Repeated PYQ entries

```text
What is Hill Climbing algorithm? Discuss any two cases where Hill climbing fails.
[04] [4 Time] [Winter 2025]

OR

What is Hill Climbing algorithm? Discuss the cases where Hill climbing fails.
[07] [Summer 2025]

OR

Discuss limitations of Hill Climbing search method.
[03] [Summer 2023]

OR

What is Hill Climbing algorithm? Discuss the cases where Hill climbing fails.
[07] [Winter 2022]

OR

Discuss Steepest-Ascent Hill Climbing algorithm and its limitations.
[07] [Winter 2021]
```

### Answer

=> **Hill climbing** is a heuristic local search algorithm.

=> It starts from an initial state and repeatedly moves to a better neighboring state.

### Algorithm

```text
1. Start with initial state.
2. Evaluate current state.
3. Generate neighboring states.
4. Select a better neighbor.
5. If no better neighbor exists, stop.
6. Otherwise move to selected neighbor and repeat.
```

### Steepest-ascent hill climbing

=> In steepest-ascent hill climbing, all neighbors are evaluated and the best neighbor is selected.

### Failure cases

1. **Local maximum**

=> Algorithm stops at a state better than its neighbors but not globally best.

2. **Plateau**

=> All neighboring states have the same value, so the algorithm has no direction.

3. **Ridge**

=> The path to goal is narrow and requires indirect movement.

### Limitations

1. Does not guarantee optimal solution.
2. Can get stuck at local maximum.
3. Can waste time on plateau.
4. Depends heavily on heuristic function.

## **Q.12 Explain Best First Search with suitable example. [04]**

### Repeated PYQ entries

```text
Explain Best First Search with suitable example.
[04] [4 Time] [Winter 2024]

OR

Discuss Best First Search method with example.
[07] [Winter 2025]

OR

Explain the best-first search algorithm using an appropriate example.
[07] [Winter 2023]

OR

Discuss Best First Search method with example.
[07] [Winter 2021]
```

### Answer

=> **Best First Search** is an informed search method that expands the most promising node first.

=> It uses a heuristic function `h(n)` to estimate closeness to the goal.

=> It uses a priority queue ordered by heuristic value.

### Algorithm

```text
1. Put initial node in OPEN list.
2. If OPEN is empty, return failure.
3. Select node with best heuristic value.
4. If selected node is goal, return solution.
5. Expand selected node.
6. Put generated successors in OPEN.
7. Put selected node in CLOSED.
8. Repeat.
```

### Example

```text
Node    h(n)
A       10
B        6
C        4
D        8
G        0
```

=> Starting from `A`, Best First Search chooses the successor with lowest `h(n)`.

=> If `C` has `h=4` and `B` has `h=6`, then `C` is expanded before `B`.

### Advantages

1. Faster than blind search when heuristic is good.
2. Avoids many useless paths.
3. Useful in route finding and puzzle solving.

### Limitations

1. Not always optimal.
2. May get trapped by poor heuristic.
3. Requires extra heuristic knowledge.

## **Q.13 Define constraint satisfaction problem (CSP). How is it formulated as search problem? [07]**

### Repeated PYQ entries

```text
Define constraint satisfaction problem (CSP). How is it formulated as search problem?
[07] [Winter 2024]
```

### Answer

=> A **Constraint Satisfaction Problem (CSP)** is a problem defined by variables, domains and constraints.

### Components

| Component | Meaning | Example |
|---|---|---|
| Variables | Items whose values must be assigned | Regions in map coloring |
| Domains | Possible values for variables | Red, Green, Blue |
| Constraints | Rules restricting assignments | Adjacent regions must have different colors |

### Formulation as search problem

1. **Initial state**

=> Empty assignment where no variable has a value.

2. **Successor function**

=> Assign a legal value to one unassigned variable.

3. **Goal test**

=> All variables are assigned and all constraints are satisfied.

4. **Path cost**

=> Usually constant or not important because only valid assignment is needed.

### Example: map coloring

=> Variables: states/regions.

=> Domain: `{Red, Green, Blue}`.

=> Constraint: neighboring regions must have different colors.

=> CSP is solved by searching through assignments and rejecting assignments that violate constraints.

## **Q.14 Explain different issues in designing of search problems. [04]**

### Repeated PYQ entries

```text
Explain different issues in designing of search problems.
[04] [2 Time] [Summer 2024]

OR

Explain different issues in designing of search problems.
[04] [Winter 2022]
```

### Answer

=> Designing a search problem requires proper representation and control decisions.

### Issues

1. **State representation**

=> States must be represented clearly and compactly.

2. **Direction of search**

=> Search may be forward from initial state or backward from goal state.

3. **Operator selection**

=> The system must decide which rule/operator to apply.

4. **Avoiding repeated states**

=> Loops and duplicate states should be detected using closed list.

5. **Choice of search strategy**

=> BFS, DFS, Best First, A* etc. must be chosen according to problem.

6. **Use of heuristic**

=> Good heuristic reduces search time.

7. **Completeness and optimality**

=> Designer must decide whether solution guarantee or best solution is required.

## **Q.15 Explain means-ends analysis with example. [04]**

### Repeated PYQ entries

```text
Explain means-ends analysis with example.
[04] [Winter 2023]
```

### Answer

=> **Means-Ends Analysis (MEA)** is a problem-solving technique that compares the current state with the goal state and tries to reduce the difference.

### Steps

1. Compare current state and goal state.
2. Identify the most important difference.
3. Select an operator that can reduce that difference.
4. If operator preconditions are not satisfied, create a subgoal.
5. Apply the operator.
6. Repeat until goal is reached.

### Example

```text
Current state: At home
Goal state: At college
Difference: Location
Operator: Take bus
Subgoal: Reach bus stop
```

=> MEA is useful in planning because it breaks a large goal into smaller subgoals.

## **Q.16 Differentiate Generate-and-Test and Best First Search algorithm. [04]**

### Repeated PYQ entries

```text
Differentiate Generate-and-Test and Best First Search algorithm.
[04] [2 Time] [Summer 2024]

OR

Differentiate Generate-and-Test algorithm with Best First Search algorithm.
[03] [Winter 2022]
```

### Answer

| Generate-and-Test | Best First Search |
|---|---|
| Generates a possible complete solution and tests it | Expands the most promising partial state |
| Usually does not use heuristic guidance | Uses heuristic function |
| Simple but may be slow | Faster with good heuristic |
| No priority queue required | Uses priority queue |
| Useful for small puzzles and CSPs | Useful for path finding and large search spaces |
| May generate many useless candidates | Reduces useless exploration |

=> Generate-and-Test is simple, while Best First Search is more directed and efficient when heuristic knowledge is available.

## **Q.17 Explain different heuristics for Blocks World problem. [03]**

### Repeated PYQ entries

```text
Explain different heuristics for Blocks World problem.
[03] [Summer 2023]
```

### Answer

=> Blocks World is a planning problem where blocks must be arranged into a goal configuration.

### Heuristics

1. **Misplaced block heuristic**

=> Count blocks not in their correct goal position.

2. **Correct support heuristic**

=> Give better value when a block is placed on the correct supporting block or table.

3. **Penalty heuristic**

=> Add penalty for blocks that must be moved before another block can be placed correctly.

4. **Goal stack heuristic**

=> Prefer completing lower blocks first because upper blocks depend on them.

=> These heuristics help the search choose moves closer to the goal arrangement.

## **Q.18 Explain AND-OR graphs. [03]**

### Repeated PYQ entries

```text
Explain AND-OR graphs.
[03] [Summer 2023]
```

### Answer

=> This question is the same as Q.7.

=> An **AND-OR graph** represents problem reduction by dividing a problem into alternative and required subproblems.

| Node | Meaning |
|---|---|
| **OR node** | Any one child solution is enough |
| **AND node** | All child subproblems must be solved |

```text
        A
      /   \
    B(OR) C(AND)
    / \    / \
   D   E  F   G
```

=> `B` is solved by `D` or `E`, while `C` is solved only when both `F` and `G` are solved.

## **Q.19 Explain depth-first search algorithm. [04]**

### Repeated PYQ entries

```text
Explain depth-first search algorithm.
[04] [2 Time] [Summer 2023]

OR

Explain depth-first search algorithm.
[04] [Summer 2022]
```

### Answer

=> **Depth First Search (DFS)** expands the deepest node first.

=> It explores one branch completely before backtracking.

=> DFS uses a stack or recursion.

### Algorithm

```text
DFS(node):
1. If node is goal, return solution.
2. Mark node as visited.
3. For each unvisited successor:
      call DFS(successor)
4. If no successor gives solution, backtrack.
```

### Example

```text
        A
      / | \
     B  C  D
    / \
   E   F

DFS order: A, B, E, F, C, D
```

### Properties

1. Requires less memory than BFS.
2. Not optimal.
3. May get stuck in infinite-depth path.
4. Complete only for finite search space with cycle checking.

## **Q.20 Explain production system. [04]**

### Repeated PYQ entries

```text
Explain production system.
[04] [Summer 2022]
```

### Answer

=> A **production system** is an AI problem-solving model based on condition-action rules.

### Rule format

```text
IF condition THEN action
```

### Components

1. **Production rules**

=> Rules that specify actions for matching conditions.

2. **Working memory**

=> Stores current facts or current state.

3. **Control strategy**

=> Decides which rule should be applied when many rules match.

4. **Recognize-act cycle**

=> Matches rules, selects a rule and applies its action.

### Example

```text
IF room is dirty THEN clean room
IF battery is low THEN go to charging station
```

=> Production systems are used in expert systems, planning and rule-based reasoning.

## **Q.21 Describe heuristic function for 8-puzzle problem. [04]**

### Repeated PYQ entries

```text
Describe heuristic function for 8-puzzle problem.
[04] [2 Time] [Winter 2021]

OR

Explain any two heuristic functions for 8-puzzle problem with an appropriate example.
[07] [Winter 2023]
```

### Answer

=> A **heuristic function** estimates how close a state is to the goal.

=> In 8-puzzle, heuristic values help A* or Best First Search choose promising states.

### 1. Misplaced tile heuristic

=> Count the number of tiles that are not in their goal position.

### 2. Manhattan distance heuristic

=> Sum of horizontal and vertical distances of each tile from its goal position.

```text
Manhattan distance = |current row - goal row| + |current column - goal column|
```

### Example

```text
Current State          Goal State
+---+---+---+          +---+---+---+
| 1 | 2 | 3 |          | 1 | 2 | 3 |
+---+---+---+          +---+---+---+
| 8 | 4 |   |          | 8 |   | 4 |
+---+---+---+          +---+---+---+
| 7 | 6 | 5 |          | 7 | 6 | 5 |
+---+---+---+          +---+---+---+
```

=> Tile `4` is misplaced and blank is ignored.

=> Misplaced tile heuristic `h1 = 1`.

=> Manhattan distance for tile `4` is 1 move, so `h2 = 1`.

### Comparison

| Heuristic | Meaning | Quality |
|---|---|---|
| Misplaced tiles | Counts wrong-position tiles | Simple |
| Manhattan distance | Counts total grid distance | More informative |

## **Q.22 Describe state space representation for Missionaries and Cannibals problem. [07]**

### Repeated PYQ entries

```text
Describe state space representation for Missionaries and Cannibals problem.
[07] [Winter 2021]
```

### Answer

=> In the Missionaries and Cannibals problem, three missionaries and three cannibals must cross a river using a boat.

=> The boat can carry one or two people.

=> On either bank, missionaries must not be outnumbered by cannibals when missionaries are present.

### State representation

```text
(M, C, B)
```

=> `M` = number of missionaries on left bank.

=> `C` = number of cannibals on left bank.

=> `B` = boat position, `L` for left and `R` for right.

### Initial and goal state

```text
Initial state: (3,3,L)
Goal state:    (0,0,R)
```

### Operators

1. Move one missionary.
2. Move two missionaries.
3. Move one cannibal.
4. Move two cannibals.
5. Move one missionary and one cannibal.

### Validity condition

```text
Left bank:  M = 0 or M >= C
Right bank: M_right = 0 or M_right >= C_right
```

### One valid solution path

```text
(3,3,L) -> (3,1,R)
(3,1,R) -> (3,2,L)
(3,2,L) -> (3,0,R)
(3,0,R) -> (3,1,L)
(3,1,L) -> (1,1,R)
(1,1,R) -> (2,2,L)
(2,2,L) -> (0,2,R)
(0,2,R) -> (0,3,L)
(0,3,L) -> (0,1,R)
(0,1,R) -> (0,2,L)
(0,2,L) -> (0,0,R)
```

=> The final state `(0,0,R)` means all missionaries and cannibals have crossed safely.
