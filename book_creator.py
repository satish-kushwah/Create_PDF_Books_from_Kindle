import time
import pyautogui
import shutil
import os
from PyPDF2 import PdfFileMerger
from PIL import Image
finalBookname = input('Enter name of book: ')

bookname = 'bookscreenshots'
try:
    shutil.rmtree(bookname)
except FileNotFoundError:
    print("folder not present")
os.mkdir(bookname)
path = os.path.dirname(__file__)+'/'+bookname+'/'
print('start taking screenshots in 5 sec')
time.sleep(5)
i = 1
print('\a')
while (1):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(path+str(format(i, '05d'))+'.png')

    if i > 1:
        if open(path+str(format(i, '05d'))+'.png', "rb").read() == open(path+str(format(i-1, '05d'))+'.png', "rb").read():
            print('\a')
            stop = input('enter 0 if book finished or just press enter: ')
            if stop == '0':
                os.remove(path+str(format(i, '05d'))+'.png')
                print('\a')
                print('reached to the end of book')
                break
            else:
                print('resuming taking screenshots in 5 sec')
                pyautogui.press('alt'+'tab')
                time.sleep(5)
                continue
    pyautogui.press('right')
    i = i+1

# creating pdf from png
path = os.path.dirname(__file__)
screenshotpath = path+'/bookscreenshots/'
try:
    shutil.rmtree('screenshot_pdfs')
except FileNotFoundError:
    print("folder not present")
os.mkdir('screenshot_pdfs')
onlyfiles = next(os.walk(screenshotpath))[2]
for i in range(1, len(onlyfiles)+1):
    image1 = Image.open(screenshotpath+str(format(i, '05d'))+'.png')
    im1 = image1.convert('RGB')
    im1.save(path+'/screenshot_pdfs/'+str(format(i, '05d'))+'.pdf')

# merging pdf
pdfs = []
for i in range(1, len(onlyfiles)+1):
    pdfs.append(str(format(i, '05d'))+'.pdf')
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(path+'/screenshot_pdfs/'+pdf)
merger.write(finalBookname+".pdf")
merger.close()
print('\a')
print('pdf of book created with name '+finalBookname+'.pdf')
