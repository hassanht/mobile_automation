import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep

    #
    # @pytest.mark.parametrize("driver", ["app_one"], indirect=True)
    # def test_app_one(appium_driver):
    # desired_caps = dict(
    #     platformName="Android",
    #     deviceName="emulator-5554",
    #     platformVersion="10",
    #     app_activity="com.terravirtua.v3.MainActivity",
    #     app_package="com.terravirtua.staging",
    # )
    # driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    # driver.start_activity(app_package="com.terravirtua.staging",app_activity="com.terravirtua.v3.MainActivity")
    # request.cls.driver = driver
    # driver.implicitly_wait(10)
    # yield driver
    # driver.quit()
    #
    # @pytest.mark.parametrize("driver", ["app_two"], indirect=True)
    # def test_app_two(appium_driver2):
    # desired_caps = dict(
    #     platformName="Android",
    #     deviceName="emulator-5554",
    #     platformVersion="10",
    #     app_activity="com.google.android.apps.chrome.Main",
    #     app_package="com.android.chrome",
    # )
    # driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    # driver.start_activity(app_package="com.android.chrome",app_activity="com.google.android.apps.chrome.Main")
    # request.cls.driver = driver
    # driver.implicitly_wait(10)
    # yield driver
    # driver.quit()

    #
    # @pytest.fixture()
    # def log_on_failure(request, appium_driver2):
    # yield
    # item = request.node
    # driver = appium_driver2
    # if item.rep_call.failed:
    #     allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
    #
    #

@pytest.fixture(scope="function")
def driver(request):
    app = request.param
    if app == "app_one":
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            # "deviceName": "RF8M20SBN8N",
            "platformVersion": "10",
            "app_activity": "com.terravirtua.v3.MainActivity",
            "app_package": "com.terravirtua.staging",
            "noReset": True,  # added capability to prevent app from resetting
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.start_activity(app_package="com.terravirtua.staging",app_activity="com.terravirtua.v3.MainActivity")
    elif app == "app_two":
        desired_caps = {
            "platformName": "Android",
            # "deviceName": "RF8M20SBN8N",
            "deviceName": "emulator-5554",
            "platformVersion": "10",
            "app_activity": "com.google.android.apps.chrome.Main",
            "app_package": "com.android.chrome",
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.start_activity(app_package="com.android.chrome", app_activity="com.google.android.apps.chrome.Main")

    yield driver
    driver.quit()

@pytest.fixture()
def log_on_failure(request, driver):
    yield
    item = request.node
    driver = driver
    if hasattr(item, 'rep_call') and item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
