# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import schedule

from CheckModified import CheckModifiedFile
from ConfigManagement import ConfigManager

config = ConfigManager()
cm = CheckModifiedFile()

timeInMinutes = config.get_config('time_in_minutes')

while True:
    schedule.every(int(timeInMinutes)).minutes.do(cm.schedule_check)
    schedule.run_pending()
    time.sleep(1)

#
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('Matthew')
#
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
