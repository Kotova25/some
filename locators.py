import my_driver


class ToolBar:
    sandwich = 'android.widget.ImageButton'

    @staticmethod
    def click_to_sandwich_button():
        my_driver.instance.find_element_by_class_name(ToolBar.sandwich).click()


class NavigationDrawer:
    bookmarks_button = 'new UiSelector().text("Закладки")'

    @staticmethod
    def click_to_bookmarks():
        my_driver.instance.find_element_by_android_uiautomator(NavigationDrawer.bookmarks_button)


class LoginWidget:
    widget = 'android.widget.RelativeLayout'

    @staticmethod
    def get_attribute_enabled():
        state = my_driver.instance.find_element_by_class_name(LoginWidget.widget).get_attribute('enabled')
        state = str(state)
        return state


