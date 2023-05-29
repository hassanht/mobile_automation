import allure
import pytest

from Screens.Addfund import Addfund
from TestCases.BaseTest import BaseTest
from Screens.SignInPage import SignInPage
from Screens.SignUpPage import SignUpPage
from Screens.Emailverificatin import Emailverification
from Screens.Marketplace import Marketplace
from Screens.Wishlist import Wishlist
from Screens.Settings import Settings
from Screens.AfterEmailSettings import AfterEmailSettings




class TestSmokeTest(BaseTest):
    """
        All Test cases of Text Fields Screen should be handled here.

    """

    # @allure.title("Check test signin to virtua")
    # @allure.description("Send the valid email and password ")
    # @pytest.mark.functional
    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # def test_signin_to_virtua(self, driver):
    #     signinpage = SignInPage(driver)
    #     # signinpage.enter_email("guriya@getnada.com")
    #     signinpage.enter_email("iqra@mailinator.com")
    #     signinpage.enter_password("12@Pakistan")
    #     signinpage.click_sign_in()
    #     assert signinpage.visibility_of_the_profile_icon() == True
    #     signinpage.click_profile_icon()
    # #
    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # @allure.title("Setting")
    # @allure.description("setting test cases")
    # def test_Settings(self, driver):
    #     settings = Settings(driver)
    #     signinpage = SignInPage(driver)
    #     signinpage.click_profile_icon()
    #     settings.click_settings()
    #     settings.click_two_step_verification()
    #     settings.click_next_button()


    @pytest.mark.parametrize("driver", ["app_two"], indirect=True)
    @allure.title("Email Verification process")
    @allure.description("Verify the email")
    def test_email_verification(self, driver):
        emailverification = Emailverification(driver)
        emailverification.enter_google_search("https://www.mailinator.com/")
        emailverification.enter_add_inox_icon("iqra")
        emailverification.click_add_now_button()
        emailverification.click_two_FA_verification_email()
        emailverification.click_email_code()

    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # @allure.title("After Email Setting")
    # @allure.description("After Email Setting")
    # def test_After_Email_Settings(self, driver):
    #     afteremailsettings = AfterEmailSettings(driver)
    #     AfterEmailSettings.click_code()
    #     AfterEmailSettings.click_verify_button()


    # @allure.title("Logout the virtua")
    # @allure.description("Click te profile icon and click the logout button")
    # @pytest.mark.functional
    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # def test_logout_to_virtua(self, driver):
    #     signinpage = SignInPage(driver)
    #     signinpage.click_profile_icon()
    #     signinpage.click_logout()
    #     signinpage.click_logout_button()

    # @allure.title("Check the Sign Up to virtua")
    # @allure.description("check all  fields")
    # @pytest.mark.functional
    # def test_signup_to_virtua(self):
    #     signuppage = SignUpPage(self.driver)
    #     signuppage.click_signup()
    #     signuppage.enter_first_name("Iqra")
    #     signuppage.enter_last_name("QA")
    #     signuppage.enter_user_name("IqraQA")
    #     signuppage.enter_email("IqraQA2@getnada.com")
    #     signuppage.click_signup_button()
    #     signuppage.enter_create_password("12@Pakistan")
    #     signuppage.enter_confirm_password("12@Pakistan")
    #     # signuppage.select_country_dropdown()
    #     signuppage.click_create_account_button()
    #

    #
    #






   






    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # @allure.title("Add fund")
    # @allure.description("Add fund process")
    # def test_Add_fund(self, driver):
    #     addfund = Addfund(driver)
    #     signinpage=SignInPage(driver)
    #     signinpage.click_profile_icon()
    #     balance=addfund.click_your_balance()
    #     addfund.click_close_popup()
    #     addfund.click_vcredit_icon()
    #     bundle_price=addfund.click_bundle_credit()
    #     addfund.click_vcredit_purchase_price()
    #     addfund.click_tap_buy_button()
    #     addfund.click_ok_button()
    #     signinpage.click_profile_icon()
    #     after_balance=addfund.click_return_balance()
    #     assert float(bundle_price)==float(after_balance)-float(balance)

    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # @allure.title("Marketplace")
    # @allure.description("Marketplace")
    # def test_Marketplace(self, driver):
    #     marketplace = Marketplace(driver)
    #     marketplace.click_marketplace_icon()
    #     marketplace.click_item_cart()
    #     marketplace.click_item_detail_button()
    #     serial_no=marketplace.click_item_serial_no()
    #     marketplace.click_close_item_detail_popup()
    #     marketplace.click_buy_now_button()
    #     marketplace.click_pay_now_button()
    #     marketplace.click_view_transaction()
    #     marketplace.click_transaction_detail()
    #     after_purchase_serial_no=marketplace.click_transaction_serial_no()
    #     assert (serial_no)==(after_purchase_serial_no)

    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # @allure.title("Wishlist")
    # @allure.description("Wishlist")
    # def test_Wishlist(self, driver):
    #     wishlist = Wishlist(driver)
    #     marketplace = Marketplace(driver)
    #     signinpage = SignInPage(driver)
    #     marketplace.click_marketplace_icon()
    #     marketplace.click_item_cart()
    #     item_title= wishlist.click_item_title()
    #     item_price=wishlist.click_item_price()
    #     wishlist.click_item_wishlist()
    #     marketplace.click_item_detail_button()
    #     serial_no = marketplace.click_item_serial_no()
    #     marketplace.click_close_item_detail_popup()
    #     wishlist.click_wishlist_back_button()
    #     signinpage.click_profile_icon()
    #     wishlist.click_wishlist_tab()
    #     wishlist_item_title=wishlist.click_wishlist_item_title()
    #     wishlist_item_price=wishlist.click_wishlist_item_price()
    #     assert (item_title)==(wishlist_item_title)
    #     assert (item_price)==(wishlist_item_price)
    #     wishlist.click_remove_wishlist_item()
    #     wishlist.click_remove_confirm_button()
