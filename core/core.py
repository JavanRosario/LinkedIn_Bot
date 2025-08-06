from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from dotenv import load_dotenv
from pathlib import Path
from time import sleep
import os

# default time for the bot
TIME_TO_SLEEP = 3

# driver directories and the .env file
CURRENT_DIR = Path(__file__).parent.parent / 'driver' / 'chromedriver.exe'
DOTENV_PATH = Path(__file__).parent.parent / 'config' / '.env'
load_dotenv(dotenv_path=DOTENV_PATH)


class LinkedinBot:
    def __init__(self) -> None:
        service = Service(executable_path=str(CURRENT_DIR))
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.driver = webdriver.Chrome(service=service)
        self.put_email = ActionChains(self.driver)

    def loguin(self):
        # linkedin login page
        self.driver.get('https://www.linkedin.com/login/')
        sleep(TIME_TO_SLEEP)
        self.put_email.send_keys(str(self.email)).perform()
        # password input selection

        self.put_password = WebDriverWait(self.driver, TIME_TO_SLEEP).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@name='session_password']"))
        )
        sleep(TIME_TO_SLEEP)
        self.put_password.send_keys(str(self.password))

        # submit input click
        self.login_click = WebDriverWait(self.driver, TIME_TO_SLEEP).until(
            EC.presence_of_element_located(
                (By.XPATH, "//form//button[@type='submit']")))

        sleep(TIME_TO_SLEEP)
        self.login_click.click()
        sleep(2)