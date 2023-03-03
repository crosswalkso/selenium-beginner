table_name = "hotels_list"


def read_all_query():
    return f"SELECT * FROM {table_name}"


def create_row_query(data_list):
    queries = []
    for data in data_list:
        values_strings = ", ".join(map(str, data))
        query = f"""
            INSERT INTO {table_name}
            VALUES ({values_strings});
            """
        queries.append(query)
    return queries
