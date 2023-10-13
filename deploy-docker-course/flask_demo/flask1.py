from flask import Flask, request

app = Flask(__name__) # declaring Flask app




@app.route("/", methods=["GET","POST"])
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    
    return str(int(a)+int(b))


# ML USAGE
def predict(house_size, house_beds):
    pass

app.run(port=7000)