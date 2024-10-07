from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData, Table, insert
import datetime
import os

app = Flask(__name__)

# Database connection
engine = create_engine(os.environ['SQL_CONF'])
metadata = MetaData()
table_name = 'outdoor'
table = Table(table_name, metadata, autoload_with=engine, schema='public')

@app.route('/add_data', methods=['POST'])
def add_data():
    temp = request.json.get('temp')
    hum = request.json.get('hum')
    date = datetime.datetime.now()

    try:
        with engine.connect() as connection:
            insert_stmt = insert(table).values(temp=temp, hum=hum, date=date)
            connection.execute(insert_stmt)
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
