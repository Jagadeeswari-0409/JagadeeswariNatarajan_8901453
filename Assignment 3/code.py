# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the youtube.com homepage
driver.get("https://www.youtube.com")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("python for beginners")
search = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon/yt-icon-shape/icon-shape/div")
search.click()
time.sleep(6)
#Get the title of the Job page
#title = driver.title
#print("Title:", title)


# Verifying that the search results page has loaded
assert "python for beginners - YouTube" in driver.title
# Selecting a course from the search results
python_for_beginners_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string")
python_for_beginners_link.click()

# Waiting for the python course page to load
time.sleep(5)
# Sharing the video link via WhatsApp
share_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
share_link.click()

# Waiting to load
time.sleep(8)

# Clicking on WhatsApp from options
WhatsApp_button = driver.find_element("xpath", "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/ytd-unified-share-panel-renderer/div[2]/yt-third-party-network-section-renderer/div[1]/yt-third-party-share-target-section-renderer/div/div/yt-share-target-renderer[2]/button/yt-icon/yt-icon-shape/icon-shape/div")
WhatsApp_button.click()
time.sleep(6)

continue_to_chat = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[2]/div[1]/a/span")
continue_to_chat.click()
time.sleep(6)



# Closing the webdriver
driver.close()

