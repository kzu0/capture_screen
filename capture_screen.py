# Python script to take screenshots of screen portions
# at regular intervals with a mouse click at specific
# coordinates between each screenshot.

# https://pyautogui.readthedocs.io/en/latest/install.html
# https://pyautogui.readthedocs.io/en/latest/screenshot.html
# https://pynput.readthedocs.io/en/latest/keyboard.html#

# pip install --upgrade pywin32 pynput pyautogui pyscreeze pillow

from pynput.mouse import Button, Controller
import pyautogui
import time
import argparse

mouse = Controller()

def get_screenshot(base_filename, pages_):

    # Read pointer position
    print('The current pointer position is {0}'.format(mouse.position))

    pages = pages_

    x_top = 647
    y_top = 162

    x_bottom = 1271
    y_bottom = 937

    width = x_bottom - x_top
    height = y_bottom - y_top

    x_click = 1891
    y_click = 561

    for i in range(1, pages + 1):

        nome_file = "{}_{}.png".format(base_filename, i)
        img = pyautogui.screenshot(nome_file, region=(x_top, y_top, width, height))

        print(f"Page {i} of {pages} acquired.")

        mouse.position = (x_click, y_click)
        mouse.click(Button.left)

        time.sleep(3)

def main():
    parser = argparse.ArgumentParser(description="Cattura screenshot multipli con PyAutoGUI.")
    parser.add_argument("base_filename", type=str, help="Output base name of screenshot files")
    parser.add_argument("pages", type=int, help="Number of pages to acquire")

    args = parser.parse_args()

    get_screenshot(args.base_filename, args.pages)

if __name__ == "__main__":
    main()
