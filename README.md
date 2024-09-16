# reward2sw

**Team Members:** Francisco Vieira, Pedro Silva

## Project Overview
The goal of this project was to develop an interface for analyzing salary revision scenarios and benefit allocations based on predefined criteria.

## Problem
In the past, evaluating salary revisions (e.g., annual increases) or benefit allocations (e.g., transport allowance for employees working in different locations) required manual filtering and updating of Excel files. This involved:
- Adding new columns with criteria (e.g., 5% salary increase)
- Calculating the impact and assessing budget alignment
- Repeating the process if results were not within budget

This manual approach was time-consuming and error-prone, particularly given the large workforce of over 1,000 employees.

## Objective
To streamline this process, we aimed to create an interface that:
- Uploads the latest employee data from an Excel file
- Applies defined criteria (e.g., 6% increase) and target groups (e.g., section heads)
- Generates an automated output for all eligible employees

The results needed to be exportable to Excel for integration with the company's ERP system (SAP).

## Outcome
We successfully developed a program that processes two Excel files:
- **Employee Database**
- **Salary Bands for Each Profession**

The program uses these files, along with specified criteria and target groups, to generate the following outputs:
- **HTML Page:** Displays the most relevant data.
- **Excel File:** Contains two sheets:
  - **Sheet 1:** An updated version of the original file with:
    - Red-marked lines for non-eligible employees
    - Yellow-marked lines for employees whose adjusted salaries would exceed the provided salary bands
    - Updated values for eligible employees
  - **Sheet 2:** A new sheet with co-workers set aside for future analysis.
