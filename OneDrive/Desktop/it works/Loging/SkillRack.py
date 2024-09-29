from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options to keep the browser open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Creating an instance of the Chrome WebDriver with options
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.skillrack.com/faces/ui/profile.xhtml')  # Update with the correct path to your HTML file

# Letting the user see and also load the element
time.sleep(2)

# Find the username and password input fields
username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='j_username']"))
    )
password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='j_password']"))
    )

    # Enter User Name
username_input.send_keys('')

    # Enter Password
password_input.send_keys('')

    # Find and click the login button
login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Login']"))
    )
login_button.click()
print("Login Successful")

    # Let the user see the result
time.sleep(15)
    # Close the browser


