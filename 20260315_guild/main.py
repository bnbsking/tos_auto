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


for _ in range(3):
    find_click("ready_battle.png", 0.7, 1, 10, 1)
    find_click("start_battle.png", 0.7, 22, 3, 1)
    find_click("role_jack.png", 0.7, 3, 10, 1)
    find_click("skill_jack1.png", 0.7, 3, 10, 1)
    find_click("skill_confirm.png", 0.7, 3, 3, 1)
    find_click("role_alai.png", 0.7, 3, 10, 1)
    find_click("skill_alai2.png", 0.7, 3, 10, 1)
    find_click("skill_confirm.png", 0.7, 3, 3, 1)
    find_click("role_terry.png", 0.7, 3, 10, 1)
    time.sleep(90)
    find_click("levelup.png", 0.7, 3, 3, 1)
    find_click("rebattle.png", 0.7, 8, 3, 1)
    r = find_click("refill.png", 0.9, 6, 3, 1)
    if r:
        find_click("skill_confirm.png", 0.7, 3, 3, 1)
        find_click("filled.png", 0.7, 3, 3, 1)
        find_click("rebattle.png", 0.7, 8, 3, 1)
