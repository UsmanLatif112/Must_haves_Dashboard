from imports import *
from lib.data import *


class Login:
    login_page = "//*[@class='signin-wrapper-box']"
    USERNAME = "//*[@class='signin-form-box'][contains(normalize-space(), 'Username')]/input"
    PASSWORD = "//*[@class='signin-form-box'][contains(normalize-space(), 'Password')]/input"
    LOGIN_BTN = "//*[@id='signinformsubmit']/button[contains(normalize-space(), 'Login')]" 

class MainPage:
    Main_Page = "//*[@class='bg-fafbff']"
    Menu_btn = "//*[@class='app-header']//*[@class='header-content-right']//*[@class='header-element']"