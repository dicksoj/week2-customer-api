import psycopg2
from faker import Faker
import random, os, time

fake = Faker()

def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# Wait for DB to be ready
time.sleep(5)

conn = get_conn()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    city VARCHAR(100),
    age INT
);
""")

for _ in range(100):
    cur.execute(
        "INSERT INTO customers (first_name, last_name, email, city, age) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
        (
            fake.first_name(),
            fake.last_name(),
            fake.unique.email(),
            fake.city(),
            random.randint(18, 80)
        )
    )

conn.commit()
cur.close()
conn.close()
print("✅ Inserted 100 synthetic customers")

