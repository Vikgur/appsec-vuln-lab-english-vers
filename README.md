# Table of Contents

- [About](#about)  
- [Content](#content)  
- [Navigation](#navigation)  
- [Usage](#usage)

---

# About

Repository for collecting all known vulnerabilities, their fixes, and DevSecOps tool configuration cases that help detect them.  

**Goal** — centralize vulnerability patterns across languages, development areas, and infrastructure to minimize the risk of vulnerable code reaching production.  

---

# Content

The repository will be gradually populated as real production cases and instructions from personal practice become available, forming a living encyclopedia of vulnerabilities, fixes, payloads, and DevSecOps tool configurations — a reference source for Senior AppSec/DevSecOps professionals.

---

# Navigation

From the root of the repository:

- `languages/` — examples of vulnerabilities by language and development area: **python**, **javascript**, **typescript**, **java**, **dotnet**, **c**, **cpp**, **erlang**, **go**, **rust**
  - Within each language: `web/`, `cli/`, `system/`, `mobile/`, `embedded/`
  - Each case contains:
    - `vuln_app.*` — vulnerable code  
    - `fixed_app.*` — patched version  
    - `exploit_payload.txt` — attack demonstration (if applicable)  
    - `README.md` — case description

- `infrastructure/` — vulnerability examples and best practices for Cloud, Orchestration, Containerization, IaC

- `devsecops/` — security tool configurations and examples: **sast**, **dast**, **fuzzing**, **secrets**, **sca**, **iac-scanning**, **ci-cd-pipelines**

---

# Usage

Navigate to the language and context of the case you want to explore, for example:  
[languages/python/web/flask/sql-injection-unparameterized-query](languages/python/web/flask/sql-injection-unparameterized-query)

Compare the vulnerable and patched code:  
[vuln_app.py](languages/python/web/flask/sql-injection-unparameterized-query/vuln_app.py) | [fixed_app.py](languages/python/web/flask/sql/flask/sql-injection-unparameterized-query/fixed_app.py)

Review the tool configurations for the case:  
[devsecops/sast/semgrep/python/sql-injection-unparameterized-query.yaml](devsecops/sast/semgrep/python/sql-injection-unparameterized-query.yaml)