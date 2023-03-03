import pyautogui as ps
import time
import os
from PIL import Image
import keyboard
from pytesseract import pytesseract
import webbrowser
# hello there my name is skanda 
print("Hello, welcome to pytype. A python bot which does your typing test faster than you.")
# speed = input("What speed would you like to see (100 ~ 250 words per minute")
# test_time = input("How many seconds do you want the test duration to be? (15s, 30s, 60s, 120s")
print("Just sit back and enjoy. The website will open by itself and do the test.")

# chrome_path = r"C:\Program Files\Google\Chrome\Application\ chrome.exe %s"
# webbrowser.get(chrome_path).open_new_tab("monkeytype.com")
# time.sleep(5)
# ps.click(x = 1162, y = 675) #cookie menu
# time.sleep(0.2)
# ps.click(x = 1233 , y = 118) #top menu
# time.sleep(0.2)
# ps.click(x = , y = ) #15s
# ps.click(x = , y = ) #30s
# ps.click(x = 1046, y = 190) #60s
# ps.click(x = , y = ) #120s



interval = 0.03
 

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img1_path = r"C:\Users\skand\Desktop\my python\autotyper\image1.png"
img2_path = r"C:\Users\skand\Desktop\my python\autotyper\image2.png"
img3_path = r"C:\Users\skand\Desktop\my python\autotyper\image3.png"


def first_image():
    image1 = ps.grab(region = (150, 451, 1600, 60))    # first line cordinates
    image1.save("image1.png")
    img = Image.open(img1_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text1 = pytesseract.image_to_string(img)
    # keyboard.write(text1)
    ps.write(text1, interval= interval)
    keyboard.press_and_release('space')

def second_image(state):
    image2 = ps.grab(region = (150, 501, 1600, 60))    # second line cordinates
    image2.save("image2.png")
    img2 = Image.open(img2_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text2 = pytesseract.image_to_string(img2)
    # keyboard.write(text2)
    ps.write(text2, interval=interval)
    keyboard.press_and_release('space')
    if(state):
        print(text2)
    # os.remove("image1.png")

def third_image(state):
    image3 = ps.grab(region = (150, 551, 1600, 60))    # third line cordinates
    image3.save("image3.png")
    img3 = Image.open(img3_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text3 = pytesseract.image_to_string(img3)
    # keyboard.write(text3)
    ps.write(text3, interval = interval)
    keyboard.press_and_release('space')
    if(state):
        print(text3)
    # os.remove("image2.png")

time.sleep(3)
img5_path = r"C:\Users\skand\Desktop\my python\autotyper\captcha.png"
img5 = Image.open(img5_path)
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(img5)
ps.write(text, interval = interval)
# time.sleep(5)
# start = time.perf_counter()
# first_image()
# second_image(True)
# third_image(True)
# stop = time.perf_counter()

# print("time taken to print three line is:", stop - start)



 
# def type():
#     time.sleep(5)
#     first_image()
#     # time.sleep(3)
#     second_image(False)
#     # time.sleep(3)
#     third_image(False)
#     time.sleep(0.2)
#     # second_image(False)
#     # third_image(False)

#     for _ in range(14):
#         second_image(False)
#         third_image(False)
#         time.sleep(0.2)

    

# type()
    







# time.sleep(10)

# os.remove("image.png")
# os.remove("image1.png")
# os.remove("image2.png")




