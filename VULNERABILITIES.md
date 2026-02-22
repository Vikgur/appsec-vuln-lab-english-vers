# Description

This file contains the complete list of HIGH/CRITICAL vulnerabilities covered in this repository.  
The goal is to demonstrate knowledge of all major threat classes across different languages, frameworks, and contexts.

# Context

## Web / Backend

### Python / Flask

*One representative example per case*

1. **SQL Injection**  
2. **Command Injection**  
3. **NoSQL Injection**  
4. **Template Injection (SSTI)**  
5. **Path Traversal**  
6. **Insecure File Upload**  
7. **Unsafe Deserialization (pickle)**  
8. **Unsafe YAML Load**  
9. **Reflected XSS**  
10. **Stored XSS**  
11. **CSRF** (state-changing POST without protection)  
12. **Broken Authentication**  
    - session fixation  
    - missing session id rotation  
    - weak session id  
13. **JWT Validation Flaws**  
    - alg confusion  
    - missing exp / aud / iss validation  
14. **IDOR** (horizontal privilege escalation)  
15. **Vertical Privilege Escalation**  
    - role checked only in UI  
    - no backend enforcement  
16. **SSRF**  
    - access to internal services  
    - metadata endpoint exposure  
17. **Open Redirect**  
18. **Insecure Cryptography**  
    - MD5 / SHA1 for passwords  
    - missing salt  
    - weak randomness  
19. **Hardcoded Secret / Secret Leakage**  
    - secrets in code  
    - debug mode / verbose errors  
20. **Dependency Risk**  
    - unpinned versions  
    - unsafe library usage  
21. **Race Condition / TOCTOU**  
    - double spending  
    - check-then-use bug  
22. **Resource Exhaustion / DoS**  
    - uncontrolled upload  
    - regex catastrophic backtracking  
23. **CORS Misconfiguration**  
    - `Access-Control-Allow-Origin: *` with credentials  
    - dynamic origin reflection