from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Marketplace(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.marketplace_icon = (MobileBy.XPATH,'(//android.widget.ImageView[@resource-id="com.terravirtua.staging:id/navigation_bar_item_icon_view"])[2]')
        self.item_cart = (MobileBy.XPATH, '//android.widget.ImageView[@resource-id="com.terravirtua.staging:id/image_main"]')
        self.item_detail_button = (MobileBy.ID, 'com.terravirtua.staging:id/btnItemDetail')
        self.item_serial_no = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="com.terravirtua.staging:id/tvDescription"])[2]')
        self.close_item_detail_popup = (MobileBy.ID, 'com.terravirtua.staging:id/touch_outside')
        self.buy_now_button = (MobileBy.ID, 'com.terravirtua.staging:id/btnBuyNow')
        self.pay_now_button = (MobileBy.ID, 'com.terravirtua.staging:id/btnPayNow')
        self.view_transaction = (MobileBy.ID, 'com.terravirtua.staging:id/btnViewTransaction')
        self.transaction_detail = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="com.terravirtua.staging:id/serial_no"])[1]')
        self.transaction_serial_no = (MobileBy.XPATH, '(//android.widget.TextView[@resource-id="com.terravirtua.staging:id/value"])[1]')

    # Data functions (methods)



    def click_marketplace_icon(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.marketplace_icon))
        element.click()

    def click_item_cart(self,):
        item_cart = self.wait_for_element(self.item_cart)
        item_cart.click()

    def click_item_detail_button(self, ):
        wait = WebDriverWait(self.driver, 10)
        item_detail_button = wait.until(EC.visibility_of_element_located(self.item_detail_button))
        item_detail_button.click()



    def click_item_serial_no(self):
        item_serial_no = self.wait_for_element(self.item_serial_no)
        item_serial_no.click()
        value = item_serial_no.text
        return value


    def click_close_item_detail_popup(self):
        close_item_detail_popup = self.wait_for_element_to_be_clickable(self.close_item_detail_popup)
        close_item_detail_popup.click()



    def click_buy_now_button(self, ):
        wait = WebDriverWait(self.driver, 10)
        buy_now_button = wait.until(EC.visibility_of_element_located(self.buy_now_button))
        buy_now_button.click()

    def click_pay_now_button(self, ):
        wait = WebDriverWait(self.driver, 10)
        pay_now_button = wait.until(EC.visibility_of_element_located(self.pay_now_button))
        pay_now_button.click()

    def click_view_transaction(self, ):
        view_transaction = self.wait_for_element_to_be_clickable(self.view_transaction)
        view_transaction.click()



    def click_transaction_detail(self):
        transaction_detail= self.wait_for_element_to_be_clickable(self.transaction_detail)
        transaction_detail.click()


    def click_transaction_serial_no(self):
        transaction_serial_no = self.wait_for_element_to_be_clickable(self.transaction_serial_no)
        transaction_serial_no.click()
        value = transaction_serial_no.text
        return value



