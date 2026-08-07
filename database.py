import sqlite3


def get_connection():
    conn = sqlite3.connect("patients.db", check_same_thread=False)
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Patient Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        age INTEGER,
        gender TEXT,
        phone TEXT,
        email TEXT UNIQUE,
        password TEXT,
        address TEXT,
        registration_date TEXT
    )
    """)

    # Admin Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Insert default admin
    cursor.execute("""
    INSERT OR IGNORE INTO admin(username,password)
    VALUES('admin','admin123')
    """)

    conn.commit()
    conn.close()


create_tables()