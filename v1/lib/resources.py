from imports import *
from lib.data import *


class Login:
    login_page = "//*[@class='signin-wrapper-box']"
    USERNAME = "//*[@class='signin-form-box'][contains(normalize-space(), 'Username')]/input"
    PASSWORD = "//*[@class='signin-form-box'][contains(normalize-space(), 'Password')]/input"
    LOGIN_BTN = "//*[@id='signinformsubmit']/button[contains(normalize-space(), 'Login')]" 

class MainPage:
    Main_Page = "//*[@class='campaign-listing-wrapper']"
    Menu_btn = "//*[@class='app-header']//*[@class='header-content-right']//*[@class='header-element']"

class QuickAnalysispage:
    main_buttion = '//*[@class="nav-item"]/a[contains(normalize-space(), "Quick Analysis")]'
    create_q_cam_page = '//*[@class="add-compaign-wrapper"]'
    gmb_cid_feild = '//*[@placeholder="Enter GMB CID"]'
    business_location = '//p[@id="business-location"]/span'
    check_gmb_cid = '//button[contains(normalize-space(), "Check")]'
    check_gmb_cid_incorrect = '//div[@class="potential-keywords"]//ul[contains(normalize-space(), "Incorrect CID, Please try again")]'
    check_gmb_cid_k = '(//div[@class="potential-keywords"]//li/a[@type="button"])[3]'
    Keyword_list = "//*[@class='potential-keywords']/ul/li/a"
    submit_btn = "//button[contains(normalize-space(), 'Submit for Analysis')]"
    Notification = "//*[@id='navbarSupportedContent']//ul[@class='admin-panel-list']/li/a"
    key_feild = "//input[@class='tagsinputfield']"
    Quick_tab = "//button[@id='campaign-tab06']"
    Edit_Quick_tab = "//*[@class='add-compaign-inner'][contains(normalize-space(), 'Edit Campaign')]"
    Edit_Quick_Cam = "//*[@placeholder='Campaign Name']"
    Key_count = "//*[@class='bootstrap-tagsinput']/input"
    Quick_tab_table = "//div[@id='campaign-tab-content06']//tbody/tr//td[@class=' mdc-data-table__cell']/div/h6"
    re_button = "//*[@id='campaignbtnresubmit']"
    Cam_tab_button = "//a[@id='campaignbuttonfordisablenavbar'][contains(normalize-space(), 'Campaigns')]"
    delete_modal = '//*[@class="modal-content"][contains(normalize-space(), "Are you sure you want to delete this campaign")]'
    delete_modal_btn = '//*[@class="modal-footer"]//button[@onclick="Delete_confirm_the_Campaign()"][contains(normalize-space(), "Yes")]'
    

class Client:
    Client_btn = "//*[@class='nav-link'][contains(normalize-space(), 'Clients')]"
    Clinet_main_page = "//*[@class='campaign-listing-wrapper']//h2[contains(normalize-space(), 'Clients')]"
    Create_Client_btn = "//*[@class='create-new-campaign-btn mobile-hide']//a[contains(normalize-space(), 'New Client')]"
    Create_Clinet_Modal = "//*[@class='modal-header']//*[contains(normalize-space(), 'Add New Client')]"
    Client_input_feild = "//*[@class='modal-body']//input[@id='client_name'][@placeholder = 'Client Name']"
    Add_Client_btn = "//*[@class='modal-footer']/button[contains(normalize-space(), 'Add Client')]"
    client_page_table = "//*[@class='client-table dataTable no-footer']//tr[2]"
    Client_search = "//*[@class='campaign-listing-wrapper'][contains(normalize-space(), 'Clients')]//input[@id='searchText']"
    Client_search_result = "//*[@class='client-table dataTable no-footer']//tr[contains(normalize-space(), 'Usman SQA new')]"
    Client_edit_btn_drop = '//*[@class="campaign-listing-wrapper"]//table//tr[contains(normalize-space(), "Usman SQA new")]//div[@class="assign-compaign-btn"]'
    Client_edit_btn = '//*[@class="campaign-listing-wrapper"]//table//tr[contains(normalize-space(), "Usman SQA new")]//div[@class="assign-campaign-box"]//a[contains(normalize-space(), "Edit Client")]'
    Client_edit_modal = '//*[@class="modal-header"][contains(normalize-space(), "Edit Client")]'
    Client_edit_modal_feild = '//*[@class="modal-content"][contains(normalize-space(), "Client Name")]//input[@id="client_name-edit-id"]'
    Client_edit_modal_btn = '//*[@class="modal-dialog"][contains(normalize-space(), "Edit Client")]//button[contains(normalize-space(), "Submit")]'

class User_Module:
    User_btn = "//*[@class='nav-link'][contains(normalize-space(), 'Users')]"
    User_main_page = "//*[@class='campaign-listing-wrapper']//h2[contains(normalize-space(), 'Users')]"
    Create_User_btn = "//*[@class='create-new-campaign-btn mobile-hide']//a[contains(normalize-space(), 'New User')]"
    Users_data_table = "(//*[@class='tab-content campaign-listing-content']//tr)[2]"
    Users_Creation_modal = '//*[@class="modal-header agent-header"][contains(normalize-space(), "Add New User")]'
    Users_name_input = '//*[@class="modal-body"]//*[@id="user_username"][@placeholder="User Name"]'
    Users_role = '//*[@class="modal-body"]//*[@class="campiagn-input-field"][@name="role_id"]'
    Users_email_input = '//*[@class="modal-body"]//*[@class="campiagn-input-field"][@placeholder="Enter Email"]'
    Users_password_input = '//*[@class="modal-body"]//*[@class="campiagn-input-field"][@id="password"]'
    Users_C_password_input = '//*[@class="modal-body"]//*[@class="campiagn-input-field"][@id="password1"]'
    Users_Create_btn = '//*[@class="modal-footer"]//button[contains(normalize-space(), "Add User")]'
    Users_Role_two = '//*[@class="modal-body"]//*[@class="campiagn-input-field"]//option[@value="2,admin"]'
    Users_Role_three = '//*[@class="modal-body"]//*[@class="campiagn-input-field"]//option[@value="3,manager"]'
    Users_Role_four = '//*[@class="modal-body"]//*[@class="campiagn-input-field"]//option[@value="4,user"]'
    Users_Role_five = '//*[@class="modal-body"]//*[@class="campiagn-input-field"]//option[@value="5,reporting_user"]'
    Users_diable_button = '//*[@class="modal-footer"]//button[@disabled="disabled"][contains(normalize-space(), "Add User")]'
    Users_create_button = '//*[@class="modal-footer"]//button[contains(normalize-space(), "Add User")]'
    Users_search = '//*[@class="campaign-listing-wrapper"]//*[@id="searchText"]'
    Users_delete_modal = "//*[@class='modal-content']//*[@class='modal-footer']//button[contains(normalize-space(), 'Yes')]"

class Team_Module:
    team_btn = '//*[@class="nav-link"][contains(normalize-space(), "Teams")]'
    team_table = '(//*[@class="campaign-listing-wrapper"]//tbody/tr)[2]'
    Create_team_btn = '(//*[@class="campaign-listing-wrapper"]//tbody/tr)[2]'
    Create_team_btn = '//*[@class="campaign-listing-wrapper"]//a[contains(normalize-space(), "Create Team")]'
    Create_team_modal = '//*[@class="modal-content"][contains(normalize-space(), "Create Team")]'
    Team_name_feild = '//*[@class="modal-content"]//input[@id="team_username"]'
    Team_pr_manager_feild = '//*[@class="modal-content"]//select[@id="primary-manager"]'
    Team_sc_manager_feild = '//*[@class="modal-content"]//select[@id="secondary-manager"]'
    Team_desc_feild = '//*[@class="modal-content"]//*[@id="desc"]'
    Team_create_btnn = '//*[@class="modal-content"]//button[contains(normalize-space(), "Create")]'
    Team_search_feild = '//*[@class="campaign-listing-inner"]//input[@id="searchText"]'
    Team_assign_modal = '//*[@class="modal-content"]//*[@class="modal-header"][contains(normalize-space(), "Assign User")]'
    Team_assign_user_drp_modal = '//*[@class="modal-content"]//*[@class="modal-body"]//*[@id="assigner-User"]'
    Team_assign_user_drp_modal_btn = '//*[@class="modal-content"]//*[@class="modal-footer"]//button[contains(normalize-space(), "Assign")]'
    Team_detail_page = '//*[@class="campaign-listing-wrapper"][contains(normalize-space(), "Team Details")]'
    Team_detail_page_assign_user = '//*[@class="campaign-listing-wrapper"][contains(normalize-space(), "Team Details")]//div[@class="create-new-campaign-btn mobile-hide"]/a[contains(normalize-space(), "Assign User")]'
    Team_detail_page_srch = '//*[@class="campaign-listing-inner"]//input[@id="searchText"]'
    

class TrafficModuleLocator:
    login_user = '//*[@id="id_login"]'
    login_password = '//*[@id="id_password"]'
    login_btn = '//*[@id = "loginButton"]'
    main_content = '//div[@id="main-content"]'
    
    campaign_name = '//*[@id="id_campaign_name"]'
    campaign_category = '//*[@id="id_campaign_category"]'
    campaign_category_option = '//option[text()="{campaign_type}"]'
    campaign_sub_category = '//*[@id="id_campaign_types"]'
    campaign_sub_category_option = '//select[@id="id_campaign_types"]//option[text()="{campaign_sub_type}"]'
    campaign_country = '//*[@id="select2-id_country-container"]'
    campaign_country_option = '//li[text() = "UNITED STATES"]'
    campaign_state = '//*[@id="id_state_iso_3"]'
    campaign_city = '//*[@id="id_city"]'
    campaign_mobile_proxy_percentage = '//*[(@id="id_mobile_proxy_percentage")]'
    campaign_average_session = '//*[@id="id_num_searches"]'
    campaign_frequency = '//*[@id="id_frequency"]'
    
    campaign_image_base64 = '//div[@style=""]//textarea[@id="id_extra_attr_base64"]'
    campaign_image_url = '//div[@style=""]//*[(@id = "id_extra_attr_url")]'
    campaign_is_spread_session = '//div[@style=""]//*[(@id="id_is_spread_session")]'
    campaign_brand_name = '//div[@style=""]//*[(@id = "id_brand_name")]'
    campaign_select_wildcard_type_option = '//div[@style=""]//div[@id="home_page_div"]'
    campaign_is_product = '//div[@style=""]//input[@name="is_product"]'
    
    campaign_keyword_modifiers = '//div[@id="div_id_keyword_modifiers" and @style=""]//tags'
    campaign_direct_url = '//div[@id="div_id_direct_url" and @style=""]//tags'
    campaign_wildcard_strign = '//div[@id="div_id_wildcard_string" and @style=""]//tags'
    campaign_tier1_url = '//div[@id="div_id_tier_1_urls" and @style=""]//tags'
    campaign_tier2_url = '//div[@id="div_id_tier_2_urls" and @style=""]//tags'
    campaign_destination_url = '//div[@id="div_id_destination_urls" and @style=""]//tags'
    campaign_tier1_url_textarea = '//textarea[@name="tier_1_urls"]'
    campaign_tier2_url_textarea = '//textarea[@name="tier_2_urls"]'
    campaign_destination_url_textarea = '//textarea[@name="destination_urls"]'
    campaign_wildcard_strign_textarea = '//textarea[@name="wildcard_string"]'
    campaign_direct_url_textarea = '//textarea[@name="direct_url"]'
    campaign_keyword_modifiers_textarea = '//textarea[@name="keyword_modifiers"]'
    
    
    campaign_create_submit_btn = '//button[@id="campaign-form-submit"]'
    campaign_create_btn = '//a[text() = "Create Campaign"]'
    campaing_edit_btn = '//a[@href = "/campaign/edit/{campaign_id}/"]'
    campaign_edit_name_input = '//input[@value="{campaign_name}"]'
    campaign_edit_save_btn = '//button[@id="campaign-form-submit"]'
    campaign_cancel_btn = '//button[text()="Cancel"]'
    campaing_delete_btn = '//a[@hx-get="/campaign/delete_campaign/{campaign_id}/"]'
    capmaign_delete_modal_btn = '//button[text()="Yes, delete it!"]'
    campaign_live_btn = '//a[contains(@hx-get, "/campaign/update_campaign_status/{campaign_id}/")]'
    cancel_status = '//span[@class = "cancel-status"]'
    live_status = '//span[@class = "success-status"]'
    
    campaign_create_check = '//div[contains(@class, "campaign-row")]//a[text()="{campaign_name}"]'
    capmaign_view_check = '//div[@id="div_id_campaign_name"]//input[@value="{campaign_name}"]'
    
    
    project_create_btn = '//button[@data-bs-target="#createProject"]'
    project_create_name_input = '//form[@hx-target="#createProject"]//input[@id="id_project_name"]'
    project_create_modal_btn = '//form[@hx-target="#createProject"]//button[@type="submit"]'
    project_created_list_check = '//a[@href="/projects/{project_id}/"]'
    project_view_check = '//div[@id="campaign_table"]'
    project_edit_btn = '//a[contains(@data-bs-target, "#editProject-{project_id}")]'
    project_edit_name_input = '//input[@value="{project_name}"]'
    project_edit_modal_btn = '//form[@hx-post="/projects/edit/{project_id}/"]//button[@type="submit"]'
    project_edit_check = '//div[contains(text(), "{edited_project_name}")]'
    project_delete_btn = '//a[@hx-get="/projects/delete/{project_id}/"]'
    project_delete_modal_btn = '//button[text()="Yes, delete it!"]'
    project_delete_check = '//div[@id="campaign_table"]'
    project_deleted_list_check = '//a[@href="/projects/{project_id}/"]'
    
    
    report_project_filter = '//select[@id="selectProject"]'
    report_project_filter_option = '//select[@id="selectProject"]//option'
    report_campaign_filter = '//select[@id="campaignSelect"]'
    report_campaign_filter_option = '//select[@id="campaignSelect"]//option'
    filter_all = '//select[@id="campaignSelectstatus"]'
    filter_all_option = '//select[@id="campaignSelectstatus"]//option'
    filter_all_success_option = '//select[@id="campaignSelectstatus"]//option[text()="Success"]'
    report_result_row = '//tr[@class="odd"]'
    
    
    campaign_error_page_row = '//div[./div[./a[contains(@href, "/campaign/detail/")]]]'
    campaign_link = '//a[contains(@href, "/campaign/detail/")]'
    campaing_error_filter = '//select'
    campaing_error_filter_option = '//option[text()="Today"]'
    
    
    




# time.sleep(1)
        # driver.refresh()
        # time.sleep(2)
        
        
        # try:
        #     User_btnn = HomePage(driver)
        #     User_btnn.click_btn(User_Module.User_btn)
            
        #     User_mainn_page = HomePage(driver)
        #     User_mainn_page.wait(User_Module.User_main_page)
            
        #     if User_mainn_page:
        #         print("successfull")
        #     else:
        #         print("Unsuccessfull")

        # except: 
        #     print("Unsuccessfull")              

        # time.sleep(1)
        # Users_data_tablee = HomePage(driver)
        # Users_data_tablee.wait(User_Module.Users_data_table)
        
        # if Users_data_tablee:
        #     time.sleep(1)
        #     Create_User_btnn = HomePage(driver)   
        #     Create_User_btnn.click_btn(User_Module.Create_User_btn)
        # else:
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
        #         Users_name_inputtt.enter_name_delay(User_Module.Users_name_input, f"{team_user_name}_3")
        #         time.sleep(0.5)
                
        #         try:
        #             Users_rolee = HomePage(driver)   
        #             Users_rolee.click_btn(User_Module.Users_role)
        #             time.sleep(2)
        #             print(f"User_role_id:3")  # Print the value of User_role_id for debugging
        #             time.sleep(0.5)
        #             Users_Role_threee = HomePage(driver)   
        #             Users_Role_threee.click_btn(User_Module.Users_Role_three)
        #         except Exception as e:
        #             print("Invalid User_role_id:")  # Print a message if the User_role_id is not expected
        #             print("Error:", e)  # Print the error message if any exception occurs
        #             print("No user role selected or invalid user role")
                
        #         time.sleep(0.5)
        #         Users_email_inputt = HomePage(driver)   
        #         Users_email_inputt.click_btn(User_Module.Users_email_input)
                
        #         time.sleep(0.5)
        #         Users_email_inputtt = HomePage(driver)
        #         Users_email_inputtt.enter_name_delay(User_Module.Users_email_input, f"{team_user_name}_3@gmail.com")
                
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
        #         Users_search_h.enter_name_delay(User_Module.Users_search, f"{team_user_name}_3")
                
        #         time.sleep(1)
        #         Users_data_table_e = HomePage(driver)
        #         Users_data_table_e.wait(User_Module.Users_data_table)
                
        #         if Users_data_table_e:
        #             user_row = WebDriverWait(driver, 30).until(
        #                         EC.presence_of_element_located((By.XPATH, f"(//*[@class='tab-content campaign-listing-content']//tr)[2][contains(normalize-space(), '{team_user_name}_3')]"))
        #                     )
        #             time.sleep(1)
        #         else:
        #             pass
        # except Exception as e:
        #     print(e)