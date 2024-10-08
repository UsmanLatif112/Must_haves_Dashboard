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

        time.sleep(1)
        Users_data_tablee = HomePage(driver)
        Users_data_tablee.waitx(User_Module.Users_data_table)
        
        if Users_data_tablee:
            time.sleep(1)
            Create_User_btnn = HomePage(driver)   
            Create_User_btnn.click_btn(User_Module.Create_User_btn)
        else:
            csvv.make_csv('BSWA user & team Module Report.csv', f'User Module, User create/edit,Fail\n', new=False)
            pass
            time.sleep(2)
            driver.quit()    
        time.sleep(1)
        Users_Creation_modall = HomePage(driver)
        Users_Creation_modall.wait(User_Module.Users_Creation_modal)

        try:
            if Users_Creation_modall:
                time.sleep(5)
                Users_name_inputt = HomePage(driver)   
                Users_name_inputt.click_btn(User_Module.Users_name_input)
                time.sleep(0.5)
                Users_name_inputtt = HomePage(driver)
                Users_name_inputtt.enter_name_delay(User_Module.Users_name_input, team_user_name)
                time.sleep(0.5)
                
                # import pdb
                # pdb.set_trace()
                try:
                    Users_rolee = HomePage(driver)   
                    Users_rolee.click_btn(User_Module.Users_role)
                    time.sleep(2)
                    print(f"User_role_id: {User_role_id}")  # Print the value of User_role_id for debugging
                    if User_role_id == role_id2:
                        print(f"User_role_id: {User_role_id}")
                        time.sleep(0.5)
                        Users_Role_twoo = HomePage(driver)   
                        Users_Role_twoo.click_btn(User_Module.Users_Role_two)
                    elif User_role_id == role_id3:
                        print(f"User_role_id: {User_role_id}")
                        time.sleep(0.5)
                        Users_Role_threee = HomePage(driver)   
                        Users_Role_threee.click_btn(User_Module.Users_Role_three)
                    elif User_role_id == role_id4:
                        print(f"User_role_id: {User_role_id}")
                        time.sleep(0.5)
                        Users_Role_fourr = HomePage(driver)   
                        Users_Role_fourr.click_btn(User_Module.Users_Role_four)
                    elif User_role_id == role_id5:
                        print(f"User_role_id: {User_role_id}")
                        time.sleep(0.5)
                        Users_Role_fivee = HomePage(driver)   
                        Users_Role_fivee.click_btn(User_Module.Users_Role_five)
                    else:
                        print("Invalid User_role_id:", User_role_id)  # Print a message if the User_role_id is not expected
                except Exception as e:
                    print("Error:", e)  # Print the error message if any exception occurs
                    print("No user role selected or invalid user role")
                
                time.sleep(0.5)
                Users_email_inputt = HomePage(driver)   
                Users_email_inputt.click_btn(User_Module.Users_email_input)
                
                time.sleep(0.5)
                Users_email_inputtt = HomePage(driver)
                Users_email_inputtt.enter_name_delay(User_Module.Users_email_input, f"{team_user_name}@gmail.com")
                
                time.sleep(0.5)
                Users_password_inputtt = HomePage(driver)   
                Users_password_inputtt.click_btn(User_Module.Users_password_input)
                
                time.sleep(0.5)
                Users_password_inputt = HomePage(driver)
                Users_password_inputt.enter_name_delay(User_Module.Users_password_input, "Bswa@12345")
                
                time.sleep(0.5)
                Users_C_password_inputt = HomePage(driver)   
                Users_C_password_inputt.click_btn(User_Module.Users_C_password_input)
                
                time.sleep(0.5)
                Users_C_password_inputtt = HomePage(driver)
                Users_C_password_inputtt.enter_name_delay(User_Module.Users_C_password_input, "Bswa@12345")
                
                time.sleep(0.5)
                Users_C_password_inputt = HomePage(driver)   
                Users_C_password_inputt.click_btn(User_Module.Users_C_password_input)
                
                try:
                    time.sleep(0.5)
                    Users_diable_buttonn = HomePage(driver)   
                    Users_diable_buttonn.click_btn(User_Module.Users_diable_button)
                except:
                    time.sleep(0.5)
                    Users_create_buttonn = HomePage(driver)   
                    Users_create_buttonn.click_btn(User_Module.Users_create_button)
                
                time.sleep(1)
                driver.refresh()
                time.sleep(1)   
                
                time.sleep(1)
                Users_data_tablee = HomePage(driver)
                Users_data_tablee.wait(User_Module.Users_data_table)

                time.sleep(1)
                Users_searchh = HomePage(driver)
                Users_searchh.wait(User_Module.Users_search)
                
                time.sleep(0.5)
                Users_searchhh = HomePage(driver)   
                Users_searchhh.click_btn(User_Module.Users_search)
                
                time.sleep(0.5)
                Users_search_h = HomePage(driver)
                Users_search_h.enter_name_delay(User_Module.Users_search, team_user_name)
                
                time.sleep(1)
                Users_data_table_e = HomePage(driver)
                Users_data_table_e.wait(User_Module.Users_data_table)
                
                if Users_data_table_e:
                    user_row = WebDriverWait(driver, 30).until(
                                EC.presence_of_element_located((By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}')]"))
                            )
                    # user_row = driver.find_element(By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}')]")
                    time.sleep(1)
                    csvv.make_csv('BSWA user & team Module Report.csv', f'User Module, User creation with name {team_user_name},Pass\n', new=False)
                else:
                    csvv.make_csv('BSWA user & team Module Report.csv', f'User Module, User creation with name {team_user_name},Pass\n', new=False)
        except Exception as e:
            print(e)
            
            
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
            else:
                print("Unsuccessfull")
        except: 
            print("Unsuccessfull")            

        time.sleep(1)
        Users_data_tablee = HomePage(driver)
        Users_data_tablee.wait(User_Module.Users_data_table)
        
        if Users_data_tablee:
            time.sleep(1)
            Create_User_btnn = HomePage(driver)   
            Create_User_btnn.click_btn(User_Module.Create_User_btn)
        else:
            pass
            time.sleep(2)
            driver.quit()    
        time.sleep(1)
        Users_Creation_modall = HomePage(driver)
        Users_Creation_modall.wait(User_Module.Users_Creation_modal)

        try:
            if Users_Creation_modall:
                time.sleep(5)
                Users_name_inputt = HomePage(driver)   
                Users_name_inputt.click_btn(User_Module.Users_name_input)
                time.sleep(0.5)
                Users_name_inputtt = HomePage(driver)
                Users_name_inputtt.enter_name_delay(User_Module.Users_name_input, f"{team_user_name}_5")
                time.sleep(0.5)
                try:
                    Users_rolee = HomePage(driver)   
                    Users_rolee.click_btn(User_Module.Users_role)
                    time.sleep(2)
                    print(f"User_role_id:5")  # Print the value of User_role_id for debugging
                    time.sleep(0.5)
                    Users_Role_fivee = HomePage(driver)   
                    Users_Role_fivee.click_btn(User_Module.Users_Role_five)
        
                except Exception as e:
                    print("Invalid User_role_id:")  # Print a message if the User_role_id is not expected
                    print("Error:", e)  # Print the error message if any exception occurs
                    print("No user role selected or invalid user role")
                
                time.sleep(0.5)
                Users_email_inputt = HomePage(driver)   
                Users_email_inputt.click_btn(User_Module.Users_email_input)
                
                time.sleep(0.5)
                Users_email_inputtt = HomePage(driver)
                Users_email_inputtt.enter_name_delay(User_Module.Users_email_input, f"{team_user_name}_5@gmail.com")
                
                time.sleep(0.5)
                Users_password_inputtt = HomePage(driver)   
                Users_password_inputtt.click_btn(User_Module.Users_password_input)
                
                time.sleep(0.5)
                Users_password_inputt = HomePage(driver)
                Users_password_inputt.enter_name_delay(User_Module.Users_password_input, "Bswa@12345")
                
                time.sleep(0.5)
                Users_C_password_inputt = HomePage(driver)   
                Users_C_password_inputt.click_btn(User_Module.Users_C_password_input)
                
                time.sleep(0.5)
                Users_C_password_inputtt = HomePage(driver)
                Users_C_password_inputtt.enter_name_delay(User_Module.Users_C_password_input, "Bswa@12345")
                
                time.sleep(0.5)
                Users_C_password_inputt = HomePage(driver)   
                Users_C_password_inputt.click_btn(User_Module.Users_C_password_input)
                
                try:
                    time.sleep(0.5)
                    Users_diable_buttonn = HomePage(driver)   
                    Users_diable_buttonn.click_btn(User_Module.Users_diable_button)
                except:
                    time.sleep(0.5)
                    Users_create_buttonn = HomePage(driver)   
                    Users_create_buttonn.click_btn(User_Module.Users_create_button)
                
                time.sleep(1)
                driver.refresh()
                time.sleep(1)   
                
                time.sleep(1)
                Users_data_tablee = HomePage(driver)
                Users_data_tablee.wait(User_Module.Users_data_table)

                time.sleep(1)
                Users_searchh = HomePage(driver)
                Users_searchh.wait(User_Module.Users_search)
                
                time.sleep(0.5)
                Users_searchhh = HomePage(driver)   
                Users_searchhh.click_btn(User_Module.Users_search)
                
                time.sleep(0.5)
                Users_search_h = HomePage(driver)
                Users_search_h.enter_name_delay(User_Module.Users_search, f"{team_user_name}_5")
                
                time.sleep(1)
                Users_data_table_e = HomePage(driver)
                Users_data_table_e.wait(User_Module.Users_data_table)
                
                if Users_data_table_e:
                    try:
                        user_row = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}_5')]"))
                                )
                        time.sleep(1)
                        delete_user = driver.find_element(By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}_5')]/td[@class=' mdc-data-table__cell'][5]")
                        time.sleep(1)
                        delete_user.click()
                        delete_user_btn = driver.find_element(By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}_5')]/td[@class=' mdc-data-table__cell'][5]//a[@href='#']")
                        time.sleep(0.5)
                        delete_user_btn.click()
                        time.sleep(0.5)
                        
                        user_delete_modal = WebDriverWait(driver, 30).until(
                                    EC.presence_of_element_located((By.XPATH, "//*[@class='modal-title'][contains(normalize-space(), 'Are you sure you want to delete this user?')]"))
                                )
                        
                        time.sleep(0.5)
                        Users_searchhh = HomePage(driver)   
                        Users_searchhh.click_btn(User_Module.Users_delete_modal)
                        
                        time.sleep(1)
                        driver.refresh()
                        time.sleep(1)   
                        
                        time.sleep(1)
                        Users_data_tablee = HomePage(driver)
                        Users_data_tablee.waitx(User_Module.Users_data_table)

                        time.sleep(1)
                        Users_searchh = HomePage(driver)
                        Users_searchh.wait(User_Module.Users_search)
                        
                        time.sleep(0.5)
                        Users_searchhh = HomePage(driver)   
                        Users_searchhh.click_btn(User_Module.Users_search)
                        
                        time.sleep(0.5)
                        Users_search_h = HomePage(driver)
                        Users_search_h.enter_name_delay(User_Module.Users_search, f"{team_user_name}_5")
                        try:
                            user_delete_modal = WebDriverWait(driver, 30).until(
                                        EC.presence_of_element_located((By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}_5')]"))
                                    )
                        except:
                            csvv.make_csv('BSWA user & team Module Report.csv', f'Delete User,User deleteion with name {team_user_name}_5,Pass\n', new=False)
                    except:
                        csvv.make_csv('BSWA user & team Module Report.csv', f'Delete User,User deleteion with name {team_user_name}_5,Fail\n', new=False)
                else:
                    csvv.make_csv('BSWA user & team Module Report.csv', f'Delete User,User deleteion with name {team_user_name}_5,Fail\n', new=False)
                    
                
        except Exception as e:
            print(e)
        
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        
        # try:
        #     time.sleep(0.5)
        #     team_btn_n = HomePage(driver)   
        #     team_btn_n.click_btn(Team_Module.team_btn)

        #     time.sleep(1)
        #     driver.refresh()
        #     time.sleep(1)

        #     time.sleep(1)
        #     team_table_e = HomePage(driver)
        #     team_table_e.wait(Team_Module.team_table)
               
        #     time.sleep(0.5)
        #     create_team_btn_n = HomePage(driver)   
        #     create_team_btn_n.click_btn(Team_Module.Create_team_btn)
            
        #     time.sleep(1)
        #     team_tablee_e = HomePage(driver)
        #     team_tablee_e.wait(Team_Module.Create_team_modal)
        #     if team_tablee_e:
        #         print("successfull")
        #         csvv.make_csv("BSWA user & team Module Report.csv", 'Team Module, Click on team Module button,Pass\n', new=False)
        #     else:
        #         print("unsuccessfull")
        #         csvv.make_csv("BSWA user & team Module Report.csv", 'Team Module, Click on team Module button,Fail\n', new=False)
            
        #     time.sleep(0.5)
        #     Team_name_feildd = HomePage(driver)   
        #     Team_name_feildd.click_btn(Team_Module.Team_name_feild)
        #     time.sleep(0.5)
        #     Team_name_feilddd = HomePage(driver)
        #     Team_name_feilddd.enter_name_delay(Team_Module.Team_name_feild, f"{team_user_name}_Team")
            
        #     time.sleep(2)
        #     # Locate the dropdown element by its ID, name, or any other selector
        #     dropdown_element = driver.find_element(By.XPATH, Team_Module.Team_pr_manager_feild)

        #     # Create a Select object
        #     select = Select(dropdown_element)

        #     # Get all options in the dropdown
        #     options = select.options

        #     # Skip the first element and select a random element from the remaining ones
        #     if len(options) > 1:
        #         random_option = random.choice(options[1:])
        #         select.select_by_visible_text(random_option.text)
        #         print(f"Selected option: {random_option.text}")
        #     else:
        #         print("Dropdown has insufficient options to select a random one.")
            
        #     time.sleep(2)
        #     # Locate the dropdown element by its ID, name, or any other selector
        #     dropdown_element = driver.find_element(By.XPATH, Team_Module.Team_sc_manager_feild)

        #     # Create a Select object
        #     select = Select(dropdown_element)

        #     # Get all options in the dropdown
        #     options = select.options

        #     # Skip the first element and select a random element from the remaining ones
        #     if len(options) > 1:
        #         random_option = random.choice(options[1:])
        #         select.select_by_visible_text(random_option.text)
        #         print(f"Selected option: {random_option.text}")
        #     else:
        #         print("Dropdown has insufficient options to select a random one.")
                
        #     time.sleep(0.5)
        #     Team_desc_feildd = HomePage(driver)   
        #     Team_desc_feildd.click_btn(Team_Module.Team_desc_feild)
        #     time.sleep(0.5)
        #     Team_desc_feilddd = HomePage(driver)
        #     Team_desc_feilddd.enter_name_delay(Team_Module.Team_desc_feild, "Team description is coming soon")
                
        #     time.sleep(0.5)
        #     Team_create_btnnn = HomePage(driver)   
        #     Team_create_btnnn.click_btn(Team_Module.Team_create_btnn)
                
            
        #     time.sleep(2)
            
        #     time.sleep(1)
        #     driver.refresh()
        #     time.sleep(1)
            
        #     time.sleep(1)
        #     Team_search_feildd = HomePage(driver)
        #     Team_search_feildd.wait(Team_Module.Team_search_feild)
            
        #     time.sleep(0.5)
        #     Team_search_feild_d = HomePage(driver)   
        #     Team_search_feild_d.click_btn(Team_Module.Team_search_feild)
            
        #     time.sleep(0.5)
        #     Team_search_feild_dd = HomePage(driver)
        #     Team_search_feild_dd.enter_name_delay(Team_Module.Team_search_feild, f"{team_user_name}_Team")
            
        #     try:
        #         Team_search_data = WebDriverWait(driver, 30).until(
        #                     EC.presence_of_element_located((By.XPATH, f'//*[@class="campaign-listing-inner"]//tbody//tr[contains(normalize-space(), "{team_user_name}_Team")]'))
        #                 )
        #         if Team_search_data:
        #             csvv.make_csv('BSWA user & team Module Report.csv', f'Team module,Team creation with name {team_user_name}_Team,Pass\n', new=False)
        #     except:
        #         csvv.make_csv('BSWA user & team Module Report.csv', f'Team module,Team creation with name {team_user_name}_Team,Fail\n', new=False)
        #     try:
        #         try:
                    
        #             team_assign = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-inner"]//tbody//tr[contains(normalize-space(), "{team_user_name}_Team")]/td[5]') 
        #             time.sleep(0.5)
        #             team_assign.click()
        #             time.sleep(1)
        #             team_assign_drp = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-inner"]//tbody//tr[contains(normalize-space(), "{team_user_name}_Team")]/td[5]//a[contains(normalize-space(), "Assign User")]') 
        #             time.sleep(0.5)
        #             team_assign.click()
        #             time.sleep(1)
        #         except:
        #             print("Failed")
                
        #         time.sleep(1)
        #         Team_assign_modal_l = HomePage(driver)
        #         Team_assign_modal_l.wait(Team_Module.Team_assign_modal)
                
        #         time.sleep(2)
        #         # Locate the dropdown element by its ID, name, or any other selector
        #         dropdown_element = driver.find_element(By.XPATH, Team_Module.Team_assign_user_drp_modal)

        #         # Create a Select object
        #         select = Select(dropdown_element)

        #         # Get all options in the dropdown
        #         options = select.options

        #         # Skip the first element and select a random element from the remaining ones
        #         if len(options) > 1:
        #             random_option = random.choice(options[1:])
        #             select.select_by_visible_text(random_option.text)
        #             print(f"Selected option: {random_option.text}")
        #         else:
        #             print("Dropdown has insufficient options to select a random one.")
                
        #         time.sleep(0.5)
        #         Team_assign_user_drp_modal_btn_n = HomePage(driver)   
        #         Team_assign_user_drp_modal_btn_n.click_btn(Team_Module.Team_assign_user_drp_modal_btn)
                
        #         time.sleep(2)
        #         team_table_e_e = HomePage(driver)
        #         team_table_e_e.wait(Team_Module.team_table)
                
        #         time.sleep(1)
        #         driver.refresh()
        #         time.sleep(1)
                
        #         time.sleep(1)
        #         Team_search_feildd = HomePage(driver)
        #         Team_search_feildd.wait(Team_Module.Team_search_feild)
                
        #         time.sleep(0.5)
        #         Team_search_feild_d = HomePage(driver)   
        #         Team_search_feild_d.click_btn(Team_Module.Team_search_feild)
                
        #         time.sleep(0.5)
        #         Team_search_feild_dd = HomePage(driver)
        #         Team_search_feild_dd.enter_name_delay(Team_Module.Team_search_feild, f"{team_user_name}_Team")

        #         Team_search_data = WebDriverWait(driver, 30).until(
        #                     EC.presence_of_element_located((By.XPATH, f'//*[@class="campaign-listing-inner"]//tbody//tr[contains(normalize-space(), "{team_user_name}_Team")]'))
        #                 )
        #         try:
        #             team_assign_n = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-inner"]//tbody//tr[contains(normalize-space(), "{team_user_name}_Team")]/td[5]') 
        #             time.sleep(0.5)
        #             team_assign_n.click()
        #             time.sleep(1)
        #             team_assign_drp = driver.find_element(By.XPATH, f'//*[@class="campaign-listing-inner"]//tbody//tr[contains(normalize-space(), "{team_user_name}_Team")]/td[5]//a[contains(normalize-space(), "View Team")]') 
        #             time.sleep(0.5)
        #             team_assign_drp.click()
        #         except:
        #             pass
        #         time.sleep(1)
        #         Team_search_feildd_d = HomePage(driver)
        #         Team_search_feildd_d.wait(Team_Module.Team_detail_page)
                
        #         time.sleep(0.5)
        #         Team_detail_page_srch_h = HomePage(driver)   
        #         Team_detail_page_srch_h.click_btn(Team_Module.Team_detail_page_srch)
                
        #         time.sleep(0.5)
        #         Team_detail_page_srch_h_h = HomePage(driver)
        #         Team_detail_page_srch_h_h.enter_name_delay(Team_Module.Team_detail_page_srch, f"{random_option.text}")
                
        #         time.sleep(1)
        #         Team_search_feildd_d = HomePage(driver)
        #         Team_search_feildd_d.wait(Team_Module.Team_detail_page)
                
        #         try:
        #             user_nameew = driver.find_element(By.XPATH, '//*[@class="campaign-listing-inner"]//tbody/tr[contains(normalize-space(), "random_option.text")]')
        #             if user_nameew:
        #                 csvv.make_csv('BSWA user & team Module Report.csv', f'Team module,User ({random_option.text})assigned to team from actions button,Pass\n', new=False)
        #         except:
        #             csvv.make_csv('BSWA user & team Module Report.csv', f'Team module,User ({random_option.text})assigned to team from actions button,Fail\n', new=False)
        #         # random_option.text
                
                
                
                
        #         # time.sleep(0.5)
        #         # Team_detail_page_assign_user_r = HomePage(driver)   
        #         # Team_detail_page_assign_user_r.click_btn(Team_Module.Team_detail_page_assign_user)
        #     except Exception as e:
        #         print(e)    
                
        # except Exception as e:
        #     print(e)
        
        
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        csvv.make_csv('BSWA user & team Module Report.csv', f'User Module, User create/edit,Fail\n', new=False)
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