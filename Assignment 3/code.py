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
#share_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
#share_link.click()

# Waiting to load
#subscribe to the video
Subscribe_link = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-smartimation/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]" )
Subscribe_link.click()
time.sleep(5)
Signin_link = driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
Signin_link.click()
time.sleep(6)
# Login to account
Account_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
time.sleep(2)
Account_link.send_keys("jaga.canada2@gmail.com")
#Enter Next
Account_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")

Account_link.click()
time.sleep(7)
#Enter Password
Password_link = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
Password_link.send_keys("savepassword")
time.sleep(3)
#Enter Next
Proceed_link = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
Proceed_link.click()
time.sleep(18)
# Verify Account signin
Verify_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[2]/button/yt-img-shadow/img")
Verify_link.click()
time.sleep(11)

# Subscribe to channel
Subscribe_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/div/ytd-subscribe-button-renderer/yt-smartimation/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
Subscribe_link.click()
time.sleep(6)

# Sharing the video link via WhatsApp
share_link = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
share_link.click()

# Waiting to load
time.sleep(5)

# Clicking on WhatsApp from options
#WhatsApp_button = driver.find_element("xpath", "/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog[2]/ytd-unified-share-panel-renderer/div[2]/yt-third-party-network-section-renderer/div[1]/yt-third-party-share-target-section-renderer/div/div/yt-share-target-renderer[2]/button/yt-icon/yt-icon-shape/icon-shape/div")
#WhatsApp_button.click()
#time.sleep(6)

# Closing the webdriver
driver.close()

