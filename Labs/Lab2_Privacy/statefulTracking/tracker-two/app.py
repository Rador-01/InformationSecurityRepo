from flask import Flask, render_template, request, make_response
import secrets

app = Flask(__name__)
mapping = {}

@app.route("/sync")
def sync():
    uid = request.cookies.get("uid")
    is_new = uid is None
    if is_new:
        uid = secrets.token_hex(8)

    partner_id = request.args.get("partner_id")
    mapping[partner_id] = uid

    print(f"\n[TRACKER-TWO] my id: {uid}, partner id: {partner_id}")
    print("--- ID MAPPING TABLE ---")
    for a, b in mapping.items():
        print(f"tracker-one {a}  =  tracker-two {b}")

    response = make_response(render_template("sync.html"))
    if is_new:
        response.set_cookie("uid", uid, max_age=365*24*3600,
                            samesite="None", secure=True)
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9200, debug=True, ssl_context="adhoc")