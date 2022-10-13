import cv2
from windowCapture import WindowCapture
from vision import Vision
import xlsxwriter
import keyboard

wincap = WindowCapture('IQ Option')
vision_dot = Vision('dot.jpg')
last = 0
count = 0
globalCount = 0
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
arr = []

while True:
    screenshot = wincap.get_screenshot()

    now = vision_dot.find(screenshot, 0.5, 'rectangles')

    if last != now:
        last = now
        count += 1
        arr.append(now)
        if count == 10:
            globalCount += 1
            key = 0
            charac = 'A'
            for ar in arr:
                if charac == "Z": # If Z encountered change to A
                    charac = ord(charac)-25
                else:
                    charac = ord(charac) + 1
                charac = chr(charac)
                print(charac)
                # worksheet.write(charac + str(globalCount), ar)
                key += 1
            charac = 'A'
            print('done')
            count = 0

    if keyboard.is_pressed('q'):
        workbook.close()
        cv2.destroyAllWindows()
        break