# **10 Advanced Topics in Software Engineering**

=> This chapter covers Component-Based Software Engineering, Client/Server Software Engineering, Web Engineering, Reengineering, CASE, Software Process Improvement, and emerging trends.

=> In exams, repeated questions are asked on **CASE building blocks**, **software process improvement**, **SPI framework**, **client/server software engineering**, **component-based development advantages/disadvantages**, and **reengineering**.

## **10.1 Component-Based Software Engineering**

=> **Component-Based Software Engineering (CBSE)** is a software development approach where software is built by integrating reusable software components.

=> A component is an independent, replaceable, and reusable software unit that provides specific functionality.

### Examples

1. Login component.
2. Payment gateway component.
3. Report generation component.
4. Authentication library.
5. UI component.

### CBSE process

```text
Identify requirements
        |
        v
Search reusable components
        |
        v
Evaluate components
        |
        v
Adapt components
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
3. Improves productivity.
4. Can improve reliability if components are tested.
5. Reduces cost.
6. Supports faster delivery.

### Disadvantages

1. Suitable components may not be available.
2. Integration problems may occur.
3. Component behavior may not fully match requirements.
4. Vendor dependency can occur.
5. Security and compatibility issues may appear.
6. Customization may be difficult.

## **10.2 Client/Server Software Engineering**

=> **Client/Server Software Engineering** is the development of software systems where processing is divided between client machines and server machines.

=> Client requests services and server provides services.

### Components

1. **Client**

=> Provides user interface and sends requests to server.

2. **Server**

=> Processes requests, manages data, and sends responses.

3. **Network**

=> Connects clients and servers.

### Diagram

```text
Client 1 ----\
Client 2 -----+---- Network ---- Server ---- Database
Client 3 ----/
```

### Example

=> In online banking, browser/mobile app is client, application server processes requests, and database server stores account data.

### Advantages

1. Centralized data management.
2. Easy resource sharing.
3. Better scalability.
4. Supports distributed users.
5. Easier maintenance at server side.

### Disadvantages

1. Network dependency.
2. Server failure affects clients.
3. Security must be managed carefully.
4. Server may become bottleneck.

## **10.3 Web Engineering**

=> **Web Engineering** is the application of software engineering principles to the development of web applications.

=> It focuses on web-specific issues such as content, navigation, usability, performance, security, compatibility, and continuous evolution.

### Characteristics of WebApps

1. Network intensive.
2. Content driven.
3. Continuously evolving.
4. User interface focused.
5. Security-sensitive.
6. Supports many users.
7. Must work across browsers and devices.

### Web engineering activities

1. Requirement analysis.
2. Content design.
3. Architecture design.
4. Navigation design.
5. User interface design.
6. Component design.
7. Testing.
8. Deployment and maintenance.

### WebApp testing areas

1. Content testing.
2. Interface testing.
3. Navigation testing.
4. Functionality testing.
5. Compatibility testing.
6. Performance testing.
7. Security testing.
8. Usability testing.

## **10.4 Reengineering**

=> **Reengineering** is the process of examining and modifying an existing software system to improve its maintainability, structure, performance, or functionality.

=> It is often used for legacy systems that are still useful but difficult to maintain.

### Reengineering process

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

### Activities

1. Inventory analysis.
2. Document restructuring.
3. Reverse engineering.
4. Code restructuring.
5. Data restructuring.
6. Forward engineering.

### Benefits

1. Improves maintainability.
2. Extends life of legacy systems.
3. Reduces maintenance cost.
4. Preserves business logic.
5. Improves performance and quality.

## **10.5 Computer-Aided Software Engineering**

=> **CASE** stands for **Computer-Aided Software Engineering**.

=> CASE tools provide automated or semi-automated support for software engineering activities such as analysis, design, coding, testing, documentation, and project management.

### Need of CASE

1. Improve productivity.
2. Reduce manual effort.
3. Improve documentation.
4. Maintain consistency.
5. Support large projects.
6. Improve quality and standardization.

## **10.6 CASE Building Blocks**

### Diagram

```text
CASE Environment
      |
Workbenches
      |
Tools
      |
Repository
      |
Integration Framework
```

### 1. CASE Tools

=> Individual tools support specific software engineering tasks.

### Examples

1. Diagramming tool.
2. Code generator.
3. Testing tool.
4. Documentation tool.
5. Project planning tool.

### 2. Workbenches

=> A workbench is a collection of tools that supports one phase or activity area.

### Examples

1. Analysis workbench.
2. Design workbench.
3. Testing workbench.

### 3. CASE Environment

=> CASE environment is an integrated collection of tools and workbenches that supports the complete SDLC.

### 4. Repository

=> Repository is central storage for project information.

### Repository contains

1. Requirement models.
2. Design diagrams.
3. Data dictionary.
4. Source code.
5. Test cases.
6. Documentation.

### 5. Integration Framework

=> Integration framework allows different CASE tools to communicate and share data.

=> It provides common user interface, data integration, and control integration.

## **10.7 Types of CASE Tools**

### 1. Upper CASE Tools

=> Support early phases of SDLC such as planning, analysis, and design.

### Examples

1. Requirement modeling tool.
2. DFD tool.
3. ER diagram tool.
4. UML design tool.

### 2. Lower CASE Tools

=> Support later phases such as coding, testing, and maintenance.

### Examples

1. Code generator.
2. Debugger.
3. Testing tool.
4. Maintenance tool.

### 3. Integrated CASE Tools

=> Support multiple phases of SDLC in an integrated environment.

### Benefits of CASE

1. Faster development.
2. Better documentation.
3. Improved consistency.
4. Better project control.
5. Supports reuse.
6. Reduces errors.

### Limitations

1. Tools may be costly.
2. Training is required.
3. Tool integration may be difficult.
4. Overdependence on tools may occur.

## **10.8 Software Process Improvement**

=> **Software Process Improvement (SPI)** is a systematic approach to analyze, evaluate, and improve the software development process.

=> Its goal is to improve quality, productivity, predictability, cost control, and customer satisfaction.

### Need

1. Reduce defects.
2. Improve development speed.
3. Reduce rework and cost.
4. Make project outcomes predictable.
5. Improve customer satisfaction.
6. Improve process maturity.

## **10.9 SPI Framework**

### Elements

1. **Process assessment**

=> Study current software process and find weaknesses.

2. **Process analysis**

=> Analyze causes of defects, delays, rework, and inefficiency.

3. **Improvement goals**

=> Define measurable goals such as reducing defects or improving delivery time.

4. **Process redesign**

=> Modify activities, methods, standards, and responsibilities.

5. **Training**

=> Train team members to follow improved process.

6. **Tool support**

=> Use tools for project management, testing, version control, and automation.

7. **Measurement**

=> Collect metrics to check whether improvement is effective.

8. **Continuous improvement**

=> Repeat improvement cycle regularly.

### SPI cycle

```text
Assess current process
        |
        v
Identify weaknesses
        |
        v
Plan improvement
        |
        v
Implement improvement
        |
        v
Measure results
        |
        v
Continue improvement
```

### Benefits

1. Reduces defects.
2. Reduces rework.
3. Improves quality.
4. Improves productivity.
5. Improves project predictability.
6. Improves customer satisfaction.

## **10.10 SPI Models and Standards**

### Examples

1. CMM.
2. CMMI.
3. ISO 9000.
4. Six Sigma.
5. PSP and TSP.

### CMMI

=> **CMMI** stands for Capability Maturity Model Integration.

=> It helps organizations improve process maturity and performance.

## **10.11 Emerging Trends in Software Engineering**

### 1. Agile and DevOps

=> Faster delivery using iterative development, CI/CD, and automation.

### 2. Cloud Computing

=> Applications are developed and deployed on cloud platforms.

### 3. Artificial Intelligence in Software Engineering

=> AI helps in code generation, testing, defect prediction, and project estimation.

### 4. Microservices

=> Applications are divided into small independent services.

### 5. Low-Code and No-Code Development

=> Applications are built using visual tools with less manual coding.

### 6. DevSecOps

=> Security is integrated into DevOps pipeline.

### 7. Internet of Things Software

=> Software is built for connected devices and sensors.

### 8. Automated Testing

=> Test automation improves speed and reliability.

## **10.12 CASE vs Manual Development**

| CASE-Based Development | Manual Development |
|---|---|
| Uses automated tools. | Relies mostly on manual effort. |
| Faster documentation and modeling. | Documentation takes more time. |
| Improves consistency. | Consistency depends on individuals. |
| Tool cost and training required. | Less tool cost but more manual work. |
| Supports large projects better. | Difficult for large complex projects. |

## **10.13 CBSE vs Traditional Development**

| CBSE | Traditional Development |
|---|---|
| Builds software using reusable components. | Builds most parts from scratch. |
| Faster if components are available. | Usually takes more time. |
| Integration is important. | Coding is major activity. |
| Component mismatch may occur. | More control over custom code. |
| Promotes reuse. | Reuse may be limited. |

## **10.14 Exam Short Questions**

### 1. Define CBSE.

=> CBSE is a development approach where software is built by integrating reusable components.

### 2. Define client/server software engineering.

=> Client/server software engineering develops systems where clients request services and servers provide services.

### 3. Define Web Engineering.

=> Web engineering applies software engineering principles to develop web applications.

### 4. Define CASE.

=> CASE means Computer-Aided Software Engineering. It provides tool support for software engineering activities.

### 5. List CASE building blocks.

=> Tools, workbenches, environment, repository, and integration framework.

### 6. What is repository in CASE?

=> Repository is central storage for project information such as models, code, documents, and test cases.

### 7. What is Upper CASE tool?

=> Upper CASE tool supports early SDLC phases such as analysis and design.

### 8. What is Lower CASE tool?

=> Lower CASE tool supports later phases such as coding, testing, and maintenance.

### 9. Define SPI.

=> SPI is a systematic approach to analyze and improve software development process.

### 10. List SPI framework elements.

=> Process assessment, analysis, improvement goals, redesign, training, tool support, measurement, and continuous improvement.

### 11. Give two emerging trends.

=> DevOps and cloud computing.

### 12. Give two advantages of CASE.

=> Faster development and better documentation.

### 13. Give two disadvantages of CBSE.

=> Suitable components may not be available and integration problems may occur.
