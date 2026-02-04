from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

patients = []

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/api/patients", methods=["GET"])
def get_patients():
    return jsonify(patients), 200

@app.route("/api/patients", methods=["POST"])
def add_patient():
    data = request.get_json()
    patients.append(data)
    return jsonify({"message": "Patient registered"}), 201

@app.route("/api/patients/<int:pid>", methods=["GET"])
def get_patient(pid):
    for p in patients:
        if p["id"] == pid:
            return jsonify(p), 200
    return jsonify({"error": "Patient not found"}), 404

@app.route("/api/patients/<int:pid>", methods=["PUT"])
def update_patient(pid):
    data = request.get_json()
    for p in patients:
        if p["id"] == pid:
            p.update(data)
            return jsonify({"message": "Patient updated"}), 200
    return jsonify({"error": "Patient not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
