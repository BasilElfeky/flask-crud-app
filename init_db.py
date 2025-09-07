import sqlite3

connection = sqlite3.connect('database.db')

with connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
    """)

print("Database initialized ✅")

