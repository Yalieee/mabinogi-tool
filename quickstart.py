import ctypes, sys
import time
from directkeys import PressKey, ReleaseKey, DIK_1, DIK_2, DIK_3, DIK_4, DIK_5, DIK_6, DIK_ESCAPE

def play(key, sleep_time):
    PressKey(key)
    ReleaseKey(key)
    time.sleep(sleep_time)
    PressKey(DIK_ESCAPE)
    ReleaseKey(DIK_ESCAPE)
    time.sleep(1)

def main():
    time.sleep(1)
    while True:
        play(DIK_1, 3)
        play(DIK_2, 2)
        play(DIK_3, 4)
        # play(DIK_4, 2)
        # play(DIK_5, 20)
        play(DIK_6, 26)

if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
