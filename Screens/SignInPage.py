from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screens.BasePage import BasePage


class SignInPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.email_input = (MobileBy.ID, 'com.terravirtua.staging:id/inputEditText')
        self.password_input = (MobileBy.XPATH, '//*[@text="Password"]')
        self.sign_in_button = (MobileBy.ID, 'com.terravirtua.staging:id/button_login')
        self.profile_icon = (MobileBy.ID,'com.terravirtua.staging:id/imageViewProfile')
        self.logout = (MobileBy.XPATH,'//*[@text="Logout"]')
        self.logout_button = (MobileBy.ID, 'com.terravirtua.staging:id/action_done')

    # Data functions (methods)
    def enter_email(self, email):
        email_element = self.wait_for_element(self.email_input)
        email_element.clear()
        email_element.send_keys(email)

    def enter_password(self, password):
        password_element = self.wait_for_element(self.password_input)
        password_element.clear()
        password_element.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.wait_for_element_to_be_clickable(self.sign_in_button)
        sign_in_button.click()

    def click_profile_icon(self):
        profile_icon = self.wait_for_element_to_be_clickable(self.profile_icon)
        profile_icon.click()


    def click_logout(self):
        logout = self.wait_for_element_to_be_clickable(self.logout)
        logout.click()

    def click_logout_button(self):
            logout_button = self.wait_for_element_to_be_clickable(self.logout_button)
            logout_button.click()

    def visibility_of_the_profile_icon(self):
        profile_icon = self.wait_for_element_to_be_clickable(self.profile_icon)
        return profile_icon.is_displayed()
