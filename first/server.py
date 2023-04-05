from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"})


@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    if "numbers" not in data:
        return jsonify({"error": "No numbers provided"}), 400
    print(data)
    numbers = data["numbers"]
    result = sum(numbers)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)
