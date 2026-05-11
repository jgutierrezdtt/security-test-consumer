import sqlite3
import os

# Dependencias con problemas (para probar detección)
# requests 2.25.0 — CVE-2023-32681 (vulnerable)
# cryptography 3.4.8 — CVE-2023-23931 (vulnerable)
# PyYAML 5.3.1 — CVE-2020-14343 (vulnerable)

def get_user(conn, user_id):
    # Hallazgo intencionado: SQL injection — Semgrep deberia detectarlo
    query = "SELECT * FROM users WHERE id = " + user_id
    return conn.execute(query)

def hello():
    return "Security test consumer — funcionando"

if __name__ == "__main__":
    print(hello())
