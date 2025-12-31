import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import function_game as fg
import traceback
def jadong_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_2


    try:
        print("=== Arduino Leonardo Keyboard Test ===")

        QTest.qWait(300)

        # for ch in "abcdefghijklmnopqrstuvwxyz":
        #     fg.arduino_press(ch)
        #     QTest.qWait(60)

        # QTest.qWait(300)
        #
        # # 테스트 2) ALT+1
        # fg.arduino_key("ALT+1")
        # QTest.qWait(500)
        #
        # # 테스트 3) CTRL+C
        # fg.arduino_key("CTRL+C")
        # QTest.qWait(500)
        #
        # # 테스트 4) TEXT
        # fg.arduino_text(" hello_from_arduino ")
        # QTest.qWait(500)
        #
        # fg.arduino_press("a")
        #
        # fg.arduino_key("ALT+1")
        #
        # fg.arduino_key("CTRL+C")
        #
        # fg.arduino_text("hello")
        auto = True
        auto_count = 0
        print("auto ? ", auto)
        while auto is True:
            auto_count += 1
            if auto_count > 100:
                auto = False

            full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\jadong\\get_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 500, 1500, 900, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("target_1", imgs_)
                fg.arduino_press("f")
                QTest.qWait(100)

            full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\jadong\\e_skill_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 300, 1500, 900, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("target_1", imgs_)
                fg.arduino_press("e")
                QTest.qWait(100)

            full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\jadong\\target_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 1500, 200, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("target_1", imgs_)

                fg.arduino_click()
                QTest.qWait(100)
            else:
                print("no target_1", auto_count)
                for i in range(10):
                    full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\jadong\\target_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 30, 1500, 200, "one", img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("target_1", imgs_)
                        break
                    else:

                        fg.arduino_press("TAB")
                    time.sleep(1)
            QTest.qWait(50)
        print("=== Arduino test done ===")

    except Exception as e:
        traceback.print_exc()

# fg.arduino_keydown("W")          # W 꾹
# QTest.qWait(800)                 # 이동 유지 (0.8초)
# fg.arduino_mouseclick_left()     # 이동 중 좌클릭 1회
# QTest.qWait(300)
# fg.arduino_keyup("W")            # W 떼기
#
# fg.arduino_keydown("W")          # W 꾹
# QTest.qWait(800)                 # 이동 유지 (0.8초)
# fg.arduino_mouseclick_left()     # 이동 중 좌클릭 1회
# QTest.qWait(300)
# fg.arduino_keyup("W")            # W 떼기


def item_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg

    print("item_check")


    try:

        full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\check\\dead\\dead_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 500, 1000, 900, "one", img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("target_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

    except Exception as e:
        traceback.print_exc()