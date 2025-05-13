import psycopg2
from itertools import product

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="lucky3-game",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Generate all combinations: 000 to 999 in "x-x-x" format
values = [f"{a}-{b}-{c}" for a, b, c in product(range(10), repeat=3)]

# Prepare data for batch insert
data = [(v,False) for v in values]

# Insert into Combinations table (assuming it has a `value` field)
insert_query = "INSERT INTO game_combination (value, is_deleted) VALUES (%s, %s)"
cur.executemany(insert_query, data)

conn.commit()
cur.close()
conn.close()

print(f"Inserted {len(data)} combinations into the database.")