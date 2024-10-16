from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, insert
from discord_manager import send_message as discord_send_message
import datetime
import os
import asyncio  # Add this
from sql_manager import get_last_data
from reporter import get_report
import routine_tasks

app = Flask(__name__)

# Database connection
engine = create_engine(os.environ['SQL_CONF'])
metadata = MetaData()


@app.route('/add_data', methods=['POST'])
def add_data():
    table_name = request.json.get('table_name')
    temp = request.json.get('temp')
    hum = request.json.get('hum')
    print(table_name,temp,hum)

    if table_name is None or temp is None or hum is None:
        return jsonify({"error": "Missing table_name, temp or hum in the request"}), 400

    try:
        table = Table(table_name, metadata, autoload_with=engine, schema='public')

        with engine.connect() as connection:
            insert_stmt = insert(table).values(temp=temp, hum=hum)
            connection.execute(insert_stmt)
            connection.commit()

        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    silent_mode = request.json.get('silent_mode', False)  # Default to False if not provided

    # Run the async function inside the synchronous route
    asyncio.run(discord_send_message(message=message, silent=silent_mode))
    return jsonify({"status": "message sent"}), 200

# TEST THIS!!!
@app.route('/send_message', methods=['POST'])
def make_report():
    routine_tasks.get_post_last_data()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
