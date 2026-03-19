
import time
from behave import given, when, then
from Page1.Dashboard import Dashboard
from Page1.Signup import Signupp
from Page1.Intro_ruby_lesson import Intro_ruby
from Page1.Idea_ideator import Ideator
from Page1.Instapost import insta









#Setup
@given("user opens quotes website")
def open_site(context):
    context.driver.get("https://techbrain.ai")
    context.driver.maximize_window()
    context.dashboard = Dashboard(context.driver)
    context.signup   = Signupp(context.driver)
    context.intro_ruby = Intro_ruby(context.driver)
    context.Ideator = Ideator(context.driver)
    context.post = insta(context.driver)
    
  
    

@then('the dashboard heading should be "{expected}"')
def verify_dashboard_heading(context, expected):
    actual = context.dashboard.get_dashboard_heading()
    assert actual == expected, f"Expected '{expected}' but got '{actual}'"
        
        
#Verify Navigation to Signup Page
@when("user click login button")
def click_login_button(context):
    context.signup.click_login_button()
    time.sleep(2)
    
@when ("user click on signup button")
def click_signup_button(context):
    context.signup.click_signup_button()
    time.sleep(2)
    
@then ("user should be signup page")
def get_signup_heading(context):
    context.signup.get_signup_heading()
    time.sleep(2)


#Verify create a new account by filling signup form
@when('user enter email "{email}" and password "{password}" and confirm password "{confirm_password}"')
def fill_signup_form(context, email, password, confirm_password):
    context.signup.fill_signup_form(email, password, confirm_password)
    time.sleep(2)
    
@when ("user click on submit button")
def click_submit_button(context):
    context.signup.click_submit_button()
    time.sleep(2)
    
    
@then('the confirmation message should be "{expected}"')
def verify_confirmation(context, expected):
    actual = context.signup.get_confirmation_text()
    assert actual == expected, f"Expected '{expected}' but got '{actual}'"
    
#Check that each lesson in 'Intro to Ruby' opens when clicked "Next" buttons.
@when ("user click on start button of Intro rubby courses")
def click_start_intro_ruby(context):
    context.intro_ruby.click_start_intro_ruby()
    time.sleep(2)
 
@then ("user click on next button")
def NEXT_BUTTON(context):
    context.intro_ruby.click_all_next_buttons()
    time.sleep(2)    


#Verify that the "Introduction to Ruby and Object-Oriented Programming" lesson opens the list of lessons.
@when ("user click on lesson list button")
def click_lesson_list(context):
    context.intro_ruby.click_lesson_list()
    time.sleep(2)
       

@then('user verify chapter text "{expected}"')
def verify_chapter_text(context, expected):
    actual = context.intro_ruby.verify_chapter_text()  
    assert actual == expected, f"Expected '{expected}' but got '{actual}'"
     
#Verify that click on finish button of lesson "Intro Ruby "lesson.  
@when ("user click on Chap 4 Ruby challenge")
def click_Chap_4_Ruby_chall(context):
    context.intro_ruby.click_Chap_4_Ruby_chall()
    time.sleep(2)
    
@when ("user click on finish button")
def click_Finish_button(context):
    context.intro_ruby.click_Finish_button()
    time.sleep(2)
    

@then('user Verifying idea sharing heading "{expected}"')
def to_Verifying_idea_sharing_heading(context, expected):
    actual = context.intro_ruby.to_Verifying_idea_sharing_heading()  
    assert actual == expected, f"Expected '{expected}' but got '{actual}'"
    
@when ("user click Start button Ideator")
def click_Start_button_Ideator(context):
    context.Ideator.click_Start_button_Ideator()
    time.sleep(2)
    
@when ("user click Hyper text nodenv")
def click_Hyper_text_nodenv(context):
    context.Ideator.click_Hyper_text_nodenv()
    time.sleep(2)
    
    
@then('user should be on nodenv github page')
def verify_nodenv_url(context):
    actual_url = context.Ideator.get_current_url()
    assert "github.com/nodenv/nodenv" in actual_url, \
    f"Expected GitHub nodenv repo but got {actual_url}"


    
#Verify that clicking "yarn" under "Setting Environment" in "/ideator-an-idea-sharing-app/lessons" redirects to documentation page

@when ("user click on yarn hyper text")
def click_Hyper_text_yarn(context):
    context.Ideator.click_Hyper_text_yarn()
    time.sleep(2)
    

@then('user should be on yarn documentation page')
def verify_yarn_url(context):
    actual_url = context.Ideator.get_current_url()
    assert "classic.yarnpkg.com" in actual_url, \
        f"Expected yarn docs but got {actual_url}"  
        
        

#Verify that clicking "rbenv" under "Setting Environment" in "/ideator-an-idea-sharing-app/lessons" redirects to Github.
@when ("user click on Hyper text rbenv")
def click_Hyper_text_rbenv(context):
    context.Ideator.click_Hyper_text_rbenv()
    time.sleep(2)
    

@then('user should be on rbenv github page')
def verify_yarn_url(context):
    actual_url = context.Ideator.get_current_url()
    assert "https://github.com/rbenv/rbenv" in actual_url, \
        f"Expected GitHub rbenv repo but got {actual_url}"  
 
 
 
        
#Verify that automatically scrolls through all lesson pages, clicks Next until the Finish button appears, clicks it (instapost)
@when("user click on start button of instapost course")
def click_Start_button_instapost(context):
    context.post.click_Start_button_instapost()

@then("user click on next button until finish button appear")
def click_all_next_and_finish(context):
    context.post.click_all_next_and_finish()
    
