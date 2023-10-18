screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
screenWidth, screenHeight

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
currentMouseX, currentMouseY

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick()     # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
    pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.


distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up
 

그 외의 추가로 알면 좋은 기능

import pyautogui

# 매 함수 호출마다 딜레이 설정
pyautogui.PAUSE = 1.5

#한글 입력
# pip install pyperclip
# pyperclip.copy("코딩유치원") 
# pyautogui.hotkey("ctrl", "v")

# confidence 정확도 입력을 통한 이미지를 찾아서 클릭
img = pyautogui.locateCenterOnScreen('x.png', confidence=0.95)
pyautogui.click(img)