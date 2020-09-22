"""
模拟点击

模拟滑动

截图
"""
import os
import time


def screen(file_path=None, device=''):
    if file_path is None:
        file_path = os.getcwd() + "/src/image/current.png"
    command = f'adb {device} exec-out screencap -p > {file_path}'
    os.system(command)


def tap(x, y, device=''):
    command = f'adb shell {device} input tap {x} {y}'
    # print(command)
    os.system(command)


def device_size(device=''):
    command = 'adb shell wm size'
    return os.popen(command).read().strip().split(':')[1].strip().split('x')


def swip_pos(device=''):
    screen_size = device_size(device)
    x = int(screen_size[0]) / 10 * 5
    y1 = int(screen_size[1]) / 8 * 2
    y2 = int(screen_size[1]) / 8 * 6
    return (x, y1), (x, y2)


def swip_up(device=''):
    (x2, y2), (x1, y1) = swip_pos()
    command = f'adb shell input swipe {x1} {y1} {x2} {y2}'
    os.system(command)


def swip_down(device='', time_sleep=1):
    (x1, y1), (x2, y2) = swip_pos()
    command = f'adb shell input swipe {x1} {y1} {x2} {y2}'
    os.system(command)
    time.sleep(time_sleep)


def back_off(sleep_time=1):
    command = f'adb shell input keyevent 4'
    os.system(command)
    time.sleep(sleep_time)
