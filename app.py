from flask import *
import pickle

f = open("re.model", "rb")
model = pickle.load(f)
f.close()

app = Flask(__name__)

@app.route("/")
def home():
    preci = request.args.get("preci")
    temp_max = request.args.get("temp_max")
    temp_min = request.args.get("temp_min")
    win = request.args.get("win")

    if preci and temp_max and temp_min and win:
        try:
            preci = float(preci)
            temp_max = float(temp_max)
            temp_min = float(temp_min)
            win = float(win)

            data = [[preci, temp_max, temp_min, win]]
            weather = model.predict(data)
            msg = "The Weather for today is " + str(weather[0]) + ". Have a nice day!"
        except ValueError:
            msg = "Invalid input. Please enter valid numbers."
    else:
        msg = ""

    return render_template("home.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
