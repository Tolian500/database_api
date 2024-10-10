from sqlalchemy import create_engine, select, MetaData, Table, and_, desc
import os

engine = create_engine(os.environ['SQL_CONF'])
metadata = MetaData()


def get_last_data():
    tables = ['indoor', 'outdoor']
    results = {}
    for table_name in tables:
        table = Table(
            table_name,
            metadata,
            autoload_with=engine  # autoload_with is correct; autoload deprecated
        )

        # Modify the select statement to order by 'datetime' in descending order
        # and limit the result to 1
        stmt = select(
            table.columns.temp,  # assuming 'temp' is the correct column for temperature
            table.columns.hum  # assuming 'hum' is the correct column for humidity
        ).order_by(
            desc(table.columns.datetime)  # ordering by datetime descending
        ).limit(1)  # limiting the results to one

        # Execute the query
        with engine.connect() as connection:
            cur_results = connection.execute(stmt).fetchall()
            results[table_name] = cur_results[0]  # store results with table name as key

    return results