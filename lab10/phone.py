import psycopg2 as psg
import csv

# --------------------------- Database Setup --------------------------- #
def connect_db():
    return psg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="21022012a",
        port=5432
    )

def create_table(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            surname VARCHAR(50) NOT NULL,
            phone VARCHAR(15) NOT NULL
        );
    """)

# ------------------------- Insert Functions --------------------------- #
def insert_from_console(cur):
    first_name = input("First name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, surname, phone) VALUES (%s, %s, %s)",
        (first_name, surname, phone)
    )

def insert_from_csv(cur, file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row if any
        for row in csv_reader:
            if len(row) >= 2:
                cur.execute(
                    "INSERT INTO phonebook (first_name, surname, phone) VALUES (%s, %s, %s)",
                    (row[0], row[1], row[2] if len(row) > 2 else "")
                )

# ---------------------------- Update ---------------------------- #
def update_entry(cur):
    print("1. Update name\n2. Update phone")
    choice = input("Choose option (1/2): ")
    
    if choice == "1":
        old_name = input("Old name: ")
        new_name = input("New name: ")
        cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    elif choice == "2":
        name = input("Name to change phone for: ")
        new_phone = input("New phone: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))

# ---------------------------- Query ---------------------------- #
def query_data(cur):
    print("1. Filter by name\n2. Filter by phone")
    choice = input("Choose option (1/2): ")

    if choice == "1":
        name = input("Enter part of name: ")
        cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{name}%",))
    else:
        phone = input("Enter phone number: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

# ---------------------------- Delete ---------------------------- #
def delete_data(cur):
    print("1. Delete by name\n2. Delete by phone")
    choice = input("Choose option (1/2): ")
    
    if choice == "1":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    else:
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

# ---------------------------- Main Menu ---------------------------- #
def main():
    conn = connect_db()
    cur = conn.cursor()

    create_table(cur)

    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from console")
        print("2. Insert from CSV file")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            insert_from_console(cur)
        elif choice == "2":
            path = input("Enter CSV file path: ")
            insert_from_csv(cur, path)
        elif choice == "3":
            update_entry(cur)
        elif choice == "4":
            query_data(cur)
        elif choice == "5":
            delete_data(cur)
        elif choice == "6":
            break
        else:
            print("Invalid option.")

        conn.commit()

    cur.close()
    conn.close()
    conn.commit()
    
if __name__ == "__main__":
    main()
