# **2 Agile Development**

=> This chapter covers agility, agile process model, agile principles, Extreme Programming (XP), Scrum, DSDM, Adaptive Software Development (ASD), other agile models, spike solution, and agile tools.

=> In exams, this unit is repeatedly asked through questions on **Agility**, **Agile principles**, **advantages and disadvantages of agile**, **XP**, **Scrum**, **DSDM**, **ASD**, and **spike solution in XP**.

## **2.1 Agility**

=> **Agility** is the ability of a software development team to respond quickly and effectively to changing requirements, technology, customer needs, and business conditions.

=> Agile development accepts that requirements may change and therefore delivers software in small iterations with regular feedback.

### Definition

=> `Agility is the ability to rapidly respond to change while delivering useful and high-quality software.`

### Need of agility

1. Requirements change frequently.
2. Customer expectations change with time.
3. Market competition requires faster delivery.
4. Technology changes rapidly.
5. Traditional models may deliver working software late.
6. Early feedback reduces project risk.

### Features of agility

1. Iterative development.
2. Incremental delivery.
3. Customer collaboration.
4. Fast response to change.
5. Team communication.
6. Working software as progress measure.
7. Continuous improvement.

## **2.2 Agile Process Model**

=> **Agile Process Model** is an iterative and incremental software development model that focuses on quick delivery of working software and customer collaboration.

### Diagram

```text
Planning -> Analysis -> Design -> Coding -> Testing -> Release
     ^                                                |
     |________________ Feedback and Change ___________|
```

### Working

1. Project is divided into small iterations.
2. Customer requirements are prioritized.
3. Team develops a small working part of software.
4. Software is tested and delivered.
5. Customer gives feedback.
6. Feedback is used in the next iteration.

### Agile vs traditional development

| Agile Development | Traditional Development |
|---|---|
| Iterative and flexible. | Mostly sequential and fixed. |
| Accepts requirement changes. | Changes are difficult. |
| Working software delivered frequently. | Working software delivered late. |
| Customer collaboration is continuous. | Customer involvement may be limited. |
| Less formal documentation. | More formal documentation. |
| Suitable for changing requirements. | Suitable for stable requirements. |

## **2.3 Agile Principles**

=> Agile principles guide the team to deliver quality software quickly and flexibly.

### Important agile principles

1. **Customer satisfaction through early and continuous delivery**

=> Deliver useful software early and regularly.

2. **Welcome changing requirements**

=> Requirement changes are accepted even late in development if they add business value.

3. **Deliver working software frequently**

=> Software is delivered in weeks rather than months.

4. **Customer and developers work together**

=> Regular collaboration reduces misunderstanding.

5. **Build projects around motivated people**

=> Give team members support, trust, and responsibility.

6. **Face-to-face communication**

=> Direct communication is effective for quick problem solving.

7. **Working software is the primary measure of progress**

=> Progress is measured by completed and usable functionality.

8. **Sustainable development**

=> Team should work at a steady pace without burnout.

9. **Technical excellence and good design**

=> Clean design and good coding improve agility.

10. **Simplicity**

=> Avoid unnecessary work and complexity.

11. **Self-organizing teams**

=> Teams decide how to complete work effectively.

12. **Continuous improvement**

=> Team regularly reviews and improves its process.

## **2.4 Advantages and Disadvantages of Agile Model**

### Advantages

1. **Handles changing requirements**

=> Agile easily adapts to new or modified requirements.

2. **Early working software**

=> Customer gets usable software early.

3. **Better customer satisfaction**

=> Continuous feedback helps build the right product.

4. **Early defect detection**

=> Frequent testing finds defects early.

5. **Improved communication**

=> Team and customer communicate regularly.

6. **Reduced risk**

=> Small iterations reduce the risk of complete project failure.

7. **Faster delivery**

=> Important features can be delivered quickly.

### Disadvantages

1. Requires active customer involvement.
2. Less formal documentation may create maintenance difficulty.
3. Scope may expand if not controlled.
4. Estimation is difficult when requirements change often.
5. Not ideal for very large teams without scaling.
6. Requires disciplined and skilled team.

## **2.5 Agile Process Models**

### Common agile models

1. Extreme Programming (XP).
2. Scrum.
3. Dynamic Systems Development Method (DSDM).
4. Adaptive Software Development (ASD).
5. Crystal.
6. Feature Driven Development (FDD).
7. Agile Unified Process (AUP).

## **2.6 Extreme Programming (XP)**

=> **Extreme Programming (XP)** is an agile software development method used for projects with changing requirements.

=> XP focuses on customer satisfaction, simple design, continuous testing, frequent releases, and strong team communication.

### XP process

```text
User Stories -> Release Planning -> Iteration Planning
     -> Design -> Coding -> Testing -> Small Release
     -> Customer Feedback
```

### XP values

1. **Communication**

=> Developers, customers, and testers communicate continuously.

2. **Simplicity**

=> Build only what is needed now.

3. **Feedback**

=> Feedback is collected from customers, tests, and team reviews.

4. **Courage**

=> Team accepts change, improves code, and removes poor design.

5. **Respect**

=> Team members respect each other's work and contribution.

## **2.7 XP Practices**

1. **User stories**

=> Requirements are written as short statements from the user's point of view.

=> Example: `As a student, I want to view my exam result online.`

2. **Planning game**

=> Customer and developers decide story priority, effort, and release plan.

3. **Small releases**

=> Working software is released frequently.

4. **Simple design**

=> Design is kept simple and focused on current requirements.

5. **Test-driven development**

=> Test cases are written before code.

=> Code is accepted when tests pass.

6. **Pair programming**

=> Two programmers work together on one computer.

=> One writes code and the other reviews logic.

7. **Refactoring**

=> Improve internal code structure without changing external behavior.

8. **Continuous integration**

=> Code is integrated and tested frequently.

9. **Collective code ownership**

=> Any developer can improve any part of code.

10. **On-site customer**

=> Customer is available to clarify requirements quickly.

11. **Coding standards**

=> Team follows common coding style.

12. **Sustainable pace**

=> Team works at a steady and manageable speed.

### Advantages of XP

1. Handles changing requirements.
2. Improves quality through continuous testing.
3. Reduces integration problems.
4. Improves communication.
5. Delivers working software frequently.

### Disadvantages of XP

1. Requires active customer availability.
2. Pair programming may increase initial cost.
3. Less formal documentation.
4. Difficult for large distributed teams.
5. Requires disciplined developers.

## **2.8 Spike Solution in XP**

=> In XP, a **spike solution** is a small experimental program created to explore a technical problem or unclear requirement.

=> It is used to reduce uncertainty before actual development.

### Purpose

1. Understand difficult requirement.
2. Check technical feasibility.
3. Compare possible solutions.
4. Reduce risk.
5. Improve estimation.

### Example

=> If a team is unsure whether payment gateway integration will work, it may create a small spike to test only payment API connection.

=> A spike is usually temporary and may be thrown away after learning is complete.

## **2.9 Scrum**

=> **Scrum** is an agile framework used to develop software in short iterations called **sprints**.

=> A sprint usually lasts 1 to 4 weeks and produces a working product increment.

### Scrum diagram

```text
Product Backlog
      |
      v
Sprint Planning
      |
      v
Sprint Backlog
      |
      v
Sprint Development + Daily Scrum
      |
      v
Product Increment
      |
      v
Sprint Review + Sprint Retrospective
```

## **2.10 Scrum Roles**

1. **Product Owner**

=> Represents customer and business needs.

=> Maintains product backlog and decides feature priority.

2. **Scrum Master**

=> Facilitates Scrum process.

=> Removes obstacles and helps team follow Scrum practices.

3. **Development Team**

=> Self-organizing team that designs, codes, tests, and delivers product increment.

## **2.11 Scrum Artifacts**

1. **Product Backlog**

=> List of all required features, improvements, and fixes.

2. **Sprint Backlog**

=> Selected work to be completed in current sprint.

3. **Product Increment**

=> Working software produced at the end of sprint.

## **2.12 Scrum Events**

1. **Sprint Planning**

=> Team selects work for the sprint.

2. **Daily Scrum**

=> Short daily meeting to discuss progress, plans, and blockers.

3. **Sprint Review**

=> Team demonstrates completed work to stakeholders.

4. **Sprint Retrospective**

=> Team discusses what went well, what went wrong, and how to improve.

### Merits of Scrum

1. Fast delivery of working software.
2. Handles changing requirements.
3. Improves team communication.
4. Frequent customer feedback.
5. Problems are identified early.
6. Increases transparency.

### Demerits of Scrum

1. Requires disciplined and experienced team.
2. Not ideal when scope is fixed and changes are not allowed.
3. Daily meetings may become ineffective if not managed.
4. Difficult for very large teams without scaling.
5. Poor product owner involvement reduces success.

## **2.13 Dynamic Systems Development Method (DSDM)**

=> **Dynamic Systems Development Method (DSDM)** is an agile framework used for rapid application development.

=> It focuses on business value, user involvement, time-boxing, and frequent delivery.

### Features

1. Active user involvement.
2. Iterative and incremental development.
3. Time-boxed delivery.
4. Prioritized requirements.
5. Frequent feedback.
6. Business value focus.

### MoSCoW prioritization

| Category | Meaning |
|---|---|
| Must have | Essential requirement. |
| Should have | Important but not critical. |
| Could have | Useful if time permits. |
| Won't have now | Not included in current delivery. |

### DSDM lifecycle

```text
Feasibility Study
      |
      v
Business Study
      |
      v
Functional Model Iteration
      |
      v
Design and Build Iteration
      |
      v
Implementation
```

### Advantages

1. Fast delivery.
2. Strong user involvement.
3. Handles changing requirements.
4. Prioritization controls scope.
5. Focuses on business needs.

### Disadvantages

1. Requires continuous user availability.
2. Not suitable for small simple projects.
3. Requires trained team.
4. Time-boxing may reduce documentation.

## **2.14 Adaptive Software Development (ASD)**

=> **Adaptive Software Development (ASD)** is an agile model used for complex and changing software projects.

=> It accepts uncertainty and encourages learning through repeated cycles.

### ASD lifecycle

```text
Speculate -> Collaborate -> Learn
     ^                         |
     |_________________________|
```

### 1. Speculate

=> Define mission, constraints, basic requirements, and iteration plan.

=> Planning is flexible because requirements may change.

### 2. Collaborate

=> Team members, customers, and stakeholders work together to build features.

=> Collaboration is important for complex systems.

### 3. Learn

=> Team learns from customer feedback, testing, defects, and review.

=> Learning is used to improve the next cycle.

### Characteristics

1. Mission-focused.
2. Feature-based planning.
3. Iterative cycles.
4. Strong collaboration.
5. Continuous learning.
6. Tolerance for change.

### Advantages

1. Suitable for uncertain requirements.
2. Encourages innovation.
3. Supports rapid change.
4. Improves customer involvement.

### Disadvantages

1. Requires experienced team.
2. Less suitable for fixed-scope projects.
3. Project control may be difficult if feedback is weak.

## **2.15 Crystal**

=> **Crystal** is a family of agile methods that focuses on people, communication, and project size.

=> Different Crystal methods are selected based on team size and project criticality.

### Features

1. People-centered approach.
2. Frequent delivery.
3. Reflective improvement.
4. Close communication.
5. Lightweight documentation.

### Example

=> Crystal Clear is used for small teams and low-criticality projects.

## **2.16 Feature Driven Development (FDD)**

=> **Feature Driven Development (FDD)** is an agile model that develops software feature by feature.

=> A feature is a small client-valued function.

### FDD process

```text
Develop overall model
      |
      v
Build feature list
      |
      v
Plan by feature
      |
      v
Design by feature
      |
      v
Build by feature
```

### Advantages

1. Clear feature-based planning.
2. Progress is easy to track.
3. Suitable for larger agile teams.
4. Focuses on customer-valued functions.

## **2.17 Agile Unified Process (AUP)**

=> **Agile Unified Process (AUP)** is a simplified agile version of Rational Unified Process.

=> It keeps important phases but applies them in an agile and iterative manner.

### Phases

1. Inception.
2. Elaboration.
3. Construction.
4. Transition.

### Disciplines

1. Modeling.
2. Implementation.
3. Testing.
4. Deployment.
5. Configuration management.
6. Project management.

## **2.18 Agile Development Tools**

=> Agile tools help teams manage tasks, collaboration, code, testing, and delivery.

### Common tool categories

1. **Project management tools**

=> Jira, Trello, Azure Boards.

2. **Version control tools**

=> Git, GitHub, GitLab, Bitbucket.

3. **Communication tools**

=> Slack, Microsoft Teams, email, video meetings.

4. **Testing tools**

=> Selenium, JUnit, Postman.

5. **CI/CD tools**

=> Jenkins, GitHub Actions, GitLab CI.

6. **Documentation tools**

=> Confluence, Notion, Markdown documents.

### Benefits

1. Better task tracking.
2. Faster communication.
3. Easier sprint planning.
4. Automated testing and build.
5. Improved visibility.

## **2.19 Agile Model vs Waterfall Model**

| Agile Model | Waterfall Model |
|---|---|
| Iterative and incremental. | Linear and sequential. |
| Requirements can change. | Requirements should be stable. |
| Working software delivered frequently. | Working software delivered at the end. |
| Customer feedback is continuous. | Customer feedback is limited. |
| Less formal documentation. | More formal documentation. |
| Suitable for changing requirements. | Suitable for fixed requirements. |

## **2.20 Scrum vs XP**

| Scrum | XP |
|---|---|
| Agile project management framework. | Agile development method. |
| Focuses on sprint planning, roles, and events. | Focuses on coding and engineering practices. |
| Uses Product Owner, Scrum Master, Development Team. | Uses practices like pair programming and TDD. |
| Does not prescribe detailed coding practices. | Strongly prescribes coding practices. |
| Sprint is usually 1 to 4 weeks. | Iterations are short and releases are frequent. |

## **2.21 Important Exam Answers**

### Agility for 3 Marks

=> Write definition, need, and 4 to 5 features.

### Agile principles for 4 or 7 Marks

=> Write definition and explain at least 8 principles. Add advantages and disadvantages if asked.

### XP for 7 Marks

=> Write definition, process diagram, values, practices, advantages, and disadvantages.

### Scrum for 7 Marks

=> Write definition, diagram, roles, artifacts, events, merits, and demerits.

### DSDM for 4 Marks

=> Write definition, features, MoSCoW prioritization, and advantages.

### ASD for 7 Marks

=> Write definition, lifecycle diagram, speculate-collaborate-learn phases, characteristics, advantages, and disadvantages.

## **2.22 Exam Short Questions**

### 1. Define agility.

=> Agility is the ability of a software team to respond quickly and effectively to changing requirements and conditions.

### 2. List any four agile principles.

=> Welcome changing requirements, deliver working software frequently, customer collaboration, and working software as progress measure.

### 3. What is agile process model?

=> Agile process model is an iterative and incremental model that delivers working software frequently with customer feedback.

### 4. List agile process models.

=> XP, Scrum, DSDM, ASD, Crystal, FDD, and AUP.

### 5. Define XP.

=> Extreme Programming is an agile method that focuses on simple design, continuous testing, pair programming, and frequent releases.

### 6. What is pair programming?

=> Pair programming is an XP practice where two programmers work together on the same code.

### 7. What is test-driven development?

=> TDD is a practice where test cases are written before code and code is developed to pass those tests.

### 8. What is spike solution?

=> A spike solution is a small experimental program used in XP to investigate a technical risk or unclear requirement.

### 9. Define Scrum.

=> Scrum is an agile framework where software is developed in short iterations called sprints.

### 10. List Scrum roles.

=> Product Owner, Scrum Master, and Development Team.

### 11. What is product backlog?

=> Product backlog is a prioritized list of all features, improvements, and fixes required in the product.

### 12. What is sprint backlog?

=> Sprint backlog is the selected work to be completed in the current sprint.

### 13. What is DSDM?

=> DSDM is an agile framework for rapid development using user involvement, time-boxing, and prioritized requirements.

### 14. What is MoSCoW?

=> MoSCoW is a prioritization technique: Must have, Should have, Could have, Won't have now.

### 15. What is ASD lifecycle?

=> ASD lifecycle contains Speculate, Collaborate, and Learn.

### 16. Give one advantage of agile.

=> Agile handles changing requirements and delivers working software early.

### 17. Give one disadvantage of agile.

=> Agile requires active customer involvement and disciplined team members.

### 18. Difference between Scrum and XP.

=> Scrum focuses on agile project management, while XP focuses on engineering practices like pair programming, TDD, and refactoring.
