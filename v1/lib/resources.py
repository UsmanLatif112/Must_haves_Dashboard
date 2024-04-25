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
    
    
    
    
    
    