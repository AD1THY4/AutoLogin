from selenium import webdriver         #importing the main selenium webdriver as in the latest selenium we dont need to download specific browsers drivers
from time import sleep    #importing sleep to delay action to view the output

driver = webdriver.Chrome()  #specifying the webdriver to be used for this automation
driver.get("https://github.com/login") # Navigate to the GitHub login page
sleep(3) # Wait for 3 seconds to allow the page to load
driver.find_element("id", "login_field").send_keys("AD1THY4") # Find the "login_field" element by its ID and enter the GitHub username
driver.find_element("id", "password").send_keys("mydogisricH123") # Find the "password" element by its ID and enter the GitHub password
driver.find_element("name", "commit").click() # Find the "commit" button element by its name and click it to log in
sleep(10) # Wait for 10 seconds (you can adjust the time as needed) to view the result
driver.quit() # Quit the webdriver, closing the browser