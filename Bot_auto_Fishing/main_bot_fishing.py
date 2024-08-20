import cv2
import numpy as np
import pyautogui
import time

pyautogui.FAILSAFE = False 
lower_blue = np.array([100, 100, 150])
upper_blue = np.array([130, 255, 255])

button_regions = {
    'A': (0, 0, 60, 70),    
    'S': (60, 0, 120, 70),  
    'D': (120, 0, 180, 70), 
    'W': (180, 0, 240, 70), 
    'Q': (240, 0, 300, 70), 
    'E': (300, 0, 360, 70)  
}

def detect_highlighted_button(frame):

    roi = frame[780:850, 810:1170]  
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blue_pixel_sums = {}
    for button, (x1, y1, x2, y2) in button_regions.items():
        region_mask = mask[y1:y2, x1:x2]
        blue_pixel_sums[button] = np.sum(region_mask)

    max_blue_pixels = max(blue_pixel_sums.values())
    
    threshold = 1000  
    
    if max_blue_pixels > threshold:
        highlighted_button = max(blue_pixel_sums, key=blue_pixel_sums.get)
        return highlighted_button
    else:
        return None

def main():
    while True:

        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        highlighted_button = detect_highlighted_button(frame)
        
        if highlighted_button:
            pyautogui.press(highlighted_button.lower())
            print(f"Pressed: {highlighted_button}")
        
        if cv2.waitKey(1) == 27:  # ESC key
            break
        
        time.sleep(1)  # Delay 

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
