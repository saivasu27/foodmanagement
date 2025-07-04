import MySQLdb
import pandas as pd

df = pd.read_csv("receivers_data.csv")

conn = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="Admin@123",  # use working password (blank if no password)
    database="food_management"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO receivers (Receiver_ID, Name, Type, City, Contact)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            int(row['Receiver_ID']),
            str(row['Name']),
            str(row['Type']),
            str(row['City']),
            str(row['Contact'])
        ))
        print(f"✅ Row inserted: {row.to_dict()}")
    except Exception as e:
        print(f"❌ Error on row {index+1}: {e}")

conn.commit()
cursor.close()
conn.close()

print("🎉 receivers_data.csv inserted!")
