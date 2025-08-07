from .login import LinkedInLogin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from time import sleep

TIME_TO_SLEEP = 3


class ConectDevs(LinkedInLogin):
    def __init__(self) -> None:
        super().__init__()

    def conect(self):
        buttons = self.driver.find_elements(
            By.XPATH, './/span[normalize-space(text())="Conectar"]')
        for i, button in enumerate(buttons):
            try:
                WebDriverWait(self.driver, TIME_TO_SLEEP).until(
                    EC.visibility_of(button))
                sleep(5)
                button.click()
                if i == len(buttons) - 1:
                    print("✅ Fim do loop — último botão clicado.")
                    sleep(10)
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", button)
            except Exception as e:
                ...
