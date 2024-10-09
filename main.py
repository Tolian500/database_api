from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, insert
import datetime
import os

app = Flask(__name__)

# Database connection
engine = create_engine(os.environ['SQL_CONF'])
metadata = MetaData()

@app.route('/add_data', methods=['POST'])
def add_data():
    table_name = request.json.get('table_name')
    temp = request.json.get('temp')
    hum = request.json.get('hum')

    if not table_name or not temp or not hum:
        return jsonify({"error": "Missing table_name, temp or hum in the request"}), 400

    # Load the table dynamically based on the request
    try:
        table = Table(table_name, metadata, autoload_with=engine, schema='public')

        with engine.connect() as connection:
            insert_stmt = insert(table).values(temp=temp, hum=hum)
            connection.execute(insert_stmt)
            connection.commit()

        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
