import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

import function_game as fg
import traceback
from function_game import click_pos_reg, imgs_set_

def go_test_ex():
    import numpy as np
    import cv2

    print("test")
    cla = "one"

    # (기존 스타일 유지) cla에 따른 plus는 imgs_set_ 내부에서 처리하는 구조면 불필요하지만,
    # 사용자가 기존 로직을 유지하는 편이 안전해서 남겨둠.
    plus = 0
    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

def go_test_ex():
    import numpy as np
    import cv2

    print("test")
    cla = "one"

    # (기존 스타일 유지) cla에 따른 plus는 imgs_set_ 내부에서 처리하는 구조면 불필요하지만,
    # 사용자가 기존 로직을 유지하는 편이 안전해서 남겨둠.
    plus = 0
    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\check\\start\\aion2_start_btn.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(300, 500, 1920, 960, "one", img, 0.8)
    if imgs_ is not None and imgs_ != False:
        print("aion2_start_btn", imgs_)
        click_pos_reg(imgs_.x, imgs_.y, cla)

    try:
        print("=== Arduino Leonardo Keyboard Test ===")
        QTest.qWait(300)

        # 사람처럼 보이게 하는 '왕복' 스텝(제자리 복귀)
        stepper = fg.MicroStepper(
            max_drift_units=2,
            fwd_ms_range=(90, 130),
            back_ms_range=(90, 130),
            left_ms_range=(80, 120),
            right_ms_range=(80, 120),
            pause_ms_range=(60, 110),
            step_cooldown_ms=(1400, 2600),
            prefer_strafe=0.75,  # 좌우 위주
        )

        auto = True
        auto_count = 0

        # 전투 카운터(타겟 "신규 획득" 기준)
        combat_count = 0
        in_combat = False
        t_used_this_combat = False

        # e는 "이미지 활성화 + 타겟팅 20번당 1회"
        target_lock_count = 0

        print("auto ? ", auto)

        fight_count = 0  # 타겟 잡혀서 전투로 판단된 횟수
        skill3_every = 20

        skill7_every = 5
        skill8_every = 10

        try:

            while auto is True:
                auto_count += 1
                # if auto_count > 100:
                #     auto = False

                full_path = "c:\\my_games\\game_aion2\\data_basic\\imgs\\check\\dead\\dead_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 500, 1000, 900, "one", img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dead_click", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    auto = False
                    break


                # ------------------------------------------------------------
                # 1) 줍기 (get_1 표시가 있으면 f)
                # ------------------------------------------------------------
                full_path = r"c:\my_games\game_aion2\data_basic\imgs\jadong\get_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = fg.imgs_set_(900, 500, 1500, 900, cla, img, 0.8)
                if imgs_:
                    print("get_1", imgs_)
                    fg.arduino_press("f")
                    QTest.qWait(100)

                # ------------------------------------------------------------
                # 2) e 스킬 (이미지 활성화 시에만 가능)
                #    + 타겟팅 20번당 1회만 누르기
                # ------------------------------------------------------------

                full_path = r"c:\my_games\game_aion2\data_basic\imgs\jadong\e_skill_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                e_ready = fg.imgs_set_(900, 300, 1500, 900, cla, img, 0.8)

                # ------------------------------------------------------------
                # 3) 타겟 확인 (target_1이 뜨면 전투 중)
                # ------------------------------------------------------------
                full_path = r"c:\my_games\game_aion2\data_basic\imgs\jadong\target_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                target = fg.imgs_set_(700, 30, 1500, 200, cla, img, 0.8)

                if target:

                    # 전투 카운트 증가 (타겟이 잡힌 상태 = 전투 사이클로 간주)
                    fight_count += 1

                    # 20번 전투마다 3 스킬 1회
                    if fight_count % skill3_every == 0:
                        print("skill_3", fight_count)
                        fg.arduino_press("3")
                        QTest.qWait(90)

                    # 5번 전투마다 7 스킬 1회
                    if fight_count % skill7_every == 0:
                        print("skill_7", fight_count)
                        fg.arduino_press("7")
                        QTest.qWait(90)

                    # 10번 전투마다 8 스킬 1회
                    if fight_count % skill8_every == 0:
                        print("skill_8", fight_count)
                        fg.arduino_press("8")
                        QTest.qWait(90)

                    # 타겟 "신규 획득" 감지
                    if not in_combat:
                        in_combat = True
                        t_used_this_combat = False
                        combat_count += 1
                        target_lock_count += 1
                        print("target_lock", combat_count, target)

                    # 기본 공격은 r (게임이 사거리 안으로 자동 접근)
                    fg.arduino_press("r")
                    QTest.qWait(80)

                    # t: 전투당 1번만
                    if not t_used_this_combat:
                        fg.arduino_press("t")
                        t_used_this_combat = True
                        QTest.qWait(80)

                    # q: 전투 3번당 1번
                    if combat_count % 3 == 0:
                        fg.arduino_press("q")
                        QTest.qWait(80)

                    # e:
                    if e_ready:
                        print("e_skill_1", e_ready)
                        fg.arduino_press("e")
                        QTest.qWait(80)

                else:
                    if in_combat:
                        # 타겟이 끊긴 순간을 전투 종료로 봄
                        in_combat = False
                        t_used_this_combat = False

                    print("no target_1", auto_count)

                    # 타겟 탐색(10회 시도)
                    found = False
                    for _ in range(10):
                        # 다시 타겟 확인
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        target = fg.imgs_set_(700, 30, 1500, 200, cla, img, 0.8)
                        if target:
                            found = True
                            break

                        fg.arduino_press("TAB")
                        # '사람처럼 보이기' 스텝(왕복으로 제자리 복귀)
                        stepper.maybe_step()
                        QTest.qWait(1000)

                    if found:
                        print("target_found_after_tab", target)

                QTest.qWait(50)
        finally:
            # 프로그램이 예외로 죽거나 강제 종료되어도(가능한 범위에서) 해제 시도
            try:
                fg.arduino_panic()
            except Exception:
                pass
    except Exception:
        traceback.print_exc()


# fg.arduino_keydown("w")          # W 꾹
# QTest.qWait(800)                 # 이동 유지 (0.8초)
# fg.arduino_mouseclick_left()     # 이동 중 좌클릭 1회
# QTest.qWait(300)
# fg.arduino_keyup("w")            # W 떼기
#
# fg.arduino_keydown("w")          # W 꾹
# QTest.qWait(800)                 # 이동 유지 (0.8초)
# fg.arduino_mouseclick_left()     # 이동 중 좌클릭 1회
# QTest.qWait(300)
# fg.arduino_keyup("w")            # W 떼기


def dead_check():
    import numpy as np
    import cv2
    import pyautogui
    import random
    from function_game import imgs_set_, click_pos_reg

    print("dead_check")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

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