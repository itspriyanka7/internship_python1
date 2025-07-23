from db_conn import get_connection

def delete_data():
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()

        # Delete all rows and reset ID
        cursor.execute("DELETE FROM priya")
        cursor.execute("ALTER TABLE priya AUTO_INCREMENT = 1")
        conn.commit()

        print("🗑️ Deleted all records and reset IDs.")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            print("🔌 Connection Closed")
