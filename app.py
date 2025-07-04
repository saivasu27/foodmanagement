import streamlit as st
import pandas as pd
import MySQLdb
from queries import (
    get_food_with_quantity_above_10,
    get_available_food_items,
    get_food_count_per_provider,
    get_claims_per_receiver,
    get_foods_expired,
    get_receivers_with_no_claims,
    get_food_count_by_location,
    get_average_quantity_by_food_type,
    get_top_5_most_claimed_foods,
    get_unclaimed_expired_foods,
    get_unexpired_food_with_quantity_gt_5,
    get_total_quantity_per_food_type,
    get_foods_claimed_multiple_times,
    get_unused_foods_by_location,
    get_provider_type_stats  # ✅ No comma here!
)


# Page config
st.set_page_config(page_title="Food Wastage Management", layout="wide")

st.title("🍱 Local Food Wastage Management System")

# Connect to MySQL
try:
    conn = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="Admin@123",  # use your actual MySQL password
        database="food_management"
    )
    cursor = conn.cursor()
    st.success("✅ Connected to MySQL database")
except Exception as e:
    st.error(f"❌ Could not connect: {e}")

# View Providers Table
if st.sidebar.button("Show Providers"):
    df = pd.read_sql("SELECT * FROM providers", conn)
    st.subheader("📋 Provider Details")
    st.dataframe(df)

# View Receivers Table
if st.sidebar.button("Show Receivers"):
    df = pd.read_sql("SELECT * FROM receivers", conn)
    st.subheader("🙋‍♀️ Receiver Details")
    st.dataframe(df)

# View Food Listings with Filters
if st.sidebar.button("Show Food Listings"):
    df = pd.read_sql("SELECT * FROM food_listings", conn)
    st.subheader("🍛 Available Food Listings")

    city_filter = st.selectbox("Filter by City", ["All"] + sorted(df["Location"].unique()))
    food_type_filter = st.selectbox("Filter by Food Type", ["All"] + sorted(df["Food_Type"].unique()))

    if city_filter != "All":
        df = df[df["Location"] == city_filter]
    if food_type_filter != "All":
        df = df[df["Food_Type"] == food_type_filter]

    st.dataframe(df)

# Show Claims
if st.sidebar.button("Show Claims"):
    df = pd.read_sql("SELECT * FROM claims", conn)
    st.subheader("📦 Food Claims Status")
    st.dataframe(df)

# Function to run SQL queries (add only once)
def run_query(query):
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = [i[0] for i in cursor.description]
    return pd.DataFrame(result, columns=columns)

st.markdown("---")
st.header("🔍 Data Insights (Query Based)")


# Question 1
if st.sidebar.button("Run Q1: Food Quantity > 10"):
    df = run_query(get_food_with_quantity_above_10())
    st.subheader("🍱 Question 1: Food items with Quantity > 10")
    st.dataframe(df)
# Question 2
if st.sidebar.button("Run Q2: Available Food Items (Not Claimed)"):
    df = run_query(get_available_food_items())
    st.subheader("✅ Question 2: Food Items Not Yet Claimed")
    st.dataframe(df)

# Question 3
if st.sidebar.button("Run Q3: Food Count per Provider"):
    df = run_query(get_food_count_per_provider())
    st.subheader("👨‍🍳 Question 3: Food Count by Each Provider")
    st.dataframe(df)

# Question 4
if st.sidebar.button("Run Q4: Claims per Receiver"):
    df = run_query(get_claims_per_receiver())
    st.subheader("🙋‍♀️ Question 4: Total Claims by Each Receiver")
    st.dataframe(df)

# Question 5
if st.sidebar.button("Run Q5: Expired Food Items"):
    df = run_query(get_foods_expired())
    st.subheader("⛔ Question 5: Expired Food Items")
    st.dataframe(df)

# Question 6
if st.sidebar.button("Run Q6: Receivers with No Claims"):
    df = run_query(get_receivers_with_no_claims())
    st.subheader("🙅 Question 6: Receivers with No Claims")
    st.dataframe(df)

# Question 7
if st.sidebar.button("Run Q7: Food Count by Location"):
    df = run_query(get_food_count_by_location())
    st.subheader("📍 Question 7: Food Count by Location")
    st.dataframe(df)

# Question 8
if st.sidebar.button("Run Q8: Average Quantity by Food Type"):
    df = run_query(get_average_quantity_by_food_type())
    st.subheader("📊 Question 8: Average Quantity by Food Type")
    st.dataframe(df)

# Question 9
if st.sidebar.button("Run Q9: Top 5 Most Claimed Foods"):
    df = run_query(get_top_5_most_claimed_foods())
    st.subheader("🏆 Question 9: Top 5 Most Claimed Foods")
    st.dataframe(df)

# Question 10
if st.sidebar.button("Run Q10: Unclaimed Expired Foods"):
    df = run_query(get_unclaimed_expired_foods())
    st.subheader("❌ Question 10: Expired & Unclaimed Food Items")
    st.dataframe(df)

# Question 11
if st.sidebar.button("Run Q11: Unexpired Foods (Qty > 5)"):
    df = run_query(get_unexpired_food_with_quantity_gt_5())
    st.subheader("✅ Question 11: Unexpired Foods with Quantity > 5")
    st.dataframe(df)

# Question 12
if st.sidebar.button("Run Q12: Total Quantity per Food Type"):
    df = run_query(get_total_quantity_per_food_type())
    st.subheader("🥗 Q12: Total Quantity per Food Type")
    st.dataframe(df)

# Question 13
if st.sidebar.button("Run Q13: Foods Claimed More Than Once"):
    df = run_query(get_foods_claimed_multiple_times())
    st.subheader("🔁 Q13: Foods Claimed Multiple Times")
    st.dataframe(df)

# Question 14
if st.sidebar.button("Run Q14: Unused Food by Location"):
    df = run_query(get_unused_foods_by_location())
    st.subheader("📍 Q14: Unclaimed Foods by Location")
    st.dataframe(df)

# Question 15
if st.sidebar.button("Run Q15: Provider Type Stats"):
    df = run_query(get_provider_type_stats())
    st.subheader("👤 Q15: Providers by Type")
    st.dataframe(df)
