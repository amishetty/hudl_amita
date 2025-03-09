from selenium.webdriver.common.by import By
import os
from login_page import LoginPage

#Test for valid username and password
def test_valid_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://www.hudl.com/en_gb/")
    # accept_cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
    # accept_cookies_button.click()
    # allow_all_button = driver.find_element(By.ID, "adroll_allow_all")
    # allow_all_button.click()
    login_page.click_login_button()
    driver.get("https://www.hudl.com/login/")
    login_page.enter_user_name((os.getenv("USER_NAME")))
    login_page.click_continue()
    login_page.enter_password((os.getenv("USER_PASSWORD")))
    login_page.click_continue()
    actual_title = driver.title
    expected_title = "Home - Hudl"
    if expected_title not in actual_title:
        raise AssertionError("Login failed")
    # dismiss_button=driver.find_element(By.CSS_SELECTOR, "[class='u-onboarding-custom__dismiss']")
    # dismiss_button.click()
    login_page.click_profile_button()
    login_page.click_logout_button()

# Test for valid username and invalid password
def test_invalid_login(driver):
    login_page=LoginPage(driver)
    driver.get("https://www.hudl.com/en_gb/")
    login_page.click_login_button()
    driver.get("https://www.hudl.com/login/")
    login_page.enter_user_name(os.getenv("USER_NAME"))
    login_page.click_continue()
    login_page.enter_password("wrongpassword")
    login_page.click_continue()
    actual_error_box=driver.find_element(By.ID,"error-element-password")
    assert "Your email or password is incorrect. Try again." in actual_error_box.text, "Displayed error is not as expected"

# Test for invalid username
def test_invalid_login_blank_username(driver):
    login_page=LoginPage(driver)
    login_page.open_page("https://www.hudl.com/en_gb/")
    login_page.click_login_button()
    driver.get("https://www.hudl.com/login/")
    login_page.enter_user_name("abc")
    login_page.click_continue()
    actual_error_box=driver.find_element(By.ID,"error-element-username")
    assert "Enter a valid email." in actual_error_box.text, "Displayed error is not as expected"


