from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Guest")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    return render_template("submit.html", username=username)

@app.route("/api/data")
def api_data():
    return jsonify({"message": "Hello from Flask API! 👋"})

if __name__ == "__main__":
    app.run(debug=True)