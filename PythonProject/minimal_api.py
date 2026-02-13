from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory sample data
DATA = [
    {"id": 1, "name": "Alice", "role": "Student"},
    {"id": 2, "name": "Bob", "role": "Developer"}
]

# ------------------------
# /hello endpoint
# ------------------------
@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return jsonify({"message": "Welcome to the Flask API!"}), 200

    if request.method == "POST":
        data = request.get_json()
        name = data.get("name", "Guest")
        return jsonify({"message": f"Hello, {name}!"}), 201


# ------------------------
# /data endpoint
# ------------------------
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify(DATA), 200

    if request.method == "POST":
        new_item = request.get_json()
        new_item["id"] = len(DATA) + 1
        DATA.append(new_item)
        return jsonify(new_item), 201


if __name__ == "__main__":
    app.run(debug=True)
