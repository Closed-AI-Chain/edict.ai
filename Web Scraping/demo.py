from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os



url ="https://www.hindustantimes.com/technology/musk-asks-managers-to-recommend-employees-replaces-them-with-nominees-report-101678434104694.html"

# taking the url as input from user
url = input("Enter url of Hindustan Times article")
driver = webdriver.Chrome()

# accessing the contents or url
driver.get(url)

# scraping the title of article
title = driver.find_element(By.XPATH, '//h1[@class="hdg1"]' ).text

# scraping publishing data of article
published_on = driver.find_element(By.XPATH, '//div[@class="actionDiv flexElm topTime"]' ).text


# scraping all text from the article
scraped_content = driver.find_element(By.XPATH, '//h2[@class="sortDec"]' ).text

p_tags = driver.find_elements(By.TAG_NAME,'p')

for i in p_tags:
    scraped_content += i.text

# scraping images

image_urls = driver.find_elements(By.XPATH, '//figure/span/picture/img')

images_data = []
print(image_urls)
for i in image_urls:
    img_url = i.get_attribute("src")
    images_data.append(img_url)

driver.quit()

# printing the details
print("Title : " ,title)
print("Published ON: ", published_on[:len(published_on)-29])
print("Data : ",scraped_content)

print("Image Urls: ", images_data)






