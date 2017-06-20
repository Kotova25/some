

class Screen:
    def __init__(self, driver):
        self.driver = driver

    sandwich = 'android.widget.ImageButton'
    bookmarks_button = '//android.widget.CheckedTextView[@text="Закладки"]'
    widget = 'android.widget.RelativeLayout'
    my_adv_button = '//android.widget.CheckedTextView[@text="Мои объявления"]'
    login_button = '//android.widget.TextView[@text="Войти"]'
    enter_button = 'button_authenticate_password'
    nickname_field = 'edit_username'
    password_field = 'edit_password'
    authenticate_button = 'button_authenticate'
    authenticate_user_name = 'text_username'
    create_my_adv = '//android.widget.CheckedTextView[@text="Разместить объявление"]'
    exit_button = 'button_exit'
    star = 'icon_bookmark'
    name_of_adv = 'text_summary'
    adv = '//android.widget.CheckedTextView[@id="design_menu_item_text"]'
    menu = '//android.support.v7.widget.RecyclerView[@id="design_navigation_view"]'

    def click_to_adv(self):
        self.driver.find_element_by_xpath(Screen.adv).click()

    def click_to_sandwich_button(self):
        self.driver.find_element_by_class_name(Screen.sandwich).click()

    def click_to_login_button(self):
        self.driver.find_element_by_xpath(Screen.login_button).click()

    def click_to_enter_button(self):
        self.driver.find_element_by_id(Screen.enter_button).click()

    def click_to_bookmarks(self):
        self.driver.find_element_by_xpath(Screen.bookmarks_button).click()

    def click_to_my_adv(self):
        self.driver.find_element_by_xpath(Screen.my_adv_button).click()

    def fill_nickname_field(self, nickname):
        self.driver.find_element_by_id(Screen.nickname_field).set_value(nickname)

    def fill_password_field(self, password):
        self.driver.find_element_by_id(Screen.password_field).set_value(password)

    def click_to_authenticate_button(self):
        self.driver.find_element_by_id(Screen.authenticate_button).click()

    def click_to_create_my_adv(self):
        self.driver.find_element_by_xpath(Screen.create_my_adv).click()

    def get_attribute_enabled(self):
        state_attribute_enabled = self.driver.find_element_by_class_name(Screen.widget).get_attribute('enabled')
        state_attribute_enabled = str(state_attribute_enabled)
        return state_attribute_enabled

    def get_attribute_current_user_name(self):
        current_user_name = self.driver.find_element_by_id(Screen.authenticate_user_name).get_attribute('text')
        current_user_name = str(current_user_name)
        return current_user_name

    def login(self, nickname, password):
        self.click_to_sandwich_button()
        self.click_to_login_button()
        self.click_to_enter_button()
        self.fill_nickname_field(nickname)
        self.fill_password_field(password)
        self.click_to_authenticate_button()

    def click_to_exit_button(self):
        self.driver.find_element_by_id(Screen.exit_button).click()

    def logout(self):
        self.click_to_sandwich_button()
        self.click_to_exit_button()

    def click_to_star(self):
        self.driver.find_element_by_id(Screen.star).click()

    def get_attribute_name_of_adv(self):
        adv_name = self.driver.find_element_by_id(Screen.name_of_adv).get_attribute('text')
        return adv_name

    def swipe_menu(self):
        self.driver.swipe(0.75, 100, 0.75, 100, 3000)
