from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Selenium WebDriver
options = Options()
options.add_argument('--headless')  # Run in headless mode (without GUI)
service = Service('/usr/local/bin/chromedriver')  # Path to the ChromeDriver

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

print(driver.title)  # This should print "Google"
driver.quit()
