"""
Root file for all the high priority fixtures.
In this file fixtures can use across the architecture.
Avoid placing unnecessary fixture in here.
"""

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Browser:
    service = Service(executable_path=GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service)
