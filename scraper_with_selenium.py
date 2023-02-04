import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv


driver = webdriver.Chrome('chromedriver 3') #your individual driver url
driver.get('https://plugandplayai_placeholder'); #research data url goes here, removed due to compliance reasons

driver.implicitly_wait(3)

#accept cookies
l=driver.find_element("xpath", '//*[@id="cookie_action_close_header"]')
l.click()


driver.implicitly_wait(15)

#load all members

i=1
button_exists=True
while(button_exists):
#while(i < 2):
    try:
        load_all_button = driver.find_element("xpath", '/html/body/div[2]/div/section[2]/div/div/div/div/div/div/div/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/button')
        load_all_button.click()
        print("Clicked pagination button in Test Nr. " + str(i))
        driver.implicitly_wait(15)
    except:
        print("No more pagination buttons in Test Nr. " + str(i))
        button_exists=False
        
    i = i+1
    

#Get Data
member_links_cleanurl = []
member_links = driver.find_elements(By.CLASS_NAME, "site-preview")
for member in member_links:
    link=member.get_attribute('data-href')
    link=link[0:link.find("TB_iframe")]
    print(link)
    member_links_cleanurl.append(link)


#Data 2 CSV
with open('ki_companies.csv', 'w+') as f:
    write = csv.writer(f)
    for link in member_links_cleanurl:
        print("Schreibe Zeile > " + link)
        write.writerow([link])

driver.quit() 
