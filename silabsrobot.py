from pywinauto.application import Application
from time import sleep
import pyautogui

def main():
    app = Application(backend="uia").start(r"D:\src\silicon-labs-desktop-app\dist\SiliconLabs-win32-x64\SiliconLabs.exe")

    app.window(title="silicon-labs-desktop-app").click_input(coords=(80, 80))
    sleep(1)
    app.window(title="silicon-labs-desktop-app").click_input(coords=(80, 530))
    sleep(4)
    app.window(title="silicon-labs-desktop-app").click_input(coords=(400, 530))
    sleep(2)
    app.window(title="silicon-labs-desktop-app").click_input(coords=(400, 530))
    sleep(2)
    pyautogui.typewrite("Hello, Python!")

if __name__ == "__main__":
    main()
