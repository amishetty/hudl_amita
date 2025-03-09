import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import (load_dotenv, dotenv_values)

#Loading variables from .env file
load_dotenv()

options=Options()
options.add_argument("--headless")
@pytest.fixture(scope="module")
def driver():
    driver=webdriver.Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()