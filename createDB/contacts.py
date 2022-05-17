import sqlite3

# Create a connection to the DB
db = sqlite3.connect("contacts.sqlite")

# Create a table by passing a sqlite command
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES ('Kevin', 1234567, 'kevin@gmail.com')")
db.execute("INSERT INTO contacts VALUES ('Sally', 5678901, 'sally@gmail.com')")

# Create a cursor to query the DB
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# returns a list containing tuples
# print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()

# close the db connection
db.close()


