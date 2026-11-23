from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(service="ShopSphere Order API", version="1.2")

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/orders")
def orders():
    return jsonify(orders=[{"id": 101, "status": "shipped"}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
