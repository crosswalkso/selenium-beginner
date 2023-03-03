import psycopg2

con = psycopg2.connect(
    user="crossp",
    host="127.0.0.1",
    port="5434",
    database="selenium_pr",
)

# --- test
print(con.closed)  # 0, connected
con.close()
print(con.closed)  # 1, disconnected
