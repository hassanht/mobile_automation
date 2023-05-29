from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from Screens.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
import pyperclip


class Emailverification(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        # Data members (locators)
        self.google_search = (MobileBy.XPATH,'//android.widget.EditText[@resource-id="com.android.chrome:id/url_bar"]')
        self.add_inbox_icon=(MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.EditText')
        self.add_now_button = (MobileBy.XPATH, "//android.widget.Button[1]")
        self.two_FA_verification_email = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2FA Activation Code")')
        self.email_code = (MobileBy.XPATH, '//android.view.View[@resource-id="html_msg_body"]')


    # Data functions (methods)

    def enter_google_search(self, google_search):
        search_box = self.driver.find_element(*self.google_search)
        search_box.clear()
        search_box.send_keys(google_search)
        search_box.send_keys(Keys.RETURN)

    def enter_add_inox_icon(self, add_inbox):
        add_inbox_icon = self.driver.find_element(*self.add_inbox_icon)
        add_inbox_icon.send_keys(add_inbox)

    def click_add_now_button(self):
        add_now_button = self.driver.find_element(*self.add_now_button)
        add_now_button.click()

    def click_two_FA_verification_email(self):
        wait = WebDriverWait(self.driver, 10)
        emails = wait.until(EC.presence_of_all_elements_located(self.two_FA_verification_email))
        if len(emails) >= 2:
            emails[1].click()
        else:
            # Handle case where there are less than 2 matching elements
            pass

    def click_email_code(self):
        wait = WebDriverWait(self.driver, 10)
        email_code = wait.until(EC.visibility_of_element_located(self.email_code))
        value = email_code.text
        email_code.click()
        print("==============",value)
        pyperclip.copy(value)
        return value












