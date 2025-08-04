from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pathlib import Path
from time import sleep


DRIVER_PATH = Path(__file__).parent / 'driver' / 'chromedriver'


class LinkedinBot:
    def __init__(self) -> None:
        service = Service(executable_path=str(DRIVER_PATH))
        self.driver = webdriver.Chrome(service=service)
