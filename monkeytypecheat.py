import pyautogui
import keyboard
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time

webdriver_path = 'C:/WebDriver/msedgedriver.exe'

options = Options()
options.use_chromium = True

service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://monkeytype.com")

time.sleep(1)

def get_active_word():
    try:
        word_active_element = driver.find_element(By.CSS_SELECTOR, ".word.active")
        letters = word_active_element.find_elements(By.TAG_NAME, "letter")
        word = "".join([letter.text for letter in letters])
        return word
    except Exception as e:
        print(f"Error finding active word: {e}")
        return None

def main():
    toggle = False
    last_toggle_time = time.time()

    try:
        while True:
            if keyboard.is_pressed('f8'):
                current_time = time.time()
                if current_time - last_toggle_time > 0.2:
                    toggle = not toggle
                    print(f"Automation {'started' if toggle else 'stopped'}")
                    last_toggle_time = current_time
                time.sleep(0.1)
            
            if toggle:
                word = get_active_word()
                if word:
                    pyautogui.write(word + ' ')
                
                time.sleep(0.001)
            else:
                time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
