# Table of Contents

- [Vulnerability](#vulnerability)  
- [Attack Surface](#attack-surface)  
- [Vulnerable Code](#vulnerable-code)  
- [Exploitation](#exploitation)  
- [Impact](#impact)  
- [Root Cause](#root-cause)  
- [Remediation](#remediation)  
- [Detection](#detection)  
- [DevSecOps Integration](#devsecops-integration)  
- [Regression Prevention](#regression-prevention)  
- [Developer Checklist](#developer-checklist)

---

# SQL Injection (CWE-89)

## Vulnerability

SQL Injection is a vulnerability that occurs when SQL queries are constructed through unsafe string concatenation with user input.

An attacker can inject their own SQL code into the application’s query, altering its logic and behavior.

Classification:

- OWASP Top-10: A03 – Injection  
- CWE: CWE-89 – Improper Neutralization of Special Elements used in an SQL Command

## Attack Surface

Common points of vulnerability:

- HTTP query parameters  
- form parameters (login / search)  
- filters and sorting  
- REST API parameters  
- any external data passed into SQL queries

## Vulnerable Code

In the vulnerable application version, SQL queries are built via direct string concatenation with user input.

Issues:

- user input is included in SQL without escaping  
- no prepared statements  
- query is not parameterized

This allows an attacker to alter the structure of the SQL query.

## Exploitation

The `exploit_payload.txt` file contains an example payload.

Example payload:

' OR 1=1 --

Result:

- the WHERE condition becomes true  
- the database returns all records  

Common exploitation techniques:

- authentication bypass  
- UNION-based extraction  
- boolean-based injection  

## Impact

Potential consequences:

- authentication bypass  
- reading data from the database  
- modification or deletion of data  
- disclosure of database structure  

In critical cases, the attack may escalate to:

- privilege escalation  
- remote command execution via DBMS functions

## Root Cause

Key engineering causes:

- unsafe string concatenation  
- lack of parameterized queries  
- absence of secure database APIs  
- insufficient user input validation

## Remediation

The proper security pattern is the use of parameterized queries.

Safe approaches:

- prepared statements  
- parameterized queries  
- ORM usage  
- strict input validation  

Core principle:

User input should never directly affect the structure of an SQL query.

## Detection

The vulnerability can be detected automatically.

SAST:

- static analysis rule detects unsafe SQL query construction  
- data flow from user input to SQL is analyzed  

DAST:

- automated scanning of HTTP endpoints  
- SQL payload injection  
- application behavior analysis  

## DevSecOps Integration

Automated checks are executed in the security pipeline.

Typical stages:

1. pre-commit checks  
2. SAST source code analysis  
3. security stage in CI/CD  
4. DAST scanning of the running application  

When a vulnerability is detected, the pipeline can block merges or releases.

## Regression Prevention

To prevent reintroduction of the vulnerability:

- add static analysis rules  
- implement security gates in CI/CD  
- perform regular application scanning  

This ensures any new attempt to add unsafe SQL is automatically detected.

## Developer Checklist

Practical developer recommendations are in the **CHECK_LIST.md** file.
