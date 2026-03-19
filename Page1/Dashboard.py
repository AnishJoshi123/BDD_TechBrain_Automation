from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Dashboard:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    DASHBOARD_HEADING = (By.XPATH, "//body//h1")

    # Actions
    def get_dashboard_heading(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADING)
        )
        return element.text