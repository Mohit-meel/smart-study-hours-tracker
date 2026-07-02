import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="study_tracker",
        user="postgres",
        password="501050@Mk"
    )
    return connection

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Connected to PostgreSQL successfully!")
        conn.close()
    except Exception as e:
        print("Error:", e)