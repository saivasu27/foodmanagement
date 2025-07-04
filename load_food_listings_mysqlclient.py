import MySQLdb
import pandas as pd

df = pd.read_csv("food_listings_data.csv")

conn = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="Admin@123",  # your working password
    database="food_management"
)

cursor = conn.cursor()

for index, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO food_listings (
                Food_ID, Food_Name, Quantity, Expiry_Date,
                Provider_ID, Provider_Type, Location, Food_Type, Meal_Type
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            int(row['Food_ID']),
            str(row['Food_Name']),
            int(row['Quantity']),
            str(row['Expiry_Date']),
            int(row['Provider_ID']),
            str(row['Provider_Type']),
            str(row['Location']),
            str(row['Food_Type']),
            str(row['Meal_Type'])
        ))
        print(f"✅ Inserted: {row.to_dict()}")
    except Exception as e:
        print(f"❌ Row {index+1} failed:", e)

conn.commit()
cursor.close()
conn.close()

print("🎉 food_listings_data.csv loaded!")
