import sqlite3
from datetime import datetime


DATABASE = "patients.db"



# Database Connection

def get_connection():

    return sqlite3.connect(
        DATABASE,
        check_same_thread=False
    )




# Create Tables

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()



    # Patient Table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        age INTEGER,

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



    # Default Admin

    cursor.execute("""
    INSERT OR IGNORE INTO admin
    (username,password)

    VALUES(?,?)

    """,
    (
        "admin",
        "admin123"
    ))



    conn.commit()
    conn.close()





# Register Patient

def register_patient(
        full_name,
        age,
        phone,
        email,
        password
):

    conn = get_connection()
    cursor = conn.cursor()


    try:

        cursor.execute("""
        INSERT INTO patients
        (
        full_name,
        age,
        phone,
        email,
        password,
        registration_date
        )

        VALUES(?,?,?,?,?,?)

        """,
        (
            full_name,
            age,
            phone,
            email,
            password,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))


        conn.commit()

        return True



    except sqlite3.IntegrityError:

        return False



    finally:

        conn.close()






# Patient Login

def login_patient(email,password):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *
    FROM patients
    WHERE email=?

    """,
    (email,))


    user = cursor.fetchone()


    conn.close()


    if user:

        return user



    return None


# ---------------- RESET PASSWORD ----------------

def reset_password(email, new_password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients
    SET password=?
    WHERE email=?
    """,
    (
        new_password,
        email
    ))

    conn.commit()

    success = cursor.rowcount > 0

    conn.close()

    return success



# Admin Login

def admin_login(username,password):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *
    FROM admin

    WHERE username=?
    AND password=?

    """,
    (
        username,
        password
    ))


    admin = cursor.fetchone()


    conn.close()


    return admin





# Create Database

create_tables()