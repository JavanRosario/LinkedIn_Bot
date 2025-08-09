from .login import LinkedInLogin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from time import sleep

TIME_TO_SLEEP = 3  # default wait time


class ConectDevs(LinkedInLogin):
    def __init__(self) -> None:
        super().__init__()  # init parent class

    def conect(self):
        while True:  # main loops
            try:
                # get initial page height
                last_height = self.driver.execute_script(
                    "return document.body.scrollHeight")

                # scroll to bottom
                while True:
                    self.driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);")
                    sleep(3)
                    new_height = self.driver.execute_script(
                        "return document.body.scrollHeight")
                    if new_height == last_height:
                        print("Chegou ao final da página")
                        break
                    last_height = new_height

                # back to top
                self.driver.execute_script("window.scrollTo(0, 0);")
                sleep(2)

                # find "Connect" buttons
                buttons = self.driver.find_elements(
                    By.XPATH, './/span[normalize-space(text())="Conectar"]')
                for button in buttons:
                    try:  # scroll into view
                        self.driver.execute_script(
                            "arguments[0].scrollIntoView(true);", button)
                        sleep(1)

                        # wait until clickable
                        WebDriverWait(self.driver, TIME_TO_SLEEP).until(
                            EC.element_to_be_clickable(button))

                        # click button
                        button.click()
                        sleep(1)

                    except ElementClickInterceptedException:
                        # force click via JS
                        self.driver.execute_script(
                            "arguments[0].click();", button)
                    except Exception as e:
                        ...
            except KeyboardInterrupt:
                # stop loop CTRL+C in terminal
                break
