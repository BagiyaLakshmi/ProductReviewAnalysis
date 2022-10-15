"""
Author:Bagiya Lakshmi S, Santhosh Kannan S P
source link: 
date: 15/10/2022
last modified:
"""



from re import S, X
from telnetlib import XASCII
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
import csv

def write_csv(scraped_list):

    f = csv.writer(open('datasets/data.csv','a'))

    needs_header = os.stat('datasets/data.csv').st_size == 0

        # do stuff

        #if file needs a header, write headers
    if needs_header:
        f.writerow(["title","store","rating","no_rating","reviews"])
        needs_header = False

    # Then, write values
    f.writerow(scraped_list)




driver = webdriver.Chrome(ChromeDriverManager().install())

def get_links():
    with open('datasets/links.csv','r') as file:
        reader = csv.reader(file)
        links_list = list(reader)
    return links_list


def get_reviews():
    review_list = []
    try:
        for i in range(10):
            profile_name = driver.find_elements(By.XPATH,'//span[@class="a-profile-name"]')
            date = driver.find_elements(By.XPATH,'//span[@class="a-size-base a-color-secondary review-date"]')
            reviews= driver.find_elements(By.XPATH,'//span[@class="a-size-base review-text review-text-content"]/span[1]')
            print(len(reviews))
            for i in range(len(reviews)):
                review_dict = {
                    "name" : profile_name[i+2].get_attribute("innerHTML"),
                    "data" : date[i+2].get_attribute("innerHTML"),
                    "review" : reviews[i].get_attribute("innerHTML"),
                }
                review_list.append(review_dict)
            next_page = driver.find_element(By.XPATH,'//li[@class="a-last"]').click()
    except:
        return review_list
    else:
        return review_list

def scrap():
    title = driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
    store=driver.find_element(By.XPATH,'//div[@class="a-section a-spacing-none"]/a').text 
    store_new=" ".join((store.split(' '))[2:])

    # rating = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[9]/div[4]/div[4]/div[3]/div/span[1]/span/span[1]/a/i[1]/span')
    # rating = driver.find_element(By.XPATH,'(//i[@class="a-icon a-icon-star a-star-4-5"]/span[@class="a-icon-alt"])[1]').get_attribute("innerHTML").split()[0]
    rating = driver.find_element(By.XPATH,'(//span[@class="a-icon-alt"])[1]').get_attribute('innerHTML').split()[0]
    no_rating = driver.find_element(By.XPATH,'(//span[@id="acrCustomerReviewText"])[1]').text
    try:
        show_all =  driver.find_element(By.XPATH,'//*[@id="cr-pagination-footer-0"]/a')
        show_all.click()
    except:
        show_all = driver.find_element(By.XPATH,'//a[@class="a-link-emphasis a-text-bold"]')
        show_all.click()
        
    reviews = get_reviews()
    write_csv([title, store_new, rating, no_rating, reviews])
    
        
    
if __name__ == "__main__":
    links_list = get_links()
    for link in links_list[:10]:
        print(link[0])
        driver.get(link[0])
        scrap()
