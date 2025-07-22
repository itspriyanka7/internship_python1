from db_conn import get_connection

def drop_table():
    try:
        conn = get_connection()
        if conn is None:
            print("⚠️ Connection failed in drop_table()")
            return
        print("✅ Connection OK for drop_table()")
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS priya")
        conn.commit()
        print("🗑️ Table 'priya' dropped successfully.")
    except Exception as e:
        print(f"❌ Error dropping table: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
