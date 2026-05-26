# **1 What is Artificial Intelligence**

## **1.1 Introduction**

=> **Definition**: `Artificial Intelligence (AI) is a branch of computer science that deals with creating machines or software systems that can perform tasks which normally require human intelligence.`

=> These tasks include reasoning, learning, problem solving, planning, understanding language, recognizing patterns and making decisions.

=> AI does not only try to copy human thinking. Its practical goal is to build **intelligent agents** that can perceive their environment and take suitable actions to achieve a goal.

### Important points

1. AI systems use knowledge, data and algorithms to solve problems.
2. AI can work in situations where exact programming is difficult.
3. AI systems may learn from experience and improve performance.
4. AI is useful in expert systems, robotics, games, speech recognition, diagnosis and planning.
5. AI often handles incomplete, uncertain or changing information.

## **1.2 Definitions and Approaches of AI**

=> Different researchers define AI from different viewpoints.

### Main AI approaches

| Approach | Meaning | Example |
|---|---|---|
| **Acting humanly** | Machine behaves like a human | Turing Test chatbot |
| **Thinking humanly** | Machine follows human-like thinking process | Cognitive model |
| **Thinking rationally** | Machine uses logic and correct reasoning | Theorem prover |
| **Acting rationally** | Machine takes the best possible action | Autonomous taxi |

### 1. Acting humanly

=> A system is intelligent if its behavior cannot be distinguished from human behavior.

=> This idea is tested using the **Turing Test**.

### 2. Thinking humanly

=> This approach studies how humans think and tries to build computer models of human thought.

=> It is related to psychology and cognitive science.

### 3. Thinking rationally

=> This approach uses laws of thought and formal logic to reach correct conclusions.

=> Example: If all humans are mortal and Socrates is human, then Socrates is mortal.

### 4. Acting rationally

=> This approach builds agents that select actions to maximize expected performance.

=> Modern AI mostly follows this approach because it is practical for real-world systems.

## **1.3 Foundations of AI**

=> AI is an interdisciplinary field. It takes ideas from many subjects.

| Foundation | Contribution to AI |
|---|---|
| **Philosophy** | Logic, reasoning, mind, knowledge and ethics |
| **Mathematics** | Probability, algorithms, optimization and formal logic |
| **Economics** | Decision making, utility and game theory |
| **Neuroscience** | Study of brain and neural processing |
| **Psychology** | Human learning, perception and behavior |
| **Computer engineering** | Efficient hardware and software for AI programs |
| **Control theory** | Feedback, stability and autonomous control |
| **Linguistics** | Natural language understanding and grammar |

## **1.4 Strong AI and Weak AI**

### Strong AI

=> **Strong AI** means an AI system that actually understands, thinks and has intelligence like a human mind.

=> Such a system would not only simulate intelligence but would truly possess reasoning, consciousness and understanding.

=> Strong AI is still a theoretical goal and has not been achieved in the full human-like sense.

### Weak AI

=> **Weak AI** means an AI system designed to perform a specific intelligent task without real consciousness or self-awareness.

=> Most current AI systems are weak AI.

### Difference between Strong AI and Weak AI

| Strong AI | Weak AI |
|---|---|
| Has real intelligence and understanding | Simulates intelligent behavior |
| General-purpose intelligence | Task-specific intelligence |
| Human-like consciousness is assumed | No consciousness is required |
| Mostly theoretical | Commonly used today |
| Example: human-level thinking machine | Example: chatbot, chess engine, recommendation system |

## **1.5 Task Domains of AI**

=> AI problems are commonly grouped into three task domains.

### Task domains

| Domain | Meaning | Examples |
|---|---|---|
| **Mundane tasks** | Common tasks humans perform naturally | Vision, speech, natural language, common sense reasoning |
| **Formal tasks** | Well-defined symbolic or mathematical tasks | Game playing, theorem proving, logic, puzzles |
| **Expert tasks** | Tasks requiring specialist knowledge | Medical diagnosis, engineering design, financial analysis |

### 1. Mundane tasks

=> These tasks look easy for humans but are difficult for machines because they need perception and common sense.

#### Examples

1. Recognizing faces.
2. Understanding spoken language.
3. Reading handwriting.
4. Moving safely in a room.
5. Understanding everyday situations.

### 2. Formal tasks

=> These tasks have clear rules and can be represented using logic, symbols or state spaces.

#### Examples

1. Chess.
2. 8-puzzle.
3. Mathematical theorem proving.
4. Game playing.
5. Search problems.

### 3. Expert tasks

=> These tasks require domain-specific knowledge and decision-making ability.

#### Examples

1. Medical diagnosis.
2. Fault diagnosis in machines.
3. Geological exploration.
4. Chemical analysis.
5. Legal or financial advice.

## **1.6 Applications of AI**

=> AI is used in many real-world areas where reasoning, prediction, automation or pattern recognition is required.

### Important application areas

1. **Game playing**

=> AI programs can play games such as chess, checkers and Go by searching possible moves and evaluating positions.

=> Example: IBM Deep Blue defeated Garry Kasparov in chess in 1997.

2. **Expert systems**

=> Expert systems use knowledge of human experts to solve domain-specific problems.

=> Example: MYCIN was used for medical diagnosis of bacterial infections.

3. **Natural language processing**

=> AI helps computers understand, translate and generate human language.

=> Example: chatbots, machine translation, grammar checking and voice assistants.

4. **Speech recognition**

=> AI converts spoken words into text or commands.

=> Example: Google Assistant, Siri and dictation software.

5. **Computer vision**

=> AI enables machines to understand images and videos.

=> Example: face recognition, object detection, medical image analysis and self-driving cars.

6. **Robotics**

=> Robots use AI for perception, movement planning and decision making.

=> Example: industrial robots, surgical robots and warehouse robots.

7. **Planning and scheduling**

=> AI prepares a sequence of actions to achieve a goal under constraints.

=> Example: NASA Remote Agent, airline scheduling and logistics planning.

8. **Medical diagnosis**

=> AI analyzes symptoms, reports and images to support doctors in diagnosis.

=> Example: cancer detection from medical scans.

9. **Autonomous vehicles**

=> AI helps vehicles detect lanes, signs, obstacles and pedestrians and then take driving decisions.

10. **Recommendation systems**

=> AI predicts user preferences and recommends items.

=> Example: movie recommendations, product suggestions and music playlists.

## **1.7 AI Problems**

=> An **AI problem** is a problem that requires intelligent behavior such as reasoning, learning, planning, perception or decision making.

=> AI problems are often difficult because the search space is large, knowledge may be incomplete and the environment may change.

### Examples of AI problems

1. Playing chess.
2. Solving the 8-puzzle.
3. Diagnosing a disease.
4. Understanding natural language.
5. Recognizing objects in an image.
6. Planning a robot path.
7. Proving a mathematical theorem.

## **1.8 AI Problem Characteristics**

=> Before selecting an AI technique, the characteristics of the problem must be studied.

### Important characteristics

| Characteristic | Meaning | Example |
|---|---|---|
| **Decomposable** | Problem can be divided into smaller subproblems | Mathematical integration |
| **Ignorable steps** | Some wrong steps can be ignored without affecting final solution | Theorem proving |
| **Recoverable steps** | Wrong steps can be undone | 8-puzzle, chess move analysis |
| **Irrecoverable steps** | Wrong step cannot be undone easily | Robot moving in real world |
| **Predictable universe** | Result of action is known | Board game |
| **Unpredictable universe** | Result may be uncertain | Medical diagnosis |
| **Good solution required** | Approximate solution is acceptable | Route planning |
| **Optimal solution required** | Best solution is necessary | Shortest path |
| **Knowledge intensive** | Large domain knowledge is needed | Expert medical system |
| **Interactive** | System must interact with user/environment | Chatbot, tutoring system |

### 1. Is the problem decomposable?

=> If a problem can be divided into independent smaller problems, it becomes easier to solve.

=> Example: A complex mathematical expression can be divided into smaller parts.

### 2. Can solution steps be ignored or undone?

=> Some problems allow wrong steps to be ignored or reversed.

=> Example: In the 8-puzzle, a tile movement can be reversed.

=> In real robot movement, a wrong movement may cause damage, so it may be irrecoverable.

### 3. Is the universe predictable?

=> In a predictable environment, the result of each action is known.

=> Example: Chess rules are fixed, so move results are predictable.

=> In an unpredictable environment, results may vary due to uncertainty.

=> Example: Disease treatment may have different effects on different patients.

### 4. Is a good solution enough?

=> Some problems need the best possible solution, while others accept a good practical solution.

=> Example: In route planning, a near-shortest route may be acceptable.

### 5. Is domain knowledge required?

=> Some problems require large expert knowledge.

=> Example: Medical diagnosis requires symptoms, diseases, tests and treatment knowledge.

### 6. Does the problem require interaction?

=> Some AI systems must continuously interact with users or the environment.

=> Example: A chatbot must understand user input and respond immediately.

## **1.9 Underlying Assumption of AI Techniques**

=> The main assumption behind AI is that intelligent reasoning can be represented and manipulated using symbols.

=> This idea is known as the **Physical Symbol System Hypothesis**.

### Physical Symbol System Hypothesis

=> A physical symbol system contains symbols, expressions and processes that can create, modify and interpret symbols.

=> The hypothesis says that a physical symbol system has the necessary and sufficient means for general intelligent action.

### Meaning in AI

1. Knowledge can be represented using symbols.
2. Symbol manipulation can produce intelligent behavior.
3. Human reasoning can be approximated by computer programs.
4. Logic, rules and search can be used for problem solving.

### Examples

1. Logic expressions.
2. Algebraic equations.
3. Chess board representation.
4. Rules in expert systems.
5. Frames and semantic networks.

## **1.10 AI Techniques**

=> An **AI technique** is a method used to represent and use knowledge efficiently to solve AI problems.

=> AI techniques are useful when data is incomplete, uncertain, changing or very large.

### Requirements of an AI technique

1. It should represent knowledge clearly.
2. It should capture general patterns, not only individual facts.
3. It should allow easy modification of knowledge.
4. It should support reasoning with incomplete information.
5. It should help search for solutions efficiently.

### Major AI techniques

| Technique | Meaning | Example |
|---|---|---|
| **Search** | Explore possible solutions | BFS, DFS, A* |
| **Use of knowledge** | Apply domain knowledge to reduce search | Expert system rules |
| **Abstraction** | Ignore unnecessary details | Map route planning |
| **Heuristics** | Use experience-based rules | Choose promising chess move |
| **Learning** | Improve from data/experience | Spam detection |

## **1.11 Level of AI Model**

=> While building AI systems, we must decide the level at which intelligence is modeled.

### Main levels

1. **Result-oriented model**

=> The system only tries to produce correct results.

=> It does not try to copy human thinking.

=> Example: A calculator solves arithmetic faster than humans but does not think like humans.

2. **Human-performance model**

=> The system tries to model how humans solve the same problem.

=> It is useful for psychology and cognitive science.

=> Example: A program that simulates human problem-solving steps.

3. **Rational-agent model**

=> The system selects actions that maximize performance according to a goal.

=> Example: A self-driving car choosing a safe and efficient driving action.

## **1.12 Criteria for Success**

=> Measuring success in AI is difficult because intelligence itself is hard to define.

=> A common criterion is whether the system performs intelligently in a given task.

### Important criteria

1. Correctness of answer.
2. Ability to learn from experience.
3. Ability to handle uncertainty.
4. Ability to act autonomously.
5. Ability to communicate naturally.
6. Ability to solve new problems.
7. Performance compared with humans or experts.

## **1.13 Turing Test**

=> **Turing Test** was proposed by Alan Turing in 1950 to test machine intelligence.

=> In this test, a human interrogator communicates with a human and a machine through text.

=> If the interrogator cannot reliably identify which one is the machine, then the machine is considered intelligent.

### Turing Test diagram

```text
------------------+
| Human Judge     |
+--------+---------+
         |
  Text conversation
         |
 +-------+--------+
 |                |
 v                v
Human          Machine
```

### Capabilities required to pass the Turing Test

1. **Natural language processing**

=> To communicate in human language.

2. **Knowledge representation**

=> To store facts and information.

3. **Automated reasoning**

=> To answer questions and draw conclusions.

4. **Machine learning**

=> To adapt and improve from experience.

### Total Turing Test

=> The **Total Turing Test** also includes physical interaction and perception.

=> It requires computer vision and robotics in addition to language and reasoning.

### Limitations

1. It tests behavior, not actual understanding.
2. A system may imitate human conversation without real intelligence.
3. It does not test creativity, emotion or consciousness directly.

## **1.14 Human Intelligence vs Machine Intelligence**

| Human Intelligence | Machine Intelligence |
|---|---|
| Biological and emotional | Artificial and programmed |
| Learns from broad life experience | Learns from data, rules or training |
| Has common sense and consciousness | Limited common sense and no proven consciousness |
| Slower in calculation | Very fast in computation |
| Can be tired or biased | Can work continuously but may inherit data bias |
| Creative and flexible | Strong in narrow tasks |

=> Machines can perform some tasks better than humans, such as fast calculation, large data analysis, repetitive work and pattern detection in huge datasets.

=> Humans are generally better at common sense reasoning, emotional understanding, creativity and adapting to completely new situations.

## **1.15 Important AI Systems and References**

### Important historical systems

| System | Area | Importance |
|---|---|---|
| **DENDRAL** | Chemistry | Identified molecular structure |
| **MYCIN** | Medicine | Diagnosed bacterial infections |
| **PROSPECTOR** | Geology | Helped mineral exploration |
| **XCON / R1** | Computer configuration | Configured computer systems |
| **Deep Blue** | Game playing | Defeated world chess champion |
| **DART** | Logistics | Supported military logistics planning |

### Historical references

1. McCulloch and Pitts introduced an early artificial neuron model in 1943.
2. Alan Turing proposed the Turing Test in 1950.
3. John McCarthy organized the Dartmouth workshop in 1956, where AI became a formal field.
4. Expert systems became popular in the 1970s and 1980s.
5. Modern AI uses machine learning, probability, optimization and large-scale data.

## **1.16 Intelligent Agent Basics**

=> **Agent**: `An agent is anything that perceives its environment through sensors and acts upon that environment through actuators.`

=> Example: A human agent uses eyes and ears as sensors and hands and legs as actuators.

=> A robotic agent may use cameras and sensors as input devices and motors as actuators.

### Agent formula

```text
Agent = Architecture + Program
```

### Important terms

| Term | Meaning |
|---|---|
| **Percept** | Input received by an agent at a particular instant |
| **Percept sequence** | Complete history of percepts received by the agent |
| **Agent function** | Mapping from percept sequence to action |
| **Agent program** | Actual program that implements the agent function |
| **Architecture** | Hardware/platform on which the agent program runs |

### Agent action cycle

```text
Environment -> Sensors -> Agent Program -> Actuators -> Environment
```

## **1.17 Task Environment**

=> A **task environment** is the problem environment in which an agent operates.

=> It is usually described using **PEAS**.

### PEAS

| Letter | Meaning | Example for automated taxi |
|---|---|---|
| **P** | Performance measure | Safe, fast, legal, comfortable driving |
| **E** | Environment | Roads, traffic, pedestrians |
| **A** | Actuators | Steering, brake, accelerator |
| **S** | Sensors | Camera, GPS, speedometer |

### Types of task environments

| Type | Meaning | Example |
|---|---|---|
| **Fully observable** | Complete state is visible | Chess |
| **Partially observable** | Some information is hidden | Poker |
| **Deterministic** | Next state is fixed by current action | 8-puzzle |
| **Stochastic** | Result involves uncertainty | Taxi driving |
| **Episodic** | Each decision is independent | Image classification |
| **Sequential** | Current action affects future decisions | Chess |
| **Static** | Environment does not change while deciding | Crossword puzzle |
| **Dynamic** | Environment changes during decision | Driving |
| **Discrete** | Finite states/actions | Board game |
| **Continuous** | Infinite or continuous values | Robot control |
| **Single-agent** | One agent operates | Crossword solver |
| **Multi-agent** | Multiple agents interact | Chess, traffic |

## **1.18 Types of Agents**

### 1. Simple reflex agent

=> It selects action only from the current percept.

=> It uses condition-action rules.

```text
if condition then action
```

=> Example: If the room is dirty, then clean it.

### 2. Model-based reflex agent

=> It maintains an internal model of the world.

=> It can work in partially observable environments.

=> Example: A robot remembers areas already cleaned.

### 3. Goal-based agent

=> It selects actions based on a goal.

=> It uses search and planning to reach the goal.

=> Example: A route planner finds a path to a destination.

### 4. Utility-based agent

=> It selects actions based on a utility value.

=> It is useful when there are many possible goals or trade-offs.

=> Example: A taxi agent chooses a route considering time, safety and cost.

### 5. Learning agent

=> It improves its performance from experience.

### Components of learning agent

1. **Performance element**: Selects external actions.
2. **Learning element**: Improves behavior using feedback.
3. **Critic**: Evaluates performance.
4. **Problem generator**: Suggests exploratory actions.

## **1.19 One Final Word**

=> AI is important because it provides techniques to solve problems that are difficult to solve using traditional programming.

=> AI systems are especially useful where knowledge is large, data is uncertain, and decisions must be made intelligently.

=> AI is not a single algorithm. It is a collection of search, reasoning, learning, knowledge representation and decision-making techniques.

## **1.20 Exam Short Questions**

### 1. Define Artificial Intelligence.

=> Artificial Intelligence is a branch of computer science that creates machines or software systems capable of performing tasks that normally require human intelligence.

### 2. List the four approaches of AI.

=> The four approaches are acting humanly, thinking humanly, thinking rationally and acting rationally.

### 3. What is the Turing Test?

=> Turing Test checks whether a machine can behave intelligently enough that a human judge cannot distinguish it from a human through text conversation.

### 4. What is the Total Turing Test?

=> Total Turing Test extends the normal Turing Test by also requiring perception and physical action through computer vision and robotics.

### 5. List the task domains of AI.

=> The task domains are mundane tasks, formal tasks and expert tasks.

### 6. Give two examples of mundane tasks.

=> Speech understanding and face recognition are examples of mundane tasks.

### 7. Give two examples of formal tasks.

=> Chess playing and theorem proving are examples of formal tasks.

### 8. Give two examples of expert tasks.

=> Medical diagnosis and machine fault diagnosis are examples of expert tasks.

### 9. What is an AI problem?

=> An AI problem is a problem requiring intelligent behavior such as reasoning, learning, planning, perception or decision making.

### 10. List any four AI problem characteristics.

=> Decomposable, predictable, recoverable and knowledge-intensive are four AI problem characteristics.

### 11. What is the Physical Symbol System Hypothesis?

=> It states that a physical symbol system has the necessary and sufficient means for general intelligent action.

### 12. Define AI technique.

=> An AI technique is a method for representing and using knowledge efficiently to solve AI problems.

### 13. List any three AI techniques.

=> Search, heuristics and knowledge representation are three AI techniques.

### 14. What is an intelligent agent?

=> An intelligent agent perceives its environment through sensors and acts on it through actuators to achieve goals.

### 15. Write the formula for an agent.

```text
Agent = Architecture + Program
```

### 16. What is PEAS?

=> PEAS stands for Performance measure, Environment, Actuators and Sensors.

### 17. List the types of task environments.

=> Fully/partially observable, deterministic/stochastic, episodic/sequential, static/dynamic, discrete/continuous and single-agent/multi-agent.

### 18. List the types of agents.

=> Simple reflex, model-based reflex, goal-based, utility-based and learning agents.

### 19. Differentiate between strong AI and weak AI.

=> Strong AI means real human-like intelligence and consciousness, while weak AI only simulates intelligent behavior for specific tasks.

### 20. Mention any four applications of AI.

=> Game playing, medical diagnosis, natural language processing and robotics are applications of AI.
