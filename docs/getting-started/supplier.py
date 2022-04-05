import os
import pymongo
from pymongo import MongoClient
from flask import Flask, request, jsonify
from bson.json_util import dumps

import json

app = Flask(__name__)

@app.route('/supplier')
def supplier_data():
  print("=== Supplier  ==", flush=True)

  client = MongoClient(host='supplier_db', port=27017, username='root', password='pass', authSource="admin")
  db = client["supplier_db"]

  supplier = db.supplier_tb.find({"name": "Supplier"})
  supplier = list(supplier)
  supplier = dumps(supplier)
  print(supplier, flush=True)
  return supplier

@app.route('/start_supplier_agent')
def start_supplier_agent():
  os.system('jupyter nbconvert --to notebook --inplace --execute supplier.ipynb')
  return "Supplier ran successfully"
