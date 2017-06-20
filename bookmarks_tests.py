import unittest
import my_driver
import locators
import test_data


class BookmarksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {'platformName': 'Android', 'platformVersion': '6.0.1', 'deviceName': 'Xiaomi Redmi 4X',
                        'appActivity': 'by.onliner.ab.activity.AdvertsActivity', 'appPackage': 'by.onliner.ab.debug'}
        server_adr = 'http://localhost:4723/wd/hub'
        cls.driver_instance = my_driver.Driver(server_adr, desired_caps)
        cls.screen = locators.Screen(cls.driver_instance.driver)
        locators.Screen.login(cls.screen, test_data.UsersData.nickname, test_data.UsersData.password)
        cls.driver_instance.driver.wait_activity('by.onliner.ab.activity.AdvertsActivity', 5)
        user_name = cls.screen.get_attribute_current_user_name()
        if user_name != test_data.UsersData.nickname:
            print("Login failed")
        cls.driver_instance.close_driver()

    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '6.0.1', 'deviceName': 'Xiaomi Redmi 4X',
                        'appActivity': 'by.onliner.ab.activity.AdvertsActivity', 'appPackage': 'by.onliner.ab.debug'}
        server_adr = 'http://localhost:4723/wd/hub'

        self.driver_instance = my_driver.Driver(server_adr, desired_caps)
        self.screen = locators.Screen(self.driver_instance.driver)

    def tearDown(self):
        self.driver_instance.close_driver()

    def test_add_bookmarks(self):
        self.driver_instance.driver.wait_activity('by.onliner.ab.activity.AdvertsActivity', 5)
        adv_name = self.screen.get_attribute_name_of_adv()
        self.screen.click_to_star()
        self.screen.click_to_sandwich_button()
        self.screen.click_to_bookmarks()
        bookmarks_name = self.screen.get_attribute_name_of_adv()
        self.assertEqual(adv_name, bookmarks_name)

    def test_delete_from_bookmarks(self):
        self.driver_instance.driver.wait_activity('by.onliner.ab.activity.AdvertsActivity', 5)
        adv_name = self.screen.get_attribute_name_of_adv()
        self.screen.click_to_star()
        self.screen.click_to_sandwich_button()
        self.screen.click_to_bookmarks()
        bookmarks_name = self.screen.get_attribute_name_of_adv()
        self.assertNotEquals(adv_name, bookmarks_name)


if __name__ == '__main__':
    """suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)"""
    suite = unittest.TestLoader().loadTestsFromTestCase(BookmarksTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
