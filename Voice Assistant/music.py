
from selenium import webdriver
import time

# importing this to serach fo the element using its UID or Classname or anything else
from selenium.webdriver.common.by import By    



class Inflow:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def music(self, query):
        self.query = query
        self.driver.get("https://www.youtube.com/results?search_query="+query)
        time.sleep(5)  # Add a short delay to let the page load

        # Find the first video link and click on it
        first_video_link = self.driver.find_element(By.CSS_SELECTOR, "#video-title")
        first_video_link.click()

        # Wait for some time to allow the video to load
        time.sleep(10)
        
       

# assist = Inflow()
# assist.music()




