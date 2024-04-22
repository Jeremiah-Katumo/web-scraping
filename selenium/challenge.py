from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep chrome browser open after program finishes running
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure chrome webdriver
driver = webdriver.Chrome()

# navigate to the (fake) newsletter registration page
driver.get("htttps://secure-retreat-92358.herokuapp.com")

# Find the first name, last name and email fields
first_name = driver.find_element(By.NAME, value="fname")
last_name = driver.find_element(By.NAME, value="lname")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Jeremy")
last_name.send_keys("Katush")
email.send_keys("jeremy@gmail.com")

# locate the signup button then click on it
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()