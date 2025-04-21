import psycopg2 as psg  

""""

-- Іздеу функциясы: Берілген үлгі бойынша өрістерінен іздейді
CREATE OR REPLACE FUNCTION search_phonebook(pattern VARCHAR)
RETURNS TABLE(id INT, first_name VARCHAR, surname VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE first_name ILIKE '%' || pattern || '%'
       OR surname ILIKE '%' || pattern || '%'
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;




-- Аты бойынша телефон жаңарту немесе егер табылмаса жаңа қолданушы қосу процедурасы
CREATE OR REPLACE PROCEDURE insert_element(name VARCHAR, new_phone VARCHAR) AS
$$
BEGIN
    UPDATE phonebook SET phone = new_phone WHERE first_name = name;
    IF NOT FOUND THEN
        INSERT INTO phonebook (first_name, surname,  phone)
        VALUES (name, 'a', new_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;



-- Тізімнен жаңа қолданушы қосатын процедура
CREATE OR REPLACE PROCEDURE insert_lst(name VARCHAR, surname VARCHAR, phone VARCHAR) AS
$$
BEGIN 
    INSERT INTO phonebook (first_name, surname, phone)
        VALUES (name, surname, phone);
END;
$$ LANGUAGE plpgsql;



-- Пагинация (шектеу және ығыстыру арқылы) сұраныс функциясы
CREATE OR REPLACE FUNCTION querys(a INT, b INT)
RETURNS TABLE(id int, first_name VARCHAR, surname VARCHAR, phone VARCHAR) AS
$$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name, phonebook.surname, phonebook.phone
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT a OFFSET b;
END;
$$ LANGUAGE plpgsql;



-- Аты бойынша өшіру, егер табылмаса телефон нөмірі бойынша өшіру процедурасы
CREATE OR REPLACE PROCEDURE delete_by(name VARCHAR, userphone VARCHAR) AS
$$
BEGIN 
    DELETE FROM phonebook
    WHERE first_name = name;
    IF NOT FOUND THEN
        DELETE FROM phonebook
        WHERE phonebook.phone = userphone;
    END IF;
END;
$$ LANGUAGE plpgsql;
"""


conn = psg.connect(host="localhost", dbname="postgres", user="postgres", password="21022012a", port=5432)

cur = conn.cursor()

# Дерекқорда phonebook кестесі жоқ болса, оны құру
cur.execute(""" CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,                     -- Бірегей ID автоматты түрде өседі
            first_name VARCHAR(50) NOT NULL,           -- Аты
            surname VARCHAR(50) NOT NULL,              -- Тегі
            phone VARCHAR(15) NOT NULL                 -- Телефон нөмірі
);
""")

# 1.Қолданушыдан ат пен телефон сұрау
print("\n--- Insert or Update User ---")
first_name = input("Enter first name: ")    # Қолданушыдан аты сұралады
phone = input("Enter phone number: ")       # Қолданушыдан телефон сұралады



# 2.Егер ат бар болса, телефон жаңартылады, болмаса жаңа жазба қосылады
cur.execute("CALL insert_element(%s, %s)", (first_name, phone)) # Процедураны шақыру
conn.commit()  # Өзгерістерді сақтау
print("User inserted or updated.")# Нәтижені шығару


# 3.Тізімнен бірнеше қолданушыны қосу
lst = [
    ["Alice", "Brown", "+1234567890"], # Қолданушылар тізімі
    ["Bob", "Smith", "+23582323457"],
    ["Eve", "White", "+2347867834"]
]
for user in lst: # Әр қолданушы үшін insert_lst процедурасын шақыру
    cur.execute("CALL insert_lst(%s, %s, %s)", (user[0], user[1], user[2]))
conn.commit() # Өзгерістерді сақтау



# 4. Пагинация функциясы — шектеу және ығыстыру бойынша мәліметтерді шығару
def pagin(limit, offset):
    cur.execute('SELECT * from querys(%s, %s)', (limit, offset))
    result = cur.fetchall() # Нәтижелерді алу
    for row in result:
        print(row) # Әр жолды шығару



# 5.Қолданушыны өшіру функциясы
def delete(name = None, phone = None):
    cur.execute("CALL delete_by(%s, %s)", (name, phone))  # delete_by процедурасын шақыру
delete(name="Madina")  # "Madina" деген атты қолданушыны өшіру
conn.commit()  # Өзгерістерді сақтау


cur.close()  # Курсорды жабу
conn.close()  # Дерекқормен байланысты жабу
