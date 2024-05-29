import os
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./yaml_files/datatest.yaml", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    browser_name = data['browser_name']


@pytest.fixture(scope='session')
def browser():
    if browser_name == 'firefox':
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
    else:
        service = ChromeService(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("Finish test")