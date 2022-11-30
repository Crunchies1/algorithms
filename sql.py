'''
The below sql function is used to search through two tables, one of which contains profile data and the other
containing data on how each profile sold goods on certain dates. We search for the profiles who have
the 3 highest total sales by joining the two tables, grouping by profile data and summing sales. We also
limit the dates to be only in June. 
'''

sql = (
    "SELECT p.first_name, p.last_name, p.email, SUM(d.amount) AS total "
    "FROM profiles p JOIN data d ON p.id = d.profile_id "
    "WHERE CAST(d.date AS Date) > '2022-05-31' AND CAST(d.date AS Date) < '2022-07-01' "
    "GROUP BY p.first_name, p.last_name, p.email "
    "ORDER BY total DESC LIMIT 3;"
    )

'''
The below sql function is used to find the 3 cheapest flats for each city in a table of flats containing their id, 
city and price. We want to create a new table 
'''

sql = (
    "SELECT id, city, price "
    "FROM "
    "( SELECT id, city, price, "
    "        ROW_NUMBER() OVER (PARTITION BY name "
    "                            ORDER BY value ASC "
    "                            ) "
    "            AS rn "
    "    FROM flats "
    ") tmp "
    "WHERE rn <= 3 "
    "ORDER BY city; " 
)