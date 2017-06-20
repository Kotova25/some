import unittest
import my_driver
import locators
import test_data


class LoginTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '6.0.1', 'deviceName': 'Xiaomi Redmi 4X',
                        'appActivity': 'by.onliner.ab.activity.AdvertsActivity', 'appPackage': 'by.onliner.ab.debug'}
        server_adr = 'http://localhost:4723/wd/hub'

        self.driver_instance = my_driver.Driver(server_adr, desired_caps)
        self.screen = locators.Screen(self.driver_instance.driver)

    def tearDown(self):
        self.driver_instance.close_driver()

    def test_cannot_go_to_bookmarks_without_login(self):
        self.screen.click_to_sandwich_button()
        self.screen.click_to_bookmarks()
        self.assertEquals("true", self.screen.get_attribute_enabled())

    def test_cannot_go_to_my_adv_without_login(self):
        self.screen.click_to_sandwich_button()
        self.screen.click_to_my_adv()
        self.assertEquals("true", self.screen.get_attribute_enabled())

    def test_cannot_go_to_create_my_adv_without_login(self):
        self.screen.click_to_sandwich_button()
        self.screen.click_to_create_my_adv()
        self.assertEquals("true", self.screen.get_attribute_enabled())

    def test_login(self):
        self.screen.login(test_data.UsersData.nickname, test_data.UsersData.password)
        user_name = self.screen.get_attribute_current_user_name()
        self.assertEquals(test_data.UsersData.nickname, user_name)


if __name__ == '__main__':
    """suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)"""
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
