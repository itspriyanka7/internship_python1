from db_conn import get_connection
from mysql.connector import IntegrityError

def insert_data():
    try:
        conn = get_connection()
        if conn is None:
            return
        # ✅ Fix: Use buffered cursor
        cursor = conn.cursor(buffered=True)
        
        data = [
            ("Priya", "priya@example.com", 22),
            ("Sneha", "snehaa@example.com", 25),
            ("Namrata", "namrata@example.com", 28),
        ]
        for name, email, age in data:
            cursor.execute("SELECT * FROM priya WHERE email = %s", (email,))
            result = cursor.fetchone()
            if not result:
                cursor.execute("INSERT INTO priya (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
        
        conn.commit()
        print("✅ Data inserted (no duplicates)!")
    except IntegrityError as e:
        print(f"⚠️ Duplicate skipped: {e}")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
