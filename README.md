# Mabinogi Tools
瑪奇用的各種工具

Tools for mabinogi.

# Tools
## Auto keyboard input
### Description
此工具會自動不間斷送出鍵盤訊號，因此可以用來提升演奏系列的技能。

This tool can send keyboard signal directly, so you can use it to play skills automatically. This is useful when you want to level up your music related skills.

### How to use
執行 quickstart.py

Run quickstart.py. Just double click it.

### Q/A
1. Why it needs to run as administrator? (為什麼需要以系統管理員身分執行)

在我的電腦上，如果不以管理者身分執行，會發現瑪奇收不到訊號。我的推測是瑪奇是以管理者身分在執行，因此要送訊號給他也需要管理者權限。如果想嘗試使用一般使用者身分執行，可以修改 `quickstart.py`:

In my PC, I found the Mabinogi process cannot receive my signals. I think the reason is that it is run as administrator. If you want to have a try, you can edit `quickstart.py` to run in current user.

```py
if __name__ == '__main__':
    if is_admin():
        main()
    else:
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
```
to
```py
if __name__ == '__main__':
    main()
```

## Mouse Auto Click
### Description
This tool can click the left button automatically. The default frequency is 0.5 seconds.

### How to Use
0. pip3 install pypiwin32
1. Run autoclick.py
2. Move the cursor to the place you want. You have 5 seconds to do it.
3. The process is stop when you move you cursor again.
