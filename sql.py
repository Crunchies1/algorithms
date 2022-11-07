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