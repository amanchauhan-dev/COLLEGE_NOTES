# **6 Software Coding and Testing**

=> This chapter covers coding standards, coding guidelines, code review, documentation, testing concepts, testing strategies, testing techniques, test cases, test suite design, conventional/OO/web/mobile testing, and testing tools.

=> In exams, repeated questions are asked on **coding standards**, **software testing**, **levels of testing**, **black box testing**, **white box testing**, **BVA**, **cyclomatic complexity**, **verification vs validation**, **alpha vs beta testing**, **stub and driver**, and **system testing**.

## **6.1 Coding**

=> **Coding** is the process of converting software design into source code using a programming language.

=> Good coding should produce readable, reliable, maintainable, and testable programs.

### Objectives

1. Convert design into working software.
2. Follow coding standards.
3. Reduce programming errors.
4. Make code easy to test.
5. Make code easy to maintain.

## **6.2 Coding Standards**

=> **Coding standards** are rules and guidelines followed while writing source code.

=> They make code consistent, readable, maintainable, and less error-prone.

### Need

1. Improve readability.
2. Reduce defects.
3. Support team development.
4. Make maintenance easier.
5. Improve code review quality.
6. Improve reusability.

### Important coding standards

1. **Naming conventions**

=> Use meaningful names for variables, functions, classes, and files.

=> Example: `calculateSalary()` is better than `cs()`.

2. **Indentation and formatting**

=> Use consistent spacing and indentation.

3. **Commenting**

=> Add useful comments for complex logic and assumptions.

4. **Modularity**

=> Divide code into small functions or modules with single responsibility.

5. **Error handling**

=> Handle invalid input, exceptions, and failures properly.

6. **Avoid duplicate code**

=> Reuse functions instead of copying logic.

7. **Use constants**

=> Avoid magic numbers. Use named constants.

8. **Security**

=> Validate input and avoid hardcoded passwords.

9. **Testing support**

=> Write code that is easy to test.

## **6.3 Coding Guidelines**

### Guidelines

1. Keep functions small and focused.
2. Use meaningful variable names.
3. Avoid deeply nested conditions.
4. Validate all input.
5. Handle errors clearly.
6. Do not duplicate code.
7. Keep business logic separate from UI.
8. Use standard libraries when suitable.
9. Write simple and understandable code.
10. Follow project coding style.

## **6.4 Code Review**

=> **Code Review** is the process of examining source code to find defects, improve quality, and ensure coding standards.

### Objectives

1. Find defects early.
2. Improve code readability.
3. Ensure coding standards.
4. Improve security.
5. Share knowledge among team members.

### Types

1. Informal review.
2. Peer review.
3. Walkthrough.
4. Inspection.
5. Automated static analysis.

### Benefits

1. Reduces testing cost.
2. Improves maintainability.
3. Finds defects before execution.
4. Improves team learning.

## **6.5 Software Documentation**

=> **Software documentation** is written information that explains requirements, design, code, testing, deployment, and usage of software.

### Types

1. **Requirement documentation**

=> SRS and requirement models.

2. **Design documentation**

=> Architecture, database, interface, and component design.

3. **Code documentation**

=> Comments, API documentation, and module descriptions.

4. **Testing documentation**

=> Test plan, test cases, test data, and test report.

5. **User documentation**

=> User manual, installation guide, and help files.

### Importance

1. Helps maintenance.
2. Supports testing.
3. Helps new developers understand system.
4. Reduces dependency on original developers.
5. Improves communication.

## **6.6 Software Testing**

=> **Software testing** is the process of executing software to find defects and verify that it satisfies specified requirements.

=> Testing increases confidence in software quality but does not prove that software is defect-free.

### Objectives

1. Find defects.
2. Verify requirements.
3. Validate user expectations.
4. Improve quality.
5. Reduce risk before delivery.
6. Check performance, security, and reliability.

## **6.7 Error, Defect and Failure**

| Term | Meaning | Example |
|---|---|---|
| Error | Human mistake during development. | Developer writes wrong formula. |
| Defect | Fault present in software artifact or code. | Wrong formula exists in code. |
| Failure | Incorrect behavior during execution. | Bill amount is calculated wrongly. |

=> Error is the cause, defect is present in software, and failure is observed during execution.

## **6.8 Verification and Validation**

| Verification | Validation |
|---|---|
| Checks whether product is being built correctly. | Checks whether correct product is being built. |
| Focuses on process and work products. | Focuses on final product and user needs. |
| Usually done without executing code. | Usually done by executing software. |
| Includes reviews, inspections, and walkthroughs. | Includes testing and acceptance testing. |
| Answers: Are we building the product right? | Answers: Are we building the right product? |

## **6.9 Levels of Testing**

```text
Acceptance Testing
System Testing
Integration Testing
Unit Testing
```

### 1. Unit Testing

=> Tests the smallest unit such as function, class, or module.

=> Usually performed by developers.

### Example

=> Test `calculateGrade(marks)` function.

### 2. Integration Testing

=> Tests combined modules to check interfaces and data flow.

### Approaches

1. Big bang.
2. Top-down.
3. Bottom-up.
4. Sandwich.

### 3. System Testing

=> Tests complete integrated software system as a whole.

=> Checks functional and non-functional requirements.

### 4. Acceptance Testing

=> Checks whether software is acceptable to customer or end user.

### Types

1. Alpha testing.
2. Beta testing.

## **6.10 Stub and Driver**

=> **Stub** and **Driver** are temporary programs used during testing.

### Stub

=> Stub is a dummy called module used when lower-level module is not ready.

=> Used in top-down testing.

### Driver

=> Driver is a dummy calling module used to test lower-level module.

=> Used in bottom-up testing.

### Example

=> If module `A` calls module `B`, and `B` is not ready, create stub for `B`.

=> If `B` is ready but `A` is not ready, create driver to call `B`.

## **6.11 Alpha and Beta Testing**

| Alpha Testing | Beta Testing |
|---|---|
| Performed at developer site. | Performed in real user environment. |
| Done by internal testers or selected customer representatives. | Done by selected real users. |
| Controlled environment. | Uncontrolled environment. |
| Done before beta testing. | Done after alpha testing. |
| Finds major defects before release. | Finds real-world usability and environment issues. |

=> Both are types of acceptance testing.

## **6.12 System Testing**

=> **System Testing** is testing of the complete integrated software system.

=> It checks whether the system satisfies the SRS.

### Need

1. Verify complete system behavior.
2. Check end-to-end workflows.
3. Detect module interaction defects.
4. Validate performance, security, usability, and recovery.

### Types

1. **Functional testing**

=> Checks whether required functions work correctly.

2. **Performance testing**

=> Checks response time, throughput, and resource usage.

3. **Stress testing**

=> Tests system under extreme load.

4. **Security testing**

=> Checks protection against unauthorized access.

5. **Recovery testing**

=> Checks recovery after crash or failure.

6. **Usability testing**

=> Checks ease of use.

7. **Compatibility testing**

=> Checks different browsers, devices, operating systems, or environments.

### Process

```text
Prepare system test plan
        |
        v
Create test cases and test data
        |
        v
Execute tests
        |
        v
Record defects
        |
        v
Fix and retest
        |
        v
Prepare test report
```

## **6.13 Black Box Testing**

=> **Black Box Testing** tests software functionality without knowing internal code structure.

=> Tester focuses on input, output, and requirements.

### Features

1. Based on SRS.
2. Code knowledge is not required.
3. Used for functional testing.
4. Finds missing or incorrect functions.
5. Useful for validation.

### Techniques

1. Equivalence Partitioning.
2. Boundary Value Analysis.
3. Decision Table Testing.
4. State Transition Testing.
5. Cause-Effect Graphing.

## **6.14 White Box Testing**

=> **White Box Testing** tests internal logic, code structure, branches, paths, and conditions.

=> Tester needs knowledge of code.

### Techniques

1. Statement coverage.
2. Branch coverage.
3. Path coverage.
4. Condition coverage.
5. Loop testing.
6. Basis path testing.

## **6.15 Black Box vs White Box Testing**

| Black Box Testing | White Box Testing |
|---|---|
| Tests external functionality. | Tests internal code structure. |
| Code knowledge is not required. | Code knowledge is required. |
| Based on SRS. | Based on program logic. |
| Finds missing or incorrect functions. | Finds logic and path errors. |
| Techniques: BVA, equivalence partitioning. | Techniques: basis path, condition testing. |
| Mostly done by testers. | Mostly done by developers/testers. |

## **6.16 Equivalence Partitioning**

=> **Equivalence Partitioning** divides input data into valid and invalid groups called equivalence classes.

=> One test case from each class is selected because values in same class are expected to behave similarly.

### Example

=> Age must be between 18 and 60.

| Class | Input | Expected result |
|---|---:|---|
| Invalid low | 15 | Reject |
| Valid | 30 | Accept |
| Invalid high | 70 | Reject |

### Advantages

1. Reduces number of test cases.
2. Covers valid and invalid input.
3. Easy to apply.

## **6.17 Boundary Value Analysis**

=> **Boundary Value Analysis (BVA)** is a black box testing technique that tests values at the boundaries of input ranges.

=> Errors often occur near boundary values.

### Example

=> If valid age range is 18 to 60, test:

```text
17, 18, 19, 59, 60, 61
```

### Guidelines

1. For range `[min, max]`, test `min-1`, `min`, `min+1`, `max-1`, `max`, `max+1`.
2. Test boundaries of input and output values.
3. Test first and last elements of arrays.
4. Test loop boundary values.
5. Include valid and invalid boundary values.

## **6.18 Cyclomatic Complexity**

=> **Cyclomatic Complexity** is a software metric that measures logical complexity of a program.

=> It gives the number of independent paths in a control flow graph.

=> It helps determine minimum number of test cases for basis path testing.

### Formula

```text
V(G) = E - N + 2
```

=> Where:

1. `E` = number of edges.
2. `N` = number of nodes.

### General formula

```text
V(G) = E - N + 2P
```

=> `P` is number of connected components.

### Alternative formula

```text
V(G) = Predicate nodes + 1
```

### Steps

1. Read program logic.
2. Draw control flow graph.
3. Represent statements or blocks as nodes.
4. Represent control flow as edges.
5. Count edges `E`.
6. Count nodes `N`.
7. Apply formula.
8. Identify independent paths.
9. Prepare at least `V(G)` test cases.

### Example

```text
if marks >= 40:
    result = "Pass"
else:
    result = "Fail"
```

=> There is one predicate node.

```text
V(G) = 1 + 1 = 2
```

=> Minimum 2 test cases are required.

## **6.19 Test Case and Test Suite**

=> **Test Case** is a set of input values, execution conditions, and expected results.

### Test case contains

1. Test case ID.
2. Objective.
3. Input data.
4. Steps.
5. Expected output.
6. Actual output.
7. Status.

=> **Test Suite** is a collection of related test cases.

### Example

=> Login test suite may contain valid login, invalid password, blank username, locked account, and password reset test cases.

## **6.20 Testing Strategies**

### Common testing strategies

1. Unit testing.
2. Integration testing.
3. Validation testing.
4. System testing.
5. Regression testing.
6. Performance testing.
7. Security testing.
8. Acceptance testing.

## **6.21 Testing Web Applications**

### WebApp testing strategies

1. Content testing.
2. Interface testing.
3. Navigation testing.
4. Functionality testing.
5. Compatibility testing.
6. Performance testing.
7. Security testing.
8. Usability testing.
9. Database testing.
10. Configuration testing.

## **6.22 Testing Mobile Applications**

### Mobile testing areas

1. Functional testing.
2. Usability testing.
3. Compatibility testing.
4. Performance testing.
5. Security testing.
6. Network testing.
7. Installation testing.
8. Interrupt testing.

## **6.23 Testing Tools**

### WinRunner

=> WinRunner is an automated functional testing tool used for GUI-based application testing.

### LoadRunner

=> LoadRunner is a performance testing tool used to test application behavior under load.

## **6.24 Exam Short Questions**

### 1. Define software testing.

=> Software testing is the process of executing software to find defects and verify requirements.

### 2. Define black box testing.

=> Black box testing tests functionality without knowing internal code.

### 3. Define white box testing.

=> White box testing tests internal code structure and logic.

### 4. What is BVA?

=> BVA is a testing technique that checks boundary values of input ranges.

### 5. Define cyclomatic complexity.

=> Cyclomatic complexity measures logical complexity and independent paths of a program.

### 6. What is a stub?

=> Stub is a dummy called module used when lower-level module is not ready.

### 7. What is a driver?

=> Driver is a dummy calling module used to test lower-level module.

### 8. What is test suite?

=> Test suite is a collection of related test cases.

### 9. What is verification?

=> Verification checks whether product is built correctly.

### 10. What is validation?

=> Validation checks whether correct product is built.
