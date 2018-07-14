import ctypes
import sys
import time
import win32api, win32con, win32gui

class MouseAction(object):
    STOP_DISTANCE = 10
    CLICK_FREQUENCY = 0.5

    def autoClick(self):
        self.start_x, self.start_y = win32gui.GetCursorPos()
        x, y = None, None

        while not self._should_stop(x, y):
            print(2)
            x, y = win32gui.GetCursorPos()
            self._click()
            time.sleep(MouseAction.CLICK_FREQUENCY)

    def _click(self):
        x, y = win32gui.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def _should_stop(self, x, y):
        ''' Stop when the cursor moved'''
        if x is None or y is None:
            return False

        return abs(self.start_x - x) > MouseAction.STOP_DISTANCE or abs(self.start_y - y) > MouseAction.STOP_DISTANCE

if __name__ == '__main__':
    if ctypes.windll.shell32.IsUserAnAdmin():
        time.sleep(5)  # time to move the cursor to the right place
        action = MouseAction()
        action.autoClick()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", sys.executable, __file__, None, 1)
