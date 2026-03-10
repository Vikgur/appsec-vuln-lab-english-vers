# Secure SQL Development Checklist

Checklist for developers before writing code that interacts with a database.

---

## 1. Never construct SQL via string concatenation

Do not include user input directly in SQL queries.

Bad example:  
`"SELECT * FROM users WHERE name = '" + user_input + "'"`

---

## 2. Always use parameterized queries

All dynamic SQL queries must use **prepared statements / parameter binding**.

Safe example:  
`SELECT * FROM users WHERE name = ?`

---

## 3. Prefer ORM or secure database APIs

If using an ORM:

- use standard ORM methods  
- avoid `raw SQL` and `execute` unless necessary  

If using SQL directly:

- apply only parameterized queries

---

## 4. Validate User Input

All data from HTTP requests should be treated as untrusted.

Minimum checks:

- enforce **string length limits**  
- validate **format** (email, UUID, date)  
- use **allowlists** for restricted values

Example:  
`status ∈ {active, inactive}`

---

## 5. Handle Dynamic SQL Parts Securely

Some SQL parts cannot be parameterized:

- `ORDER BY`  
- `LIMIT`  
- `OFFSET`  
- column names  
- table names

For these cases:

- use an **allowlist of permitted values**

---

## 6. Do Not Expose SQL Errors to Users

Users must not see:

- SQL query text  
- Database structure  
- Table names  
- Stack traces

Only show a generic error message.

---

## 7. Review SQL Code Before Commit

Before committing code, ensure:

- no SQL string concatenation  
- parameterized queries are used  
- input is validated  
- unsafe raw SQL is avoided
