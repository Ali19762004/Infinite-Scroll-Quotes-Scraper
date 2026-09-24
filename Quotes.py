from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
all_quotes=[]
driver=webdriver.Chrome()
driver.get('https://quotes.toscrape.com/scroll')
while True:
    height=driver.execute_script('return document.body.scrollHeight;')
    before_scrolling=driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
    New_Height=driver.execute_script('return document.body.scrollHeight;')
    quotes=driver.find_elements(By.CSS_SELECTOR,'div.quote')
    for quote in quotes:
        quotes_txt=quote.find_element(By.CSS_SELECTOR,'span.text').text
        quotes_author=quote.find_element(By.CSS_SELECTOR,'small.author').text
        quotes_tags=quote.find_element(By.CSS_SELECTOR,'div.tags').text

        all_quotes.append([quotes_txt,quotes_author,quotes_tags])

    print('all_quotes')
    '''try:
        next_btn_page=driver.find_element(By.CSS_SELECTOR,'li.next a').get_attribute('href')
        driver.get(next_btn_page)
    except:
        print('all pages are collected succefully!') '''
    if  height==New_Height:
        break
with open('quotes_toscrap.csv','w',newline='',encoding='utf-8-sig') as file:
    writer=csv.writer(file)
    writer.writerow(['quote','author','tags'])
    writer.writerows(all_quotes)
print('created succefuly')    
time.sleep(5)
driver.close()
driver.quit()