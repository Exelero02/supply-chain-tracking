import os, sqlite3, random, datetime as dt
DB = os.environ.get("DB_PATH","orders.sqlite")

SCHEMA = """
CREATE TABLE IF NOT EXISTS orders(
  order_id INTEGER PRIMARY KEY, customer TEXT,
  promised_date DATE, ship_date DATE, delivery_date DATE
);
"""

def init_db(conn): conn.executescript(SCHEMA)

def simulate(conn, n=100, start="2025-08-15"):
    rng = random.Random(42); start_date = dt.date.fromisoformat(start)
    cur = conn.cursor()
    for i in range(1, n+1):
        promised = start_date + dt.timedelta(days=rng.randint(1,10))
        ship = promised - dt.timedelta(days=rng.randint(1,3))
        delay = rng.choices([0,1,2,3,5],[0.6,0.2,0.1,0.08,0.02])[0]
        delivery = promised + dt.timedelta(days=delay)
        cur.execute("INSERT INTO orders VALUES(?,?,?,?,?)",
                    (i, f"Customer {rng.randint(1,5)}", promised.isoformat(), ship.isoformat(), delivery.isoformat()))
    conn.commit()

if __name__=="__main__":
    conn = sqlite3.connect(DB); init_db(conn); simulate(conn); print("Simulated 100 orders.")
