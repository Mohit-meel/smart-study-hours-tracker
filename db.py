import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="study_tracker",
        user="postgres",
        password="501050@Mk"
    )
    return connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS study_records(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        subject VARCHAR(100),
        hours FLOAT,
        date DATE
    )
    """)

    conn.commit()
    cur.close()
    conn.close()


def insert_record(name, subject, hours, date):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO study_records(name, subject, hours, date) VALUES (%s, %s, %s, %s)",
        (name, subject, hours, date)
    )

    conn.commit()
    cur.close()
    conn.close()


def view_records():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM study_records ORDER BY id")

    records = cur.fetchall()

    cur.close()
    conn.close()

    return records


def update_record(record_id, name, subject, hours, date):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE study_records
        SET name=%s,
            subject=%s,
            hours=%s,
            date=%s
        WHERE id=%s
    """, (name, subject, hours, date, record_id))

    conn.commit()
    cur.close()
    conn.close()


def delete_record(record_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM study_records WHERE id=%s",
        (record_id,)
    )

    conn.commit()
    cur.close()
    conn.close()


def search_record(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM study_records WHERE name=%s",
        (name,)
    )

    records = cur.fetchall()

    cur.close()
    conn.close()

    return records


def dashboard_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM study_records")
    total_records = cur.fetchone()[0]

    cur.execute("SELECT COALESCE(SUM(hours),0) FROM study_records")
    total_hours = cur.fetchone()[0]

    cur.execute("""
        SELECT subject, SUM(hours)
        FROM study_records
        GROUP BY subject
    """)

    subject_data = cur.fetchall()

    cur.close()
    conn.close()

    return total_records, total_hours, subject_data