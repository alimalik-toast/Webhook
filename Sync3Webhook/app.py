import subprocess

from flask import Flask, request, make_response

application = Flask(__name__)


@application.route('/webhook', methods=['POST'])
def respond():
    data = request.json
    status = data["state"]

    if status == "POS":
        subprocess.call("./verify.sh")
        return make_response("Success")

    elif status == "AI":
        subprocess.call("./ocs.sh")
        return make_response("Success")
    else:
        make_response("Failure")


if __name__ == '__main__':
    application.run(host='0.0.0.0')
