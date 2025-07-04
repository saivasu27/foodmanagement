import MySQLdb

print("🔍 Connecting using mysqlclient (MySQLdb)...")

try:
    conn = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="Admin@123",  # change if needed
        database="food_management"
    )
    print("✅ Connected successfully!")

    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    for row in cursor.fetchall():
        print("📦", row[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ ERROR:", e)

print("✅ Done")
