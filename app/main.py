from fastapi import FastAPI
import psycopg2, os

app = FastAPI()

def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.get("/customers")
def get_customers(city: str = None, min_age: int = None, max_age: int = None):
    conn = get_conn()
    cur = conn.cursor()

    query = "SELECT first_name, last_name, email, city, age FROM customers WHERE 1=1"
    params = []

    if city:
        query += " AND city = %s"
        params.append(city)

    if min_age:
        query += " AND age >= %s"
        params.append(min_age)

    if max_age:
        query += " AND age <= %s"
        params.append(max_age)

    cur.execute(query, tuple(params))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [
        {"first_name": r[0], "last_name": r[1], "email": r[2], "city": r[3], "age": r[4]}
        for r in rows
    ]

