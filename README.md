# Table of Contents

- [About](#about)  
- [Approach](#approach)
- [Content](#content)  
- [Navigation](#navigation)  
- [Usage](#usage)

---

# About  

This repository represents a practical AppSec integration model embedded into the SDLC.

Through real-world security cases, I:

- systematize vulnerabilities across languages, frameworks, and infrastructure  
- formalize exploitation patterns and remediation approaches  
- develop detection rules and DevSecOps tool configurations for automated control  
- implement security gates in CI/CD pipelines  
- reduce the risk of vulnerable code reaching production  

The goal is not to create a vulnerability catalog, but to build a reproducible security process — from risk identification to automated enforcement and regression prevention.

---

## Approach

The repository is built using a reproducible methodology:

1. Identify the attack surface of the language and selected context  
2. Build a consolidated pool of high/critical vulnerabilities  
3. Map vulnerabilities to specific frameworks  
4. Implement vulnerable code  
5. Demonstrate exploitation  
6. Analyze the root cause  
7. Implement the fix  
8. Add detection rules (DevSecOps tooling)  
9. Integrate the case into the shared security pipeline  
10. Implement automated regression checks  

---

# Content 

Each case includes:

- vulnerability class description and threat model  
- exploitation example  
- root cause analysis  
- remediation approach  
- SAST / DAST / dependency scanning rules  
- CI security gate configuration  
- prevention strategy to avoid recurrence  

This repository demonstrates a practical approach to:

- building AppSec controls  
- automating security validation  
- reducing pre-release vulnerability exposure  
- integrating security into development workflows without degrading delivery velocity  

It reflects an operational security model focused on measurable risk reduction and automated enforcement.

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