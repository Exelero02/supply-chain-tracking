# Supply Chain Order Tracking Simulation

This project simulates a **supply chain order tracking system** that monitors customer orders, shipments, and deliveries.  
It demonstrates how to calculate **key performance indicators (KPIs)** such as on-time delivery percentage and late order analysis using SQL and Python.

---

## Features
- **Simulation** (`simulation.py`)  
  Generates synthetic customer orders with promised, shipped, and delivered dates. Random delays are introduced to simulate real-world scenarios.  

- **Analysis** (`analysis.py`)  
  Provides SQL-based KPI reports:
  - On-time delivery percentage
  - Top delayed orders (sorted by days late)

- **Testing** (`tests/`)  
  - Validates that KPI calculations are correct  
  - Ensures metrics stay within expected ranges  

---

## Tech Stack
- **Python 3.9+**
- **SQLite (via `sqlite3`)**
- **pytest** (optional, for automated testing)

---

## Quickstart
```bash
# 1. Navigate to the project folder
cd 03_supply_chain_order_tracking

# 2. Simulate orders and create database
python simulation.py

# 3. Run analysis reports
python analysis.py

# 4. (Optional) Run automated tests
pytest -q
```
