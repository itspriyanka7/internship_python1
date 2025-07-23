import mysql.connector
from db_config import db_config

def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("✅ Connection Successfully Established")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ Connection Failed: {err}")
        return None

# Optional: Close connection after testing
conn = get_connection()
if conn:
    conn.close()
    print("🔌 Connection Closed")
