# Table of Contents

- [About the Project](#about-the-project)  
- [Approach](#approach)  
- [Navigation](#navigation)  
- [How to Use the Lab](#how-to-use-the-lab)

---

# About the Project

This repository demonstrates a practical model of integrating AppSec into the SDLC.

While working on real-world cases, I:

- systematize vulnerabilities by language, framework, and infrastructure  
- formalize exploitation patterns and remediation  
- analyze root causes of vulnerabilities and secure architectural patterns  
- define detection and prevention approaches that can be integrated into DevSecOps processes  
- reduce the risk of vulnerable code reaching production through secure development practices  

**Project Goal** — a vulnerability catalog with a reproducible security process: from risk identification to remediation and prevention of recurrence.

---

# Approach

The repository is populated following a reproducible methodology:

1. Define the attack surface of the language and chosen context  
2. Build a pool of high/critical vulnerabilities  
3. Map vulnerabilities to specific frameworks  
4. Implement vulnerable code  
5. Demonstrate exploitation  
6. Analyze root cause  
7. Implement correct remediation  
8. Formalize prevention recommendations  
9. Define automated detection rules  
10. Prepare regression prevention practices  

---

# Navigation

From the repository root:

1. `devsecops/` — practical examples of security tool configurations used to prevent vulnerability regression.

2. `infrastructure/` — vulnerabilities and best practices for cloud, containerization, orchestration, and IaC.

3. `languages/` — language-specific vulnerabilities and contexts.

Within each language, contexts include:

- `web`  
- `cli`  
- `system`  
- `mobile`  
- `embedded`  

Each case contains:

- `vuln_app.*` — vulnerable implementation  
- `fixed_app.*` — fixed version  
- `exploit_payload.txt` — exploitation example  
- `CHECK_LIST.md` — prevention recommendations  
- `README.md` — vulnerability analysis  

4. `README.md` — a brief guide on using the lab.

5. `VULNERABILITIES.md` — vulnerability catalog with descriptions and recommendations, organized by category.

---

# How to Use the Lab

**Example: SQL Injection in Python/Flask**

1. Navigate to the language and context of interest:  
[languages/python/web/flask/sql-injection-unparameterized-query](languages/python/web/flask/sql-injection-unparameterized-query)

2. Review the vulnerable implementation:  
[vuln_app.py](languages/python/web/flask/sql-injection-unparameterized-query/vuln_app.py)

3. Examine the exploitation example:  
[exploit_payload.txt](languages/python/web/flask/sql-injection-unparameterized-query/exploit_payload.txt)

4. Study the vulnerability analysis:  
[README.md](languages/python/web/flask/sql-injection-unparameterized-query/README.md)

5. Compare the vulnerable and fixed implementations:  
[vuln_app.py](languages/python/web/flask/sql-injection-unparameterized-query/vuln_app.py) | [fixed_app.py](languages/python/web/flask/sql-injection-unparameterized-query/fixed_app.py)

6. Review prevention recommendations in the checklist:  
[CHECK_LIST.md](languages/python/web/flask/sql-injection-unparameterized-query/CHECK_LIST.md)

7. Study and integrate the automated detection rule into CI/CD:  
[devsecops/sast/semgrep/python/flask/sql-injection-unparameterized-query.yaml](devsecops/sast/semgrep/python/flask/sql-injection-unparameterized-query.yaml)

The lab enables going through the full vulnerability analysis cycle:

**vulnerability → exploitation → analysis → remediation → prevention → automated detection**

# Final Recommendations for Using the Checklist: SQL Injection in Python/Flask

**For Audit:**

- Go through each checklist item, verifying the presence of SQL injection vulnerabilities in code and configuration  
- Use automated tools, such as SQLi detectors or Flask request analyzers  

**For Development:**

- Integrate checklist items into the development and CI/CD process: parameterized queries, ORM usage, input validation  
- Train the team on secure database practices and proper handling of user data  

**For Operations:**

- Regularly update dependencies (Flask, SQL drivers)  
- Monitor logs for suspicious database queries  

**For In-Depth Analysis:**

- Attempt SQL injection tests in a controlled test environment  
- Map findings to OWASP Top 10 for additional verification  
- Ensure the Semgrep configuration correctly detects vulnerabilities across different query variations
