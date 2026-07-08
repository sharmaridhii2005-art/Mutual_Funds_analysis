import sqlite3

conn = sqlite3.connect("database/bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("=" * 40)
print("Tables in database")
print("=" * 40)

for table in tables:
    print(table[0])

conn.close()