import os
from src.adbTools import screen, tap, swip_up, swip_down, back_off
from src.opencvImage import find_bao_xiang
import time
import random


def adb_check():
    if os.popen('adb devices').read().find('List of devices attached') == -1:
        exit("E: adb not fond")


def ad_close():
    # 关闭广告
    time_sp = 0
    while True:
        screen()
        res, pos, _ = find_bao_xiang('close_ad.png', 0.99)
        # 计时器
        # print('ad wathching', time_sp)
        if res:
            tap(pos[0], pos[1])
            time.sleep(3)
            break
        else:
            time_sp += 1
            time.sleep(1)


def click_bao_xiang_ad():
    # 看广告在赚金币
    screen()
    res, pos, _ = find_bao_xiang('bao_xiang_warch_ad.png')
    if not res:
        # print('not fond open bao xiang')
        return False
    # print(res, pos)
    tap(pos[0], pos[1])
    time.sleep(2)
    return True


def click_bao_xiang():
    # 找到宝箱
    screen()
    res, pos, max_val = find_bao_xiang('open_bao_xiang.png', 0.93)
    # print('bao xiang : ', max_val)
    if not res:
        # print('not fond open bao xiang ', max_val)
        return False
    # print(res, pos)
    tap(pos[0], pos[1])
    time.sleep(2)
    return True


def click_bao_xiang_enter():
    # 找到宝箱入口， 并进入
    screen()
    res, pos, max_val = find_bao_xiang('bao_xiang.png', 0.9)
    # print(max_val)
    if not res:
        # print('not fond bao xiang ru kou')
        # back_off()
        return False
    tap(pos[0], pos[1])
    time.sleep(2)
    return True


def job_click_treasure_box():
    # print(1)
    if random.randint(1, 5) != 2:
        return
    swip_up()
    swip_up()
    screen()
    res = click_bao_xiang_enter()
    if not res:
        return
    res = click_bao_xiang()
    if not res:
        # 如果宝箱打开时间未到， 后退一步
        back_off()
        return
    res = click_bao_xiang_ad()
    if not res:
        back_off()
        return
    ad_close()
    back_off()


def job_watch_video():
    tmp_num = random.randint(1, 8)
    if tmp_num == 2:
        swip_down()
    else:
        swip_up()
    time.sleep(random.randint(5, 7))


def click_time_limit_btn():
    # 找到宝箱
    screen()
    res, pos, max_value = find_bao_xiang('go_and_get.png', 0.97)
    # print(max_value)
    if not res:
        # print('not fond btn')
        return False
    # print(res, pos)
    tap(pos[0], pos[1])
    time.sleep(2)
    return True


def job_time_limit_job():
    if random.randint(1, 5) != 2:
        return
    res = click_bao_xiang_enter()
    if not res:
        return
    swip_down()
    swip_down()
    res = click_time_limit_btn()
    if not res:
        # print('not fond btn')
        back_off()
        return False
    ad_close()
    back_off()
    return True


def main():
    while True:
        job_watch_video()
        job_click_treasure_box()
        job_time_limit_job()


if __name__ == '__main__':
    main()
