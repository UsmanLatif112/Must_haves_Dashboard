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


def init_the_testing(Client_name, User_name, Pass_word):
    try:
        urll = "https://app.brandsignals.io/"
        driver = initialize_and_navigate(urll)
        
        action_chains = ActionChains(driver)
        try:
            Login_Pagee = HomePage(driver)
            Login_Pagee.wait5(Login.login_page)
        except:
            pass
        csvv = HomePage(driver)
        csvv.make_csv('BSWA Client Module Report.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
        
        # Enter Username.
        Username = HomePage(driver)
        Username.click_btn(Login.USERNAME)
        time.sleep(0.5)
        Username = HomePage(driver)
        Username.enter_Name(Login.USERNAME, User_name)
        
        # Enter Password.
        time.sleep(0.5)
        Password = HomePage(driver)
        Password.click_btn(Login.PASSWORD)
        time.sleep(0.5)
        Password = HomePage(driver)
        Password.enter_Name(Login.PASSWORD, Pass_word)
    
        # Enter Password.
        time.sleep(0.5)
        Login_btn = HomePage(driver)
        Login_btn.click_btn(Login.LOGIN_BTN)
        
        # main page s
        try:
                
            mainpage = HomePage(driver)
            mainpage.wait5(MainPage.Main_Page)
            
            if mainpage:
                print("Successfull")
                csvv.make_csv("BSWA Client Module Report.csv", 'Login,Login with correct username and password,Pass\n', new=False)
            else:
                print("UnSuccessfull")
                csvv.make_csv("BSWA Client Module Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
            
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Client Module Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        try:
            Client_btnn = HomePage(driver)
            Client_btnn.click_btn(Client.Client_btn)
            Clinet_mainn_page = HomePage(driver)
            Clinet_mainn_page.wait5(Client.Clinet_main_page)
            
            if Clinet_mainn_page:
                print("successfull")
                csvv.make_csv("BSWA Client Module Report.csv", 'Client Module,Click on client module,Pass\n', new=False)
            else:
                print("Unsuccessfull")
                csvv.make_csv("BSWA Client Module Report.csv", 'Client Module,Click on client module,Fail\n', new=False)
        except: 
            print("Unsuccessfull")
            csvv.make_csv("BSWA Client Module Report.csv", 'Client Module,Click on client module,Fail\n', new=False)              
        
        try:
            
            Client_tablee = HomePage(driver)
            Client_tablee.wait5e(Client.client_page_table)
            
            if Client_tablee:
                print("successfull")
            else:
                print("Unsuccessfull")
        
        except:
            print("Unsuccessfull")
            pass
        
        time.sleep(0.5)
        Create_Cient_btnn = HomePage(driver)   
        Create_Cient_btnn.click_btn(Client.Create_Client_btn)
        
        try:
            
            Create_Clinet_Modall = HomePage(driver)
            Create_Clinet_Modall.wait5(Client.Create_Clinet_Modal)
            
            if Client_tablee:
                print("successfull")
            else:
                print("Unsuccessfull")
        
        except:
            print("Unsuccessfull")
            pass
        
        time.sleep(0.5)
        Client_input_feildd = HomePage(driver)   
        Client_input_feildd.click_btn(Client.Client_input_feild)
        
        time.sleep(0.5)
        Client_input_feildd = HomePage(driver)
        Client_input_feildd.enter_Name(Client.Client_input_feild, Client_name)
        
        time.sleep(0.5)
        Add_Client_btnn = HomePage(driver)   
        Add_Client_btnn.click_btn(Client.Add_Client_btn)
        
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        
        try:
            
            Client_tablee = HomePage(driver)
            Client_tablee.wait5e(Client.client_page_table)
            
            if Client_tablee:
                print("successfull")
            else:
                print("Unsuccessfull")
        
        except:
            print("Unsuccessfull")
            pass
        
        time.sleep(1)
        Client_searchh = HomePage(driver)   
        Client_searchh.click_btn(Client.Client_search)
        
        time.sleep(1)
        Client_searchh = HomePage(driver)
        Client_searchh.enter_Name(Client.Client_search, Client_name)
        
        time.sleep(2)
        try:
            Clientt_nameee = WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH,f"//*[@class='client-table dataTable no-footer']//tr[contains(normalize-space(), '{Client_name}')]",)))
            
            if Clientt_nameee:
                print("successfull")
                csvv.make_csv("BSWA Client Module Report.csv", f'Create Client,Client created with name ({Client_name}),Pass\n', new=False)
            else:
                print("Unsuccessfull")
       
                csvv.make_csv("BSWA Client Module Report.csv", 'Create Client,Client creation failed,Fail\n', new=False)
        except:
            print("Unsuccessfull")
            pass
        try:
            time.sleep(0.5)
            Client_edit_btn_drop = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-wrapper"]//table//tr[contains(normalize-space(), "{Client_name}")]//div[@class="assign-compaign-btn"]')
            time.sleep(0.5)
            Client_edit_btn_drop.click()
            time.sleep(0.5)
            Client_edit_btn = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-wrapper"]//table//tr[contains(normalize-space(), "{Client_name}")]//div[@class="assign-campaign-box"]//a[contains(normalize-space(), "Edit Client")]')
            time.sleep(0.5)
            Client_edit_btn.click()
        except Exception as e:
            print(e)
        time.sleep(0.5)
        Client_edit_modall = HomePage(driver)
        Client_edit_modall.waittt(Client.Client_edit_modal)
        time.sleep(0.5)
        try:
            if Clientt_nameee:
                print("successfull")
                csvv.make_csv("BSWA Client Module Report.csv", f'Edit Client,Click on edit client button,Pass\n', new=False)
            else:
                print("Unsuccessfull")
                csvv.make_csv("BSWA Client Module Report.csv", 'CEdit Client,Click on edit client button,Fail\n', new=False)
        except:
            csvv.make_csv("BSWA Client Module Report.csv", 'Edit Client,Click on edit client button,Fail\n', new=False)
            pass
        
        time.sleep(0.5)
        Client_edit_modal_feildd = HomePage(driver)   
        Client_edit_modal_feildd.click_btn(Client.Client_edit_modal_feild)
        
        time.sleep(0.5)
        action_chains.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        
        time.sleep(0.5)
        Client_edit_modal_feilldd = HomePage(driver)
        Client_edit_modal_feilldd.enter_Name(Client.Client_edit_modal_feild, f"{Client_name} Edited")
        
        time.sleep(0.5)
        Client_edit_modal_btnn = HomePage(driver)   
        Client_edit_modal_btnn.click_btn(Client.Client_edit_modal_btn)
        
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        
        try:
            
            Client_tablee = HomePage(driver)
            Client_tablee.wait5e(Client.client_page_table)
            
            if Client_tablee:
                print("successfull")
            else:
                print("Unsuccessfull")
        
        except:
            print("Unsuccessfull")
            pass
        
        time.sleep(0.5)
        Client_searchh = HomePage(driver)   
        Client_searchh.click_btn(Client.Client_search)
        
        time.sleep(0.5)
        Client_searchh = HomePage(driver)
        Client_searchh.enter_Name(Client.Client_search, Client_name)
        
        time.sleep(0.5)
        try:
            Clientt_nameee = WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH,f"//*[@class='client-table dataTable no-footer']//tr[contains(normalize-space(), '{Client_name} Edited')]",)))
            
            if Clientt_nameee:
                print("successfull")
                csvv.make_csv("BSWA Client Module Report.csv", f'Edit Client,Client edited with name ({Client_name} Edited),Pass\n', new=False)
            else:
                print("Unsuccessfull")
       
                csvv.make_csv("BSWA Client Module Report.csv", 'Edit Client,Client edited,Fail\n', new=False)
        except:
            print("Unsuccessfull")
            pass
        
        time.sleep(1)
        # <button id="download-pdf-button" style="display:none;">Download PDF</button>
        
        try:
            driver.get("https://app.brandsignals.io/campaign/create/")
            Create_cam = HomePage(driver)
            Create_cam.wait5e(Client.Create_cam_pag)
            time.sleep(0.5)
            time.sleep(0.5)
            Client_search_cam = HomePage(driver)   
            Client_search_cam.click_btn(Client.Client_search_ca)
            time.sleep(0.5)
            Client_search_ca_inn = HomePage(driver)   
            Client_search_ca_inn.click_btn(Client.Client_search_ca_in)
            time.sleep(0.5)
            Client_search_ca_in_n = HomePage(driver)
            Client_search_ca_in_n.enter_Name(Client.Client_search_ca_in, Client_name)
            try:
                Client_search_ca_in_nn = WebDriverWait(driver, 5000).until(EC.visibility_of_element_located((By.XPATH,f'//*[@class="select2-container select2-container--default select2-container--open"]//*[@class="select2-results"][contains(normalize-space(), "{Client_name}")]',)))
                
                if Client_search_ca_in_nn:
                    print("successfull")
                    csvv.make_csv("BSWA Client Module Report.csv", f'Campaign creation,Client in campaign creation select client drop down,Pass\n', new=False)
                else:
                    print("Unsuccessfull")
        
                    csvv.make_csv("BSWA Client Module Report.csv", 'Campaign creation,Client in campaign creation select client drop down,Fail\n', new=False)
            except:
                print("Unsuccessfull")
                pass
        except Exception as e:
            print(f"An exception occurred: {e}")   
        
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        csvv.make_csv('BSWA Client Module Report.csv', f'Client Modal, Client create/edit,Fail\n', new=False)
        pass
    time.sleep(1)
    driver.quit()

    time.sleep(0.5)
    
    result_file = 'BSWA Client Module Report.csv'
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content