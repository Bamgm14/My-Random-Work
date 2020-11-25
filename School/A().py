from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import selenium.webdriver 


driver = webdriver.Firefox()
driver.get("http://www.google.com/")
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
# You can use (Keys.CONTROL + 't') on other OSs

# Load a page 
driver.get('http://stackoverflow.com/')
# Make the tests...

# close the tab
# (Keys.CONTROL + 'w') on other OSs.
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 


driver.close()
