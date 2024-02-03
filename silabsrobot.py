from pywinauto import application
from pywinauto.application import Application
from time import sleep
import pyautogui


class CustomLibrary:
    def __init__(self):
        self.app = None

    def open_application(self, app_path):
        #self.app = Application(backend="uia").start("D:\src\silicon-labs-desktop-app\dist\SiliconLabs-win32-x64\SiliconLabs.exe")
        #self.app = Application(backend="uia").start("D:\\src\\silicon-labs-desktop-app\\dist\\SiliconLabs-win32-x64\\SiliconLabs.exe")
        self.app = Application(backend="uia").start(r"D:\src\silicon-labs-desktop-app\dist\SiliconLabs-win32-x64\SiliconLabs.exe")

        self.app.window(title="silicon-labs-desktop-app").click_input(coords=(80, 80))
        sleep(1)
        self.app.window(title="silicon-labs-desktop-app").click_input(coords=(80, 530))
        sleep(4)
        self.app.window(title="silicon-labs-desktop-app").click_input(coords=(400, 530))
        sleep(2)
        self.app.window(title="silicon-labs-desktop-app").click_input(coords=(400, 530))
        sleep(2)
        pyautogui.typewrite("Hello, Python!")
