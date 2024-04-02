#how to add automation to the assistant


from selenium import webdriver
import time

# importing this to serach fo the element using its UID or Classname or anything else
from selenium.webdriver.common.by import By    

# importing this to automatically press all the keys like enter, shift etc.
from selenium.webdriver.common.keys import Keys

class Inflow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search=self.driver.find_element(By.ID,"searchInput").send_keys(self.query+Keys.ENTER)
        time.sleep(10)


# assist = Inflow()
# assist.get_info()




