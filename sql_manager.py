from sqlalchemy import create_engine, select, MetaData, Table, and_, desc


def get_last_data(metadata: MetaData, engine: create_engine):
    tables = ['indoor', 'outdoor']
    results = {}
    for table_name in tables:
        print(table_name)
        table = Table(
            table_name,
            metadata,
            autoload_with=engine
        )

        # Modify the select statement to order by 'datetime' in descending order
        # and limit the result to 1
        stmt = select([
            table.columns.temp,  # assuming 'temp' is the correct column for temperature
            table.columns.hum  # assuming 'hum' is the correct column for humidity
        ]).order_by(
            desc(table.columns.datetime)  # ordering by datetime descending
        ).limit(1)  # limiting the results to one

        # Execute the query
        connection = engine.connect()
        cur_results = connection.execute(stmt).fetchall()
        results[table_name] = cur_results  # store results with table name as key

    return results
