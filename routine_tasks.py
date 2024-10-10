from sqlalchemy import create_engine, MetaData, Table, insert
import os
import sql_manager
import reporter
from discord_manager import send_message as discord_send_message
import asyncio



def get_post_last_data():
    weather_data = sql_manager.get_last_data()
    report = reporter.get_report(*weather_data['indoor'])
    asyncio.run(discord_send_message(message=report, silent=True))




if __name__ == "__main__":
    get_post_last_data()
