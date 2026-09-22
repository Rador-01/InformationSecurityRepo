from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<page>")
def page(page="home"):
    return render_template("index.html", page=page)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8002, debug=True)