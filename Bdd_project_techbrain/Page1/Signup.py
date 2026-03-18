from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Signupp:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    LOGIN_BUTTON = (By.XPATH, "//nav//a[2]/span")
    SIGNUP_BUTTON = (By.XPATH, "//*[@id='new_user']//a[@href='/users/sign_up']")
    SIGNUP_HEADING = (By.XPATH, "//h2[text()='Sign up']")
    EMAIL_FIELD = (By.XPATH, '//*[@id="user_email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//*[@id="user_password_confirmation"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="new_user"]/div[2]/input')
    CONFIRMATION_TEXT = (By.XPATH, "//p[contains(text(),'Woops')]")

    # Actions
    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def click_signup_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGNUP_BUTTON)).click()

    def get_signup_heading(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SIGNUP_HEADING))
        return element.text

    def fill_signup_form(self, email, password, confirm_password):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD_FIELD)).send_keys(confirm_password)

    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def get_confirmation_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION_TEXT))
        return element.text