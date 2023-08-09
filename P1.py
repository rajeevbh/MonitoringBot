from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Provide the path to the ChromeDriver executable
chrome_driver_path = "/path/to/chromedriver"  # Replace with the actual path on your system

# Set the executable path as an environment variable
webdriver.chrome.driver = chrome_driver_path

# Set up the Selenium webdriver with Chrome driver
driver = webdriver.Chrome()

# URL of the web page with dynamic content
url = "https://quotes.toscrape.com/"

# Navigate to the web page
driver.get(url)

# Use explicit wait with element_to_be_clickable condition
wait = WebDriverWait(driver, 5)  # Wait up to 30 seconds
dynamic_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.dynamic-content')))

# Once the element is found, extract its text
dynamic_content = dynamic_element.text
print("Dynamic Content:")
print(dynamic_content)

# Close the browser window
driver.quit()
