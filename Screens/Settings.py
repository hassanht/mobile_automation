from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import pyperclip



class Settings(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.settings= (MobileBy.XPATH, '//android.widget.TextView[@resource-id ="com.terravirtua.staging:id/title"]')
        self.two_step_verification=(MobileBy.XPATH,'//android.widget.Switch[@resource-id="com.terravirtua.staging:id/action_switch"]')
        self.next_button = (MobileBy.XPATH, '//android.widget.Button[@resource-id="com.terravirtua.staging:id/action_next"]')
        self.code = (MobileBy.ID, 'com.terravirtua.staging:id/inputEditText')
        self.verify_button = (MobileBy.ID, 'com.terravirtua.staging:id/action_verify')




    # Data functions (methods)

    def click_settings(self):
        settings = self.driver.find_elements(*self.settings)[4]  # 4th index is the 5th element
        settings.click()

    def click_two_step_verification(self):
        verifications = self.driver.find_elements(*self.two_step_verification)
        verifications[1].click()



    def click_next_button(self):
        next_button = self.driver.find_element(*self.next_button)
        next_button.click()

    def click_code(self):
        enter_code = self.driver.find_element(*self.code)
        enter_code.click()
        value = pyperclip.paste()
        enter_code.send_keys(value)

    def click_verify_button(self):
        verify_button = self.driver.find_element(*self.verify_button)
        verify_button.click()


