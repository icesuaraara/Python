import cv2
import numpy as np
import pyautogui  # เพิ่มการนำเข้าไลบรารี pyautogui
from pynput.keyboard import Controller
import time

keyboard = Controller()

# Define the HSV range for detecting the blue highlight
lower_blue = np.array([100, 100, 150])
upper_blue = np.array([130, 255, 255])

# Define the regions corresponding to each button (A, S, D, W, Q, E) with coordinates
button_regions = {
    'A': (0, 0, 60, 70),    
    'S': (60, 0, 120, 70),  
    'D': (120, 0, 180, 70), 
    'W': (180, 0, 240, 70), 
    'Q': (240, 0, 300, 70), 
    'E': (300, 0, 360, 70)  
}

def detect_highlighted_button(frame):
    # Adjust ROI for the specific UI area based on 1920x1080 Fullscreen resolution
    roi = frame[780:850, 810:1170]  
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    blue_pixel_sums = {}
    for button, (x1, y1, x2, y2) in button_regions.items():
        region_mask = mask[y1:y2, x1:x2]
        blue_pixel_sums[button] = np.sum(region_mask)

    # Find the button with the maximum blue pixel sum, if it exceeds a threshold
    max_blue_pixels = max(blue_pixel_sums.values())
    
    # Define a threshold to ensure that the button is actually highlighted
    threshold = 1000  # This value may need to be adjusted based on testing
    
    if max_blue_pixels > threshold:
        highlighted_button = max(blue_pixel_sums, key=blue_pixel_sums.get)
        return highlighted_button
    else:
        return None

def main():
    last_pressed_button = None  # Store the last button that was pressed

    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Detect the highlighted button
        highlighted_button = detect_highlighted_button(frame)
        
        # Press the highlighted button if it is detected and not pressed before
        if highlighted_button and highlighted_button != last_pressed_button:
            keyboard.press(highlighted_button.lower())
            keyboard.release(highlighted_button.lower())
            print(f"Pressed: {highlighted_button}")
            last_pressed_button = highlighted_button  # Update the last pressed button
        
        # Optional: Display the frame (for debugging)
        # cv2.imshow('Frame', frame)
        
        # Break the loop with a key press (for example, ESC)
        if cv2.waitKey(1) == 27:  # ESC key
            break
        
        time.sleep(1)  # Delay to prevent overloading the CPU

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
