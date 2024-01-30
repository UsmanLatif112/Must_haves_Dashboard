import requests
import csv
from csv import reader
import time
from flask import  request
from lib.driver import *
from imports import *
from lib.resources import *
from lib.page import *
from lib.data import *


def init_the_testing(GMB_cid, User_name, Pass_word):
    driver = initialize_and_navigate(url)
    
    
    Login_Pagee = HomePage(driver)
    Login_Pagee.wait(Login.login_page)
    
    # Enter Username.
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.click_btn(Login.USERNAME)
    time.sleep(0.5)
    Username = HomePage(driver)
    Username.enter_name_delay(Login.USERNAME, User_name)
    
    # Enter Password.
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.click_btn(Login.PASSWORD)
    time.sleep(0.5)
    Password = HomePage(driver)
    Password.enter_name_delay(Login.PASSWORD, Pass_word)
   
   # Enter Password.
    time.sleep(0.5)
    Login_btn = HomePage(driver)
    Login_btn.click_btn(Login.LOGIN_BTN)
    
    # main page 
    mainpage = HomePage(driver)
    mainpage.wait(MainPage.Main_Page)
    
    if mainpage:
        print("Successfull")
    else:
        print("UnSuccessfull")
    
    csvv = HomePage(driver)
    csvv.make_csv('BSWA Quick Analysis Report.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Pass\n', new=False)
    
    
    driver.quit()
    
    result_file = 'BSWA Quick Analysis Report.csv'
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content
    