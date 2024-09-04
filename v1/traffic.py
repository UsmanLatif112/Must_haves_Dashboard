# Imports
from lib.driver import *
from lib import data, page, resources


# Sample Data
project_name = "-AI-TEST-PROJECT-SQA"
edited_project_name = "-AI-TEST-PROJECT-SQA-EDITED"
project_id = None

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
        
        self.driver.get(data.ce_project_listing_page)
        
        # Test Case 1: Create Project
        self.base_page.click_btn(resources.TrafficModuleLocator.project_create_btn)
        self.base_page.wait(resources.TrafficModuleLocator.project_create_name_input).send_keys(project_name)
        self.base_page.click_btn(resources.TrafficModuleLocator.project_create_modal_btn)
        project_created = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project creation failed"
        project_id = self.driver.current_url.split("/")[-2]
        self.driver.get(data.ce_project_listing_page)
        project_found_in_listing = self.base_page.wait(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id)), "Project creation failed"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Create Project, {"Pass" if project_created[0] and project_found_in_listing[0] else f"Fail - {project_created[1]}"}\n', new=False)
        
        # Test Case 2: View Project
        self.driver.get(data.ce_project_listing_page)
        self.base_page.click_btn(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id))
        project_viewed = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project view failed"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        
        # Test Case 3: Edit Project
        self.driver.get(data.ce_project_listing_page)
        self.base_page.click_btn(resources.TrafficModuleLocator.project_edit_btn.format(project_id=project_id))
        project_edit_input = self.base_page.wait(resources.TrafficModuleLocator.project_edit_name_input.format(project_name=project_name))
        project_edit_input.clear()
        project_edit_input.send_keys(edited_project_name)
        self.base_page.click_btn(resources.TrafficModuleLocator.project_edit_modal_btn.format(project_id=project_id))
        project_edited = self.base_page.wait(resources.TrafficModuleLocator.project_edit_check.format(edited_project_name=edited_project_name)), "Project edit failed"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Edit Project, {"Pass" if project_edited[0] else f"Fail - {project_edited[1]}"}\n', new=False)
        
        # Test Case 4: Delete Project
        self.base_page.click_btn(resources.TrafficModuleLocator.project_delete_btn.format(project_id=project_id))
        self.base_page.click_btn(resources.TrafficModuleLocator.project_delete_modal_btn)
        project_deleted = not self.base_page.wait(resources.TrafficModuleLocator.project_deleted_list_check.format(project_id=project_id)), "Project deletion failed"
        self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Delete Project, {"Pass" if project_deleted else f"Fail - {project_deleted[1]}"}\n', new=False)

    def campaign_crud_test_cases(self):
        # Add your campaign CRUD test cases here
        pass
    
    def full_dashboard_must_haves(self):
        self.login_test_cases()
        self.project_crud_test_cases()



# def ce_run_script():
#     driver = initialize_and_navigate(data.ce_traffic_url)
#     base_page = page.HomePage(driver)
#     campaign_name_field = base_page.wait(resources.TrafficModuleLocator.campaign_name)
#     campaign_name_field.send_keys("Test Campaign")
#     base_page.click_btn(resources.TrafficModuleLocator.campaign_category)
#     base_page.click_btn(resources.TrafficModuleLocator.campaign_sub_category)
    
    
# if __name__ == "__main__":
#     project_crud_test_cases()
    
    