import sqlite3
from db import get_db
'''
This file is to execute the SQL 
'''
# -------------------
# Getting user information
# -------------------

def get_user_by_username(username):
    conn = get_db() # connect to database
    cur = conn.cursor() #for sql
    cur.execute("SELECT * FROM Users WHERE username = ?", (username,)) 
    return cur.fetchone() 

def create_user(username, password_hash):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Users (username, password_hash) VALUES (?, ?)
    """, (username, password_hash))

    user_id = cur.lastrowid
    cur.execute("""
        INSERT INTO Visitor_Info (user_id, name, phone, affiliation)
        VALUES (?, ?, ?, ?)
    """, (user_id, "", "", ""))

    conn.commit()
    return user_id

def get_admin_by_username(username):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Admins WHERE username = ?", (username,))
    return cur.fetchone()

# -------------------
# Visitors making or changing reservation
# -------------------

def create_reservation(user_id, date, time, location, purpose):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Reservations (user_id, visit_date, visit_time, location, purpose, status)
        VALUES (?, ?, ?, ?, ?, 'pending')
    """, (user_id, date, time, location, purpose))
    conn.commit()
    return cur.lastrowid

# for checking visitors' reservation history
def get_reservations_by_user(user_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Reservations
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (user_id,))
    return cur.fetchall()

# changing the reservation history, and change the states to pending 
def update_reservation(reservation_id, date, time, location, purpose):
    conn = get_db()
    cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE Reservations
            SET visit_date=?, visit_time=?, location=?, purpose=?, status='pending'
            WHERE reservation_id=?
        """, (date, time, location, purpose, reservation_id))
        conn.commit()
    except Exception as e:
        print(f"Database update failed: {e}")
        conn.rollback() 
        raise 
    finally:
        # close the connection to release lock
        if conn:
            conn.close()

# delete by reservation_id
def delete_reservation(reservation_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM Reservations WHERE reservation_id=?", (reservation_id,))
    conn.commit()
    if conn:
        conn.close()

def get_user_profile(user_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.user_id, u.username,
               v.name, v.phone, v.affiliation, v.updated_at
        FROM Users u
        LEFT JOIN Visitor_Info v ON u.user_id = v.user_id
        WHERE u.user_id = ?
    """, (user_id,))
    return cur.fetchone()


def update_user_profile(user_id, name, phone, affiliation):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Visitor_Info
        SET name = ?, phone = ?, affiliation = ?, updated_at = CURRENT_TIMESTAMP
        WHERE user_id = ?
    """, (name or "", phone or "", affiliation or "", user_id))
    conn.commit()
    return cur.rowcount

# -------------------
# Admin: see all reservations + approve or reject reservations + reports of reservations
# -------------------

def admin_get_all_reservations(status=None, date=None, location=None):
    conn = get_db()
    conn.row_factory = sqlite3.Row  # Ensure rows are returned as dict-like objects
    cur = conn.cursor()

    # Query now joins Reservations (r) and Users (u) to get the username.
    query = """
        SELECT r.*, u.username AS user 
        FROM Reservations r
        JOIN Users u ON r.user_id = u.user_id
        WHERE 1=1
    """
    params = []

    if status:
        query += " AND r.status=?"
        params.append(status)

    if date:
        query += " AND r.visit_date=?"
        params.append(date)

    if location:
        query += " AND r.location LIKE ?"
        params.append(f"%{location}%")

    query += " ORDER BY r.updated_at DESC"

    cur.execute(query, params)
    return cur.fetchall() # Returns list of rows, each row containing 'user' (username)


def admin_update_reservation_status(reservation_id, status, admin_id, comment):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Reservations 
        SET status=?, admin_id=?, review_comment=?, updated_at=CURRENT_TIMESTAMP
        WHERE reservation_id=?
    """, (status, admin_id, comment, reservation_id))
    conn.commit()

def get_pending_count():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Reservations WHERE status='pending'")
    return cur.fetchone()[0]

def get_admin_by_id(admin_id):
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # Adjust fields based on your actual database schema
    cur.execute("SELECT admin_id, username, email, phone FROM Admin_Info WHERE admin_id = ?", (admin_id,))
    return cur.fetchone()

def update_admin_info(admin_id, email, phone):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Admin_Info 
        SET email = ?, phone = ?
        WHERE admin_id = ?
    """, (email, phone, admin_id))
    conn.commit()
    return cur.rowcount

# -----------------------
# Today's Visitors Count
# -----------------------
def get_today_visitors_count():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT COUNT(*)
        FROM Reservations
        WHERE visit_date = DATE('now','localtime')
        AND status = 'approved'
    """)
    return cur.fetchone()[0]

def get_most_popular_location():
    conn = get_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""
        SELECT location, COUNT(*) AS total
        FROM Reservations
        WHERE visit_date = DATE('now','localtime')AND status='approved'
        GROUP BY location
        ORDER BY total DESC
        LIMIT 1 
    """)
    return cur.fetchone() 

# not yet used
def get_today_approved_visitors():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.username, r.visit_time, r.location
        FROM Reservations r
        JOIN Users u ON r.user_id = u.user_id
        WHERE r.visit_date = DATE('now','localtime')
        AND r.status = 'approved'
        ORDER BY r.visit_time
    """)
    return cur.fetchall()

def get_daily_report():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT location, COUNT(*) AS total
        FROM Reservations
        WHERE visit_date = DATE('now','localtime')AND status='approved'
        GROUP BY location
    """)
    return cur.fetchall()

def create_visitor_info(user_id, name, phone, affiliation):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Visitor_Info (user_id, name, phone, affiliation) VALUES (?, ?, ?, ?)
    """, (user_id, name or "", phone or "", affiliation or ""))
    conn.commit()
    return cur.lastrowid

