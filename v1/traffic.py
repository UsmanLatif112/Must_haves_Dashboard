# Imports
from lib.driver import *
from lib import data, page, resources


# Sample Data

class TestCases:
    def __init__(self):
        self.driver = initialize_and_navigate(data.ce_traffic_url)
        self.base_page = page.HomePage(self.driver)
        self.base_page.make_csv('CE_traffic_must_haves.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    
    def login_test_cases(self):
        # Test Case 1: Invalid Login (Invalid Username and Password)
        self.driver.get(data.ce_traffic_url)
        self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys("invalid_user")
        self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys("invalid_pass")
        self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
        login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid credentials"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        
        # Test Case 2: Valid Username, Invalid Password
        self.driver.get(data.ce_traffic_url)
        self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys(data.ce_login_username)
        self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys("invalid_pass")
        self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
        login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid password"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        
        # Test Case 3: Invalid Username, Valid Password
        self.driver.get(data.ce_traffic_url)
        self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys("invalid_user")
        self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys(data.ce_login_password)
        self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
        login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid username"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password), {'Pass' if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        
        # Test Case 4: Valid Login
        self.driver.get(data.ce_traffic_url)
        self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys(data.ce_login_username)
        self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys(data.ce_login_password)
        self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
        login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login failed with valid credentials"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password), {'Pass' if login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        


    def project_crud_test_cases(self):
        # Add your project CRUD test cases here
        pass

    def campaign_crud_test_cases(self):
        # Add your campaign CRUD test cases here
        pass




# def ce_run_script():
#     driver = initialize_and_navigate(data.ce_traffic_url)
#     base_page = page.HomePage(driver)
#     campaign_name_field = base_page.wait(resources.TrafficModuleLocator.campaign_name)
#     campaign_name_field.send_keys("Test Campaign")
#     base_page.click_btn(resources.TrafficModuleLocator.campaign_category)
#     base_page.click_btn(resources.TrafficModuleLocator.campaign_sub_category)
    
    
# if __name__ == "__main__":
#     ce_run_script()
    
    