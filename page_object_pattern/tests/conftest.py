import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import allure

from page_object_pattern.utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    # self.driver = webdriver.Chrome(ChromeDriverManager(driver_version='117.0.5938.89').install())
    # self.driver.implicitly_wait(10)
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get_screenshot_as_png()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()