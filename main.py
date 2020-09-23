import os
from src.adbTools import screen, tap, swip_up, swip_down, back_off
from src.opencvImage import find_bao_xiang

import time
import random
from shutil import copyfile


def log_warning(img):
    """
    [INFO] [2020-12-02 12:32:12] [未找到] [实时截图: 3423432.png]
    """
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    tmp_png_name = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '.png'

    current_img_path = os.getcwd() + '/src/image/current.png'
    tmp_png_path = os.getcwd() + '/src/log/tmpImg/' + tmp_png_name

    copyfile(current_img_path, tmp_png_path)

    log_info_msg = f"[WARNING] [{now_time}] [{img} 未找到] [实时截图: {tmp_png_name}]"
    log_path = os.getcwd() + '/src/log/'
    log_file_name = time.strftime('%Y-%m-%d', time.localtime()) + '_log.log'
    with open(log_path + log_file_name, 'a') as f:
        f.write(log_info_msg + "\n")
        f.close()
    print(log_info_msg)


def log_info(img):
    """
    [INFO] [2020-12-02 12:32:12] [未找到] [实时截图: 3423432.png]
    """
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    tmp_png_name = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '.png'

    current_img_path = os.getcwd() + '/src/image/current.png'
    tmp_png_path = os.getcwd() + '/src/log/tmpImg/' + tmp_png_name

    copyfile(current_img_path, tmp_png_path)

    log_info_msg = f"[INFO] [{now_time}] [{img} 已经找到] [实时截图: {tmp_png_name}]"
    log_path = os.getcwd() + '/src/log/'
    log_file_name = time.strftime('%Y-%m-%d', time.localtime()) + '_log.log'
    with open(log_path + log_file_name, 'a') as f:
        f.write(log_info_msg + "\n")
        f.close()
    # print(log_info_msg)


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
            time.sleep(4)
            break
        else:
            time_sp += 1
            time.sleep(1)


def open_treasure_box():
    if get_probability(5):
        # swip_up()
        # swip_up()
        screen()
        res = find_img_and_click('bao_xiang.png', 0.9, 2)
        if not res:
            return
        res = find_img_and_click('open_bao_xiang.png', 0.93, 2)
        if not res:
            back_off()
            return
        res = find_img_and_click('bao_xiang_warch_ad.png', 0.8, 2)
        if not res:
            back_off()
            return
        ad_close()
        back_off()
        return


def find_img_and_click(img, similar, click_time_sleep):
    screen()
    res, pos, max_value = find_bao_xiang(img, similar)
    if not res:
        log_warning(img)
        return False
    log_info(img)
    tap(pos[0], pos[1])
    time.sleep(click_time_sleep)
    return True


def get_probability(num):
    # return True
    if random.randint(0, num) == 0:
        return True
    else:
        return False


def watch_video(time_sleep_min=5, time_sleep_max=7, probability=4):
    if get_probability(probability):
        swip_down()
    else:
        swip_up()
    time.sleep(random.randint(time_sleep_min, time_sleep_max))


def time_limit_job():
    if get_probability(5):
        res = find_img_and_click('bao_xiang.png', 0.9, 2)
        if res:
            swip_down()
            swip_down()
            res = find_img_and_click('go_and_get.png', 0.97, 2)
            if not res:
                # print('not fond btn')
                back_off()
                return
            ad_close()
            back_off()
            return


def main():
    while True:
        watch_video()
        open_treasure_box()
        time_limit_job()


if __name__ == '__main__':
    main()
