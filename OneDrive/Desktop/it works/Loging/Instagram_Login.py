import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import s
# Set up Chrome options to keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Creating an instance of the Chrome WebDriver with options
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.instagram.com/')  # Update with the correct path to your HTML file

# Letting the user see and also load the element
time.sleep(2)

# Find the username and password input fields
username_input = WebDriverWait(browser, 6).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[1]/div/label/input"))
    )
password_input = WebDriverWait(browser, 6).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[2]/div/label/input"))
    )

    # Enter User Name
username_input.send_keys('')

    # Enter Password
password_input.send_keys('')

    # Find and click the login button
login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[3]/button"))
    )
login_button.click()
print("Login Successful")

    # Let the user see the result
time.sleep(3)
    # Close the browser

browser.get('https://www.instagram.com/reels')

  # Update with the correct path to your HTML file
print("Scrolling")

while(1):
    current_url = browser.current_url
    d=s.get_instagram_video_duration(current_url)

    print(f"Current URL: {current_url}")
    print(d)
    time.sleep(7)


