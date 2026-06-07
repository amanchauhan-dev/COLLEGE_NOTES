# **4 Requirement Analysis and Specification**

=> This chapter covers understanding requirements, requirement engineering, elicitation, analysis, modeling, SRS, functional and non-functional requirements, DFD, use case diagram, and CRC modeling.

=> In exams, repeated questions are asked on **requirement engineering tasks**, **requirement elicitation**, **functional and non-functional requirements**, **good SRS characteristics**, **SRS contents**, **DFD**, **use case diagram**, and **CRC modeling**.

## **4.1 Requirement**

=> A **requirement** is a statement of what the software system should do or what quality/constraint it should satisfy.

### Examples

1. User shall login using username and password.
2. System shall generate monthly report.
3. System shall respond within 2 seconds.
4. Password must be encrypted.

### Need of requirements

1. Understand customer needs.
2. Define project scope.
3. Prepare design.
4. Estimate cost and schedule.
5. Prepare test cases.
6. Avoid misunderstanding.

## **4.2 Requirement Engineering**

=> **Requirement Engineering** is the process of discovering, analyzing, documenting, validating, and managing software requirements.

=> It helps developers understand what the customer wants and what the system must do.

### Diagram

```text
Inception
   |
   v
Elicitation
   |
   v
Elaboration
   |
   v
Negotiation
   |
   v
Specification
   |
   v
Validation
   |
   v
Requirement Management
```

### Importance

1. Reduces misunderstanding between customer and developer.
2. Helps prepare accurate SRS.
3. Reduces rework.
4. Improves software quality.
5. Helps in design and testing.
6. Controls requirement changes.

## **4.3 Requirement Engineering Tasks**

### 1. Inception

=> Inception means understanding the basic problem, business need, stakeholders, and project scope.

### Activities

1. Identify stakeholders.
2. Understand business goals.
3. Define problem boundary.
4. Decide initial feasibility.

### 2. Elicitation

=> Elicitation means collecting requirements from stakeholders.

### Techniques

1. Interviews.
2. Questionnaires.
3. Observation.
4. Brainstorming.
5. Workshops.
6. Prototyping.

### 3. Elaboration

=> Elaboration means refining collected requirements into detailed models and descriptions.

### Outputs

1. Use cases.
2. Data models.
3. Behavior models.
4. Scenario descriptions.

### 4. Negotiation

=> Negotiation resolves conflicts between requirements and prioritizes them based on cost, time, and value.

### Example

=> Customer wants all features in one month, but team negotiates priority and delivers important features first.

### 5. Specification

=> Specification means documenting requirements formally in SRS.

### 6. Validation

=> Validation checks whether requirements are correct, complete, consistent, feasible, and clear.

### 7. Requirement Management

=> Requirement management tracks and controls requirement changes throughout the project.

## **4.4 Requirement Elicitation**

=> **Requirement Elicitation** is the activity of collecting requirements from customers, users, managers, domain experts, and other stakeholders.

### Elicitation techniques

1. **Interviews**

=> Ask direct questions to stakeholders.

### Advantages

1. Useful for detailed information.
2. Clarifies doubts immediately.

2. **Questionnaires**

=> Written questions are given to many users.

### Advantages

1. Useful for large user groups.
2. Saves time.

3. **Observation**

=> Analyst observes users doing real work.

### Advantages

1. Finds actual workflow.
2. Helps discover hidden requirements.

4. **Brainstorming**

=> Group discussion is used to generate ideas quickly.

5. **Workshops**

=> Stakeholders meet together to discuss, refine, and agree on requirements.

6. **Prototyping**

=> A sample system is built to get feedback.

### Elicitation challenges

1. Users may not know exact needs.
2. Requirements may conflict.
3. Stakeholders may use unclear language.
4. Business rules may be hidden.
5. Requirements may change over time.

## **4.5 Functional Requirements**

=> **Functional requirements** describe what the software system must do.

=> They define system services, inputs, outputs, processing, and behavior.

### Examples

1. User can register and login.
2. System can generate invoice.
3. Student can view result.
4. Admin can add or delete products.
5. System can calculate fine.

### Hotel management examples

1. System shall allow receptionist to book rooms.
2. System shall maintain guest details.
3. System shall show available rooms.
4. System shall generate bills.
5. System shall allow check-in and check-out.

## **4.6 Non-Functional Requirements**

=> **Non-functional requirements** describe how well the system should perform.

=> They define quality attributes and constraints.

### Types

1. Performance.
2. Security.
3. Reliability.
4. Availability.
5. Usability.
6. Maintainability.
7. Portability.
8. Scalability.

### Examples

1. Login response must be within 2 seconds.
2. Password must be encrypted.
3. System should be available 24/7.
4. User interface should be easy to use.
5. System should support backup and recovery.

### Functional vs Non-functional

| Functional Requirement | Non-Functional Requirement |
|---|---|
| Describes what system does. | Describes quality or constraint. |
| Defines services and behavior. | Defines performance, security, usability, etc. |
| Example: Generate bill. | Example: Generate bill within 2 seconds. |

## **4.7 Requirement Stability and Correctness**

=> Requirements must be **correct** because wrong requirements lead to wrong software.

=> Requirements must be **stable** because frequent uncontrolled changes increase cost, delay, and defects.

### Why stable and correct requirements are important

1. Reduce rework.
2. Improve design accuracy.
3. Improve testing quality.
4. Control cost and schedule.
5. Improve customer satisfaction.
6. Reduce project risk.

## **4.8 Requirement Analysis**

=> **Requirement Analysis** is the process of studying requirements to find conflicts, incompleteness, ambiguity, and feasibility issues.

### Activities

1. Classify requirements.
2. Identify conflicts.
3. Check feasibility.
4. Prioritize requirements.
5. Model requirements.
6. Define constraints.
7. Prepare analysis documents.

### Output

=> Main output of requirement analysis is a clear and complete SRS and requirement models.

## **4.9 Requirement Modeling**

=> **Requirement Modeling** represents requirements using diagrams, models, and structured descriptions.

### Types of requirement models

1. **Scenario-based models**

=> Use cases and user stories.

2. **Data models**

=> ER diagram and data dictionary.

3. **Flow-oriented models**

=> Data Flow Diagram.

4. **Behavioral models**

=> State diagram and activity diagram.

5. **Class-based models**

=> Class diagram and CRC cards.

## **4.10 Software Requirement Specification (SRS)**

=> **SRS** stands for **Software Requirement Specification**.

=> It is a formal document that describes functional requirements, non-functional requirements, constraints, interfaces, and acceptance criteria of software.

### Importance

1. Acts as agreement between customer and developer.
2. Base document for design and coding.
3. Helps prepare test cases.
4. Supports project estimation.
5. Reduces misunderstanding.
6. Helps maintenance.

## **4.11 Contents of SRS**

### 1. Introduction

=> Purpose, scope, definitions, references, and overview.

### 2. Overall Description

=> Product perspective, product functions, user characteristics, constraints, assumptions, and dependencies.

### 3. Functional Requirements

=> Detailed functions and services the system must provide.

### 4. Non-Functional Requirements

=> Performance, reliability, security, usability, availability, and maintainability.

### 5. External Interface Requirements

=> User interface, hardware interface, software interface, and communication interface.

### 6. Data Requirements

=> Data storage, validation, database, data format, and data relationships.

### 7. System Constraints

=> Operating system, hardware, legal rules, standards, language, and environment constraints.

### 8. Use Cases or Scenarios

=> User interactions with the system.

### 9. Acceptance Criteria

=> Conditions used to decide whether system satisfies requirements.

## **4.12 Characteristics of Good SRS**

1. **Correct**

=> SRS must represent actual customer needs.

2. **Complete**

=> All required functions, constraints, and interfaces must be included.

3. **Consistent**

=> Requirements should not conflict with each other.

4. **Unambiguous**

=> Every requirement should have only one meaning.

5. **Feasible**

=> Requirements should be possible within time, cost, and technology.

6. **Verifiable**

=> Requirements should be testable.

7. **Traceable**

=> Each requirement should be traceable from source to design, code, and test.

8. **Modifiable**

=> SRS should be easy to update.

9. **Understandable**

=> SRS should be clear to customer, developer, and tester.

## **4.13 Data Flow Diagram**

=> **Data Flow Diagram (DFD)** shows how data moves through a system.

=> It represents external entities, processes, data stores, and data flows.

### Symbols

| Symbol | Meaning |
|---|---|
| External entity | Source or destination of data. |
| Process | Transforms input data into output data. |
| Data store | Stores data. |
| Data flow | Movement of data. |

### DFD for Library Management System

```text
              Book request / return
Member ------------------------------+
                                     |
                                     v
                           +--------------------+
Librarian ---------------->| Library Management |
Book details / issue info  |       System       |
                           +---------+----------+
                                     |
                  +------------------+------------------+
                  v                                     v
            Book Database                         Member Database
```

### Explanation

1. Member searches, issues, and returns books.
2. Librarian manages books and members.
3. Book database stores book information.
4. Member database stores member details.
5. Issue record stores book issue and return details.

## **4.14 Use Case Diagram**

=> **Use Case Diagram** shows interaction between actors and system functions.

### Elements

1. **Actor**

=> External user or system interacting with software.

2. **Use case**

=> Function or service provided by system.

3. **Association**

=> Relationship between actor and use case.

### Use Case Diagram for ATM System

```text
Customer -------- Insert Card
Customer -------- Enter PIN
Customer -------- Withdraw Cash
Customer -------- Balance Inquiry
Customer -------- Deposit Cash
Customer -------- Transfer Funds
Customer -------- Change PIN
Customer -------- Print Receipt

ATM System ------ Validate Account ------ Bank Server
ATM System ------ Update Transaction ---- Bank Server

Technician ------ Refill Cash
Technician ------ Maintain ATM
```

### Use Case Diagram for Online Shopping Website

```text
Customer -------- Register/Login
Customer -------- Search Product
Customer -------- View Product
Customer -------- Add to Cart
Customer -------- Place Order
Customer -------- Make Payment -------- Payment Gateway
Customer -------- Track Order

Admin ----------- Manage Products
Admin ----------- Manage Orders
Admin ----------- Generate Reports

Delivery Staff -- Update Delivery Status
```

## **4.15 CRC Modeling**

=> **CRC** stands for **Class-Responsibility-Collaborator**.

=> CRC modeling is an object-oriented analysis technique used to identify classes, responsibilities, and collaborators.

### CRC card structure

```text
+-----------------------------------+
| Class Name                         |
+------------------+----------------+
| Responsibilities | Collaborators  |
+------------------+----------------+
```

### Terms

1. **Class**

=> Object or concept in system.

2. **Responsibility**

=> What the class knows or does.

3. **Collaborator**

=> Other class that helps fulfill responsibility.

### CRC for Email System User

```text
+------------------------------------------------------+
| Class: EmailSystemUser                               |
+-----------------------------+------------------------+
| Responsibilities            | Collaborators          |
+-----------------------------+------------------------+
| Login to email account      | AuthenticationService  |
| Compose email               | EmailMessage           |
| Send email                  | MailServer             |
| Receive email               | Inbox                  |
| Read email                  | EmailMessage           |
| Delete email                | Inbox, TrashFolder     |
| Manage contacts             | ContactList            |
| Attach files                | Attachment             |
+-----------------------------+------------------------+
```

### Benefits

1. Simple and easy to understand.
2. Helps identify classes early.
3. Shows responsibilities clearly.
4. Shows collaboration between classes.
5. Useful in object-oriented analysis.

## **4.16 Requirement Validation**

=> Requirement validation checks whether requirements are correct, complete, consistent, feasible, and testable.

### Techniques

1. Requirement reviews.
2. Prototyping.
3. Test case generation.
4. User approval.
5. Consistency checking.

### Validation checklist

1. Are all requirements clear?
2. Are any requirements missing?
3. Are requirements testable?
4. Are requirements realistic?
5. Do requirements conflict?
6. Are all stakeholders satisfied?

## **4.17 Requirement Management**

=> **Requirement Management** controls requirement changes during the software lifecycle.

### Activities

1. Identify requirements.
2. Store requirements.
3. Track requirement status.
4. Handle change requests.
5. Perform impact analysis.
6. Update SRS.
7. Maintain traceability.

### Need

1. Requirements change during development.
2. Uncontrolled changes increase cost and risk.
3. Changes must be approved and tracked.
4. Test cases and design must stay updated.

## **4.18 Exam Short Questions**

### 1. Define requirement.

=> Requirement is a statement of what the system should do or what quality/constraint it should satisfy.

### 2. Define requirement engineering.

=> Requirement engineering is the process of gathering, analyzing, documenting, validating, and managing requirements.

### 3. List requirement engineering tasks.

=> Inception, elicitation, elaboration, negotiation, specification, validation, and management.

### 4. What is requirement elicitation?

=> Requirement elicitation is the process of collecting requirements from stakeholders.

### 5. Define functional requirement.

=> Functional requirement describes what the system must do.

### 6. Define non-functional requirement.

=> Non-functional requirement describes quality attributes or constraints of the system.

### 7. What is SRS?

=> SRS is a formal document that describes functional and non-functional requirements of software.

### 8. List characteristics of good SRS.

=> Correct, complete, consistent, unambiguous, feasible, verifiable, traceable, modifiable, and understandable.

### 9. What is DFD?

=> DFD is a diagram that shows flow of data through processes, data stores, and external entities.

### 10. What is use case diagram?

=> Use case diagram shows interaction between actors and system functions.

### 11. What is CRC modeling?

=> CRC modeling identifies classes, responsibilities, and collaborators in object-oriented analysis.

### 12. Why requirements must be stable?

=> Stable requirements reduce rework, cost, delay, and defects.
