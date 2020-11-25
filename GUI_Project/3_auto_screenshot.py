from PIL import ImageGrab
import time

time.sleep(5)    # 5 second wait for the user to get ready

for i in range(1,11): # 2초 간격으로 10개 이미지 저장
    img = ImageGrab.grab()
    img.save("image{}.png".format(i))   # 파일로 저장 image{1..10}.png
    time.sleep(2)