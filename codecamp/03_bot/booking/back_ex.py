import psycopg2


def back_ex(queries):
    con = psycopg2.connect(
        user="crossp",
        host="127.0.0.1",
        port="5434",
        database="selenium_pr",
    )

    cur = con.cursor()
    for query in queries:
        cur.execute(query)
    con.commit()
    cur.close()
    con.close()
