"""
Author:Bagiya Lakshmi S, Santhosh Kannan S P
source link: 
date: 15/10/2022
last modified:
"""



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
import csv

def write_csv(csv_path,scraped_dict,header):

    f = csv.DictWriter(open(csv_path,'a'),fieldnames=header)

    needs_header = os.stat(csv_path).st_size == 0

        # do stuff

        #if file needs a header, write headers
    if needs_header:
        f.writerow(header)
        needs_header = False

    # Then, write values
    if isinstance(scraped_dict,list):
        for i in scraped_dict:
            f.writerow(i)
    else:
        f.writerow(scraped_dict)
        




driver = webdriver.Chrome(ChromeDriverManager().install())

def get_links():
    with open('datasets/links.csv','r') as file:
        reader = csv.reader(file)
        links_list = list(reader)
    return links_list


def get_reviews(link_id):
    review_list = []
    try:
        for i in range(50):
            time.sleep(5)
            profile_name = driver.find_elements(By.XPATH,'//span[@class="a-profile-name"]')
            date = driver.find_elements(By.XPATH,'//span[@class="a-size-base a-color-secondary review-date"]')
            reviews= driver.find_elements(By.XPATH,'//span[@class="a-size-base review-text review-text-content"]/span[1]')
            reviewers_rating = driver.find_elements(By.XPATH, '//i[@data-hook="review-star-rating"]/span[@class="a-icon-alt"]')
            print(len(reviews))
            for i in range(len(reviews)):
                review_dict = {
                    "id" : link_id,
                    "name" : profile_name[i+2].get_attribute("innerHTML"),
                    "data" : date[i+2].get_attribute("innerHTML"),
                    "reviewers_rating":reviewers_rating[1].get_attribute("innerHTML").split()[0],
                    "review" : reviews[i].get_attribute("innerHTML"),
                }
                review_list.append(review_dict)
            next_page = driver.find_element(By.XPATH,'//li[@class="a-last"]')
            next_page.click()
    except Exception as e:
        print(e)
        return review_list
    else:
        return review_list

def scrap(link_id):
    title = driver.find_element(By.XPATH,'//*[@id="productTitle"]').text
    store=driver.find_element(By.XPATH,'//div[@class="a-section a-spacing-none"]/a').text 
    store_new=" ".join((store.split(' '))[2:])
    rating = driver.find_element(By.XPATH,'(//span[@class="a-icon-alt"])[1]').get_attribute('innerHTML').split()[0]
    no_rating = driver.find_element(By.XPATH,'(//span[@id="acrCustomerReviewText"])[1]').text
    info_dict = {
        "id" : link_id,
        "title" : title,
        "store" : store_new,
        "rating" : rating,
        "no_rating" : no_rating,
    }
    write_csv('datasets/data.csv',info_dict,{"id":"id","title":"title","store":"store","rating":"rating","no_rating":"no_rating"})
    
    
    try:
        show_all =  driver.find_element(By.XPATH,'//*[@id="cr-pagination-footer-0"]/a')
        show_all.click()
    except:
        show_all = driver.find_element(By.XPATH,'//a[@class="a-link-emphasis a-text-bold"]')
        show_all.click()
    
    reviews = get_reviews(link_id)
    write_csv("datasets/reviews.csv",reviews,{"id":"id","name":"name","data":"data","reviewers_rating":"reviewers_rating","review":"review"})
    
        
    
if __name__ == "__main__":
    links_list = get_links()
    link_id = 0
    while(link_id<500):
        print(links_list[link_id][0])
        driver.get(links_list[link_id][0])
        scrap(link_id)
        link_id+=1
