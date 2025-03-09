from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.dropdown_button = (By.XPATH, "//a[contains(text(), 'Log in')]")
        self.username_textbox = (By.XPATH, "//input[@name='username']")
        self.password_textbox = (By.XPATH, "//input[@name='password']")
        self.login_button = (By.NAME, "action")
        self.profile_button = (By.CSS_SELECTOR, "[class='hui-globaluseritem__display-name']")
        self.logout_button = (By.XPATH, "//span[text()='Log Out']")

    def open_page(self,url):
        self.driver.get(url)

    def enter_user_name(self,username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_continue(self):
        self.driver.find_element(*self.login_button).click()

    def click_login_button(self):
        self.driver.find_element(*self.dropdown_button).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def click_profile_button(self):
        self.driver.find_element(*self.profile_button).click()





