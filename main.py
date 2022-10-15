import cv2
from windowCapture import WindowCapture
from vision import Vision
import xlsxwriter
import keyboard
import time
import datetime

wincap = WindowCapture('IQ Option')
vision_dot = Vision('dot.jpg')
last = count = globalCount = 0
workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()
arr = []
letter = 'A'

def charac(word):
    wordConveted = ""
    invertedWord = word[::-1]

    numeric = -1
    for i, charac in enumerate(invertedWord):
        if i-1 == numeric:
            if charac == "Z":
                if(i == len(invertedWord)-1):
                    wordConveted += "A"
                numeric = i
                wordConveted += chr( ord(charac)-25 )
            else:
                wordConveted += chr( ord(charac) + 1 )
        else:
            wordConveted += charac


    return wordConveted[::-1]
    

timeout = 0;
while True:
    screenshot = wincap.get_screenshot()

    now = vision_dot.find(screenshot, 0.5, 'rectangles')

    if timeout < time.time():
        timeout = time.time() + 0.25
        count += 1
        print(now)
        arr.append(last-now)
        arr.append(datetime.datetime.now())
        last = now
        print(count)
        if count == 10:
            key = 0
            for ar in arr:
                print("Saved "+letter+str(globalCount))
                worksheet.write(letter + str(globalCount), ar)
                letter = charac(letter)
                key += 1
            globalCount += 1
            letter = 'A'
            arr = []
            count = 0
    if keyboard.is_pressed('q'):
        workbook.close()
        cv2.destroyAllWindows()
        break
        