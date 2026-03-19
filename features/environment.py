from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os

def before_scenario(context, scenario):
    print("DEBUG: before_scenario is running")  # 👈 to confirm it's working

    options = Options()

    # Headless mode for CI (GitHub Actions)
    if os.getenv("HEADLESS", "true").lower() != "false":
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # Initialize driver
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()