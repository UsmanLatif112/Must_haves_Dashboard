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
    actions = ActionChains(driver)
    try:
        Login_Pagee = HomePage(driver)
        Login_Pagee.wait(Login.login_page)
    except:
        pass
    csvv = HomePage(driver)
    csvv.make_csv('BSWA Quick Analysis Report.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    
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
    try:
            
        mainpage = HomePage(driver)
        mainpage.wait(MainPage.Main_Page)
        
        if mainpage:
            print("Successfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Pass\n', new=False)
        else:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
        
    except:
        print("UnSuccessfull")
        csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
    
    
    time.sleep(0.5)
    main_buttion = HomePage(driver)
    main_buttion.click_btn(QuickAnalysispage.main_buttion)
    
    # main page 
    try:
            
        create_q_cam_page = HomePage(driver)
        create_q_cam_page.wait(QuickAnalysispage.create_q_cam_page)
        
        if create_q_cam_page:
            print("Successfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis page button,Pass\n', new=False)
        else:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis page button,Fail\n', new=False)
        
    except:
        print("UnSuccessfull")
        csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis page button,Fail\n', new=False)
    
    time.sleep(0.5)
    gmb_cid_feild = HomePage(driver)
    gmb_cid_feild.click_btn(QuickAnalysispage.gmb_cid_feild)
    
    time.sleep(0.5)
    gmb_cid_feild = HomePage(driver)
    gmb_cid_feild.enter_name_delay(QuickAnalysispage.gmb_cid_feild, GMB_cid)
    
    time.sleep(0.5)
    check_gmb_cid = HomePage(driver)
    check_gmb_cid.click_btn(QuickAnalysispage.check_gmb_cid)
    
    try:
            
        check_gmb_cid_k = HomePage(driver)
        check_gmb_cid_k.waittt(QuickAnalysispage.check_gmb_cid_k)
        
        if check_gmb_cid_k:
            print("Successfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Pass\n', new=False)
        else:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Fail\n', new=False)
        
    except:
        print("UnSuccessfull")
        csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Fail\n', new=False)
    
    time.sleep(1)
    actions.send_keys(Keys.PAGE_DOWN).perform()
    
    Keyword_list = HomePage(driver)
    time.sleep(2)
    Keyword_list = HomePage.get_key_words(driver)
    
    business_name = driver.find_element(By. XPATH, QuickAnalysispage.business_location)
    time.sleep(2)
    submit_btn = HomePage(driver)
    submit_btn.click_btn(QuickAnalysispage.submit_btn)
    
    time.sleep(0.5)
    driver.refresh()
    time.sleep(0.5)
    
    try:
        while True:

            time.sleep(5)
            time.sleep(0.5)
            driver.refresh()
            time.sleep(0.5)
            Noti = HomePage(driver)
            Noti.click_btn(QuickAnalysispage.Notification)
            time.sleep(0.5)
            Notifications = f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {business_name.text} quick analysis completed.')]/h6"
            Noti =driver.find_element(By.XPATH, Notifications)
            if Noti:
                print("Successfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", f'Create quick analysis campaign,Create quick analysis campaign {Noti.text},Pass\n', new=False)
                break
            else:
                print("fail")
                
    except:
        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Create quick analysis campaign,Create quick analysis campaign with correct data,fail\n', new=False)
        pass
    
    
    
    
    
    
    
    driver.quit()
    
    
    result_file = 'BSWA Quick Analysis Report.csv'
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content
    