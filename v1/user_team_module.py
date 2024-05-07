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


def init_the_testing(USer_Role,team_user_name, User_name, Pass_word):
    try:
        driver = initialize_and_navigate(url)
        
        action_chains = ActionChains(driver)
        try:
            Login_Pagee = HomePage(driver)
            Login_Pagee.wait(Login.login_page)
        except:
            pass
        csvv = HomePage(driver)
        csvv.make_csv('BSWA user & team Module Report.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
        
        User_role_id = USer_Role
        role_id2 = "2"
        role_id3 = "3"
        role_id4 = "4"
        role_id5 = "5"
        print(User_role_id)
        # Enter Username.
        time.sleep(1.5)
        Username = HomePage(driver)
        Username.click_btn(Login.USERNAME)
        time.sleep(1.5)
        Username = HomePage(driver)
        Username.enter_name_delay(Login.USERNAME, User_name)
        
        # Enter Password.
        time.sleep(1.5)
        Password = HomePage(driver)
        Password.click_btn(Login.PASSWORD)
        time.sleep(1.5)
        Password = HomePage(driver)
        Password.enter_name_delay(Login.PASSWORD, Pass_word)
    
        # Enter Password.
        time.sleep(1.5)
        Login_btn = HomePage(driver)
        Login_btn.click_btn(Login.LOGIN_BTN)
        
        # main page s
        try:
                
            mainpage = HomePage(driver)
            mainpage.wait(MainPage.Main_Page)
            
            if mainpage:
                print("Successfull")
                csvv.make_csv("BSWA user & team Module Report.csv", 'Login,Login with correct username and password,Pass\n', new=False)
            else:
                print("UnSuccessfull")
                csvv.make_csv("BSWA user & team Module Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
            
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA user & team Module Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
        
        
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        
        
        try:
            User_btnn = HomePage(driver)
            User_btnn.click_btn(User_Module.User_btn)
            
            User_mainn_page = HomePage(driver)
            User_mainn_page.wait(User_Module.User_main_page)
            
            if User_mainn_page:
                print("successfull")
                csvv.make_csv("BSWA user & team Module Report.csv", 'User Module,Click on User module, Pass\n', new=False)
            else:
                print("Unsuccessfull")
                csvv.make_csv("BSWA user & team Module Report.csv", 'User Module,Click on User module, Fail\n', new=False)
        
        except: 
            print("Unsuccessfull")
            csvv.make_csv("BSWA user & team Module Report.csv", 'User Module,Click on User module, Fail\n', new=False)              

        # time.sleep(1)
        # Users_data_tablee = HomePage(driver)
        # Users_data_tablee.wait(User_Module.Users_data_table)
        
        # if Users_data_tablee:
        #     time.sleep(1)
        #     Create_User_btnn = HomePage(driver)   
        #     Create_User_btnn.click_btn(User_Module.Create_User_btn)
        # else:
        #     csvv.make_csv('BSWA user & team Module Report.csv', f'Client Modal, Client create/edit,Fail\n', new=False)
        #     pass
        #     time.sleep(2)
        #     driver.quit()    
        # time.sleep(1)
        # Users_Creation_modall = HomePage(driver)
        # Users_Creation_modall.wait(User_Module.Users_Creation_modal)

        # try:
        #     if Users_Creation_modall:
        #         time.sleep(5)
        #         Users_name_inputt = HomePage(driver)   
        #         Users_name_inputt.click_btn(User_Module.Users_name_input)
        #         time.sleep(0.5)
        #         Users_name_inputtt = HomePage(driver)
        #         Users_name_inputtt.enter_name_delay(User_Module.Users_name_input, team_user_name)
        #         time.sleep(0.5)
                
        #         # import pdb
        #         # pdb.set_trace()
        #         try:
        #             Users_rolee = HomePage(driver)   
        #             Users_rolee.click_btn(User_Module.Users_role)
        #             time.sleep(2)
        #             print(f"User_role_id: {User_role_id}")  # Print the value of User_role_id for debugging
        #             if User_role_id == role_id2:
        #                 print(f"User_role_id: {User_role_id}")
        #                 time.sleep(0.5)
        #                 Users_Role_twoo = HomePage(driver)   
        #                 Users_Role_twoo.click_btn(User_Module.Users_Role_two)
        #             elif User_role_id == role_id3:
        #                 print(f"User_role_id: {User_role_id}")
        #                 time.sleep(0.5)
        #                 Users_Role_threee = HomePage(driver)   
        #                 Users_Role_threee.click_btn(User_Module.Users_Role_three)
        #             elif User_role_id == role_id4:
        #                 print(f"User_role_id: {User_role_id}")
        #                 time.sleep(0.5)
        #                 Users_Role_fourr = HomePage(driver)   
        #                 Users_Role_fourr.click_btn(User_Module.Users_Role_four)
        #             elif User_role_id == role_id5:
        #                 print(f"User_role_id: {User_role_id}")
        #                 time.sleep(0.5)
        #                 Users_Role_fivee = HomePage(driver)   
        #                 Users_Role_fivee.click_btn(User_Module.Users_Role_five)
        #             else:
        #                 print("Invalid User_role_id:", User_role_id)  # Print a message if the User_role_id is not expected
        #         except Exception as e:
        #             print("Error:", e)  # Print the error message if any exception occurs
        #             print("No user role selected or invalid user role")
                
        #         time.sleep(0.5)
        #         Users_email_inputt = HomePage(driver)   
        #         Users_email_inputt.click_btn(User_Module.Users_email_input)
                
        #         time.sleep(0.5)
        #         Users_email_inputtt = HomePage(driver)
        #         Users_email_inputtt.enter_name_delay(User_Module.Users_email_input, f"{team_user_name}@gmail.com")
                
        #         time.sleep(0.5)
        #         Users_password_inputtt = HomePage(driver)   
        #         Users_password_inputtt.click_btn(User_Module.Users_password_input)
                
        #         time.sleep(0.5)
        #         Users_password_inputt = HomePage(driver)
        #         Users_password_inputt.enter_name_delay(User_Module.Users_password_input, "Bswa@12345")
                
        #         time.sleep(0.5)
        #         Users_C_password_inputt = HomePage(driver)   
        #         Users_C_password_inputt.click_btn(User_Module.Users_C_password_input)
                
        #         time.sleep(0.5)
        #         Users_C_password_inputtt = HomePage(driver)
        #         Users_C_password_inputtt.enter_name_delay(User_Module.Users_C_password_input, "Bswa@12345")
                
        #         time.sleep(0.5)
        #         Users_C_password_inputt = HomePage(driver)   
        #         Users_C_password_inputt.click_btn(User_Module.Users_C_password_input)
                
        #         try:
        #             time.sleep(0.5)
        #             Users_diable_buttonn = HomePage(driver)   
        #             Users_diable_buttonn.click_btn(User_Module.Users_diable_button)
        #         except:
        #             time.sleep(0.5)
        #             Users_create_buttonn = HomePage(driver)   
        #             Users_create_buttonn.click_btn(User_Module.Users_create_button)
                
        #         time.sleep(1)
        #         driver.refresh()
        #         time.sleep(1)   
                
        #         time.sleep(1)
        #         Users_data_tablee = HomePage(driver)
        #         Users_data_tablee.wait(User_Module.Users_data_table)

        #         time.sleep(1)
        #         Users_searchh = HomePage(driver)
        #         Users_searchh.wait(User_Module.Users_search)
                
        #         time.sleep(0.5)
        #         Users_searchhh = HomePage(driver)   
        #         Users_searchhh.click_btn(User_Module.Users_search)
                
        #         time.sleep(0.5)
        #         Users_search_h = HomePage(driver)
        #         Users_search_h.enter_name_delay(User_Module.Users_search, team_user_name)
                
        #         time.sleep(1)
        #         Users_data_table_e = HomePage(driver)
        #         Users_data_table_e.wait(User_Module.Users_data_table)
                
        #         if Users_data_table_e:
        #             user_row = WebDriverWait(driver, 30).until(
        #                         EC.presence_of_element_located((By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}')]"))
        #                     )
        #             # user_row = driver.find_element(By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}')]")
        #             time.sleep(1)
        #             csvv.make_csv('BSWA user & team Module Report.csv', f'User Modal, User creation with name {team_user_name},Pass\n', new=False)
        #         else:
        #             csvv.make_csv('BSWA user & team Module Report.csv', f'User Modal, User creation with name {team_user_name},Pass\n', new=False)
        # except Exception as e:
        #     print(e)
         
        import pdb
        pdb.set_trace()      
        try:
            time.sleep(0.5)
            team_btn_n = HomePage(driver)   
            team_btn_n.click_btn(Team_Module.team_btn)

            time.sleep(1)
            driver.refresh()
            time.sleep(1)

            time.sleep(1)
            team_table_e = HomePage(driver)
            team_table_e.wait(Team_Module.team_table)
            
            if team_table_e:
                time.sleep(1)
                csvv.make_csv('BSWA user & team Module Report.csv', f'Team Modal, Click on team modal button,Pass\n', new=False)
            else:
                csvv.make_csv('BSWA user & team Module Report.csv', f'Team Modal, Click on team modal button,Fail\n', new=False)
        except Exception as e:
            print(e)
                
                
                
    #     try:
            
    #         Create_Clinet_Modall = HomePage(driver)
    #         Create_Clinet_Modall.wait(Client.Create_Clinet_Modal)
            
    #         if Client_tablee:
    #             print("successfull")
    #         else:
    #             print("Unsuccessfull")
        
    #     except:
    #         print("Unsuccessfull")
    #         pass
        
    #     time.sleep(1)
    #     Client_input_feildd = HomePage(driver)   
    #     Client_input_feildd.click_btn(Client.Client_input_feild)
        
    #     time.sleep(1)
    #     Client_input_feildd = HomePage(driver)
    #     Client_input_feildd.enter_name_delay(Client.Client_input_feild, Client_name)
        
    #     time.sleep(1)
    #     Add_Client_btnn = HomePage(driver)   
    #     Add_Client_btnn.click_btn(Client.Add_Client_btn)
        
    #     time.sleep(1)
    #     driver.refresh()
    #     time.sleep(1)
        
    #     try:
            
    #         Client_tablee = HomePage(driver)
    #         Client_tablee.waittt(Client.client_page_table)
            
    #         if Client_tablee:
    #             print("successfull")
    #         else:
    #             print("Unsuccessfull")
        
    #     except:
    #         print("Unsuccessfull")
    #         pass
        
    #     time.sleep(1)
    #     Client_searchh = HomePage(driver)   
    #     Client_searchh.click_btn(Client.Client_search)
        
    #     time.sleep(1)
    #     Client_searchh = HomePage(driver)
    #     Client_searchh.enter_name_delay(Client.Client_search, Client_name)
        
    #     time.sleep(2)
    #     try:
    #         Clientt_nameee = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,f"//*[@class='client-table dataTable no-footer']//tr[contains(normalize-space(), '{Client_name}')]",)))
            
    #         if Clientt_nameee:
    #             print("successfull")
    #             csvv.make_csv("BSWA Client Module Report.csv", f'Create Client,Client created with name ({Client_name}),Pass\n', new=False)
    #         else:
    #             print("Unsuccessfull")
       
    #             csvv.make_csv("BSWA Client Module Report.csv", 'Create Client,Client creation failed,Fail\n', new=False)
    #     except:
    #         print("Unsuccessfull")
    #         pass
        
    #     # import pdb
    #     # pdb.set_trace()
    #     try:
    #         time.sleep(1)
    #         Client_edit_btn_drop = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-wrapper"]//table//tr[contains(normalize-space(), "{Client_name}")]//div[@class="assign-compaign-btn"]')
    #         time.sleep(0.5)
    #         Client_edit_btn_drop.click()
            
    #         time.sleep(0.5)
    #         Client_edit_btn = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-wrapper"]//table//tr[contains(normalize-space(), "{Client_name}")]//div[@class="assign-campaign-box"]//a[contains(normalize-space(), "Edit Client")]')
    #         time.sleep(0.5)
    #         Client_edit_btn.click()
    #     except Exception as e:
    #         print(e)
    #     time.sleep(1)
    #     Client_edit_modall = HomePage(driver)
    #     Client_edit_modall.waittt(Client.Client_edit_modal)
    #     time.sleep(1)
    #     try:
    #         if Clientt_nameee:
    #             print("successfull")
    #             csvv.make_csv("BSWA Client Module Report.csv", f'Edit Client,Click on edit client button,Pass\n', new=False)
    #         else:
    #             print("Unsuccessfull")
    #             csvv.make_csv("BSWA Client Module Report.csv", 'CEdit Client,Click on edit client button,Fail\n', new=False)
    #     except:
    #         csvv.make_csv("BSWA Client Module Report.csv", 'Edit Client,Click on edit client button,Fail\n', new=False)
    #         pass
        
    #     time.sleep(1)
    #     Client_edit_modal_feildd = HomePage(driver)   
    #     Client_edit_modal_feildd.click_btn(Client.Client_edit_modal_feild)
        
    #     time.sleep(1)
    #     action_chains.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACK_SPACE).perform()
        
    #     time.sleep(1)
    #     Client_edit_modal_feilldd = HomePage(driver)
    #     Client_edit_modal_feilldd.enter_name_delay(Client.Client_edit_modal_feild, f"{Client_name} Edited")
        
    #     time.sleep(1)
    #     Client_edit_modal_btnn = HomePage(driver)   
    #     Client_edit_modal_btnn.click_btn(Client.Client_edit_modal_btn)
        
    #     time.sleep(2)
    #     driver.refresh()
    #     time.sleep(1)
        
    #     try:
            
    #         Client_tablee = HomePage(driver)
    #         Client_tablee.waittt(Client.client_page_table)
            
    #         if Client_tablee:
    #             print("successfull")
    #         else:
    #             print("Unsuccessfull")
        
    #     except:
    #         print("Unsuccessfull")
    #         pass
        
    #     time.sleep(1)
    #     Client_searchh = HomePage(driver)   
    #     Client_searchh.click_btn(Client.Client_search)
        
    #     time.sleep(1)
    #     Client_searchh = HomePage(driver)
    #     Client_searchh.enter_name_delay(Client.Client_search, Client_name)
        
    #     time.sleep(2)
    #     try:
    #         Clientt_nameee = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,f"//*[@class='client-table dataTable no-footer']//tr[contains(normalize-space(), '{Client_name} Edited')]",)))
            
    #         if Clientt_nameee:
    #             print("successfull")
    #             csvv.make_csv("BSWA Client Module Report.csv", f'Edit Client,Client edited with name ({Client_name} Edited),Pass\n', new=False)
    #         else:
    #             print("Unsuccessfull")
       
    #             csvv.make_csv("BSWA Client Module Report.csv", 'Edit Client,Client edited,Fail\n', new=False)
    #     except:
    #         print("Unsuccessfull")
    #         pass
        
    #     time.sleep(5)
        # <button id="download-pdf-button" style="display:none;">Download PDF</button>
        
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        csvv.make_csv('BSWA user & team Module Report.csv', f'Client Modal, Client create/edit,Fail\n', new=False)
        pass
    time.sleep(2)
    driver.quit()

    time.sleep(1)
    
    result_file = 'BSWA user & team Module Report.csv'
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content