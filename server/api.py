from urllib import response
import mapDB
from flask import Flask, request, jsonify
from flask_cors import CORS
import main
import searchNew

app = Flask(__name__)

cors = CORS(app)
logIn = {"email": "IDF@gmail.com", "password": '1234'}


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if logIn["email"] == email and logIn["password"] == password:
        return logIn
    return "Not Found"


@app.route("/MoveRobut", methods=["POST"])
def MoveRobut():
    searchNew.start()
    print("הסריקה הסתימה בהצלחה😊")
    arr_data = [mapDB.walls, mapDB.mines, mapDB.abducted, mapDB.terrorists, mapDB.arrNumImg]
    return arr_data


if __name__ == "__main__":
    app.run()

