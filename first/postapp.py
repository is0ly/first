from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://ilya:rfnz2015@212.109.218.163/ilya"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).one()
        return jsonify(user.to_dict())
    except NoResultFound:
        return jsonify({"error": "User not found"}), 404


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    try:
        user = User(name=data["name"], email=data["email"], password=data["password"])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email address already exists"}), 400


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    try:
        user = User.query.filter_by(id=user_id).one()
        user.name = data["name"]
        user.email = data["email"]
        user.password = data["password"]
        db.session.commit()
        return jsonify(user.to_dict())
    except NoResultFound:
        return jsonify({"error": "User not found"}), 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).one()
        db.session.delete(user)
        db.session.commit()
        return "", 204
    except NoResultFound:
        return jsonify


# запуск приложения
if __name__ == "__main__":
    app.run(debug=True, port=5001)
