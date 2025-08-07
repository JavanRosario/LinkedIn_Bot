from .login import LinkedInLogin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from time import sleep

TIME_TO_SLEEP = 3


class ConectDevs(LinkedInLogin):
    def __init__(self) -> None:
        super().__init__()

    def conect(self):
        buttons = self.driver.find_elements(
            By.XPATH, '//span[normalize-space(text())="Conectar"]')
        element = self.driver.find_element(
            By.XPATH, '/html/body/div/dialog/div/div/div/div/section/div/div/div')
        actions = ActionChains(self.driver)
        for button in buttons:
            try:
                WebDriverWait(self.driver, TIME_TO_SLEEP).until(
                    EC.visibility_of(button))
                sleep(5)
                button.click()
                actions.move_to_element(button).click(
                ).send_keys(Keys.PAGE_DOWN).perform()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", button)
            except Exception as e:
                ...
