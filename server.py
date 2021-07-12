from flask import Flask, render_template
from helpers import generate_checkerboard
app = Flask(__name__)

@app.route('/')
def checkerboard_1():
    result = generate_checkerboard(8, 8)
    return render_template("checkerboard.html", result = result)

#adding int: to <int:times> is the same as line 12
@app.route('/<int:y>')
def checkerboard_2(y):
    result = generate_checkerboard(8, y)
    return render_template("checkerboard.html", result = result)

@app.route('/<int:x>/<int:y>')
def checkerboard_3(x, y):
    result = generate_checkerboard(x, y)
    return render_template("checkerboard.html", result = result)
    # times = int(times)
    # return render_template("index.html", times = times, color = color)

@app.route('/<int:x>/<int:y>/<color0>/<color1>')
def generate_colorboard(x, y, color0, color1):
    funkycolors = []

    for j in range (0, y):
        temp = []
        for i in range(0, x):
            temp.append((i + j) % 2)
        funkycolors.append(temp)
    return render_template("checkerboard.html", funkycolors = funkycolors, color0 = color0, color1 = color1)
    # times = int(times)

if __name__=="__main__":
    app.run(debug=True)