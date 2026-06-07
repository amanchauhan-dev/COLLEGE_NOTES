# **5 Software Design**

=> This chapter covers software design concepts, design principles, architectural design, component-level design, procedural design, object-oriented design, coupling, cohesion, user interface design, and web application design.

=> In exams, repeated questions are asked on **coupling and cohesion**, **types of coupling**, **types of cohesion**, **procedural vs object-oriented design**, **architectural styles**, **golden rules of UI design**, **characteristics of good UI**, and **web design pyramid**.

## **5.1 Software Design**

=> **Software Design** is the process of converting software requirements into a blueprint for implementation.

=> It defines software architecture, modules, interfaces, data, components, and user interface.

### Need of design

1. Converts SRS into technical solution.
2. Reduces complexity.
3. Improves maintainability.
4. Helps coding and testing.
5. Supports reuse.
6. Improves quality.

### Design output

1. Architecture design.
2. Data design.
3. Interface design.
4. Component-level design.
5. User interface design.

## **5.2 Design Concepts**

### 1. Abstraction

=> Abstraction means showing essential details and hiding unnecessary details.

=> Example: A user uses `login()` without knowing internal authentication logic.

### 2. Architecture

=> Architecture defines overall structure of software, major components, and their relationships.

### 3. Pattern

=> A design pattern is a reusable solution to a common design problem.

=> Example: MVC pattern.

### 4. Modularity

=> Modularity divides software into small independent modules.

### 5. Information Hiding

=> Internal details of a module are hidden from other modules.

=> Only necessary interface is exposed.

### 6. Functional Independence

=> A module should perform one specific task with minimum dependency on other modules.

=> It is achieved by high cohesion and low coupling.

### 7. Refinement

=> Refinement means developing design from high-level details to low-level details step by step.

### 8. Refactoring

=> Refactoring improves internal structure of software without changing external behavior.

## **5.3 Design Principles**

1. Design should be traceable to requirements.
2. Design should not reinvent existing solutions.
3. Design should be simple and understandable.
4. Design should be modular.
5. Design should support maintainability.
6. Design should minimize coupling.
7. Design should maximize cohesion.
8. Design should handle errors properly.
9. Design should be reviewed to reduce defects.
10. Design should support future changes.

## **5.4 Modularity**

=> **Modularity** is the division of software into separate modules.

=> Each module performs a specific function.

### Advantages

1. Reduces complexity.
2. Makes testing easier.
3. Improves maintenance.
4. Supports parallel development.
5. Increases reusability.
6. Improves understanding.

## **5.5 Coupling**

=> **Coupling** is the degree of dependency between software modules.

=> Low coupling is desirable because modules become independent and easier to change.

### Types of coupling

1. **Content coupling**

=> One module directly uses or modifies internal data or code of another module.

=> It is the worst type of coupling.

2. **Common coupling**

=> Multiple modules share global data.

=> Change in global data can affect many modules.

3. **External coupling**

=> Modules depend on externally imposed data formats, protocols, or devices.

=> Example: Two modules depend on same external file format.

4. **Control coupling**

=> One module passes control information, such as flag, to control logic of another module.

5. **Stamp coupling**

=> A complete data structure is passed, but the called module uses only part of it.

6. **Data coupling**

=> Modules communicate only by passing required data values.

=> It is the best and most acceptable type.

### Effects of high coupling

1. Maintenance becomes difficult.
2. Testing becomes complex.
3. Reusability decreases.
4. Changes create side effects.
5. Portability decreases.

## **5.6 Cohesion**

=> **Cohesion** is the degree to which elements inside a module are related to each other.

=> High cohesion is desirable because a module becomes focused and understandable.

### Types of cohesion

1. **Coincidental cohesion**

=> Unrelated tasks are placed in one module.

=> Worst type of cohesion.

2. **Logical cohesion**

=> Related category of tasks are grouped, but selected by control flag.

=> Example: A module handles all input operations.

3. **Temporal cohesion**

=> Tasks related by time are grouped.

=> Example: Initialization module.

4. **Procedural cohesion**

=> Tasks are grouped because they follow a specific sequence.

=> Example: Read input, validate input, print output.

5. **Communicational cohesion**

=> Tasks operate on the same data.

=> Example: Read, update, and print student record.

6. **Sequential cohesion**

=> Output of one task becomes input of another task.

=> Example: Calculate marks and then calculate grade.

7. **Functional cohesion**

=> All elements perform one well-defined function.

=> Best type of cohesion.

### Effects of high cohesion

1. Improves readability.
2. Makes testing easier.
3. Improves reusability.
4. Reduces maintenance effort.
5. Reduces defects.

## **5.7 Coupling vs Cohesion**

| Coupling | Cohesion |
|---|---|
| Measures dependency between modules. | Measures relatedness inside a module. |
| Low coupling is desirable. | High cohesion is desirable. |
| Affects inter-module communication. | Affects internal module quality. |
| High coupling makes changes difficult. | High cohesion makes module easier to understand. |
| Example: Module A directly modifies Module B data. | Example: Salary module only calculates salary. |

=> Good design should have **low coupling** and **high cohesion**.

## **5.8 Coupling and Software Portability**

=> **Software portability** is the ability of software to run in different environments with minimum changes.

=> High coupling reduces portability because modules may depend on specific platforms, databases, devices, or APIs.

### Examples

| Situation | Effect |
|---|---|
| Code directly uses Windows registry APIs. | Difficult to port to Linux. |
| Business logic directly uses MySQL queries everywhere. | Difficult to shift to PostgreSQL. |
| UI and business logic are mixed. | Difficult to create web/mobile version. |
| Database access is separated using interface. | Easier to change database. |

=> Low coupling improves portability, reusability, and maintainability.

## **5.9 Architectural Design**

=> **Architectural Design** defines the high-level structure of software.

=> It identifies major components, their responsibilities, interfaces, and communication.

### Importance

1. Provides system blueprint.
2. Manages complexity.
3. Supports quality attributes.
4. Helps team communication.
5. Guides detailed design and implementation.

## **5.10 Architectural Styles**

### 1. Data-Centered Architecture

=> A central data store is accessed by different components.

=> Example: Repository system, database-centered system.

### 2. Data-Flow Architecture

=> Data flows through a series of transformations.

=> Example: Compiler, batch processing system.

### 3. Call and Return Architecture

=> Main program calls subprograms or procedures.

=> Example: Traditional procedural program.

### 4. Object-Oriented Architecture

=> System is organized around objects that contain data and methods.

=> Example: Java application with classes.

### 5. Layered Architecture

=> Software is divided into layers. Each layer uses services of lower layer.

### 6. Client-Server Architecture

=> Client sends requests and server provides services.

=> Example: Web application.

### 7. MVC Architecture

=> Model handles data, View handles UI, Controller handles input and flow.

### 8. Microservices Architecture

=> Application is divided into small independent services.

## **5.11 Layered Architecture**

=> In **Layered Architecture**, software is divided into layers with clear responsibilities.

### Diagram

```text
Presentation Layer
        |
Business Logic Layer
        |
Data Access Layer
        |
Database Layer
```

### Layers

1. **Presentation layer**

=> Handles user interface and user input.

2. **Business logic layer**

=> Handles rules and processing.

3. **Data access layer**

=> Handles database operations.

4. **Database layer**

=> Stores data.

### Advantages

1. Easy to maintain.
2. Supports separation of concerns.
3. Layers can be changed independently.
4. Improves reusability.
5. Suitable for web and enterprise applications.

### Disadvantages

1. Too many layers may reduce performance.
2. Poor layer design increases complexity.

## **5.12 Component-Level Design**

=> **Component-level design** defines internal details of each software component or module.

=> It describes data structures, algorithms, interfaces, and processing logic.

### Contents

1. Module name.
2. Inputs and outputs.
3. Internal data.
4. Algorithm.
5. Interface with other modules.
6. Error handling.

## **5.13 Procedural Design**

=> **Procedural Design** organizes software around procedures or functions.

=> It follows a top-down approach.

### Features

1. Focuses on functions.
2. Data and functions are separate.
3. Uses sequence, selection, iteration, and function calls.
4. Suitable for small and straightforward systems.

### Example

```text
main()
  readData()
  calculateTotal()
  printBill()
```

## **5.14 Object-Oriented Design**

=> **Object-Oriented Design (OOD)** organizes software around objects and classes.

=> Objects combine data and methods.

### Features

1. Class and object.
2. Encapsulation.
3. Inheritance.
4. Polymorphism.
5. Abstraction.
6. Message passing.

### Example

```text
Class: Student
Data: rollNo, name, marks
Methods: calculateGrade(), displayResult()
```

### Advantages

1. Improves reusability.
2. Easier maintenance.
3. Natural modeling of real-world entities.
4. Supports modularity.
5. Good for large systems.

## **5.15 Procedural Design vs Object-Oriented Design**

| Procedural Design | Object-Oriented Design |
|---|---|
| Focuses on procedures/functions. | Focuses on objects/classes. |
| Data and functions are separate. | Data and methods are combined. |
| Uses top-down design. | Uses object modeling. |
| Less suitable for large changing systems. | Suitable for large reusable systems. |
| Reuse through functions. | Reuse through inheritance/composition. |
| Example: C program with functions. | Example: Java program with classes. |

## **5.16 User Interface Design**

=> **User Interface Design** is the process of designing screens and interactions between user and software.

=> A good UI makes software easy to learn, easy to use, efficient, and error-free.

### Characteristics of good UI

1. Simple.
2. Consistent.
3. Easy to learn.
4. Easy to navigate.
5. Provides feedback.
6. Prevents errors.
7. Supports undo/cancel.
8. Readable and clear.
9. Efficient for frequent users.
10. Accessible.

## **5.17 Golden Rules of User Interface Design**

### 1. Place the user in control

=> User should feel in control of the software.

### Guidelines

1. Provide undo, redo, cancel, and back options.
2. Allow flexible navigation.
3. Avoid forcing unnecessary actions.
4. Provide shortcuts for expert users.
5. Give feedback after actions.

### 2. Reduce the user's memory load

=> UI should reduce the amount of information the user must remember.

### Guidelines

1. Use menus, icons, lists, and default values.
2. Show clear labels and instructions.
3. Group related fields together.
4. Use auto-complete and suggestions.
5. Keep screen layout simple.

### 3. Make the interface consistent

=> Similar actions and elements should look and behave the same throughout the system.

### Guidelines

1. Use consistent button names.
2. Use same colors and icons for same meaning.
3. Keep navigation style same.
4. Use standard terminology.
5. Display messages consistently.

### Benefits

1. Reduces user errors.
2. Improves learnability.
3. Increases user satisfaction.
4. Makes software easier to operate.

## **5.18 Web Application Design**

=> **Web Application Design** is the process of designing web-based software that runs through browsers or web clients.

### Important design concerns

1. User interface.
2. Navigation.
3. Content.
4. Performance.
5. Security.
6. Compatibility.
7. Scalability.
8. Accessibility.

## **5.19 Web Design Pyramid**

=> **Web Design Pyramid** represents important layers of web application design.

### Diagram

```text
        Aesthetics
      User Interface
   Navigation Design
  Component Design
 Architectural Design
    Data Design
```

### 1. Data Design

=> Defines data objects, database structure, relationships, and data flow.

=> Example: Customer, product, order, and payment tables.

### 2. Architectural Design

=> Defines overall structure of web application.

=> Example: Client-server, MVC, layered architecture.

### 3. Component Design

=> Defines logic of web components such as login, search, cart, payment, and reports.

### 4. Navigation Design

=> Defines how users move between pages and features.

=> Good navigation should be simple and consistent.

### 5. User Interface Design

=> Defines screens, forms, buttons, menus, colors, and layout.

### 6. Aesthetic Design

=> Defines visual appearance such as fonts, spacing, images, and color balance.

### Importance

1. Organizes web design decisions.
2. Improves usability.
3. Supports maintainability.
4. Improves consistency.
5. Reduces design errors.

## **5.20 Class Diagram for Hospital Management System**

=> A class diagram shows classes, attributes, methods, and relationships.

```text
+----------------+        +----------------+
| Patient        |        | Doctor         |
+----------------+        +----------------+
| patientId      |        | doctorId       |
| name           |        | name           |
| age            |        | specialization |
+----------------+        +----------------+
| register()     |        | diagnose()     |
| bookAppt()     |        | prescribe()    |
+-------+--------+        +--------+-------+
        |                          |
        v                          v
+----------------+        +----------------+
| Appointment    |        | Prescription   |
+----------------+        +----------------+
| appointmentId  |        | prescriptionId |
| date           |        | medicine       |
| time           |        | advice         |
+----------------+        +----------------+
| schedule()     |        | print()        |
+-------+--------+        +--------+-------+
        |
        v
+----------------+
| Bill           |
+----------------+
| billId         |
| amount         |
| paymentStatus  |
+----------------+
| generateBill() |
| receivePay()   |
+----------------+
```

### Relationships

1. Patient books appointment.
2. Doctor attends appointment.
3. Doctor creates prescription.
4. Bill is generated for patient.

## **5.21 Important Exam Comparisons**

### Coupling vs Cohesion

=> Write definition, comparison table, types if asked, and effects on modules.

### Procedural vs Object-Oriented Design

=> Write comparison table with focus, data handling, reuse, and suitability.

### Architectural styles

=> List styles and explain one such as layered architecture with diagram.

### UI golden rules

=> Explain three rules: place user in control, reduce memory load, and consistency.

## **5.22 Exam Short Questions**

### 1. Define software design.

=> Software design is the process of converting requirements into a blueprint for implementation.

### 2. What is modularity?

=> Modularity is dividing software into separate modules.

### 3. Define coupling.

=> Coupling is the degree of dependency between modules.

### 4. Define cohesion.

=> Cohesion is the degree of relatedness of elements inside a module.

### 5. Which coupling is best?

=> Data coupling is best.

### 6. Which cohesion is best?

=> Functional cohesion is best.

### 7. What is architectural design?

=> Architectural design defines high-level structure, components, interfaces, and communication of software.

### 8. List architectural styles.

=> Data-centered, data-flow, call and return, object-oriented, layered, client-server, MVC, and microservices.

### 9. Define procedural design.

=> Procedural design organizes software around procedures or functions.

### 10. Define object-oriented design.

=> Object-oriented design organizes software around classes and objects.

### 11. List golden rules of UI design.

=> Place user in control, reduce user's memory load, and make interface consistent.

### 12. What is web design pyramid?

=> Web design pyramid represents layers of web design: data, architecture, component, navigation, UI, and aesthetics.

### 13. What is information hiding?

=> Information hiding means internal details of a module are hidden from other modules.

### 14. What is functional independence?

=> Functional independence means a module performs one specific task with low coupling and high cohesion.
