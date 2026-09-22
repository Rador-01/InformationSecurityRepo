from flask import Flask, render_template, request, make_response, redirect
from datetime import datetime
import secrets

app = Flask(__name__)
log = []

@app.route("/track")
def track():
    tid = request.cookies.get("tid")
    is_new = tid is None
    if is_new:
        tid = secrets.token_hex(8)

    log.append((datetime.now().strftime("%H:%M:%S"), tid,
                request.args.get("site"), request.args.get("page")))

    print(f"\n--- PROFILE {tid} ---")
    for time, t, site, page in log:
        if t == tid:
            print(time, site, page)

    response = make_response(render_template("tracker.html"))
    if is_new:
        response.set_cookie("tid", tid, max_age=365*24*3600,
                            samesite="None", secure=True)
    return response

@app.route("/sync")
def sync():
    tid = request.cookies.get("tid")
    is_new = tid is None
    if is_new:
        tid = secrets.token_hex(8)

    print(f"[TRACKER-ONE] my id is {tid}, redirecting to tracker-two")

    response = redirect(f"https://tracker-two.test:9200/sync?partner_id={tid}")
    if is_new:
        response.set_cookie("tid", tid, max_age=365*24*3600,
                            samesite="None", secure=True)
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True, ssl_context="adhoc")