import sqlite3, os
DB = os.environ.get("DB_PATH","orders.sqlite")

def on_time_percentage(conn):
    c = conn.cursor()
    c.execute("SELECT ROUND(100.0 * AVG(CASE WHEN delivery_date <= promised_date THEN 1.0 ELSE 0.0 END),2) FROM orders")
    return c.fetchone()[0]

def late_orders(conn):
    c = conn.cursor()
    c.execute("""SELECT order_id, customer, promised_date, delivery_date,
                        CAST((julianday(delivery_date)-julianday(promised_date)) AS INT) AS days_late
                 FROM orders WHERE delivery_date > promised_date
                 ORDER BY days_late DESC, order_id LIMIT 10""")
    return c.fetchall()

if __name__=="__main__":
    conn = sqlite3.connect(DB)
    print("On-time %:", on_time_percentage(conn))
    print("Late orders:", late_orders(conn))
