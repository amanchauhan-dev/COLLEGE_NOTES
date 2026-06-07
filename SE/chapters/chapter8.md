# **8 Software Maintenance and Configuration Management**

=> This chapter covers software maintenance, types of maintenance, re-engineering, reverse engineering, forward engineering, Software Configuration Management, configuration items, version control, and change control.

=> In exams, repeated questions are asked on **types of maintenance**, **software re-engineering process model**, **reverse engineering**, **forward engineering**, **reverse vs forward engineering**, **SCM process**, **version control**, and **change control**.

## **8.1 Software Maintenance**

=> **Software Maintenance** is the process of modifying software after delivery to correct faults, improve performance, adapt to environment changes, or add new features.

### Need

1. Defects are found after delivery.
2. User requirements change.
3. Business rules change.
4. Hardware or operating system changes.
5. Security updates are required.
6. Performance must be improved.

### Maintenance process

```text
Change request
      |
      v
Impact analysis
      |
      v
Approval
      |
      v
Modify software
      |
      v
Test changes
      |
      v
Deploy updated version
      |
      v
Update documentation
```

## **8.2 Types of Software Maintenance**

### 1. Corrective Maintenance

=> Corrective maintenance fixes defects found after software delivery.

### Example

=> Correct wrong tax calculation in billing software.

### 2. Adaptive Maintenance

=> Adaptive maintenance modifies software to work in changed environment.

### Example

=> Update software to support new operating system, database, or browser.

### 3. Perfective Maintenance

=> Perfective maintenance improves functionality, performance, or usability.

### Example

=> Add export-to-PDF feature or improve dashboard layout.

### 4. Preventive Maintenance

=> Preventive maintenance improves internal structure to avoid future problems.

### Example

=> Refactor code, improve security, optimize database, or update old libraries.

### Comparison

| Type | Purpose | Example |
|---|---|---|
| Corrective | Fix defects. | Fix wrong bill calculation. |
| Adaptive | Adapt to new environment. | Support new OS. |
| Perfective | Improve features/performance. | Add report export. |
| Preventive | Prevent future issues. | Refactor code. |

## **8.3 Software Re-Engineering**

=> **Software Re-engineering** is the process of analyzing and modifying existing software to improve its maintainability, performance, structure, or functionality.

=> It is mainly used for legacy systems.

### Need

1. Old software is difficult to maintain.
2. Documentation is missing.
3. Code structure is poor.
4. Technology is outdated.
5. Business still depends on old system.
6. Replacement from scratch is costly.

### Benefits

1. Improves maintainability.
2. Extends life of legacy software.
3. Reduces maintenance cost.
4. Improves performance and quality.
5. Preserves useful business logic.

## **8.4 Software Re-Engineering Process Model**

### Diagram

```text
Inventory Analysis
        |
        v
Document Restructuring
        |
        v
Reverse Engineering
        |
        v
Code Restructuring
        |
        v
Data Restructuring
        |
        v
Forward Engineering
```

### 1. Inventory Analysis

=> Identify existing applications and decide which systems need re-engineering.

### 2. Document Restructuring

=> Create, update, or improve documentation.

=> Useful when old documentation is missing or outdated.

### 3. Reverse Engineering

=> Analyze existing software to understand design, data, architecture, and behavior.

### 4. Code Restructuring

=> Improve code structure without changing external behavior.

=> Example: Remove duplicate code and improve modularity.

### 5. Data Restructuring

=> Improve database design, file structure, and data organization.

### 6. Forward Engineering

=> Build improved software using recovered information and new requirements.

## **8.5 Reverse Engineering**

=> **Reverse Engineering** is the process of analyzing an existing software system to understand its components, design, architecture, data, and behavior.

=> It moves backward from implementation to design or requirement understanding.

### Purpose

1. Understand legacy software.
2. Recover missing documentation.
3. Identify architecture.
4. Support maintenance.
5. Find reusable components.
6. Support re-engineering.

### Activities

1. Source code analysis.
2. Data structure analysis.
3. Control flow analysis.
4. Interface analysis.
5. Database analysis.
6. Documentation recovery.

### Example

=> If an old payroll system has no design document, reverse engineering studies source code and database tables to recreate design diagrams.

### Advantages

1. Helps maintain old systems.
2. Reduces dependency on original developers.
3. Improves understanding before modification.
4. Helps recover lost documentation.

## **8.6 Forward Engineering**

=> **Forward Engineering** is the process of developing software from requirements and design toward implementation.

=> It moves in the normal direction: requirements, design, coding, testing, and deployment.

### Purpose

1. Build a new system.
2. Convert recovered design into improved implementation.
3. Modernize legacy software.
4. Add new features using proper engineering process.

### Activities

1. Requirement specification.
2. Architecture and detailed design.
3. Coding.
4. Testing.
5. Deployment.

## **8.7 Reverse Engineering vs Forward Engineering**

| Reverse Engineering | Forward Engineering |
|---|---|
| Moves from code/system to design understanding. | Moves from requirements/design to implementation. |
| Used mainly for existing systems. | Used for new or improved systems. |
| May not modify software. | Produces working software. |
| Recovers documentation, design, and architecture. | Creates code, database, and executable product. |
| Example: Study old code to draw design diagram. | Example: Build new payroll system from SRS. |

=> In re-engineering, reverse engineering is often done first to understand old system, and forward engineering is then used to build improved system.

## **8.8 Software Configuration Management**

=> **Software Configuration Management (SCM)** is a set of activities used to identify, organize, control, and track changes in software work products.

=> SCM ensures that correct version of software, documents, code, test cases, and configuration files is available.

### Need

1. Software changes frequently.
2. Many developers work on same project.
3. Multiple versions and releases exist.
4. Change history must be traceable.
5. Unauthorized changes must be prevented.
6. Correct build must be delivered.

## **8.9 Software Configuration Items**

=> **Software Configuration Items (SCIs)** are work products controlled by SCM.

### Examples

1. SRS document.
2. Design document.
3. Source code.
4. Test cases.
5. Database scripts.
6. Build files.
7. User manual.
8. Configuration files.
9. Release notes.

## **8.10 SCM Process**

### Diagram

```text
Configuration Identification
          |
          v
Version Control
          |
          v
Change Control
          |
          v
Configuration Auditing
          |
          v
Status Accounting and Reporting
```

### 1. Configuration Identification

=> Identify and name software configuration items.

=> Define baselines and relationships between items.

### 2. Version Control

=> Manage different versions of software items.

=> Supports check-in, check-out, branching, merging, history, and rollback.

### 3. Change Control

=> Ensure requested changes are evaluated and approved before implementation.

### 4. Configuration Auditing

=> Check whether configuration items are complete, correct, and consistent.

### Types

1. **Functional audit**

=> Checks whether required functionality is implemented.

2. **Physical audit**

=> Checks whether all required files and documents are present.

### 5. Status Accounting

=> Records and reports current status of configuration items, versions, changes, and releases.

### Benefits

1. Prevents confusion due to multiple versions.
2. Supports team coordination.
3. Provides change traceability.
4. Improves release management.
5. Prevents unauthorized changes.
6. Reduces integration problems.

## **8.11 Baseline**

=> **Baseline** is an approved version of a software configuration item that can be changed only through formal change control.

### Examples

1. Approved SRS baseline.
2. Approved design baseline.
3. Tested release baseline.

### Importance

1. Provides stable reference point.
2. Supports version control.
3. Helps track approved changes.
4. Prevents uncontrolled modification.

## **8.12 Version Control**

=> **Version Control** is the process of managing different versions of software configuration items.

### Features

1. Maintains history of changes.
2. Supports check-in and check-out.
3. Supports branching and merging.
4. Allows rollback to old version.
5. Helps multiple developers work together.
6. Shows who changed what and when.

### Example

=> Git is a version control system used to manage source code history and branches.

### Benefits

1. Avoids overwriting changes.
2. Supports team collaboration.
3. Allows recovery from mistakes.
4. Helps release management.

## **8.13 Change Control**

=> **Change Control** is the process of managing requested changes in a controlled and approved way.

### Change control steps

```text
Submit change request
        |
        v
Impact analysis
        |
        v
Approve or reject
        |
        v
Implement approved change
        |
        v
Test and verify
        |
        v
Update baseline and documentation
```

### Change Control Board

=> **Change Control Board (CCB)** is a group responsible for reviewing, approving, or rejecting change requests.

### Impact analysis checks

1. Cost impact.
2. Schedule impact.
3. Quality impact.
4. Technical impact.
5. Risk impact.
6. Resource impact.

## **8.14 Version Control vs Change Control**

| Version Control | Change Control |
|---|---|
| Manages versions of files and products. | Manages approval and implementation of changes. |
| Focuses on history and revision tracking. | Focuses on decision and control process. |
| Supports branching, merging, rollback. | Supports change request, impact analysis, approval. |
| Example: Git branch. | Example: Approved change request. |

## **8.15 Configuration Audit**

=> **Configuration Audit** checks whether software configuration items are correct, complete, and consistent.

### Functional audit

=> Verifies that software performs required functions.

### Physical audit

=> Verifies that required files, documents, versions, and components are present.

### Benefits

1. Ensures correct release.
2. Finds missing documents or files.
3. Confirms approved changes.
4. Improves quality control.

## **8.16 Status Accounting**

=> **Status Accounting** records and reports information about configuration items and change activities.

### Includes

1. Current version of each item.
2. Approved changes.
3. Pending changes.
4. Implemented changes.
5. Fixed defects.
6. Release contents.

### Importance

1. Provides project visibility.
2. Supports audits.
3. Helps managers track changes.
4. Improves communication.

## **8.17 SCM Tools**

### Examples

1. Git.
2. GitHub.
3. GitLab.
4. Subversion.
5. Bitbucket.
6. Azure DevOps.

### Uses

1. Source code versioning.
2. Branching and merging.
3. Change tracking.
4. Release management.
5. Collaboration.

## **8.18 Exam Short Questions**

### 1. Define software maintenance.

=> Software maintenance is modifying software after delivery to correct faults, improve performance, adapt to changes, or add features.

### 2. List types of maintenance.

=> Corrective, adaptive, perfective, and preventive maintenance.

### 3. Define re-engineering.

=> Re-engineering is analyzing and modifying existing software to improve maintainability, quality, performance, or functionality.

### 4. Define reverse engineering.

=> Reverse engineering is analyzing existing software to understand its design, architecture, data, and behavior.

### 5. Define forward engineering.

=> Forward engineering is developing software from requirements and design toward implementation.

### 6. What is SCM?

=> SCM is a set of activities used to identify, control, and track changes in software work products.

### 7. What is SCI?

=> Software Configuration Item is a work product controlled by SCM, such as SRS, source code, or test case.

### 8. What is baseline?

=> Baseline is an approved version of a configuration item changed only through formal change control.

### 9. What is version control?

=> Version control manages different versions and history of software items.

### 10. What is change control?

=> Change control manages requested changes through impact analysis, approval, implementation, and verification.

### 11. What is configuration audit?

=> Configuration audit checks whether configuration items are complete, correct, and consistent.

### 12. What is CCB?

=> Change Control Board is a group that approves or rejects change requests.
