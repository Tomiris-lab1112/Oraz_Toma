import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Toma"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS snake2 (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20)
);
""")

conn.commit()

print("Таблица phonebook успешно создана!")

cur.close()
conn.close()