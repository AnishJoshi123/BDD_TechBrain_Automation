from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import StaleElementReferenceException


class Ideator:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        
    # Locator 
    Start_button_Ideator = (By.XPATH, "//a[contains(@href,'ideator-an-idea-sharing-app/lessons/setting-up-the-environment')]/span")
    Hyper_text_nodenv = (By.XPATH, "//ul/li[1]/a")
    Verify_nodenv_Github = (By.XPATH, "//div[@id='repository-container-header']/div//span[1]/a")
    
    
    Hyper_text_yarn = (By.XPATH, "//ul/li[2]/a")
    Verify_yarn_doocument = (By.XPATH, "//main//h1")
    
    
    Hyper_text_rbenv = (By.XPATH, "//ul/li[3]/a")
    Verify_rbenv_Github = (By.XPATH, "//strong[@itemprop='name']/a")
    
    #Action
    def click_Start_button_Ideator(self):
        self.wait.until(EC.element_to_be_clickable(self. Start_button_Ideator)).click()
        
    
        
     #window scroll
    def click_Hyper_text_nodenv(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("window.scrollBy(0,1800);")
        time.sleep(1)  # small pause after scroll
        wait.until(EC.element_to_be_clickable(self.Hyper_text_nodenv)).click()
        
        # Wait for new tab
        wait.until(lambda d: len(d.window_handles) > 1)
    
        # Switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
    
    def get_current_url(self):
        return self.driver.current_url

    def get_nodenv_repo_name(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(
        EC.visibility_of_element_located(self.Verify_nodenv_Github)) 
        return element.text
    
    
    
    
    
    
    def click_Hyper_text_yarn(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("window.scrollBy(0,1800);")
        time.sleep(1)  # small pause after scroll
        self.wait.until(EC.element_to_be_clickable(self.Hyper_text_yarn)).click()
        
        # Wait for new tab
        wait.until(lambda d: len(d.window_handles) > 1)
    
        # Switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
       
    def get_yarn_repo_name(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.Verify_yarn_doocument))
        return element.text

    def get_current_url(self):
        return self.driver.current_url  
    
    
    
    
    
    def click_Hyper_text_rbenv(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("window.scrollBy(0,1800);")
        time.sleep(1)  # small pause after scroll
        self.wait.until(EC.element_to_be_clickable(self.Hyper_text_rbenv)).click()
        
         # Wait for new tab
        wait.until(lambda d: len(d.window_handles) > 1)
    
        # Switch to new tab
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        
    def get_rbenv_repo_name(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(self.Verify_rbenv_Github))
        return element.text
        
        
    
    
    
    
        
    