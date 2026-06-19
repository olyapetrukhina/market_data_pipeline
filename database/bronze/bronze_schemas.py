import sqlite3

BRONZE_PRICE_DATA = """
CREATE TABLE IF NOT EXISTS bronze_price_data(
id INTEGER PRIMARY KEY AUTOINCREMENT,
ticker_requested TEXT NOT NULL,
trade_date TEXT NOT NULL,
open_price REAL,
high_price REAL,
low_price REAL,
close_price REAL,
volume INTEGER,
adj_close REAL,
dividends REAL,
stock_splits REAL,
fetched_at TEXT NOT NULL,
pipeline_run_id TEXT NOT NULL,
period_requested TEXT NOT NULL,
interval_requested TEXT NOT NULL,
fetch_status TEXT NOT NULL,
source TEXT NOT NULL,

UNIQUE (
        ticker_requested,
        trade_date,
        source
    )
);
"""

def init_db(db_path: str) -> None:
    try:
        with sqlite3.connect(db_path) as conn:
            conn.execute("PRAGMA foreign_keys = ON;")
            conn.executescript(BRONZE_PRICE_DATA)

    except sqlite3.Error as error:
        print("Error occurred:", error)
        raise

if __name__ == '__main__':
    init_db('/Users/olgapetrukhina/market-data-pipeline/database/bronze/bronze_price_data.db')