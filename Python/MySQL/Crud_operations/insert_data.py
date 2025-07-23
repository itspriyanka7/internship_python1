from db_conn import get_connection

def insert_data():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        query = "INSERT INTO priya (name, email, age) VALUES (%s, %s, %s)"
        data = [
            ("Priya", "priya@example.com", 22),
            ("Sneha", "snehaa@example.com", 25),
            ("Namrata", "namrata@example.com", 30)
        ]
        cursor.executemany(query, data)
        conn.commit()
        print("✅ Data inserted!")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
