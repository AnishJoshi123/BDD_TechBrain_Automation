from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


def before_scenario(context, scenario):
    options = Options()

    # Headless mode by default (can be disabled with HEADLESS=false)
    if os.getenv("HEADLESS", "true").lower() != "false":
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    # FIX: Use webdriver-manager to install ChromeDriver automatically
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    context.driver.implicitly_wait(10)


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()