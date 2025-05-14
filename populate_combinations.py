import psycopg2
from itertools import product

# Connect to our DB, update connection appropriately
conn = psycopg2.connect(
    dbname="lucky3-game",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Use to generate all combinations: 0-0-0 to 9-9-9
values = [f"{a}-{b}-{c}" for a, b, c in product(range(10), repeat=3)]

# Use to generate all combinations: 0-0 to 9-9
# values = [f"{a}-{b}" for a, b in product(range(10), repeat=2)]

data = [(v,False) for v in values]

insert_query = "INSERT INTO game_combination (value, is_deleted) VALUES (%s, %s)"
cur.executemany(insert_query, data)

conn.commit()
cur.close()
conn.close()

print(f"Inserted {len(data)} combinations into the database.")