from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def login_to_rankone(username, password):
    try:
        
        # Path to Chrome Driver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1366,768")
        options.add_argument('--log-level=3')
        options.add_argument('--silent')
        driver = webdriver.Chrome(options=options)

        # Open sign-in page
        driver.get("https://www.rankone.global/signin")

        time.sleep(5)

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

            profile_button = driver.find_element(By.CSS_SELECTOR, ".header-button")
            profile_name = profile_button.get_attribute("href")

            short_profile_name = profile_name.split("/")[-1]

            print(short_profile_name)
            return profile_name, short_profile_name

        else:
            print("Login failed.")
            return False, None
        

    except Exception as e:
        print(f"Error during login: {e}")
        return False
    
    finally:
        driver.quit()