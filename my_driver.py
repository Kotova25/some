from appium import webdriver


class Driver:
    def __init__(self, host, caps):
        self.driver = webdriver.Remote(host, caps)

    def close_driver(self):
        self.driver.quit()
