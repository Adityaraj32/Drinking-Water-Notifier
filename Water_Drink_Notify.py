'''
Author: Adityaraj Yadav 
Date: 17 January 2022
Project Name: Drinking Water Notifier
Purpose:For Practising Purpose
'''


import time
from plyer import notification

while True:
    notification.notify(
        title="Please Drink Water",
        message="""Here are some reasons our body needs water:
                1. It lubricates the joints
                2. It forms saliva and mucus""",
        app_icon = "D:\\A Pythonreal\\Drinking_Water.ico",
        timeout=10
    )
    time.sleep(60*60)
