from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import pyperclip



class AfterEmailSettings(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.code = (MobileBy.ID, 'com.terravirtua.staging:id/inputEditText')
        self.verify_button = (MobileBy.ID, 'com.terravirtua.staging:id/action_verify')




    # Data functions (methods)


    def click_code(self):
        enter_code = self.driver.find_element(*self.code)
        enter_code.click()
        value = pyperclip.paste()
        enter_code.send_keys(value)

    def click_verify_button(self):
        verify_button = self.driver.find_element(*self.verify_button)
        verify_button.click()


