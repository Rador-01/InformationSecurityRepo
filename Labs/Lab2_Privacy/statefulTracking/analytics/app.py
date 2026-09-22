from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
log = []

@app.route("/collect")
def collect():
    uid = request.args.get("uid")
    site = request.args.get("site")
    page = request.args.get("page")

    log.append((datetime.now().strftime("%H:%M:%S"), uid, site, page))

    print(f"\n--- PROFILE {uid} ---")
    for time, u, s, p in log:
        if u == uid:
            print(time, s, p)
    print("Cookies received:", dict(request.cookies))

    return "", 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9100, debug=True)