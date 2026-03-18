from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import StaleElementReferenceException


class Intro_ruby:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    START_INTRO_RUBY = (By.XPATH, "//a[contains(@href,'goals-of-the-intro-course')]")
    NEXT_BUTTON = (By.XPATH, "//form//button[@type='submit']")
    
    lesson_list_button = (By.XPATH, "//a[contains(@href,'introduction-to-ruby-and-object-oriented-programming')]/span[text()='Lists']")
    Chapter_text = (By.XPATH, "//h2[contains(text(), 'Chapter 1: Getting Started with Web Development')]")
    

    Chap_4_Ruby_chall = (By.XPATH, "//div[4]/h3[5]/a")
    Finish_button = (By.XPATH, "//button[@type='submit']/span")
    Verifying_idea_sharing_heading = (By.XPATH, "//div/div[2]/h2")
    
    
    click_quiz = (By.XPATH, "//a[contains(@href,'quiz')]")
   

    # Actions
    def click_start_intro_ruby(self):
        self.wait.until(EC.element_to_be_clickable(self.START_INTRO_RUBY)).click()

    
    def click_all_next_buttons(self):
        while True:
            try:
                # Re-locate the element EVERY iteration, don't reuse old reference
                next_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NEXT_BUTTON)
                )
                next_btn.click()
                time.sleep(1)
            except (TimeoutException, StaleElementReferenceException):
                break  # No more next buttons
      
 
    def click_lesson_list(context):
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.element_to_be_clickable(context.lesson_list_button)).click()


    def verify_chapter_text(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Chapter_text)) 
        return element.text  # return the text
    
    
    def click_Chap_4_Ruby_chall(self):
        self.wait.until(EC.element_to_be_clickable(self.Chap_4_Ruby_chall)).click()
    
    def click_Finish_button(self):
        self.wait.until(EC.element_to_be_clickable(self. Finish_button)).click()
        
    def to_Verifying_idea_sharing_heading(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Verifying_idea_sharing_heading)) 
        return element.text  # return the text
    
    
    
    
    

    
    def To_click_quiz(self):
        self.wait.until(EC.element_to_be_clickable(self.click_quiz)).click()
    
    