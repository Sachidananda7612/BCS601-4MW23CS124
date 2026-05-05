from flask import Flask, render_template, request

app = Flask(__name__)

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

@app.route("/", methods=["GET", "POST"])
def index():
    result = []

    if request.method == "POST":
        n = int(request.form["num"])
        result = fibonacci(n)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
