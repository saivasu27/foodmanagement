import MySQLdb
import pandas as pd

df = pd.read_csv("claims_data.csv")

conn = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="Admin@123",  # your working password if any
    database="food_management"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO claims (Claim_ID, Food_ID, Receiver_ID, Status, Timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            int(row['Claim_ID']),
            int(row['Food_ID']),
            int(row['Receiver_ID']),
            str(row['Status']),
            str(row['Timestamp'])
        ))
        print(f"✅ Inserted: {row.to_dict()}")
    except Exception as e:
        print(f"❌ Error on row {index+1}:", e)

conn.commit()
cursor.close()
conn.close()

print("🎉 claims_data.csv inserted successfully!")
