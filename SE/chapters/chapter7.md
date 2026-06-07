# **7 Quality Assurance and Management**

=> This chapter covers quality concepts, Software Quality Assurance, software reviews, Formal Technical Review, software reliability, software safety, ISO 9000, CMM, Six Sigma, and SQA plan.

=> In exams, repeated questions are asked on **SQA importance**, **SQA activities**, **FTR**, **software reliability metrics**, **software reliability vs safety**, **CMM levels**, **Six Sigma**, **quality standards**, and **SQA plan**.

## **7.1 Software Quality**

=> **Software quality** is the degree to which software satisfies stated and implied requirements, user expectations, and quality attributes.

### Quality attributes

1. Correctness.
2. Reliability.
3. Usability.
4. Efficiency.
5. Maintainability.
6. Portability.
7. Security.
8. Availability.

### Importance

1. Improves customer satisfaction.
2. Reduces defects.
3. Reduces maintenance cost.
4. Improves reliability.
5. Improves business reputation.
6. Supports long-term use.

## **7.2 Software Quality Assurance**

=> **Software Quality Assurance (SQA)** is a planned and systematic set of activities used to ensure that software process and product meet quality requirements.

=> SQA focuses on defect prevention, process improvement, and standards compliance.

### Importance of SQA

1. Prevents defects.
2. Ensures standards and procedures are followed.
3. Improves reliability and maintainability.
4. Reduces rework and maintenance cost.
5. Improves customer satisfaction.
6. Supports reviews, audits, testing, and metrics.

## **7.3 SQA Activities**

### Activities

1. Prepare SQA plan.
2. Define standards and procedures.
3. Conduct formal technical reviews.
4. Perform audits.
5. Monitor testing activities.
6. Collect and analyze quality metrics.
7. Report defects and non-compliance.
8. Ensure corrective actions.
9. Support process improvement.

### Formal Technical Review as SQA activity

=> FTR finds defects in requirements, design, code, and test cases before they become costly.

=> It improves quality and reduces rework.

## **7.4 SQA Plan**

=> **SQA Plan** is a formal document that describes quality assurance activities, responsibilities, standards, reviews, audits, and procedures for a software project.

### Objectives

1. Ensure software satisfies requirements.
2. Define quality standards.
3. Plan reviews and audits.
4. Assign quality responsibilities.
5. Improve defect prevention.

### Contents

1. **Purpose and scope**

=> Defines quality activities covered by the plan.

2. **Reference documents**

=> Lists SRS, standards, design documents, and procedures.

3. **Quality objectives**

=> Defines measurable quality goals.

4. **Reviews and audits**

=> Defines inspections, walkthroughs, FTRs, and audits.

5. **Testing strategy**

=> Defines test levels, responsibilities, and test documentation.

6. **Defect reporting**

=> Defines how defects are logged, tracked, corrected, and verified.

7. **Roles and responsibilities**

=> Assigns tasks to SQA team, developers, testers, and project manager.

8. **Tools and records**

=> Defines tools for testing, SCM, metrics, and reporting.

## **7.5 Software Reviews**

=> **Software review** is a quality activity in which people examine software work products to find defects and improve quality.

### Work products reviewed

1. SRS.
2. Design document.
3. Source code.
4. Test cases.
5. User manual.
6. Database design.

### Types

1. Informal review.
2. Walkthrough.
3. Inspection.
4. Formal Technical Review.

## **7.6 Formal Technical Review**

=> **Formal Technical Review (FTR)** is a structured review process used to find defects in software work products.

### Objectives

1. Find defects early.
2. Verify correctness and completeness.
3. Ensure standards are followed.
4. Improve software quality.
5. Reduce testing and maintenance cost.

### Participants

1. **Review leader**

=> Plans and controls the review meeting.

2. **Author**

=> Person who created the work product.

3. **Reviewers**

=> Technical people who inspect the work product.

4. **Recorder**

=> Records defects, decisions, and action items.

### FTR process

```text
Planning -> Preparation -> Review Meeting -> Defect Recording
        -> Rework -> Follow-up
```

### Steps

1. Review leader schedules meeting.
2. Author distributes material.
3. Reviewers study material individually.
4. Review meeting is conducted.
5. Defects are recorded.
6. Author corrects defects.
7. Review leader verifies corrections.

### Benefits

1. Detects defects before testing.
2. Improves team understanding.
3. Ensures compliance with standards.
4. Reduces rework cost.
5. Improves final software quality.

## **7.7 Software Reliability**

=> **Software reliability** is the probability that software will operate without failure for a specified time in a specified environment.

### Need

1. Critical systems require failure-free operation.
2. Reliability improves user trust.
3. Failures can cause financial loss.
4. Reliable software reduces maintenance cost.

## **7.8 Software Reliability Metrics**

### 1. MTTF - Mean Time To Failure

=> Average time software operates before a failure occurs.

```text
MTTF = Total operating time / Number of failures
```

### 2. MTTR - Mean Time To Repair

=> Average time required to repair software after failure.

```text
MTTR = Total repair time / Number of repairs
```

### 3. MTBF - Mean Time Between Failures

=> Average time between two consecutive failures.

```text
MTBF = MTTF + MTTR
```

### 4. POFOD - Probability of Failure on Demand

=> Probability that software fails when a service request is made.

=> Example: `0.001` means 1 failure in 1000 demands.

### 5. ROCOF - Rate of Occurrence of Failure

=> Frequency of failures in a given time period.

=> Example: 2 failures per 100 hours.

### 6. Availability

=> Percentage of time software is available for use.

```text
Availability = MTTF / (MTTF + MTTR)
```

## **7.9 Software Reliability vs Software Safety**

| Software Reliability | Software Safety |
|---|---|
| Probability of failure-free operation for specified time. | Ability to avoid conditions that cause harm or damage. |
| Focuses on correct continuous operation. | Focuses on preventing hazardous consequences. |
| Reliable system may still be unsafe in rare cases. | Safe system tries to avoid danger even if failure occurs. |
| Example: Banking app runs without crashing. | Example: Medical system prevents overdose. |

=> Reliability is about failure-free operation, while safety is about avoiding unacceptable risk.

## **7.10 Quality Standards**

### Common quality standards and models

1. ISO 9000.
2. ISO 9001.
3. CMM.
4. CMMI.
5. Six Sigma.
6. IEEE software engineering standards.

## **7.11 ISO 9000**

=> **ISO 9000** is a family of international quality management standards.

=> It helps organizations define and follow quality management processes.

### ISO 9001

=> ISO 9001 defines requirements for a quality management system.

### Main points

1. Customer focus.
2. Documented quality process.
3. Defined responsibilities.
4. Corrective and preventive actions.
5. Internal audits.
6. Continuous improvement.

### Benefits

1. Improves process discipline.
2. Increases customer confidence.
3. Reduces defects.
4. Supports consistent quality.

## **7.12 Capability Maturity Model**

=> **CMM** stands for **Capability Maturity Model**.

=> It is used to evaluate and improve maturity of an organization's software process.

### CMM levels diagram

```text
Level 5: Optimizing
Level 4: Managed
Level 3: Defined
Level 2: Repeatable
Level 1: Initial
```

### Level 1: Initial

=> Process is unpredictable, informal, and poorly controlled.

=> Success depends on individual effort.

### Level 2: Repeatable

=> Basic project management practices are established.

=> Cost, schedule, and requirements are tracked.

### Level 3: Defined

=> Standard software processes are documented and followed across the organization.

### Level 4: Managed

=> Processes are measured and controlled using quantitative metrics.

### Level 5: Optimizing

=> Organization focuses on continuous process improvement using feedback and innovation.

### Benefits

1. Improves process quality.
2. Reduces project risk.
3. Improves predictability.
4. Supports continuous improvement.
5. Helps assess process maturity.

## **7.13 Six Sigma**

=> **Six Sigma** is a quality improvement strategy used to reduce defects and process variation.

=> It aims for very low defect rate, approximately 3.4 defects per million opportunities.

### Six Sigma in SQA

1. Improves software process.
2. Reduces defects.
3. Uses data-based decision making.
4. Improves customer satisfaction.
5. Supports continuous improvement.

## **7.14 DMAIC**

=> DMAIC is used to improve an existing process.

| Step | Meaning |
|---|---|
| Define | Define problem, customer needs, and goals. |
| Measure | Measure current process performance. |
| Analyze | Find root causes of defects. |
| Improve | Apply solutions to remove causes. |
| Control | Monitor process to maintain improvement. |

## **7.15 DMADV**

=> DMADV is used to design a new process or product.

| Step | Meaning |
|---|---|
| Define | Define customer requirements and project goals. |
| Measure | Measure critical quality factors. |
| Analyze | Analyze design alternatives. |
| Design | Design improved process or product. |
| Verify | Verify that design satisfies requirements. |

## **7.16 SQA vs Testing**

| SQA | Testing |
|---|---|
| Process-oriented. | Product-oriented. |
| Focuses on defect prevention. | Focuses on defect detection. |
| Includes standards, reviews, audits, metrics. | Includes executing test cases. |
| Performed throughout lifecycle. | Mostly performed after coding stages. |

## **7.17 Exam Short Questions**

### 1. Define software quality.

=> Software quality is the degree to which software satisfies requirements and user expectations.

### 2. Define SQA.

=> SQA is a planned and systematic set of activities used to ensure software process and product quality.

### 3. List SQA activities.

=> SQA plan, standards, reviews, audits, testing monitoring, metrics, defect reporting, and corrective actions.

### 4. What is FTR?

=> FTR is a structured review used to find defects in software work products.

### 5. Define software reliability.

=> Software reliability is the probability of failure-free operation for specified time in specified environment.

### 6. What is MTBF?

=> MTBF is Mean Time Between Failures and equals MTTF + MTTR.

### 7. What is CMM?

=> CMM is a model used to evaluate and improve software process maturity.

### 8. List CMM levels.

=> Initial, Repeatable, Defined, Managed, and Optimizing.

### 9. What is Six Sigma?

=> Six Sigma is a quality improvement strategy used to reduce defects and process variation.

### 10. What is SQA plan?

=> SQA plan is a document describing quality assurance activities, standards, reviews, audits, and responsibilities.
