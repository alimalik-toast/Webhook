import subprocess

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def respond():
    data = request.json
    status = data["state"]

    if status == "AI":
        subprocess.call("./verify.sh")
        return make_response("Success")

    elif status == "POS":
        subprocess.call("./ocs.sh")
        return make_response("Success")
    else:
        make_response("Failure")


if __name__ == '__main__':
    app.run()
