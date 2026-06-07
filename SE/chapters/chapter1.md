# **1 Introduction to Software and Software Engineering**

=> This chapter covers software basics, software engineering, layered technology, software myths, software crisis, process framework activities, umbrella activities, and important software process models.

=> In exams, this unit is important because questions are repeatedly asked on **software characteristics**, **software engineering as layered technology**, **spiral model**, **prototype model**, **incremental model**, **waterfall model**, **RAD model**, and **component-based development**.

## **1.1 Software**

=> **Software** is a collection of computer programs, procedures, data, configuration files, and related documentation used to perform specific tasks on a computer system.

=> Software is not only source code. It also includes:

1. Programs.
2. Data structures.
3. Configuration files.
4. User manuals.
5. Design documents.
6. Test cases.
7. Operating procedures.

### Definition

=> `Software is a set of instructions, data, and documents that enable a computer system to solve a problem or perform a useful task.`

### Examples

1. Operating system.
2. Banking application.
3. College management system.
4. Mobile application.
5. Web browser.
6. Compiler.

## **1.2 Characteristics of Software**

1. **Software is developed, not manufactured**

=> Software is engineered by requirement analysis, design, coding, and testing.

=> It is not manufactured like hardware in a factory.

2. **Software does not wear out**

=> Hardware can fail due to dust, heat, or physical damage.

=> Software does not physically wear out, but it may fail due to defects, poor design, or changing environment.

3. **Software is mostly custom-built**

=> Many software systems are developed according to specific user or organization requirements.

4. **Software is intangible**

=> Software cannot be touched physically.

=> Its quality is judged by behavior, performance, reliability, usability, and maintainability.

5. **Software is complex**

=> Software contains many modules, data structures, interfaces, conditions, and execution paths.

6. **Software is easy to change but difficult to maintain correctly**

=> A small change in one module can affect other modules if design is poor.

7. **Software requires continuous maintenance**

=> Software must be updated for defect correction, new requirements, new platforms, and security.

## **1.3 Software is Engineered, Not Manufactured**

=> Software is called engineered because it is created using engineering principles, methods, tools, and disciplined processes.

### Justification

| Software Engineering | Manufacturing |
|---|---|
| Main work is analysis, design, coding, and testing. | Main work is physical production. |
| Copying software has very low cost. | Each manufactured item has material cost. |
| Quality depends on logic and design. | Quality depends on material and production process. |
| Software does not physically wear out. | Manufactured products may wear out physically. |
| Maintenance is due to defects and changes. | Maintenance is due to physical damage or wear. |

=> Therefore, software is engineered through intellectual and systematic activities, not manufactured physically.

## **1.4 Evolving Role of Software**

=> Earlier, software was mainly used for scientific calculations and simple data processing.

=> Today, software controls business, communication, education, banking, healthcare, transportation, entertainment, and embedded devices.

### Role of software

1. **Business automation**

=> Payroll, accounting, inventory, banking, and e-commerce systems.

2. **Decision support**

=> Software helps managers analyze data and make decisions.

3. **Communication**

=> Email, messaging, video calls, and social media.

4. **Embedded systems**

=> Software controls machines, vehicles, medical devices, and smart appliances.

5. **Web and mobile applications**

=> Software provides online services to users anywhere.

6. **Artificial intelligence and data analysis**

=> Software helps in prediction, automation, and intelligent systems.

## **1.5 Software Crisis**

=> **Software crisis** refers to difficulties faced in developing large and complex software systems within time, budget, and quality limits.

### Causes

1. Increasing software complexity.
2. Unclear and changing requirements.
3. Poor project planning.
4. Lack of disciplined development process.
5. Inadequate testing.
6. Poor communication with users.
7. Shortage of skilled developers.

### Symptoms

1. Projects delivered late.
2. Cost exceeds budget.
3. Software does not satisfy user needs.
4. Software contains many defects.
5. Maintenance becomes difficult.
6. Documentation is incomplete.

### Solution

=> Software Engineering was introduced to solve software crisis using systematic process, methods, tools, quality assurance, and project management.

## **1.6 Software Myths**

=> **Software myths** are false beliefs about software development.

=> They create unrealistic expectations and project problems.

### Management myths

1. **Myth: Existing standards and procedures are enough**

=> Reality: Standards must be practical, followed properly, and improved continuously.

2. **Myth: If project is late, add more programmers**

=> Reality: Adding people late may increase delay because new members need training and coordination.

3. **Myth: Outsourcing removes software project risk**

=> Reality: Outsourcing still needs requirement clarity, monitoring, quality control, and communication.

### Customer myths

1. **Myth: General objective is enough to start coding**

=> Reality: Clear and complete requirements are necessary.

2. **Myth: Requirements can be changed easily anytime**

=> Reality: Late changes increase cost, delay, and risk.

### Practitioner myths

1. **Myth: Once program works, job is complete**

=> Reality: Testing, documentation, deployment, and maintenance are also required.

2. **Myth: Quality can be checked only after coding**

=> Reality: Quality must be built into requirements, design, coding, reviews, and testing.

3. **Myth: Software engineering creates unnecessary documentation**

=> Reality: Proper documentation improves maintenance and communication.

## **1.7 Software Engineering**

=> **Software Engineering** is the application of engineering principles, methods, tools, and processes for developing high-quality software within time and budget.

### Definition

=> `Software Engineering is a systematic, disciplined, and measurable approach to the development, operation, and maintenance of software.`

### Objectives

1. Develop reliable software.
2. Complete project within time and budget.
3. Improve maintainability.
4. Reduce defects.
5. Manage complexity.
6. Satisfy user requirements.
7. Improve productivity.

### Need of software engineering

1. Software systems are large and complex.
2. Manual development causes errors.
3. Requirements change frequently.
4. Cost and schedule must be controlled.
5. Quality and reliability are important.
6. Maintenance cost is high.

## **1.8 Software Engineering as a Layered Technology**

=> Software Engineering is called **layered technology** because it is built on different layers that support systematic software development.

### Diagram

```text
+------------------+
|      Tools       |
+------------------+
|     Methods      |
+------------------+
|     Process      |
+------------------+
|  Quality Focus   |
+------------------+
```

### 1. Quality Focus

=> Quality focus is the foundation of software engineering.

=> Every activity should aim to produce reliable, usable, maintainable, and secure software.

### 2. Process

=> Process defines the framework for software development.

=> It tells what activities should be performed and in what order.

=> Examples: communication, planning, modeling, construction, deployment.

### 3. Methods

=> Methods provide technical ways to perform software engineering activities.

=> Examples: requirement analysis methods, design methods, testing techniques, estimation methods.

### 4. Tools

=> Tools provide automated or semi-automated support for process and methods.

=> Examples: Git, MS Project, testing tools, CASE tools, IDEs.

### Importance

1. Provides disciplined development.
2. Improves quality.
3. Supports project control.
4. Reduces defects.
5. Improves productivity.

## **1.9 Software Process**

=> A **software process** is a set of activities, actions, and tasks used to develop and maintain software.

### Difference between activity, action and task

| Term | Meaning |
|---|---|
| Activity | Major work area such as planning or testing. |
| Action | Set of related tasks inside an activity. |
| Task | Small unit of work with clear output. |

## **1.10 Process Framework Activities**

=> A generic software process framework contains five major activities.

### Diagram

```text
Communication -> Planning -> Modeling -> Construction -> Deployment
```

### 1. Communication

=> Communicate with customer and stakeholders to understand requirements.

=> Output: problem statement, initial requirements, project scope.

### 2. Planning

=> Estimate cost, schedule, resources, risks, and prepare project plan.

=> Output: project plan, schedule, resource plan.

### 3. Modeling

=> Create requirement models and design models.

=> It includes data model, architecture, interface design, and component design.

### 4. Construction

=> Convert design into code and perform testing.

=> It includes coding, unit testing, integration testing, and debugging.

### 5. Deployment

=> Deliver software to users and collect feedback.

=> It includes installation, training, support, and maintenance.

## **1.11 Umbrella Activities**

=> **Umbrella activities** are supporting activities performed throughout the software process.

### Important umbrella activities

1. **Software project tracking and control**

=> Monitor project progress and take corrective action.

2. **Risk management**

=> Identify, analyze, reduce, and monitor project risks.

3. **Software Quality Assurance**

=> Ensure that software process and product meet quality standards.

4. **Formal Technical Reviews**

=> Review requirements, design, code, and test cases to find defects early.

5. **Software Configuration Management**

=> Manage versions and changes in software work products.

6. **Measurement**

=> Collect metrics for effort, cost, schedule, defects, and quality.

7. **Documentation**

=> Prepare and maintain technical and project documents.

8. **Reuse management**

=> Identify and manage reusable components.

## **1.12 Product, Process and Project**

| Term | Meaning | Example |
|---|---|---|
| Product | Final software delivered to user. | Library management system. |
| Process | Steps followed to build software. | Waterfall or agile process. |
| Project | Temporary effort to build product. | Developing library system in 4 months. |

### Process metrics, product metrics and project metrics

| Metric type | Measures | Examples |
|---|---|---|
| Process metrics | Effectiveness of development process. | Defect removal efficiency, review defects. |
| Product metrics | Quality and size of software product. | LOC, function points, complexity, reliability. |
| Project metrics | Project execution and control. | Effort, cost, schedule variance, productivity. |

## **1.13 Software Process Model**

=> A **software process model** is a structured representation of software development activities.

=> It gives a roadmap for developing software.

### Need

1. Provides discipline.
2. Helps planning and estimation.
3. Improves communication.
4. Reduces risk.
5. Helps manage large projects.

## **1.14 Linear Sequential Model / Waterfall Model**

=> **Waterfall Model** is a linear sequential process model where each phase is completed before the next phase starts.

### Diagram

```text
Requirement Analysis
        |
        v
System Design
        |
        v
Implementation
        |
        v
Testing
        |
        v
Deployment
        |
        v
Maintenance
```

### Phases

1. **Requirement analysis**

=> Collect and document user requirements.

2. **Design**

=> Prepare architecture, database design, interface design, and module design.

3. **Implementation**

=> Convert design into code.

4. **Testing**

=> Test software to find defects and verify requirements.

5. **Deployment**

=> Deliver software to users.

6. **Maintenance**

=> Correct defects and update software after delivery.

### Advantages

1. Simple and easy to understand.
2. Clear phases and documentation.
3. Easy to manage for small projects.
4. Suitable when requirements are stable.

### Disadvantages

1. Difficult to handle requirement changes.
2. Working software is delivered late.
3. Risk is discovered late.
4. Not suitable for complex and uncertain projects.

## **1.15 Prototyping Model**

=> **Prototyping Model** builds a working sample of the system to understand and refine requirements.

=> It is useful when requirements are unclear.

### Diagram

```text
Requirement Gathering
        |
        v
Quick Design
        |
        v
Build Prototype
        |
        v
Customer Evaluation
        |
        v
Refine Requirements
        |
        v
Final Product Development
```

### Working

1. Basic requirements are collected.
2. Quick design is prepared.
3. Prototype is developed.
4. Customer evaluates prototype.
5. Feedback is collected.
6. Requirements are refined.
7. Final system is developed.

### Types

1. **Throwaway prototype**

=> Used only for learning requirements and discarded later.

2. **Evolutionary prototype**

=> Improved gradually until it becomes final product.

### Advantages

1. Clarifies unclear requirements.
2. Improves customer involvement.
3. Useful for UI-heavy systems.
4. Reduces requirement misunderstanding.
5. Early feedback is available.

### Disadvantages

1. Customer may think prototype is final product.
2. Poor design may enter final system.
3. Documentation may be ignored.
4. Too many changes may increase cost.

## **1.16 RAD Model**

=> **RAD** stands for **Rapid Application Development**.

=> RAD is an incremental process model that focuses on fast development using reusable components, tools, and parallel teams.

### RAD phases

```text
Business Modeling -> Data Modeling -> Process Modeling
     -> Application Generation -> Testing and Turnover
```

### 1. Business Modeling

=> Understand business functions and information flow.

### 2. Data Modeling

=> Identify data objects and relationships.

### 3. Process Modeling

=> Define processes that transform data.

### 4. Application Generation

=> Generate application using tools, reusable components, and code generators.

### 5. Testing and Turnover

=> Test components and deliver system.

### Advantages

1. Fast development.
2. Encourages reuse.
3. User feedback is frequent.
4. Suitable for modular applications.

### Disadvantages

1. Requires skilled developers.
2. Requires strong user involvement.
3. Not suitable for very complex or high-risk systems.
4. Needs modular design.

### Prototype model vs RAD model

| Prototype Model | RAD Model |
|---|---|
| Used when requirements are unclear. | Used when quick delivery is required. |
| Builds sample system for requirement clarity. | Builds complete system rapidly. |
| Focuses on learning requirements. | Focuses on speed and reuse. |
| Prototype may be thrown away. | RAD increments become part of final product. |

## **1.17 Incremental Process Model**

=> **Incremental Process Model** develops software in small parts called increments.

=> Each increment delivers a working version of the software.

### Diagram

```text
Requirements
     |
     v
+----------------+   +----------------+   +----------------+
| Increment 1     |-->| Increment 2     |-->| Increment 3     |
| Core features   |   | More features   |   | Final features  |
+----------------+   +----------------+   +----------------+
     |                    |                    |
     v                    v                    v
 Release 1            Release 2            Final Release
```

### Working

1. Overall requirements are divided into increments.
2. Core features are developed first.
3. First increment is delivered to user.
4. Feedback is collected.
5. Later increments add more features.
6. Final product is completed after all increments.

### Example

=> Online shopping system:

1. Increment 1: Login and product search.
2. Increment 2: Cart and order.
3. Increment 3: Payment and tracking.

### Advantages

1. Early working software.
2. Customer feedback is frequent.
3. Important features are delivered first.
4. Risk is reduced.
5. Testing is easier for smaller releases.

### Disadvantages

1. Requires good planning.
2. Integration may become difficult.
3. Architecture must be designed carefully.

### Incremental model vs Waterfall model

| Incremental Model | Waterfall Model |
|---|---|
| Delivers software in increments. | Delivers complete software at end. |
| Supports changing requirements. | Changes are difficult. |
| Customer feedback is frequent. | Feedback is late. |
| Testing is done in each increment. | Testing is done after implementation. |
| Suitable for modular projects. | Suitable for stable requirements. |

## **1.18 Spiral Process Model**

=> **Spiral Model** is a risk-driven process model that combines iterative development, prototyping, and waterfall-style planning.

=> It is suitable for large, complex, and high-risk projects.

### Diagram

```text
Planning
   |
   v
Risk Analysis
   |
   v
Engineering
   |
   v
Customer Evaluation
   |
   v
Next Spiral Cycle
```

### Phases

1. **Planning**

=> Define objectives, alternatives, constraints, resources, cost, and schedule.

2. **Risk Analysis**

=> Identify and reduce technical, cost, schedule, and requirement risks.

=> Prototypes may be built to reduce risk.

3. **Engineering**

=> Design, code, test, and develop the current version.

4. **Customer Evaluation**

=> Customer evaluates the version and gives feedback.

### Why Spiral Model is called Meta Model

=> Spiral model is called a **Meta Model** because it can combine other process models.

=> Each spiral cycle may use waterfall, prototyping, incremental, or other approaches depending on project risk.

### Why Spiral Model suits large-scale software

1. Large systems have high risk.
2. Requirements may change.
3. Cost and schedule must be controlled.
4. Customer feedback is needed.
5. System can be developed in cycles.

### Advantages

1. Strong risk management.
2. Suitable for large projects.
3. Supports changing requirements.
4. Allows prototyping.
5. Frequent customer feedback.

### Disadvantages

1. Costly for small projects.
2. Requires risk analysis expertise.
3. Complex to manage.
4. Time estimation may be difficult.

### Spiral model vs Waterfall model

| Spiral Model | Waterfall Model |
|---|---|
| Iterative and risk-driven. | Linear and sequential. |
| Risk analysis is central. | Risk analysis is limited. |
| Handles changing requirements. | Best for stable requirements. |
| Customer feedback in every cycle. | Customer feedback mostly at end. |
| Suitable for large projects. | Suitable for small/simple projects. |

## **1.19 Evolutionary Process Models**

=> **Evolutionary models** develop software through repeated versions.

=> Software evolves over time based on user feedback and changing requirements.

### Examples

1. Prototyping model.
2. Spiral model.
3. Incremental model.

### Features

1. Iterative development.
2. Customer feedback.
3. Gradual refinement.
4. Supports changing requirements.

## **1.20 Agile Process Model**

=> **Agile Process Model** develops software in short iterations with frequent customer feedback and quick response to change.

=> Detailed agile development is covered in Chapter 2.

### Features

1. Iterative and incremental.
2. Customer collaboration.
3. Working software delivered frequently.
4. Accepts changing requirements.
5. Team communication is important.

### Advantages

1. Fast delivery.
2. Flexible to changes.
3. Higher customer satisfaction.
4. Early defect detection.

### Disadvantages

1. Requires customer involvement.
2. Less formal documentation.
3. Scope may change frequently.

## **1.21 Component-Based Development**

=> **Component-Based Development (CBD)** builds software using reusable software components.

=> A component is an independent and replaceable software unit that provides specific functionality.

### Process

```text
Identify candidate components
        |
        v
Search reusable components
        |
        v
Adapt components if needed
        |
        v
Integrate components
        |
        v
Test complete system
```

### Advantages

1. Reduces development time.
2. Promotes reuse.
3. Reduces cost.
4. Improves productivity.
5. Tested components may improve reliability.

### Disadvantages

1. Suitable components may not be available.
2. Integration problems may occur.
3. Component may not exactly match requirements.
4. Vendor dependency may occur.
5. Security and compatibility issues may appear.

## **1.22 Choosing a Process Model**

| Situation | Suitable model |
|---|---|
| Requirements are stable and clear | Waterfall |
| Requirements are unclear | Prototype |
| Fast development is required | RAD |
| Early partial delivery is needed | Incremental |
| Large high-risk system | Spiral |
| Requirements change frequently | Agile |
| Reusable components are available | Component-based development |

## **1.23 Important Exam Comparisons**

### Waterfall vs Incremental

| Waterfall | Incremental |
|---|---|
| Linear development. | Development in increments. |
| Complete product delivered at end. | Partial working product delivered early. |
| Less flexible. | More flexible. |
| Risk discovered late. | Risk reduced through early releases. |

### Prototype vs RAD

| Prototype | RAD |
|---|---|
| Clarifies unclear requirements. | Develops system quickly. |
| Focuses on sample model. | Focuses on rapid complete application. |
| Prototype may be discarded. | RAD output becomes final software. |
| Useful for UI and requirement discovery. | Useful for modular business applications. |

### Spiral vs Waterfall

| Spiral | Waterfall |
|---|---|
| Iterative and risk-driven. | Sequential. |
| Suitable for large projects. | Suitable for small stable projects. |
| Allows customer feedback. | Feedback is late. |
| More costly. | Simpler and cheaper. |

## **1.24 Frequently Asked Long Answers**

### Spiral Model for 7 Marks

=> Write definition, diagram, four phases, why suitable for large projects, advantages, and disadvantages.

### Incremental Model for 7 Marks

=> Write definition, diagram, working steps, example, advantages, disadvantages, and comparison with waterfall if asked.

### Prototype Model for 7 Marks

=> Write definition, diagram, working, types, advantages, disadvantages, and when it is useful.

### Layered Technology for 3 or 4 Marks

=> Write diagram with Quality Focus, Process, Methods, Tools and explain each layer.

## **1.25 Exam Short Questions**

### 1. Define software.

=> Software is a collection of programs, data, procedures, and documentation used to perform specific tasks on a computer system.

### 2. Why software does not wear out?

=> Software has no physical parts, so it does not wear out physically. It fails due to defects, wrong changes, or environment changes.

### 3. What is software crisis?

=> Software crisis is the difficulty of developing software within time, budget, and quality limits.

### 4. Define software engineering.

=> Software engineering is a systematic, disciplined, and measurable approach to development, operation, and maintenance of software.

### 5. List layers of software engineering.

=> Quality focus, process, methods, and tools.

### 6. Define software process.

=> Software process is a set of activities, actions, and tasks used to develop and maintain software.

### 7. List process framework activities.

=> Communication, planning, modeling, construction, and deployment.

### 8. List umbrella activities.

=> Project tracking, risk management, SQA, FTR, SCM, measurement, documentation, and reuse management.

### 9. Which model is suitable for large-scale software?

=> Spiral model, because it is risk-driven and iterative.

### 10. Why is Spiral Model called Meta Model?

=> Because it can combine other process models such as waterfall, prototyping, and incremental models.

### 11. When is Prototype Model useful?

=> When requirements are unclear or users cannot describe exact needs.

### 12. What is RAD?

=> RAD means Rapid Application Development. It focuses on fast development using reusable components and tools.

### 13. What is component-based development?

=> It is a development approach where software is built by integrating reusable components.

### 14. What is the main disadvantage of Waterfall Model?

=> It does not handle changing requirements well and working software is delivered late.

### 15. What is the main advantage of Incremental Model?

=> It delivers working software early in increments.
