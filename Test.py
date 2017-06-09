import unittest
from appium import webdriver



class AbOnlinerAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Xiaomi Redmi 4X'
        desired_caps['appActivity'] = 'by.onliner.ab.activity.AdvertsActivity'
        desired_caps['appPackage'] = 'by.onliner.ab.debug'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_cannot_go_to_bookmarks_without_login(self):
        sandwich = self.driver.find_element_by_class_name('android.widget.ImageButton')
        sandwich.click()
        bookmates_button = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Закладки")')
        bookmates_button.click()
        widget = self.driver.find_element_by_class_name('android.widget.RelativeLayout')
        state = str(widget.get_attribute('enabled'))
        assert(state == "true")


# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AbOnlinerAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
