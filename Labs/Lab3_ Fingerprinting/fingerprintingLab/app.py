from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print("\n========== NEW VISIT ==========")
    # Information about the request and network connection
    print("IP address        :", request.remote_addr)
    print("HTTP method       :", request.method)
    
    # Examples of passive HTTP features
    print("User-Agent        :", request.headers.get("User-Agent"))
    print("Accept-Language   :", request.headers.get("Accept-Language"))
    
    # additional passive features
    print("Accept            :", request.headers.get("Accept"))
    print("Accept-Encoding   :", request.headers.get("Accept-Encoding"))
    print("Sec-CH-UA         :", request.headers.get("Sec-CH-UA"))
    print("Sec-CH-UA-Platform:", request.headers.get("Sec-CH-UA-Platform"))
    print("Sec-Fetch-Dest    :", request.headers.get("Sec-Fetch-Dest"))
    print("================================\n")
    
    return render_template("index.html")


@app.route("/collect", methods=["POST"])
def collect():
    print("\nACTIVE FEATURES:")
    for name, value in request.get_json().items():
        print(f"{name:11}: {value}")
    return "OK"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)