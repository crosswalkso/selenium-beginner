import psycopg2
from queries import *

con = psycopg2.connect(
    user="crossp",
    host="127.0.0.1",
    port="5434",
    database="selenium_pr",
)

cur = con.cursor()
query = read_all_query()
# create_row_query(
#     ["'Banana'", 5],
# )
cur.execute(query)
print(cur.fetchall())  # 읽어올때 사용
con.commit()
cur.close()
con.close()
