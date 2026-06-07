# **3 Managing Software Project**

=> This chapter covers software metrics, project estimation, project planning, scheduling, tracking, COCOMO, Gantt chart, earned value analysis, and risk management.

=> In exams, repeated questions are asked on **process/product/project metrics**, **function point**, **COCOMO**, **Gantt chart**, **project scheduling**, **risk management**, **RMMM**, **reactive vs proactive risks**, and **risk components/drivers**.

## **3.1 Software Project Management**

=> **Software Project Management** is the activity of planning, organizing, monitoring, and controlling software project resources to complete the project within time, cost, scope, and quality constraints.

### Need

1. Software projects are complex.
2. Requirements may change.
3. Cost and schedule must be controlled.
4. Team members must coordinate properly.
5. Risks must be handled early.
6. Quality must be maintained.

### Main activities

1. Project planning.
2. Estimation.
3. Scheduling.
4. Risk management.
5. Tracking and control.
6. Quality management.
7. Communication management.

## **3.2 Software Metrics**

=> **Software metrics** are quantitative measures used to evaluate software process, product, and project.

=> Metrics help managers make decisions based on data instead of guesswork.

### Benefits

1. Improve project planning.
2. Measure quality.
3. Control cost and schedule.
4. Improve productivity.
5. Identify process weaknesses.
6. Support future estimation.

## **3.3 Process, Product and Project Metrics**

| Metric type | Meaning | Examples |
|---|---|---|
| Process metrics | Measure effectiveness of development process. | Defect removal efficiency, review effectiveness, rework percentage. |
| Product metrics | Measure characteristics of software product. | LOC, function points, complexity, reliability, maintainability. |
| Project metrics | Measure project execution and control. | Effort, cost, schedule variance, productivity, staffing. |

### Process Metrics

=> Process metrics are collected across projects to improve the software development process.

### Examples

1. Number of defects found during review.
2. Average defect correction time.
3. Defect removal efficiency.
4. Rework effort.
5. Review effectiveness.

### Product Metrics

=> Product metrics measure software size, complexity, quality, and performance.

### Examples

1. Lines of Code (LOC).
2. Function Point (FP).
3. Cyclomatic complexity.
4. Defect density.
5. Reliability.

### Project Metrics

=> Project metrics help project manager track and control a specific project.

### Examples

1. Actual effort vs planned effort.
2. Actual cost vs planned cost.
3. Schedule variance.
4. Number of people assigned.
5. Milestone completion.

## **3.4 Function-Oriented Metrics**

=> **Function-oriented metrics** measure software size based on functionality delivered to the user.

=> The most common function-oriented metric is **Function Point (FP)**.

### Function Point components

| Component | Meaning |
|---|---|
| External Inputs (EI) | Data entering the system. |
| External Outputs (EO) | Reports or output screens. |
| External Inquiries (EQ) | Query with input and output. |
| Internal Logical Files (ILF) | Logical data maintained by system. |
| External Interface Files (EIF) | External data used by system. |

### Average weights

| Component | Simple | Average | Complex |
|---|---:|---:|---:|
| External Inputs | 3 | 4 | 6 |
| External Outputs | 4 | 5 | 7 |
| External Inquiries | 3 | 4 | 6 |
| Internal Logical Files | 7 | 10 | 15 |
| External Interface Files | 5 | 7 | 10 |

### Formula

```text
FP = UFP * VAF
VAF = 0.65 + (0.01 * sum Fi)
```

=> `UFP` means Unadjusted Function Point.

=> `VAF` means Value Adjustment Factor.

### Steps

1. Count EI, EO, EQ, ILF, and EIF.
2. Decide complexity: simple, average, or complex.
3. Multiply each count by its weight.
4. Add all values to get UFP.
5. Calculate VAF.
6. Calculate FP.

### Example

=> Inputs = 8, Outputs = 12, Inquiries = 4, Logical files = 41, Interfaces = 1, sum Fi = 41, all average.

| Component | Count | Average weight | Value |
|---|---:|---:|---:|
| EI | 8 | 4 | 32 |
| EO | 12 | 5 | 60 |
| EQ | 4 | 4 | 16 |
| ILF | 41 | 10 | 410 |
| EIF | 1 | 7 | 7 |

```text
UFP = 32 + 60 + 16 + 410 + 7 = 525
VAF = 0.65 + (0.01 * 41) = 1.06
FP = 525 * 1.06 = 556.5
```

=> Function Point = **556.5**, approximately **557 FP**.

## **3.5 Software Project Estimation**

=> **Software Project Estimation** is the process of estimating effort, cost, time, resources, and people required for a software project.

### Need

1. Prepare project budget.
2. Decide project schedule.
3. Allocate resources.
4. Decide feasibility.
5. Track actual progress.

### Estimation factors

1. Software size.
2. Project complexity.
3. Team experience.
4. Technology used.
5. Required reliability.
6. Reuse of components.
7. Development environment.

## **3.6 COCOMO Model**

=> **COCOMO** stands for **Constructive Cost Model**.

=> It is an algorithmic cost estimation model developed by Barry Boehm.

=> It estimates effort, development time, cost, and staffing based mainly on software size in KLOC.

### Project modes

1. **Organic mode**

=> Small and simple projects developed by experienced team in familiar environment.

=> Example: Simple business application.

2. **Semi-detached mode**

=> Medium complexity projects with mixed team experience.

=> Example: Compiler or database system.

3. **Embedded mode**

=> Complex projects with strict hardware, software, or real-time constraints.

=> Example: Real-time control system.

### Basic COCOMO formulas

```text
Effort (PM) = a * (KLOC)^b
Development Time = c * (Effort)^d
```

### Constants

| Mode | a | b | c | d |
|---|---:|---:|---:|---:|
| Organic | 2.4 | 1.05 | 2.5 | 0.38 |
| Semi-detached | 3.0 | 1.12 | 2.5 | 0.35 |
| Embedded | 3.6 | 1.20 | 2.5 | 0.32 |

### Types of COCOMO

1. **Basic COCOMO**

=> Uses only software size and project mode.

2. **Intermediate COCOMO**

=> Uses cost drivers such as reliability, product complexity, team capability, and tools.

3. **Detailed COCOMO**

=> Applies estimation to different phases of software development.

### Advantages

1. Simple and systematic.
2. Useful for early project planning.
3. Helps estimate effort and schedule.
4. Supports comparison between projects.

### Limitations

1. Depends on accurate KLOC estimation.
2. Constants may not fit every organization.
3. Less suitable for modern agile/reuse projects without adjustment.

## **3.7 Software Project Planning**

=> **Project planning** defines project scope, objectives, tasks, resources, schedule, risks, and deliverables.

### Contents of project plan

1. Project scope.
2. Project objectives.
3. Task list.
4. Effort and cost estimation.
5. Schedule and milestones.
6. Resource allocation.
7. Risk management plan.
8. Quality plan.
9. Communication plan.
10. Tracking and control mechanism.

## **3.8 W5HH Principle**

=> W5HH is a project planning principle suggested by Barry Boehm.

=> It helps prepare a practical project plan by asking seven questions.

| Question | Meaning |
|---|---|
| Why is the system being developed? | Business reason and value. |
| What will be done? | Scope and deliverables. |
| When will it be done? | Schedule and milestones. |
| Who is responsible? | Roles and responsibilities. |
| Where are they organizationally located? | Team structure and communication. |
| How will the job be done? | Technical and management approach. |
| How much resource is needed? | Budget, effort, people, and tools. |

### Importance

1. Gives planning clarity.
2. Reduces confusion.
3. Defines responsibility.
4. Helps estimate resources.
5. Improves communication.

## **3.9 Project Scheduling**

=> **Project scheduling** is the process of dividing project work into tasks, estimating duration, assigning resources, and arranging tasks on a timeline.

### Scheduling process

```text
Identify tasks
      |
      v
Estimate duration
      |
      v
Identify dependencies
      |
      v
Assign resources
      |
      v
Prepare schedule
      |
      v
Track and update progress
```

### Steps

1. Break project into tasks using Work Breakdown Structure.
2. Estimate time required for each task.
3. Identify task dependencies.
4. Assign developers and resources.
5. Define milestones.
6. Prepare Gantt chart or network diagram.
7. Track actual progress.
8. Revise schedule when needed.

## **3.10 Gantt Chart**

=> **Gantt Chart** is a horizontal bar chart used to show project activities against time.

=> It helps in project planning, scheduling, tracking, and reporting.

### Example

```text
Task                  Week1 Week2 Week3 Week4 Week5 Week6
Requirement Analysis  =====
Design                      =====
Coding                            ===========
Testing                                      =====
Deployment                                         ===
```

### Features

1. Tasks are shown vertically.
2. Time is shown horizontally.
3. Bars show start and finish time.
4. Overlapping bars show parallel tasks.
5. Milestones can be shown.
6. Progress can be compared with planned schedule.

### Advantages

1. Easy to understand.
2. Shows project timeline clearly.
3. Helps track progress.
4. Shows task duration and overlap.
5. Useful for communication with stakeholders.

### Limitations

1. Complex for very large projects.
2. Dependency handling is limited compared to PERT/CPM.
3. Frequent changes require chart updates.

## **3.11 Earned Value Analysis**

=> **Earned Value Analysis (EVA)** is a project tracking technique that compares planned work, completed work, and actual cost.

### Important terms

1. **Planned Value (PV)**

=> Budgeted cost of work scheduled.

2. **Earned Value (EV)**

=> Budgeted cost of work actually completed.

3. **Actual Cost (AC)**

=> Actual cost spent for completed work.

4. **Schedule Variance (SV)**

```text
SV = EV - PV
```

5. **Cost Variance (CV)**

```text
CV = EV - AC
```

6. **Schedule Performance Index (SPI)**

```text
SPI = EV / PV
```

7. **Cost Performance Index (CPI)**

```text
CPI = EV / AC
```

### Interpretation

| Condition | Meaning |
|---|---|
| SV > 0 | Ahead of schedule. |
| SV < 0 | Behind schedule. |
| CV > 0 | Under budget. |
| CV < 0 | Over budget. |
| SPI > 1 | Schedule performance is good. |
| CPI > 1 | Cost performance is good. |

## **3.12 Risk**

=> **Risk** is a possible future event that may negatively affect software project cost, schedule, quality, performance, or customer satisfaction.

### Examples

1. Requirement changes.
2. Staff leaving the project.
3. New technology failure.
4. Schedule delay.
5. Budget overrun.
6. Poor performance.

## **3.13 Reactive and Proactive Risk Approach**

| Reactive Risk Approach | Proactive Risk Approach |
|---|---|
| Action is taken after risk becomes a problem. | Risks are identified and planned before they occur. |
| Crisis handling approach. | Prevention and control approach. |
| Usually increases cost and delay. | Reduces risk probability and impact. |
| No strong early planning. | Includes risk identification, analysis, mitigation, and monitoring. |
| Example: Hire replacement after developer leaves. | Example: Train backup developer early. |

=> Proactive risk management is better because it reduces uncertainty before it damages the project.

## **3.14 Types of Software Risks**

1. **Project risks**

=> Affect project plan, cost, schedule, staffing, and resources.

=> Example: Schedule delay.

2. **Technical risks**

=> Affect design, implementation, integration, performance, or technology.

=> Example: New framework does not work as expected.

3. **Business risks**

=> Affect product success, market value, funding, or business goal.

=> Example: Customer cancels project funding.

4. **Requirement risks**

=> Affect clarity, completeness, stability, or correctness of requirements.

=> Example: Frequent requirement changes.

## **3.15 Risk Management**

=> **Risk Management** is the process of identifying, analyzing, planning, and controlling risks in a software project.

### Activities

```text
Risk Identification
        |
        v
Risk Projection
        |
        v
Risk Refinement
        |
        v
Risk Mitigation, Monitoring and Management
```

### 1. Risk Identification

=> Identify possible risks using checklists, past project data, team discussion, and expert opinion.

### 2. Risk Projection

=> Estimate probability and impact of each risk.

### 3. Risk Refinement

=> Break major risks into smaller causes and consequences.

### 4. Risk Mitigation, Monitoring and Management

=> Prepare preventive actions, track risk indicators, and apply contingency plans.

## **3.16 RMMM Plan**

=> **RMMM** stands for **Risk Mitigation, Monitoring, and Management**.

=> It is a plan that describes how risks will be handled during software development.

### 1. Risk Mitigation

=> Mitigation means taking preventive actions to reduce probability or impact of risk.

### Examples

| Risk | Mitigation action |
|---|---|
| Requirement changes | Use change control and frequent customer review. |
| Staff leaving | Keep documentation and backup team member. |
| New technology failure | Build prototype or spike solution. |
| Schedule delay | Add buffer and track milestones. |

### 2. Risk Monitoring

=> Monitoring means observing risk indicators during the project.

### Examples

1. Track schedule slippage.
2. Check defect rate.
3. Monitor staff workload.
4. Review change requests.

### 3. Risk Management

=> Management means applying contingency plan when risk becomes a real problem.

=> Example: If key developer leaves, assign trained backup and revise schedule.

### Contents of RMMM plan

1. Risk description.
2. Risk category.
3. Probability.
4. Impact.
5. Mitigation steps.
6. Monitoring indicators.
7. Contingency plan.
8. Responsible person.

## **3.17 Risk Components and Risk Drivers**

=> **Risk components** are project areas affected by risk.

=> **Risk drivers** are factors that cause or increase risk.

### Risk components

1. **Performance risk**

=> Software may not meet functional or performance requirements.

2. **Cost risk**

=> Project cost may exceed budget.

3. **Support risk**

=> Software may be difficult to maintain or support.

4. **Schedule risk**

=> Project may not finish on time.

### Risk drivers

1. Product size.
2. Business impact.
3. Customer characteristics.
4. Process definition.
5. Development environment.
6. Technology to be built.
7. Staff size and experience.

### Difference

| Risk Components | Risk Drivers |
|---|---|
| Areas affected by risk. | Causes or factors creating risk. |
| Show what may be damaged. | Show why risk may occur. |
| Example: cost, schedule, performance, support. | Example: new technology, unclear requirements, inexperienced staff. |

## **3.18 MS Project Tool**

=> MS Project is a project management tool used for planning, scheduling, assigning resources, and tracking project progress.

### Uses

1. Create task list.
2. Prepare Gantt chart.
3. Assign resources.
4. Track progress.
5. Manage dependencies.
6. Prepare reports.

## **3.19 Exam Short Questions**

### 1. Define software metric.

=> Software metric is a quantitative measure used to evaluate software process, product, or project.

### 2. Define process metric.

=> Process metric measures effectiveness of software development process.

### 3. Define product metric.

=> Product metric measures characteristics of software product such as size, complexity, or reliability.

### 4. Define project metric.

=> Project metric measures project execution factors such as effort, cost, schedule, and productivity.

### 5. What is COCOMO?

=> COCOMO is an algorithmic cost estimation model used to estimate effort and development time.

### 6. What is Gantt chart?

=> Gantt chart is a horizontal bar chart used to show project tasks against time.

### 7. What is risk?

=> Risk is a possible future event that may negatively affect project success.

### 8. What is RMMM?

=> RMMM means Risk Mitigation, Monitoring, and Management.

### 9. Give two examples of project risks.

=> Schedule delay and budget overrun.

### 10. What is earned value analysis?

=> Earned value analysis compares planned value, earned value, and actual cost to track project performance.
