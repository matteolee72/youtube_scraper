from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

filename = 'mothershipsg_videos_info.csv'

csv_file = open(filename, 'w', newline="", encoding="utf-8") #newline = "" to remove spaces between rows
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Views', 'Duration', 'How Long Ago'])

##### Web scrapper for infinite scrolling page #####
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.youtube.com/user/MothershipSG/videos")
def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:
        # Get old scroll position
        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(2)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

scroll_to_bottom(driver)
time.sleep(5)

videos = driver.find_elements_by_class_name('style-scope ytd-grid-video-renderer')

for video in videos:
    title = video.find_element_by_xpath('.//*[@id="video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    duration = video.find_element_by_xpath('.//*[@id="overlays"]/ytd-thumbnail-overlay-time-status-renderer/span').text
    when = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text
    print(title,views,duration,when)
    csv_writer.writerow([title,views,duration,when])
csv_file.close
