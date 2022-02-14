"""
Root file for all the high priority fixtures.
In this file fixtures can use across the architecture.
Avoid placing unnecessary fixture in here.
"""
import logging

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="class")
def setup(request):
    logging.info("initiating chrome driver")
    service = Service(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get("http://kajabi.com")
    request.cls.driver = driver

    yield driver
    driver.close()


