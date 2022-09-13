import time

from flask import Flask, make_response
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

app = Flask(__name__)


def create_driver_session(session_id, executor_url):
    from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

    # Save the original function, so we can revert our patch
    org_command_execute = RemoteWebDriver.execute

    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return org_command_execute(self, command, params)

    # Patch the function before creating the driver object
    RemoteWebDriver.execute = new_command_execute

    new_driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    new_driver.session_id = session_id

    # Replace the patched function with original function
    RemoteWebDriver.execute = org_command_execute

    return new_driver


@app.route('/webhook', methods=['POST'])
def respond():
    link1 = "https://www.google.com"
    link2 = "https://www.youtube.com/"
    binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    options = Options()
    options.binary = binary
    driver = webdriver.Firefox(options=options, executable_path='C:\\Data\\Software\\geckodriver-v0.31.0'
                                                                '-win64\\geckodriver.exe')
    # driver.close()  # this prevents the dummy browser
    # url = driver.command_executor._url
    # session_id = driver.session_id
    # driver = webdriver.Remote(command_executor=url, desired_capabilities={})
    # driver.session_id = session_id
    # driver.get(link1)
    # time.sleep(5)
    # driver.get(link2)

    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get(link1)
    time.sleep(5)
    driver.get(link2)

    # print(request.json)
    # firefox = webbrowser.Mozilla('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    # "C:\Program Files\Mozilla Firefox\firefox.exe"
    # /usr/bin/firefox
    # firefox.open('www.dawn.com', new=0, autoraise=True)
    return make_response("Success")


if __name__ == '__main__':
    app.run()
