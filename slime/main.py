import pyautogui
import time


PICS_PATH = "./pics"


def find_click(img_name: str, conf: float, success_sleep: int, fail_retry: int, fail_sleep: int) -> bool:
    retry = 0
    while retry < fail_retry:
        try:
            pos = pyautogui.locateOnScreen(f'{PICS_PATH}/{img_name}', confidence=conf)
            break
        except:
            retry += 1
            time.sleep(fail_sleep)
    if retry == fail_retry:
        print(f"Cannot detect {img_name}")
        return 0
    pyautogui.click(pos)
    time.sleep(success_sleep)
    return 1


def move_click(x: int, y: int, sleep: int):
    pyautogui.moveTo(x, y, duration=1)
    pyautogui.click()
    time.sleep(sleep)


refill_times = 0
for i in range(20):
    print(f"iteration - {i}")
    find_click("ready_battle.png", 0.7, 1, 3, 1)
    find_click("start_battle.png", 0.7, 110, 3, 1)
    find_click("boss.png", 0.7, 3, 3, 1)
    find_click("role_chue.png", 0.7, 30, 10, 1)
    find_click("levelup.png", 0.7, 3, 3, 1)
    find_click("rebattle.png", 0.7, 8, 3, 1)
    
    r = find_click("bag_full.png", 0.7, 3, 3, 1)
    if r:
        find_click("skill_confirm.png", 0.7, 5, 3, 1)
        find_click("move_materials.png", 0.9, 5, 3, 1)
        find_click("auto_select.png", 0.9, 3, 3, 1)
        find_click("move_materials2.png", 0.9, 5, 3, 1)
        find_click("skill_confirm.png", 0.7, 5, 3, 1)
        find_click("skill_confirm.png", 0.7, 5, 3, 1)
        move_click(918, 921, 6)  # energy ring
        move_click(932, 470, 5)  # center tower
        find_click("ino_era.png", 0.7, 5, 3, 1)
        find_click("dark_level.png", 0.7, 5, 3, 1)
        move_click(930, 603, 5)  # 4-th level
        find_click("level-4.3.png", 0.7, 6, 3, 1)

    r = find_click("refill.png", 0.9, 6, 3, 1)
    if r:
        if refill_times == 0:
            break
        refill_times -= 1
        find_click("skill_confirm.png", 0.7, 3, 3, 1)
        find_click("filled.png", 0.7, 3, 3, 1)
        find_click("rebattle.png", 0.7, 8, 3, 1)

    r = find_click("empty_friend.png", 0.7, 10, 3, 1)
    if r:
        move_click(867, 184, 5)  # select_friend
        find_click("friend_confirm.png", 0.7, 6, 3, 1)
