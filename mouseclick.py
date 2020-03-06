import win32gui

import os

import win32api

import time

import win32con

hwnd_title = dict()

WM_APPCOMMAND = 0x319


def click_px(pos):
    last_x, last_y = win32api.GetCursorPos()
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.SetCursorPos([last_x, last_y])


def click_px_r(pos):
    last_x, last_y = win32api.GetCursorPos()
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.SetCursorPos([last_x, last_y])


def main():
    print("""鼠标自动点击挂机
    
    使用方法：
      输入点击间隔的秒数，然后按下回车，将鼠标放到想要点击的位置即可。
    
      直接关闭程序窗口，即可停止自动点击。
    
    ！！！ 请不要在挂机时触动鼠标，建议把鼠标翻过来  ！！！
    
    """)
    sleep_time = int(input("请输入点击间隔的秒数，然后按下回车: "))

    ready_time = 10
    for si in range(ready_time):
        print("将在%s秒后开始，请将鼠标移到想点击的位置。" % str(ready_time - si))
        time.sleep(1)

    print("开始进程!\n===========================\n\n")

    last_i = 0
    while True:
        last_i += 1
        x, y = win32api.GetCursorPos()
        click_px([x, y])
        print("已经点击%d次" % last_i)
        time.sleep(sleep_time)


if __name__ == '__main__':
    while True:
        x, y = [1907, 461]
        click_px([x, y])
        time.sleep(3)

    # main()
