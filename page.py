class Training:
    def __init__(self, driver):
        self.driver = driver

    def click_button(self):
        button = self.driver.find_element_by_css_selector("href$='/login'")
        button.click()
        return Training
