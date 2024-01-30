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
    check_gmb_cid_k = '(//div[@class="potential-keywords"]//li/a[@type="button"])[3]'
    Keyword_list = "//*[@class='potential-keywords']/ul/li/a"
    submit_btn = "//button[contains(normalize-space(), 'Submit for Analysis')]"
    Notification = "//*[@id='navbarSupportedContent']//ul[@class='admin-panel-list']/li/a"