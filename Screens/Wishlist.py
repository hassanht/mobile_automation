from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC


class Wishlist(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.item_title = (MobileBy.ID, 'com.terravirtua.staging:id/tvTitle')
        self.item_price = (MobileBy.ID, 'com.terravirtua.staging:id/tvAmount')
        self.item_wishlist = (MobileBy.ID, 'com.terravirtua.staging:id/ivWishList')
        self.wishlist_back_button = (MobileBy.ID, 'com.terravirtua.staging:id/ivBack')
        self.wishlist_tab = (MobileBy.ID, 'com.terravirtua.staging:id/wishlist')
        self.wishlist_item_title = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.terravirtua.staging:id/avatar_name"]')
        self.wishlist_item_price = (MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.terravirtua.staging:id/balance"]')
        self.remove_wishlist_item = (MobileBy.XPATH, '//android.widget.ImageView[@resource-id = "com.terravirtua.staging:id/action_remove"]')
        self.remove_confirm_button = (MobileBy.ID, 'com.terravirtua.staging:id/action_done')






    # Data functions (methods)

    def click_item_title(self):
        wait = WebDriverWait(self.driver, 10)
        item_title = wait.until(EC.visibility_of_element_located(self.item_title))
        item_title.click()
        return item_title.text


    def click_item_price(self):
        wait = WebDriverWait(self.driver, 10)
        item_price = wait.until(EC.visibility_of_element_located(self.item_price))
        item_price.click()
        return item_price.text

    def click_item_wishlist(self):
        wait = WebDriverWait(self.driver, 10)
        item_wishlist = wait.until(EC.visibility_of_element_located(self.item_wishlist))
        item_wishlist.click()

    def click_wishlist_back_button(self):
        wait = WebDriverWait(self.driver, 10)
        wishlist_back_button = wait.until(EC.visibility_of_element_located(self.wishlist_back_button))
        wishlist_back_button.click()


    def click_wishlist_tab(self):
        wait = WebDriverWait(self.driver, 10)
        wishlist_tab = wait.until(EC.visibility_of_element_located(self.wishlist_tab))
        wishlist_tab.click()

    def click_wishlist_item_title(self):
        wait = WebDriverWait(self.driver, 10)
        wishlist_item_titles = wait.until(EC.visibility_of_all_elements_located(self.wishlist_item_title))
        wishlist_item_title = wishlist_item_titles[0]
        return wishlist_item_title.text

    def click_wishlist_item_price(self):
        wait = WebDriverWait(self.driver, 10)
        wishlist_item_price = wait.until(EC.visibility_of_all_elements_located(self.wishlist_item_price))
        wishlist_item_price = wishlist_item_price[0]
        return wishlist_item_price.text

    def click_remove_wishlist_item(self):
        wait = WebDriverWait(self.driver, 10)
        remove_wishlist_item = wait.until(EC.visibility_of_all_elements_located(self.remove_wishlist_item))
        remove_wishlist_item = remove_wishlist_item[0]
        remove_wishlist_item.click()


    def click_remove_confirm_button(self):
        wait = WebDriverWait(self.driver, 10)
        remove_confirm_buttton = wait.until(EC.visibility_of_element_located(self.remove_confirm_button))
        remove_confirm_buttton.click()