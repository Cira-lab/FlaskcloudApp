from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Praise Jesus,this is Faith Ng'ang'a 😊"
if __name__ == " __main__":
    app.run(debug=True)
