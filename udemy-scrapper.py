from operator import imod
from queue import Empty
from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydb"]
#mycollection = mydb["courses"]

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(By.XPATH, xpath)
    except NoSuchElementException:
        return False
    return True

#getting user input
link="https://www.udemy.com/courses/search/?src=ukw&q="

query = input('Search for a course : \n') 
link+=query
#link+="&index=prod_all_launched_products_term_optimization&entityTypeDescription=Courses"

s=Service("C:\Chromedriver\chromedriver.exe")

Chrome_Options = Options()
#options.add_argument('--incognito')
#Chrome_Options.add_argument('start-maximized')
Chrome_Options.add_argument('--headless')
Chrome_Options.add_argument('user-agent=fake-useragent')
#options.headless=True

driver = webdriver.Chrome(service=s, options= Chrome_Options)

nested_Links = []

keys = ('Provider', 'Offered_By', 'Course_Name', 'Skills', 'Ratings', 'Duration', 'Price', 'Certification', 'Reviews', 'Language')
dict_data = {}
data = []
def insertIntoDict(key,value):
    #if not key in dict_data:
        dict_data[key] = value
    #else:
    #    dict_data[key].append((value))

def is_float(str):
    try:
        float(str)
        return True
    except:
        return False

def print_Func(d):
    j=0
    index = 1
    for l in d:
        if l != "":
            #text_split = l.text
            #splitted = text_split.splitlines()
            #print(l.text)
            #insertIntoDict("_id", index)
            #insertIntoDict("Provider", "Coursera")
            #insertIntoDict("Offered_By",splitted[0])
            #insertIntoDict("Course_Name",splitted[1])
            #insertIntoDict("Skills",splitted[2])
            #if(is_float(splitted[3])):
            #    duration= splitted[5].split('· ')
            #    insertIntoDict("Ratings", splitted[3])
            #    insertIntoDict("Duration",duration[2])
            #else:
            #    insertIntoDict("Ratings","None")
            #    duration= splitted[3].split('· ')
            #    insertIntoDict("Duration", duration[2])
            #data.append(dict_data)
            #dict_copy = dict_data.copy() 
            #data.append(dict_copy)
            #print(spli[0])
            print(l.text+"\n\n")
            #print(link[j].get_attribute('href')+"\n\n")
            #j+=1
            #index = index+1
        
    #for key,value in dict_data.items():
    #    print(key, value)
    #    print()
    #x = mycollection.insert_many(data)
    #print()
    #print(data)
    

def store_NestedLinks(links):
    for l in links:
        nested_Links.append(l.get_attribute('href'))


driver.get(link)
content = driver.page_source

delay1 = 10
delay2 = 3


myElem1 = WebDriverWait(driver, delay1).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='udlite-heading-sm pagination--page--13HGb']")))
number_of_pages = int(driver.find_element(By.CSS_SELECTOR, "span[class='udlite-heading-sm pagination--page--13HGb']").text)
#print(number_of_pages)

for i in range (number_of_pages-1):
    myElem1 = WebDriverWait(driver, delay1).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[class='course-card--main-content--2XqiY course-card--has-price-text--1c0ze']")))
    link_elem = driver.find_elements(By.CSS_SELECTOR, "div[class='course-card--main-content--2XqiY course-card--has-price-text--1c0ze']")
#print(link_elem.text)
    print_Func(link_elem)

    time.sleep(15)
    myElem2 = WebDriverWait(driver, delay2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-page='+1']")))
    print("Page is ready!")
    element = driver.find_element(By.CSS_SELECTOR, "a[data-page='+1']").click()
    #driver.execute_script('arguments[0].scrollIntoView(true);', element)
    #driver.execute_script('window.scrollBy(0, -200);')
    #element.click()
    print("************************Moving to page", i+2) 

            
        
#else:
#    print("No next page")


    