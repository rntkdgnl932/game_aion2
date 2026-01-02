import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import function_game as fg
import traceback
from function_game import click_pos_reg, imgs_set_, click_pos_2

close_list = "c:\\my_games\\game_aion2\\data_basic\\imgs\\clean_screen\\close"
close_files = [
    f for f in os.listdir(close_list)
    if os.path.isfile(os.path.join(close_list, f))
]


def bag_clean_up_start(cla):
    import numpy as np
    import cv2
    from jadong import jadong_start
    print("bag_clean_up_start")

    try:
        opened = False
        opened_count = 0

        while opened is False:
            opened_count += 1
            if opened_count > 7:
                opened = True

            full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\action\\bag_open\\bag_opened.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 40, 1920, 1040, "one", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("bag_opened", imgs_)
                full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\action\\bag_open\\cube_in.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 40, 1920, 1040, "one", img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag_opened", imgs_)
                    click_pos_reg(1720, 1015, cla)
                else:
                    click_pos_reg(1835, 125, cla)
            QTest.qWait(1000)

    except Exception as e:
        traceback.print_exc()

def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_for
    print("out_check")

    try:
        out = False
        full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\check\\out\\camera.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 40, 300, 1040, "one", img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("camera", imgs_)
            out = True
            for i in range(len(close_files)):
                print("list => ", str(close_files[i]))
                full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\clean_screen\\close\\" + str(
                    close_files[i])

                # ✅ 1) 파일 존재 확인 (없으면 스킵)
                if not os.path.isfile(full_path):
                    print("[SKIP] file not found:", full_path)
                    continue

                # ✅ 2) fromfile 실패 방어
                try:
                    img_array = np.fromfile(full_path, np.uint8)
                except Exception as e:
                    print("[SKIP] np.fromfile error:", full_path, e)
                    continue

                # ✅ 3) 빈 파일/읽기 실패 방어
                if img_array is None or img_array.size == 0:
                    print("[SKIP] empty or unreadable:", full_path)
                    continue

                # ✅ 4) 디코딩 실패 방어 (img=None 방지)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                if img is None:
                    print("[SKIP] imdecode failed:", full_path)
                    continue

                imgs_for = imgs_set_for(0, 40, 1920, 1040, "one", img, 0.8)

                # ✅ 5) imgs_for가 None이면 len()에서 터지므로 순서만 바꿈(구조 유지)
                if imgs_for is not None and len(imgs_for) > 0:
                    print("close_files", str(close_files[i]), imgs_for)

                    out = False




        return out

    except Exception as e:
        traceback.print_exc()

