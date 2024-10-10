from sqlalchemy import create_engine, MetaData, Table, insert
import os
import sql_manager


if __name__ is "__main__":
    weather_data = sql_manager.get_last_data()
    print(weather_data)