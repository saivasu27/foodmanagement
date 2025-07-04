import MySQLdb
import pandas as pd

# ✅ Load the CSV file
df = pd.read_csv("providers_data.csv")

# ✅ Connect to MySQL
conn = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="Admin@123",  # ← use your working password (empty string if no password)
    database="food_management"
)

cursor = conn.cursor()

# ✅ Insert data
for index, row in df.iterrows():
    try:
        query = """
            INSERT INTO providers (Provider_ID, Name, Type, Address, City, Contact)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            int(row['Provider_ID']),
            str(row['Name']),
            str(row['Type']),
            str(row['Address']),
            str(row['City']),
            str(row['Contact'])
        )
        cursor.execute(query, values)
        print(f"✅ Row inserted: {values}")
    except Exception as e:
        print(f"❌ Failed at row {index + 1}: {e}")

# ✅ Save and close
conn.commit()
cursor.close()
conn.close()

print("🎉 All done! Data inserted into 'providers'.")
