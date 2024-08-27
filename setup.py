import pyautogui as pag
import time
import pyperclip
import subprocess

# Define the coordinates and use the `actions` list
actions = [
    (610, 531, 4),  # next
    (286, 459, 4),  # Accept terms
    (610, 531, 4),  # next
    (610, 531, 4),  # next
    (610, 531, 4),  # next
    (610, 531, 4),  # install
    (387, 253, 10),  # type pass
    (387, 298, 4),  # type pass
    (564, 598, 4),  # ok
    (610, 531, 4),  # finish
    (849, 746, 10),  # open litemanager
    (522, 388, 4),  # click connect
    (460, 321, 4),  # right click (select all)
    (506, 387, 4),  # click copy
    (397, 437, 4),  # open options
    (394, 286, 4),  # click auto connect
    (510, 312, 4),  # change timeout interval
    (521, 502, 4),  # click okey
]

# Wait for a few seconds to give time to focus on the target application
time.sleep(10)
password = "Minarul01BD"
timeout = "10"
    
for x, y, duration in actions:
    if (x, y, duration) == (387, 253, 10):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (387, 298, 4):
        pag.click(x, y, duration=duration)
        pag.typewrite(password)
    elif (x, y, duration) == (460, 321, 4):
        pag.rightClick(x, y, duration=duration)
    elif (x, y, duration) == (610, 531, 4):
        pag.click(x, y, duration=duration)
        cmd = r'"C:\Program Files (x86)\LiteManager Pro - Server\ROMServer.exe" /start'
        subprocess.run(cmd, shell=True)
    elif (x, y, duration) == (510, 312, 4):
        pag.click(x, y, duration=duration)
        pag.press('backspace')  # Press backspace once
        pag.press('backspace')  # Press backspace againsetup
        pag.typewrite(timeout)
    else:
        pag.click(x, y, duration=duration)

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}')

def save_command():
    clipboard_text = pyperclip.paste()
    password_echo = 'LiteManager Password : Minarul01BD'  
    save_echo_to_batch('show.bat', f'LiteManager ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)

if __name__ == "__main__":
    save_command()

print("Done , Log in Credintials is below")
