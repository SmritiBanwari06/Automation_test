import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.browser = driver
    yield driver
    driver.quit()
