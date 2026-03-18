Feature: Techbrain website

Scenario: Open website
    Given user opens quotes website
    Then the dashboard heading should be "Courses"

Scenario: Verify Navigation to Signup Page
    Given user opens quotes website
    When user click login button
    And user click on signup button
    Then user should be signup page

Scenario: Verify create a new account by filling signup form
    Given user opens quotes website
    When user click login button
    And user click on signup button
    And user enter email "romeo3433321@gmail.com" and password "Rider123@@##" and confirm password "Rider123@@##"
    And user click on submit button
    Then the confirmation message should be "Woops! It looks like you reached a bad page :("


Scenario: Check that each lesson in 'Intro to Ruby' opens when clicked "Next" buttons.
    Given user opens quotes website
    when user click on start button of Intro rubby courses
    Then user click on next button 

Scenario: Verify that the "Introduction to Ruby and Object-Oriented Programming" lesson opens the list of lessons.
    Given user opens quotes website
    when user click on lesson list button
    Then user verify chapter text "Chapter 1: Getting Started with Web Development"


Scenario: Verify that click on finish button of lesson "Intro Ruby "lesson.
    Given user opens quotes website
    when user click on lesson list button
    And user click on Chap 4 Ruby challenge
    And user click on finish button
    Then user Verifying idea sharing heading "Ideator - an Idea Sharing App"

Scenario: Verify that clicking "nodenv" under "Setting Environment" in "/ideator-an-idea-sharing-app/lessons" redirects to GitHub
    Given user opens quotes website
    When user click Start button Ideator
    And user click Hyper text nodenv
    Then user should be on nodenv github page

Scenario: Verify that clicking "yarn" under "Setting Environment" in "/ideator-an-idea-sharing-app/lessons" redirects to documentation page
    Given user opens quotes website
    When user click Start button Ideator
    And user click on yarn hyper text 
    Then user should be on yarn documentation page

Scenario: Verify that clicking "rbenv" under "Setting Environment" in "/ideator-an-idea-sharing-app/lessons" redirects to Github.
    Given user opens quotes website
    When user click Start button Ideator
    And user click on Hyper text rbenv
    Then user should be on rbenv github page

Scenario: Verify that automatically scrolls through all lesson pages, clicks Next until the Finish button appears, clicks it(instapost courses)
     Given user opens quotes website
     When user click on start button of instapost course
     Then user click on next button until finish button appear









    

