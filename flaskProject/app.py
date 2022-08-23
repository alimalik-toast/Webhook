import subprocess

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def respond():
    data = request.json
    status = data["Status"]
    if status == "Verify":
        subprocess.call("./verify.sh")
    else:
        subprocess.call("./ocs.sh")

    return make_response("Hello World 2")


if __name__ == '__main__':
    app.run()
