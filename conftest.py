import allure
import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options


@pytest.fixture(scope='function')
def driver():
    print('\nStart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=2880,1800')
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
    else:
        driver = webdriver.Chrome(service=Service())
        driver.maximize_window()
    yield driver
    print('\nQuit browser...')
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def clear_allure_result_folder():
    allure_result_folder = "allure_results"
    if not os.path.exists(allure_result_folder):
        os.makedirs(allure_result_folder)
    else:
        for file_name in os.listdir(allure_result_folder):
            file_path = os.path.join(allure_result_folder, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
    yield


# @allure.feature("Make a Screenshot")
# def pytest_runtest_make_report(item, call):
#     if call.when == 'call':
#         if call.excinfo is not None:
#             try:
#                 driver = item.funcargs['driver']
#                 driver.save_screenshot('allure-results/screenshot.png')
#                 allure.attach.file('allure-results/screenshot.png', name='Screenshot',
#                                    attachment_type=allure.attachment_type.PNG)
#                 allure.attach(driver.page_source, name="HTML source", attachment_type=allure.attachment_type.HTML)
#             except Exception as e:
#                 print(f"Failed to take screenshot: {e}")
