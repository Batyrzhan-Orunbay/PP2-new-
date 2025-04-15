import psycopg2 as psg  # PostgreSQL-пен жұмыс істеу үшін кітапхана
import csv  # CSV файлмен жұмыс істеу үшін

# Дерекқормен қосылу
conn = psg.connect(
    host="localhost",dbname="postgres",user="postgres",password="21022012a",port=5432              )

cur = conn.cursor()  # Сұраныс жіберу үшін курсор аламыз

# PhoneBook кестесін жасау (бар болса - жасамайды)
cur.execute(""" 
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,           
        first_name VARCHAR(50) NOT NULL,  
        surname VARCHAR(50) NOT NULL,      
        phone VARCHAR(15) NOT NULL        
);
""")

first_name = input("first name: ")  # Қолданушыдан ат сұраймыз
phone = input("phone: ")            # Қолданушыдан телефон сұраймыз

cur.execute(
    "INSERT INTO phonebook (first_name, surname, phone) VALUES (%s, %s, %s)",
    (first_name, "a", phone)  # Тегін "a" деп қоямыз
)

#CSV файлы арқылы дерек қосу 
with open('c:\\Users\\BATYRZHAN\\Desktop\\python\\PP2-new-\\lab10\\txt.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)  # CSV оқимыз

    for line in csv_reader:
        # Әр жолды phonebook кестесіне қосамыз
        cur.execute(
            "INSERT INTO phonebook (first_name, surname, phone) VALUES (%s, %s, %s)",
            (line[0], "a", line[1])  # Тек аты мен телефонын аламыз
        )

#Жаңарту (Update)
update = int(input("Update data? (1, 0) "))  # Жаңарту керек пе?
if update:
    old_name = input("old name:")           # Қай атты ауыстыру керек
    new_name = input("new name:")           # Жаңа ат
    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE first_name = %s", 
        (new_name, old_name)
    )

# Сұрау (Query) фильтр арқыл
filt = int(input("filter by name or phone? (1, 0) "))  # 1 - ат, 0 - телефон
if filt:
    filter_name = input("filter by name: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s", 
        (f"%{filter_name}%",)  # Ішінде "filter_name" бар атаулар
    )
else:
    filter_phone = input("filter by phone: ")
    cur.execute(
        "SELECT * FROM phonebook WHERE phone = %s", 
        (filter_phone,)  # Толық телефон сәйкестігі
    )

rows = cur.fetchall() # Нәтижені шығару
for row in rows:
    print(row)

#Өшіру (Delete)
delete = int(input("delete name or phone? (1, 0) "))  # 1 - атпен, 0 - телефонмен өшіру
if delete:
    delete_name = input("name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (delete_name,))
else:
    delete_phone = input("phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

conn.commit() # ЖАСАЛҒАН ӨЗГЕРІСТЕРДІ САҚТАУ

cur.close()
conn.close()
