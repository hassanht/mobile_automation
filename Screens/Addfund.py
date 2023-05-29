import self as self
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

class Addfund(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.your_balance=(MobileBy.ID, 'com.terravirtua.staging:id/text_balance')
        self.close_popup=(MobileBy.ID, 'com.terravirtua.staging:id/action_close')
        self.vcredit_icon=(MobileBy.XPATH,'//android.widget.ImageView[@resource-id="com.terravirtua.staging:id/navigation_bar_item_icon_view"]')
        self.bundle_credit = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.terravirtua.staging:id/bundle_gem"]')
        self.vcredit_purchase_price=(MobileBy.XPATH,'//android.widget.TextView[@resource-id="com.terravirtua.staging:id/bundle_value"]')
        self.tap_buy_button=(MobileBy.ID, 'com.android.vending:id/button_group')
        self.ok_button = (MobileBy.ID, 'com.terravirtua.staging:id/action_done')
        self.return_balance = (MobileBy.ID, 'com.terravirtua.staging:id/text_balance')
    # Data functions (methods)
    def click_your_balance(self):
        your_balance = self.wait_for_element_to_be_clickable(self.your_balance)
        balance_str = your_balance.text
        balance = balance_str.split()[0]
        return balance

    def click_close_popup(self):
        close_popup = self.wait_for_element_to_be_clickable(self.close_popup)
        close_popup.click()

    def click_vcredit_icon(self):
        elements = self.driver.find_elements(*self.vcredit_icon)
        fourth_element = elements[4]  # Index 3 corresponds to the fourth matching element
        fourth_element.click()

    def click_bundle_credit(self):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.bundle_credit))
        if not isinstance(elements, list):
            elements = [elements]
        first_element = elements[0]  # Index 0 corresponds to the first matching element
        text_value = first_element.text.split()[0]  # Split the text value and take the first part
        print("Clicked on element with text:", text_value)
        return text_value

    def click_vcredit_purchase_price(self):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.vcredit_purchase_price))
        first_element = elements[0]  # Index 0 corresponds to the first matching element
        first_element.click()

    def click_tap_buy_button(self):
        tap_buy_button = self.wait_for_element_to_be_clickable(self.tap_buy_button)
        tap_buy_button.click()


    def click_ok_button(self):
        ok_button = self.wait_for_element_to_be_clickable(self.ok_button)
        ok_button.click()

    def click_return_balance(self):
        return_balance = self.wait_for_element_to_be_clickable(self.return_balance)
        balance_str = return_balance.text
        return_balance = balance_str.split()[0]
        print("====",return_balance)
        return return_balance

