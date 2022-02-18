import datetime
import time
from win10toast_click import ToastNotifier

def water_reminder():
    toaster = ToastNotifier()
    toaster.show_toast(
        title='Remember to drink water :)',
        msg='This is your reminder to drink water!',
        duration=None,
        threaded=True,
        icon_path='C:\\Users\\madyf\\prog\\desktopNotif\\img\\water.ico'
        )
    time.sleep(60*60)