# **2 Problems, State Space Search and Heuristic Search**

## **2.1 Problem Solving in AI**

=> **Problem solving** means finding a sequence of actions that transforms an initial state into a goal state.

=> In AI, a problem must be represented formally so that a search algorithm can explore possible actions and find a solution.

### Important parts of a problem

1. **Initial state**

=> Starting state of the problem.

2. **Actions / operators**

=> Legal moves that can be applied in a state.

3. **Transition model / successor function**

=> Describes the state produced after applying an action.

4. **Goal test**

=> Checks whether a state is a goal state.

5. **Path cost**

=> Numeric cost of the path from initial state to current state.

### Example

=> In an 8-puzzle problem, the initial state is the starting tile arrangement, actions are blank-tile moves, goal test checks final arrangement, and path cost is usually the number of moves.

## **2.2 Defining Problems as State Space Search**

=> **State space** is the set of all possible states reachable from the initial state by applying legal operators.

=> **State space search** means searching through this set of states to find a path from the initial state to a goal state.

### State space representation

```text
Initial State -> Apply Operators -> New States -> ... -> Goal State
```

### Search tree terms

| Term | Meaning |
|---|---|
| **State** | Configuration of the problem |
| **Node** | Data structure containing state, parent, action, cost and depth |
| **Root node** | Node representing the initial state |
| **Leaf node** | Node not yet expanded |
| **Fringe / frontier** | Generated nodes waiting for expansion |
| **Expanded node** | Node whose successors are generated |
| **Search strategy** | Rule for selecting the next node from the fringe |

### Node representation

1. State.
2. Parent node.
3. Action used to reach the state.
4. Path cost `g(n)`.
5. Depth.

## **2.3 Tree Search and Graph Search**

### Tree search algorithm

```text
1. Create root node from initial state.
2. Put root node into fringe.
3. If fringe is empty, return failure.
4. Remove one node from fringe according to search strategy.
5. If node satisfies goal test, return solution.
6. Expand node and add successors to fringe.
7. Repeat steps 3 to 6.
```

### Graph search algorithm

=> Graph search avoids repeated states using an explored set or closed list.

```text
1. Put initial node in OPEN list.
2. Keep CLOSED list empty.
3. Select best node from OPEN.
4. If it is goal, return solution.
5. Move it to CLOSED.
6. Generate successors.
7. Add only non-repeated useful successors to OPEN.
8. Repeat until OPEN is empty.
```

### Difference between tree search and graph search

| Tree Search | Graph Search |
|---|---|
| May generate same state many times | Avoids repeated states |
| No closed list required | Uses closed/explored list |
| Simple but may loop | More efficient in cyclic spaces |
| Suitable for small acyclic problems | Suitable for real search problems |

## **2.4 Measuring Search Performance**

=> Search algorithms are evaluated using four criteria.

| Criterion | Meaning |
|---|---|
| **Completeness** | Finds a solution if one exists |
| **Optimality** | Finds the best/least-cost solution |
| **Time complexity** | Number of nodes generated or expanded |
| **Space complexity** | Maximum number of nodes stored in memory |

=> `b` usually denotes branching factor, `d` denotes depth of shallowest goal and `m` denotes maximum depth.

## **2.5 Uninformed Search Strategies**

=> **Uninformed search** is also called **blind search**.

=> It uses only the problem definition and does not use extra knowledge about which state is closer to the goal.

### Important uninformed searches

1. Breadth First Search.
2. Depth First Search.
3. Uniform Cost Search.
4. Depth Limited Search.
5. Iterative Deepening Search.
6. Bidirectional Search.

## **2.6 Breadth First Search (BFS)**

=> **BFS** expands the shallowest node first.

=> It explores the search tree level by level.

=> It uses a **FIFO queue**.

### Algorithm

```text
1. Insert initial node into queue.
2. If queue is empty, return failure.
3. Remove node from front of queue.
4. If node is goal, return solution.
5. Expand node.
6. Insert all successors at rear of queue.
7. Repeat.
```

### Example order

```text
        A
      / | \
     B  C  D
    / \    |
   E   F   G

BFS order: A, B, C, D, E, F, G
```

### Properties

| Property | BFS |
|---|---|
| Complete | Yes, if branching factor is finite |
| Optimal | Yes, if all step costs are equal |
| Time | `O(b^(d+1))` |
| Space | `O(b^(d+1))` |

### When BFS is better than DFS

=> BFS is better when the goal is expected to be near the root or when the shortest path is required.

=> Example: Finding the shortest path in an unweighted graph.

## **2.7 Depth First Search (DFS)**

=> **DFS** expands the deepest node first.

=> It follows one path as deep as possible before backtracking.

=> It uses a **stack** or recursion.

### Algorithm

```text
DFS(node):
1. If node is goal, return solution.
2. Mark node as visited.
3. For each unvisited successor:
      call DFS(successor)
4. If no successor gives solution, backtrack.
```

### Example order

```text
        A
      / | \
     B  C  D
    / \    |
   E   F   G

DFS order: A, B, E, F, C, D, G
```

### Properties

| Property | DFS |
|---|---|
| Complete | No in infinite-depth spaces; yes in finite spaces with cycle checking |
| Optimal | No |
| Time | `O(b^m)` |
| Space | `O(bm)` |

### Limitations

1. Can get stuck in infinite path.
2. Does not guarantee shortest solution.
3. Search order strongly affects result.

## **2.8 BFS vs DFS**

| Point | BFS | DFS |
|---|---|---|
| Expansion | Level by level | Deep path first |
| Data structure | Queue | Stack / recursion |
| Completeness | Complete for finite branching | Not complete in infinite spaces |
| Optimality | Optimal for equal step cost | Not optimal |
| Memory | High | Low |
| Best use | Shortest path in unweighted graph | Memory-limited deep search |

## **2.9 Uniform Cost Search**

=> **Uniform Cost Search (UCS)** expands the node with the lowest path cost `g(n)`.

=> It is useful when step costs are different.

=> It uses a priority queue ordered by `g(n)`.

### Properties

1. Complete if every step cost is positive.
2. Optimal because it expands lowest-cost path first.
3. May require high memory.

## **2.10 Depth Limited and Iterative Deepening Search**

### Depth Limited Search

=> DLS is DFS with a fixed depth limit.

=> It avoids infinite paths but may miss the solution if the limit is too small.

### Iterative Deepening DFS

=> IDDFS repeatedly applies DLS with increasing depth limits.

```text
for depth = 0 to infinity:
    result = DLS(initial, depth)
    if result is solution:
        return result
```

=> It combines BFS completeness with DFS low memory.

## **2.11 Bidirectional Search**

=> Bidirectional search runs two searches:

1. Forward from initial state.
2. Backward from goal state.

=> Search stops when both frontiers meet.

=> Time and space complexity can reduce from `O(b^d)` to `O(b^(d/2))`.

## **2.12 Production Systems**

=> **Production system** is a problem-solving model based on production rules.

=> A production rule has the form:

```text
IF condition THEN action
```

### Components

| Component | Meaning |
|---|---|
| **Production rules** | Set of condition-action rules |
| **Working memory** | Current facts/state |
| **Control strategy** | Selects which rule to apply |
| **Recognize-act cycle** | Match rules, choose rule, apply action |

### Recognize-act cycle

```text
1. Match rule conditions with working memory.
2. Create conflict set of applicable rules.
3. Select one rule using control strategy.
4. Apply rule action.
5. Update working memory.
6. Repeat until goal is reached.
```

### Example

```text
IF room is dirty THEN clean room
IF battery is low THEN go to charging station
```

## **2.13 Production Characteristics**

=> Production characteristics describe how a production rule system behaves.

### Main characteristics

| Characteristic | Meaning |
|---|---|
| **Monotonic** | Applying a rule does not prevent later application of another useful rule |
| **Non-monotonic** | Applying a rule may prevent or remove another rule's usefulness |
| **Partially commutative** | Order of independent rule applications does not affect final result |
| **Non-partially commutative** | Rule order affects final result |

### Monotonic vs non-monotonic

| Monotonic | Non-monotonic |
|---|---|
| Facts are not deleted | Facts may be deleted or changed |
| Easier to reason | More complex |
| Example: theorem proving | Example: planning with changing world |

## **2.14 Production System Characteristics**

=> A good production system should have suitable control and rule properties.

### Important characteristics

1. Rules should be clear and modular.
2. Rules should be easy to add, delete or modify.
3. Control strategy should avoid useless search.
4. Conflict resolution should select the most suitable rule.
5. System should support backtracking when needed.
6. System should avoid repeated states.
7. System should terminate when a goal is reached.

## **2.15 Issues in the Design of Search Programs**

=> Designing a search program requires choosing representation, direction and control strategy.

### Important issues

1. **Direction of search**

=> Search may be forward from initial state or backward from goal state.

2. **Rule selection**

=> When many rules are applicable, the system must choose the best rule.

3. **State representation**

=> States should be represented compactly and clearly.

4. **Avoiding repeated states**

=> Loops and duplicate states must be detected.

5. **Choosing data structure**

=> Queue, stack or priority queue depends on the search strategy.

6. **Use of heuristic knowledge**

=> Heuristics reduce search effort by selecting promising states.

7. **Completeness and optimality**

=> The designer must decide whether guaranteed solution or best solution is required.

## **2.16 Additional AI Problems**

### Toy problems

=> Toy problems have exact and simple descriptions. They are useful for understanding search algorithms.

#### Examples

1. 8-puzzle.
2. Water jug problem.
3. Missionaries and Cannibals.
4. Tower of Hanoi.
5. 8-queen problem.
6. Cryptarithmetic.

### Real-world problems

=> Real-world problems are larger, less predictable and more complex.

#### Examples

1. Route finding.
2. Travelling Salesman Problem.
3. Robot navigation.
4. VLSI layout.
5. Assembly sequencing.
6. Medical diagnosis.

## **2.17 Water Jug Problem**

=> In the water jug problem, we are given jugs of fixed capacity and must measure a required amount of water.

### State representation

=> For two jugs of capacity `m` and `n`, a state is represented as:

```text
(x, y)
```

=> `x` is water in first jug and `y` is water in second jug.

### Operators

1. Fill first jug.
2. Fill second jug.
3. Empty first jug.
4. Empty second jug.
5. Pour first jug into second jug.
6. Pour second jug into first jug.

### Example: 8 liter and 5 liter jugs, get 4 liters in 8 liter jug

```text
Jug capacities: (8, 5)
Initial state:  (0, 0)
Goal:           (4, y)

(0,0) -> (0,5) -> (5,0) -> (5,5) -> (8,2)
      -> (0,2) -> (2,0) -> (2,5) -> (7,0)
      -> (7,5) -> (8,4) -> (0,4) -> (4,0)
```

=> Final state `(4,0)` has exactly 4 liters in the 8-liter jug.

## **2.18 8-Puzzle Problem**

=> 8-puzzle has eight numbered tiles and one blank space on a 3x3 board.

=> The goal is to move tiles by sliding the blank to reach the required goal configuration.

### State representation

```text
Initial State           Goal State
+---+---+---+           +---+---+---+
| 2 | 8 | 3 |           | 1 | 2 | 3 |
+---+---+---+           +---+---+---+
| 1 | 6 | 4 |           | 8 |   | 4 |
+---+---+---+           +---+---+---+
| 7 |   | 5 |           | 7 | 6 | 5 |
+---+---+---+           +---+---+---+
```

### Operators

1. Move blank up.
2. Move blank down.
3. Move blank left.
4. Move blank right.

### Common heuristic functions

| Heuristic | Meaning |
|---|---|
| `h1(n)` | Number of misplaced tiles |
| `h2(n)` | Sum of Manhattan distances of tiles from goal positions |

=> Manhattan distance is usually more informative than misplaced-tile count.

## **2.19 Missionaries and Cannibals Problem**

=> Three missionaries and three cannibals must cross a river using a boat that can carry at most two people.

=> On either bank, missionaries must never be outnumbered by cannibals if missionaries are present.

### State representation

```text
(M, C, B)
```

=> `M` = missionaries on left bank, `C` = cannibals on left bank, `B` = boat side.

=> Initial state: `(3,3,L)`

=> Goal state: `(0,0,R)`

### Operators

1. Move one missionary.
2. Move two missionaries.
3. Move one cannibal.
4. Move two cannibals.
5. Move one missionary and one cannibal.

### Valid state condition

```text
M = 0 or M >= C on left bank
M_right = 0 or M_right >= C_right on right bank
```

## **2.20 Cryptarithmetic Problem**

=> Cryptarithmetic is a puzzle where letters represent digits and the arithmetic equation must be true.

### Constraints

1. Each letter represents exactly one digit.
2. Different letters must have different digits.
3. Leading letters cannot be zero.
4. Arithmetic operation must be correct.

### Example

```text
  SEND
+ MORE
------
 MONEY
```

=> One solution is:

```text
S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2

  9567
+ 1085
------
 10652
```

## **2.21 Generate-and-Test**

=> **Generate-and-Test** is a simple search technique that generates possible solutions and tests each one against the goal condition.

### Algorithm

```text
1. Generate a possible solution.
2. Test whether it satisfies all conditions.
3. If yes, return solution.
4. If no, generate another solution.
5. Repeat until solution is found or all possibilities fail.
```

### Advantages

1. Simple to implement.
2. Useful when possible solutions can be generated easily.
3. Works for constraint-based puzzles.

### Limitations

1. Inefficient without heuristic guidance.
2. May generate many useless candidates.
3. Can be very slow for large search spaces.

## **2.22 Hill Climbing**

=> **Hill climbing** is a heuristic search method that moves from the current state to a better neighboring state.

=> It is called local search because it keeps only the current state and its neighbors.

### Simple hill climbing algorithm

```text
1. Start with initial state.
2. Evaluate current state.
3. Generate neighboring states.
4. Select a better neighbor.
5. If no better neighbor exists, stop.
6. Otherwise move to better neighbor and repeat.
```

### Steepest-ascent hill climbing

=> It evaluates all neighbors and chooses the best neighbor.

### Hill climbing problems

| Problem | Meaning |
|---|---|
| **Local maximum** | State better than neighbors but not globally best |
| **Plateau** | Flat area where many states have same value |
| **Ridge** | Narrow path where progress requires indirect moves |

### Limitations

1. Can stop at local maximum.
2. Can wander on plateau.
3. Can fail on ridges.
4. Does not guarantee optimal solution.
5. Depends heavily on heuristic function.

## **2.23 Best First Search**

=> **Best First Search** expands the most promising node according to an evaluation function.

=> It uses a priority queue.

### Evaluation function

```text
f(n) = h(n)
```

=> `h(n)` estimates the distance or cost from node `n` to the goal.

### Algorithm

```text
1. Put initial node in OPEN.
2. If OPEN is empty, return failure.
3. Remove node with best heuristic value from OPEN.
4. If node is goal, return solution.
5. Generate successors.
6. Put successors into OPEN according to heuristic value.
7. Put expanded node into CLOSED.
8. Repeat.
```

### Example

```text
Node    h(n)
A       10
B        6
C        4
D        8
Goal     0
```

=> Best First Search expands the node with the smallest `h(n)` first.

## **2.24 Breadth First Search vs Best First Search**

| Breadth First Search | Best First Search |
|---|---|
| Blind search | Heuristic search |
| Expands shallowest node | Expands most promising node |
| Uses queue | Uses priority queue |
| Does not use `h(n)` | Uses heuristic function |
| Complete for finite branching | Completeness depends on implementation |
| Optimal for equal step costs | Not always optimal |

## **2.25 Generate-and-Test vs Best First Search**

| Generate-and-Test | Best First Search |
|---|---|
| Generates candidate solution and tests it | Expands best-looking partial state |
| Usually unguided | Guided by heuristic |
| Simple but inefficient | More efficient with good heuristic |
| No priority queue required | Uses priority queue |
| Useful for small constraint puzzles | Useful for path-finding/search problems |

## **2.26 Problem Reduction and AND-OR Graphs**

=> **Problem reduction** solves a complex problem by breaking it into smaller subproblems.

=> It is represented using **AND-OR graphs**.

### OR node

=> An OR node is solved if any one child is solved.

=> Example: To reach a city, choose route A or route B.

### AND node

=> An AND node is solved only if all required child subproblems are solved.

=> Example: To pass a course, pass theory and practical.

### AND-OR graph diagram

```text
        A
      /   \
    B(OR) C(AND)
    / \    / \
   D   E  F   G

B is solved by D or E.
C is solved only when F and G both are solved.
```

## **2.27 Constraint Satisfaction Problem (CSP)**

=> A **Constraint Satisfaction Problem** is a problem defined by variables, domains and constraints.

### CSP formulation

| Component | Meaning | Example in map coloring |
|---|---|---|
| **Variables** | Items to assign values | Regions |
| **Domains** | Possible values | Red, Green, Blue |
| **Constraints** | Rules restricting assignments | Adjacent regions must have different colors |

### CSP as search

=> A state is a partial assignment of values to variables.

=> Initial state is empty assignment.

=> Operators assign a value to an unassigned variable.

=> Goal state is a complete assignment satisfying all constraints.

### Examples

1. Map coloring.
2. 8-queen problem.
3. Sudoku.
4. Cryptarithmetic.
5. Timetable scheduling.

## **2.28 Means-Ends Analysis**

=> **Means-Ends Analysis (MEA)** is a problem-solving technique that compares current state with goal state and reduces the difference.

### Steps

1. Compare current state and goal state.
2. Find the most important difference.
3. Select an operator that reduces the difference.
4. If operator preconditions are not satisfied, create a subgoal.
5. Apply operator.
6. Repeat until goal is reached.

### Example

=> Goal: reach college from home.

```text
Current state: At home
Goal state: At college
Difference: Location
Operator: Take bus
Subgoal: Reach bus stop
```

=> MEA is useful in planning because it works backward through differences and subgoals.

## **2.29 A* Search**

=> **A\* search** is an informed search algorithm that combines actual path cost and estimated goal cost.

### Evaluation function

```text
f(n) = g(n) + h(n)
```

| Term | Meaning |
|---|---|
| `g(n)` | Actual cost from start to node `n` |
| `h(n)` | Estimated cost from node `n` to goal |
| `f(n)` | Estimated total solution cost through `n` |

### Algorithm

```text
1. Put start node in OPEN.
2. Set g(start)=0 and calculate f(start).
3. Select node with smallest f(n) from OPEN.
4. If selected node is goal, return path.
5. Move selected node to CLOSED.
6. Generate successors and calculate g, h and f.
7. If a better path to a successor is found, update it.
8. Repeat until goal is found or OPEN is empty.
```

### Admissible heuristic

=> A heuristic is **admissible** if it never overestimates the true cost to the goal.

```text
h(n) <= h*(n)
```

=> If `h(n)` is admissible and step costs are positive, A* is optimal.

### Underestimation and overestimation

| Case | Effect |
|---|---|
| `h(n)` underestimates true cost | A* remains optimal but may expand more nodes |
| `h(n)` equals true cost | A* directly follows optimal path |
| `h(n)` overestimates true cost | A* may become faster but may lose optimality |

## **2.30 AO* Search**

=> **AO\*** is a heuristic search algorithm used for AND-OR graphs.

=> It finds the best solution graph, not only a single path.

### AO* algorithm

```text
1. Start with initial node.
2. Follow marked best arcs to find a non-terminal tip node.
3. Expand that tip node.
4. Assign heuristic values to newly generated nodes.
5. Update cost of ancestors using AND/OR cost rules.
6. Mark the best successor or successor set.
7. Stop when the start node is solved.
```

### Cost rules

1. **OR node**

=> Choose the child with minimum cost.

```text
Cost(A) = min(cost of each child path)
```

2. **AND node**

=> Add costs of all required children.

```text
Cost(A) = sum(costs of required child subproblems)
```

### Use

=> AO* is used in planning, diagnosis and problem reduction problems where all subproblems of an AND node must be solved.

## **2.31 Blocks World Heuristics**

=> Blocks World contains blocks on a table. The goal is to rearrange blocks into a target configuration.

### Common heuristics

1. **Number of misplaced blocks**

=> Count blocks not in their goal position.

2. **Support relation heuristic**

=> Give score based on whether a block is supported by the correct block/table.

3. **Goal stack heuristic**

=> Prefer moves that complete lower blocks first because upper blocks depend on them.

4. **Penalty heuristic**

=> Add penalty for blocks that must be moved before correct placement is possible.

## **2.32 Exam Short Questions**

### 1. Define state space search.

=> State space search is the process of searching through possible states to find a path from the initial state to a goal state.

### 2. List components of a well-defined problem.

=> Initial state, actions, transition model/successor function, goal test and path cost.

### 3. What is a successor function?

=> A successor function generates all possible next states from a given state by applying legal actions.

### 4. Define fringe/frontier.

=> Fringe or frontier is the set of generated nodes that are waiting to be expanded.

### 5. List performance measures of search algorithms.

=> Completeness, optimality, time complexity and space complexity.

### 6. Define BFS and DFS.

=> BFS expands nodes level by level using a queue, while DFS expands the deepest node first using stack or recursion.

### 7. Compare BFS and DFS.

=> BFS is complete and optimal for equal costs but needs more memory; DFS uses less memory but is not optimal and may get stuck in deep paths.

### 8. What is a production system?

=> A production system is a rule-based problem-solving model using condition-action rules, working memory and a control strategy.

### 9. List production system components.

=> Production rules, working memory, control strategy and recognize-act cycle.

### 10. Define generate-and-test.

=> Generate-and-test generates possible solutions and tests each one until a valid solution is found.

### 11. What is hill climbing?

=> Hill climbing is a heuristic local search method that repeatedly moves to a better neighboring state.

### 12. Define local maximum, plateau and ridge.

=> Local maximum is a non-global peak, plateau is a flat area with equal values, and ridge is a narrow path where direct improvement is difficult.

### 13. Define best first search.

=> Best first search expands the most promising node according to a heuristic evaluation function.

### 14. What is a heuristic function?

=> A heuristic function estimates how close a state is to the goal.

### 15. Define CSP.

=> A Constraint Satisfaction Problem consists of variables, domains and constraints that must be satisfied.

### 16. What is means-ends analysis?

=> Means-ends analysis reduces the difference between current state and goal state by selecting suitable operators.

### 17. Write A* evaluation function.

```text
f(n) = g(n) + h(n)
```

### 18. What is an admissible heuristic?

=> An admissible heuristic never overestimates the true cost to reach the goal.

### 19. Define AO* algorithm.

=> AO* is a heuristic search algorithm used to find the best solution graph in AND-OR graphs.

### 20. What is an AND-OR graph?

=> An AND-OR graph represents problem reduction using OR nodes for alternatives and AND nodes for required subproblems.

### 21. Give two heuristics for 8-puzzle.

=> Misplaced tile count and Manhattan distance.

### 22. Give state representation for missionaries and cannibals.

```text
(M, C, B)
```

=> `M` is missionaries on left bank, `C` is cannibals on left bank and `B` is boat side.
