import pyautogui
import time


#1. 화면 크기 출력
# print(pyautogui.size())

#2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

#3. 마우스 위치 이동
# pyautogui.moveTo(31,245)
# pyautogui.moveTo(31,245,1)

# #4. 마우스 클릭
# # pyautogui.click()
# # pyautogui.click(button="right")
# # pyautogui.doubleClick()
# pyautogui.click(clicks=3, interval=1) # 3번 클릭 1초마다

#5. 마우스 드래스
# 547,48  409,50
pyautogui.moveTo(622,52,2)
pyautogui.dragTo(451,51,2)