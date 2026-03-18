from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class insta:

    #Locators 
    START_BUTTON  = (By.XPATH, "//a[contains(@href,'/instapost-share-your-photos-online/lessons/practice-practice-practice')]/span")
    FINISH_BUTTON = (By.XPATH, "//form//button[.//span[text()='Finish']]")
    NEXT_BUTTON   = (By.XPATH, "//form//button[.//span[text()='Next lesson']]")
    
    #Action
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_Start_button_instapost(self):
        self.wait.until(EC.element_to_be_clickable(self.START_BUTTON)).click()
        time.sleep(2)

    def click_all_next_and_finish(self):
        while True:
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            current_position = 0
            increment = 200

            while current_position < last_height:
                self.driver.execute_script(f"window.scrollBy(0, {increment});")
                time.sleep(0.5)
                current_position += increment
                last_height = self.driver.execute_script("return document.body.scrollHeight")

            try:
                finish_btn = self.driver.find_element(*self.FINISH_BUTTON)
                self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", finish_btn)
                self.driver.execute_script("arguments[0].click();", finish_btn)
                print("Finish button clicked, lesson completed!")
                break

            except:
                try:
                    next_btn = self.driver.find_element(*self.NEXT_BUTTON)
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});", next_btn)
                    self.driver.execute_script("arguments[0].click();", next_btn)
                    time.sleep(1)

                except:
                    self.driver.execute_script("window.scrollBy(0, 200);")
                    time.sleep(0.5)