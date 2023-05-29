from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage


class SignUpPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.signup = (MobileBy.ID, 'com.terravirtua.staging:id/text_sign_up')
        self.first_name = (MobileBy.ID, 'com.terravirtua.staging:id/inputEditText')
        self.last_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Last Name")')
        self.user_name = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Username")')
        self.email_input = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Email")')
        self.signup_button = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign up")')
        self.create_password_input = (MobileBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.terravirtua.staging:id/inputLayoutPassword"]//android.widget.FrameLayout//android.widget.EditText[@resource-id="com.terravirtua.staging:id/inputEditText"]')
        self.create_confirm_password_input = (MobileBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.terravirtua.staging:id/inputLayoutConfirmPassword"]//android.widget.FrameLayout//android.widget.EditText[@resource-id="com.terravirtua.staging:id/inputEditText"]')
        # self.dropdown_element = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Country of residence (Optional)")')
        self.create_account_button = (MobileBy.ID, 'com.terravirtua.staging:id/button_create_account')

    # Data functions (methods)
    def click_signup(self):
        signup_element = self.wait_for_element_to_be_clickable(self.signup)
        point = signup_element.location
        x = point['x'] + signup_element.size['width'] - 10
        y = point['y'] + signup_element.size['height'] - 10
        TouchAction(self.driver).tap(x=x, y=y).perform()

    def enter_first_name(self, first_name_value):
        first_name_element = self.wait_for_element(self.first_name)
        first_name_element.send_keys(str(first_name_value))

    def enter_last_name(self, last_name):
        last_name_element = self.wait_for_element(self.last_name)
        last_name_element.set_value(last_name)

    def enter_user_name(self, last_name):
        user_name_element = self.wait_for_element(self.user_name)
        user_name_element.send_keys(last_name)

    def enter_email(self, email):
        email_element = self.wait_for_element(self.email_input)
        email_element.clear()
        email_element.send_keys(email)

    def click_signup_button(self, ):
        signup_button = self.wait_for_element_to_be_clickable(self.signup_button)
        signup_button.click()

    def enter_create_password(self, create_password, ):
        password_element = self.wait_for_element(self.create_password_input)
        # password_element.click()
        password_element.send_keys(create_password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_element = self.wait_for_element(self.create_confirm_password_input)
        confirm_password_element.send_keys(confirm_password)

    # def select_country_dropdown(self):
    #     # Create a Select object
    #     select = Select(self.dropdown)
    #
    #     # Select an option by its value
    #     select.select_by_value('Albania')

    def click_create_account_button(self, ):
        create_account_button = self.wait_for_element_to_be_clickable(self.create_account_button)
        create_account_button.click()
