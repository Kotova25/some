from appium import webdriver

instance = None


def initialize(caps):
    global instance
    instance = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    return instance


def close_driver():
    global instance
    instance.quit()
