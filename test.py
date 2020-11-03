import time
import csv
import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import matplotlib.pyplot as plt

chrome_path = "/home/saiabhishek/chromedriver/chromedriver" #location of the chromedriver. change this to according to your chromedriver location
driver = webdriver.Chrome(chrome_path)

driver.get('https://www.coronatracker.com/country/india/')
time.sleep(3)
confirmed = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[1]/p[1]').text
confirmed.replace(" ","")
recovered = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[2]/p[1]').text
recovered.replace(" ","")
death = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[3]/p[1]').text
death.replace(" ","")
crit_cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[2]/div[1]/div/div/div[1]/div[2]').text
crit_cases.replace(" ","")
case_recieving_treatment = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[2]/div[2]/div/div/div[1]/div[2]').text
case_recieving_treatment.replace(" ","")
new_cases = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div/div[1]/div[2]/div/div[2]/div[1]/p[3]').text
new_cases.replace(" ","")

with open('somefile.txt', 'w') as the_file:
    the_file.write(confirmed+'\n')
    the_file.write(recovered+'\n')
    the_file.write(death+'\n')
    the_file.write(crit_cases+'\n')
    the_file.write(case_recieving_treatment+'\n')
    the_file.write(new_cases+'\n')
