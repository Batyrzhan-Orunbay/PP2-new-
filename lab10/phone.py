import psycopg2 as psg
import csv

conn = psg.connect(host="localhost", dbname="postgres", user="postgres", password="21022012a", port=5432)

cur = conn.cursor()

# Create Table
cur.execute(""" CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
);
""")

# Insert first name and phone number by terminal
first_name = input("first name: ")
phone = input("phone: ")

cur.execute(
    "INSERT INTO phonebook (first_name, surname, phone) VALUES (%s, %s, %s)",
    (first_name,"a", phone)
)


# Insert first name and phone by csv file
with open('c:/Users/BATYRZHAN/Desktop/python/PP2-new-/lab10/txt.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        cur.execute(
            "INSERT INTO phonebook (first_name, surname, phone) VALUES (%s, %s, %s)",
            (line[0], "a" , line[1])
        )

# Update Data
update = int(input("Update data? (1, 0) "))
if update:
    old_name = input("old name:")
    new_name = input("new name:")
    cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))


# Query Data with Filters
filt = int(input("filter by name or phone? (1, 0) "))

if filt:
    filter_name = input("filter by name: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{filter_name}%"))
else:
    filter_phone = input("filter by phone: ")
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (filter_phone,))
rows = cur.fetchall()
for row in rows:
    print(row)

# Delete From Table
delete = int(input("delete name or phone? (1, 0) "))

if delete:
    delete_name = input("name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (delete_name,))
else:
    delete_phone = input("phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

conn.commit()

cur.close()
conn.close()