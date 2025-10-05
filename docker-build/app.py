# app.py
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
# client = MongoClient("mongodb://root:example@mongo:27017/")
client = MongoClient("mongodb://root:example@mongodb:27017/")

db = client["test"]
orders_collection = db["orders"]

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    # Insert the order into MongoDB
    """ 
        Insert the order into MongoDB
        for example: '{"product": "Laptop", "price": 1200}'
        more stuff
    """
    result = orders_collection.insert_one({
        "product": data["product"],
        "price": data["price"]
    })
    return {"status": "ok", "id": str(result.inserted_id)}, 201

@app.route("/orders", methods=["GET"])
def list_orders():
    # Get all orders and convert ObjectId to string
    orders = list(orders_collection.find({}, {"_id": 1, "product": 1, "price": 1}))
    for order in orders:
        order["_id"] = str(order["_id"])
    return jsonify(orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
