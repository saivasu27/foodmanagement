import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin123",  # Change if your password is different
        database="food_management"
    )
    print("✅ Connected to MySQL!")
except mysql.connector.Error as err:
    print("❌ Connection failed:", err)
    exit()

cursor = conn.cursor()

# Show existing tables
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
print("\n📋 Tables in 'food_management':")
for t in tables:
    print("-", t[0])

# Show number of rows in 'providers'
cursor.execute("SELECT COUNT(*) FROM providers;")
count = cursor.fetchone()[0]
print(f"\n📦 Rows in 'providers' table: {count}")

cursor.close()
conn.close()
