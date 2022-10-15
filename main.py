import cv2
from windowCapture import WindowCapture
from vision import Vision
from excel import excel
import xlsxwriter
import keyboard
import time
import datetime

wincap = WindowCapture('IQ Option')
vision_dot = Vision('dot.jpg')
vision_chegada = Vision('chegada.jpg')
last = sumLast = 0 
globalCount = 1
arr = []

excelT = excel('trade.xlsx')

waitTimeout = 0.15
timeout = 0
chegada = True
while True:
    # try:
    if timeout < time.time():
        screenshot = wincap.get_screenshot()

        now = vision_dot.find(screenshot, 0.5, 'rectangles')[1]
        chegadaPos = vision_chegada.find(screenshot, 0.5, 'rectangles')[0]

        print(chegadaPos)
        timeout = time.time() + waitTimeout
        arr.append(last-now)
        arr.append(datetime.datetime.now())
        last = now
        if chegadaPos == 0 and chegada == False:
            chegada = True
            arr.append(sumLast)
            arr.append(waitTimeout)
            sumLast = excelT.write(arr)
            arr = []
        elif chegadaPos != 0 and chegada == True:
            chegada = False

    if keyboard.is_pressed('q'):
        break
    # except:
    #     break
    
excelT.workbook.close()
cv2.destroyAllWindows()