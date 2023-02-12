import pyautogui
import pywhatkit
import pyperclip
import webbrowser
import time


x, y = 280, 302
x_chat, y_chat = 900, 900


def main_loop():
    # open web browser and wait
    URL = "https://teams.microsoft.com"
    webbrowser.open(URL)
    time.sleep(20)
    
    s = []

    while True:
        # Set mouse to initial position
        pyautogui.click(x=x, y=y)
        time.sleep(2)
        pyautogui.click(x=x_chat, y=y_chat)
        time.sleep(2)

        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        s.append(pyperclip.paste())

        if len(s) > 1:
            s = s[-2:]
            if s[-1] != s[-2]:
                l = s[-1].split("\r\n")
                new_msg = l[-7] + "\n" + l[-6]
                print("New message: " + new_msg)
                pywhatkit.sendwhatmsg_to_group_instantly(group_id="H8WkMVzLROiKk2JrpnsL3F", 
                                                         message=new_msg, 
                                                         tab_close=True)
        
        print("Waiting 1 minute until reading again...")
        time.sleep(60)


if __name__ == '__main__':
    main_loop()         