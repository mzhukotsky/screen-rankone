from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def login_to_rankone(username, password):
    try:
        
        # Path to Chrome Driver
        driver = webdriver.Chrome()

        # Open sign-in page
        driver.get("https://www.rankone.global/signin")

        # Finding field for login and password input
        login_input = driver.find_element(By.NAME, 'username')
        login_input.send_keys(username)

        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(password)

        # Click Login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Waiting for login
        time.sleep(10)

        # Checking if login was successful
        if driver.current_url == "https://www.rankone.global/":
            print("Login successful.")
            return True
        else:
            print("Login failed.")
            return False

    except Exception as e:
        print(f"Error during login: {e}")
        return False
    
    finally:
        driver.quit()