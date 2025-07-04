# queries.py

def get_food_with_quantity_above_10():
    return "SELECT * FROM food_listings WHERE Quantity > 10"

def get_available_food_items():
    return """
        SELECT * FROM food_listings
        WHERE Food_ID NOT IN (SELECT Food_ID FROM claims)
    """

def get_food_count_per_provider():
    return """
        SELECT p.Name AS Provider, COUNT(f.Food_ID) AS Food_Count
        FROM providers p
        JOIN food_listings f ON p.Provider_ID = f.Provider_ID
        GROUP BY p.Name
    """

def get_claims_per_receiver():
    return """
        SELECT r.Name AS Receiver, COUNT(c.Claim_ID) AS Total_Claims
        FROM receivers r
        JOIN claims c ON r.Receiver_ID = c.Receiver_ID
        GROUP BY r.Name
    """

# ✅ Q5 to Q10 (Final Fixed Version)

def get_foods_expired():
    return """
        SELECT f.Food_ID, f.Food_Name, f.Expiry_Date, f.Quantity, p.Name AS Provider_Name
        FROM food_listings f
        JOIN providers p ON f.Provider_ID = p.Provider_ID
        WHERE f.Expiry_Date < CURDATE()
    """

def get_receivers_with_no_claims():
    return """
        SELECT r.Name AS Receiver_Name, COUNT(c.Claim_ID) AS Total_Claims
        FROM receivers r
        LEFT JOIN claims c ON r.Receiver_ID = c.Receiver_ID
        GROUP BY r.Name
        HAVING Total_Claims = 0
    """

def get_food_count_by_location():
    return """
        SELECT Location, COUNT(*) AS Food_Count
        FROM food_listings
        GROUP BY Location
        ORDER BY Food_Count DESC
    """

def get_average_quantity_by_food_type():
    return """
        SELECT Food_Type, AVG(Quantity) AS Average_Quantity
        FROM food_listings
        GROUP BY Food_Type
    """

def get_top_5_most_claimed_foods():
    return """
        SELECT f.Food_Name, COUNT(c.Claim_ID) AS Total_Claims
        FROM claims c
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        GROUP BY f.Food_Name
        ORDER BY Total_Claims DESC
        LIMIT 5
    """

def get_unclaimed_expired_foods():
    return """
        SELECT f.Food_ID, f.Food_Name, f.Expiry_Date, f.Quantity, p.Name AS Provider_Name
        FROM food_listings f
        JOIN providers p ON f.Provider_ID = p.Provider_ID
        WHERE f.Expiry_Date < CURDATE()
          AND f.Food_ID NOT IN (SELECT Food_ID FROM claims)
    """

def get_unexpired_food_with_quantity_gt_5():
    return """
        SELECT Food_Name, Quantity, Expiry_Date
        FROM food_listings
        WHERE Quantity > 5 AND Expiry_Date >= CURDATE()
    """
# ✅ Q12
def get_total_quantity_per_food_type():
    return """
        SELECT Food_Type, SUM(Quantity) AS Total_Quantity
        FROM food_listings
        GROUP BY Food_Type
    """

# ✅ Q13
def get_foods_claimed_multiple_times():
    return """
        SELECT f.Food_Name, COUNT(c.Claim_ID) AS Claim_Count
        FROM claims c
        JOIN food_listings f ON c.Food_ID = f.Food_ID
        GROUP BY f.Food_Name
        HAVING Claim_Count > 1
    """

# ✅ Q14
def get_unused_foods_by_location():
    return """
        SELECT f.Location, COUNT(*) AS Unused_Food_Count
        FROM food_listings f
        LEFT JOIN claims c ON f.Food_ID = c.Food_ID
        WHERE c.Claim_ID IS NULL
        GROUP BY f.Location
    """

def get_provider_type_stats():
    return """
        SELECT Type AS Provider_Type, COUNT(*) AS Total_Providers
        FROM providers
        GROUP BY Type
    """
