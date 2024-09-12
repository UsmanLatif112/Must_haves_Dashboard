# Imports
import json
import random
from lib.driver import *
from lib import data, page, resources
from traffic_sample_data import *



class TrafficBase:
    def add_tagify_data(self, base_page, campaign, driver):
        
        if "wildcard_string" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_strign)
            base_page.send_key_with_action_chain(wildcard_field, campaign_wildcard_string)
            time.sleep(2)
            
        if "tier1_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url)
            base_page.send_key_with_action_chain(wildcard_field, campaign_tier1_url)
            time.sleep(2)
            
        if "tier2_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url)
            base_page.send_key_with_action_chain(wildcard_field, campaign_tier2_url)
            time.sleep(2)

        if "destination_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_destination_url)
            base_page.send_key_with_action_chain(wildcard_field, campaign_destination_url)
            time.sleep(2)
            
        if "keyword_modifiers" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers)
            base_page.send_key_with_action_chain(wildcard_field, campaign_keyword_modifiers)
            time.sleep(2)

        if "direct_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_direct_url)
            base_page.send_key_with_action_chain(wildcard_field, campaign_direct_url)
            time.sleep(2)
            
    def add_input_field_data(self, base_page, campaign, driver):

        if "image_base64_code" in campaign["fields"]:
            base_page.wait(resources.TrafficModuleLocator.campaign_image_base64).send_keys(campaign_image_base64)
        if "image_url" in campaign["fields"]:
            base_page.wait(resources.TrafficModuleLocator.campaign_image_url).send_keys(campaign_image_url)
        if "is_spread_session" in campaign["fields"]:
            base_page.click_btn(resources.TrafficModuleLocator.campaign_is_spread_session)
        if "brand_name" in campaign["fields"]:
            base_page.wait(resources.TrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
        if "select_wildcard_type_option" in campaign["fields"]:
            base_page.click_btn(resources.TrafficModuleLocator.campaign_select_wildcard_type_option)
        if "is_product" in campaign["fields"]:
            base_page.click_btn(resources.TrafficModuleLocator.campaign_is_product)
        if "gmb_cid" in campaign["fields"]:
            base_page.wait(resources.TrafficModuleLocator.campaign_gmb_cid).send_keys(campaign_gmb_cid)
        if "geo_latitude" in campaign["fields"]:
            base_page.wait(resources.TrafficModuleLocator.campaign_geo_latitude).send_keys(campaign_geo_latitude)
        if "geo_longitude" in campaign["fields"]:
            base_page.wait(resources.TrafficModuleLocator.campaign_geo_longitude).send_keys(campaign_geo_longitude)

    def edit_tagify_data(self, base_page, campaign, driver):
        
        if "wildcard_string" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_strign)
            base_page.click_btn(resources.TrafficModuleLocator.wildcard_string_xpath.format(wildcard_string=campaign_wildcard_string[-1]))
            base_page.send_key_with_action_chain(wildcard_field, campaign_wildcard_string_edited)
            time.sleep(2)

        if "tier1_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url)
            base_page.click_btn(resources.TrafficModuleLocator.tiered_1_url_xpath.format(tier_1_url=campaign_tier1_url[-1]))
            base_page.send_key_with_action_chain(wildcard_field, campaign_tier1_url_edited)
            time.sleep(2)

        if "tier2_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url)
            base_page.click_btn(resources.TrafficModuleLocator.tiered_2_url_xpath.format(tier_2_url=campaign_tier2_url[-1]))
            base_page.send_key_with_action_chain(wildcard_field, campaign_tier2_url_edited)
            time.sleep(2)


        if "destination_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_destination_url)
            base_page.click_btn(resources.TrafficModuleLocator.destination_url_xpath.format(destination_url=campaign_destination_url[-1]))
            base_page.send_key_with_action_chain(wildcard_field, campaign_destination_url_edited)
            time.sleep(2)
            
        if "keyword_modifiers" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers)
            base_page.click_btn(resources.TrafficModuleLocator.keyword_modifiers_xpath.format(keyword_modifiers=campaign_keyword_modifiers[-1]))
            base_page.send_key_with_action_chain(wildcard_field, campaign_keyword_modifiers_edited)
            time.sleep(2)

        if "direct_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_direct_url)
            base_page.click_btn(resources.TrafficModuleLocator.direct_url_xpath.format(direct_url=campaign_direct_url[-1]))
            base_page.send_key_with_action_chain(wildcard_field, campaign_direct_url_edited)
            time.sleep(2)
            
    def edit_input_field_data(self, base_page, campaign, driver):
        
        if "image_base64_code" in campaign["fields"]:
            image_base64_field = base_page.wait(resources.TrafficModuleLocator.campaign_image_base64)
            image_base64_field.clear()
            image_base64_field.send_keys(campaign_image_base64_edited)
            
        if "image_url" in campaign["fields"]:
            image_url_field = base_page.wait(resources.TrafficModuleLocator.campaign_image_url)
            image_url_field.clear()
            image_url_field.send_keys(campaign_image_url_edited)
            
        if "brand_name" in campaign["fields"]:
            brand_name_field = base_page.wait(resources.TrafficModuleLocator.campaign_brand_name)
            brand_name_field.clear()
            brand_name_field.send_keys(campaign_brand_name_edited)
            
        base_page.click_btn(resources.TrafficModuleLocator.campaign_country)
        time.sleep(0.5)
        base_page.click_btn(resources.TrafficModuleLocator.campaign_country_option.format(country=campaign_country_edited))
            
        average_session_field = base_page.wait(resources.TrafficModuleLocator.campaign_average_session)
        average_session_field.clear()
        average_session_field.send_keys(campaign_average_session_edited)
            
        base_page.click_btn(resources.TrafficModuleLocator.campaign_frequency)
        time.sleep(2)
        base_page.click_btn(resources.TrafficModuleLocator.campaign_frequency_option)
        
        input_field = base_page.wait(resources.TrafficModuleLocator.campaign_edit_name_input.format(campaign_name=campaign_name))
        input_field.clear()
        input_field.send_keys(campaign_name_edited)
        
    def edit_campaign_check(self, base_page, campaign, driver):
        passed = True
        
        if "image_base64_code" in campaign["fields"]:
            image_base64_field = base_page.wait(resources.TrafficModuleLocator.campaign_image_base64_edit_check.format(campaign_image_base64=campaign_image_base64_edited))
            if not image_base64_field and passed:
                passed = False
                
        if "image_url" in campaign["fields"]:
            image_url_field = base_page.wait(resources.TrafficModuleLocator.campaign_image_url_edit_check.format(campaign_image_url=campaign_image_url_edited))
            if not image_url_field and passed:
                passed = False
                
        if "wildcard_string" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_edit_check.format(campaign_wildcard=campaign_wildcard_string_edited[-1]))
            if not wildcard_field and passed:
                passed = False
                
        if "tier1_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url_edit_check.format(campaign_tier1_url=campaign_tier1_url_edited[-1]))
            if not wildcard_field and passed:
                passed = False
                
        if "tier2_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url_edit_check.format(campaign_tier2_url=campaign_tier2_url_edited[-1]))
            if not wildcard_field and passed:
                passed = False
                
        if "destination_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_destination_url_edit_check.format(campaign_destination_url=campaign_destination_url_edited[-1]))
            if not wildcard_field and passed:
                passed = False
                
        if "keyword_modifiers" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers_edit_check.format(campaign_keyword_modifiers=campaign_keyword_modifiers_edited[-1]))
            if not wildcard_field and passed:
                passed = False
                
        if "direct_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.TrafficModuleLocator.campaign_direct_url_edit_check.format(campaign_direct_url=campaign_direct_url_edited[-1]))
            if not wildcard_field and passed:
                passed = False
                
        if "brand_name" in campaign["fields"]:
            brand_name_field = base_page.wait(resources.TrafficModuleLocator.campaign_brand_name_edit_check.format(campaign_brand_name=campaign_brand_name_edited))
            if not brand_name_field and passed:
                passed = False
                
        campaign_edited = self.base_page.wait(resources.TrafficModuleLocator.campaign_name_edit_check.format(campaign_name=campaign_name_edited))
        if not campaign_edited and passed:
            passed = False
            
        average_session_field = base_page.wait(resources.TrafficModuleLocator.campaign_average_session_edit_check.format(campaing_average_session=campaign_average_session_edited))
        if not average_session_field and passed:
            passed = False
            
        # frequency_field = base_page.wait(resources.TrafficModuleLocator.campaign_frequency_edit_check.format(frequency="Monthly"))
        # if not frequency_field and passed:
        #     passed = False
            
        return passed
            
    def old_traffic_edit_fields(self, base_page, campaign, driver):
        if "keyword_modifiers" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_keyword_modifiers_edit_field.format(keyword=campaign_keyword_modifiers[-1]))
            base_page.remove_text(wildcard_field, campaign_keyword_modifiers[-1])
            base_page.send_key_with_action_chain(wildcard_field, campaign_keyword_modifiers_edited)
            time.sleep(2)

        if "direct_url" in campaign["fields"]:
            direct_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_direct_url_edit_field.format(direct_url=campaign_direct_url[-1]))
            base_page.remove_text(direct_url_field, campaign_direct_url[-1])
            base_page.send_key_with_action_chain(direct_url_field, campaign_direct_url_edited)
        time.sleep(2)
            
        if "wildcard_string" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_wildcard_strign_edit_field.format(wildcard=campaign_wildcard_string[-1]))
            base_page.remove_text(wildcard_field, campaign_wildcard_string[-1])
            base_page.send_key_with_action_chain(wildcard_field, campaign_wildcard_string_edited)
        time.sleep(2)

        if "tier1_url" in campaign["fields"]:
            tier_1_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_tier1_url_edit_field.format(tier_url=campaign_tier1_url[-1]))
            base_page.remove_text(tier_1_url_field, campaign_tier1_url[-1])
            base_page.send_key_with_action_chain(tier_1_url_field, campaign_tier1_url_edited)
            time.sleep(2)

            
        if "tier2_url" in campaign["fields"]:
            tier_2_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_tier2_url_edit_field.format(tier_url=campaign_tier2_url[-1]))
            base_page.remove_text(tier_2_url_field, campaign_tier2_url[-1])
            base_page.send_key_with_action_chain(tier_2_url_field, campaign_tier2_url_edited)
            time.sleep(2)

        if "destination_url" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_destination_url_edit_field.format(destination_url=campaign_destination_url[-1]))
            base_page.remove_text(wildcard_field, campaign_destination_url[-1])
            base_page.send_key_with_action_chain(wildcard_field, campaign_destination_url_edited)
            time.sleep(2)
            
        if "brand_name" in campaign["fields"]:
            brand_name_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_brand_name_edit_field.format(brand=campaign_brand_name))
            brand_name_field.clear()
            brand_name_field.send_keys(campaign_brand_name_edited)
            time.sleep(2)
            
        input_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_name_input.format(campaign_name=campaign_name))
        input_field.clear()
        input_field.send_keys(campaign_name_edited)
        time.sleep(2)
        
        average_session_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_average_session_edit_field)
        average_session_field.clear()
        average_session_field.send_keys(campaign_average_session_edited)
        time.sleep(2)
        
            
        country_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_country_edit_field)
        driver.execute_script("arguments[0].innerHTML = arguments[1];", country_field, resources.OldTrafficModuleLocator.country_inner_html_edited)
        
    def old_traffic_edit_fields_check(self, base_page, campaign, driver):
        passed = True
        
        if "keyword_modifiers" in campaign["fields"]:
            keyword_modifiers_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_keyword_modifiers_edit_field.format(keyword=campaign_keyword_modifiers_edited[-1]))
            if not keyword_modifiers_field and passed:
                passed = False
        time.sleep(2)

        if "direct_url" in campaign["fields"]:
            direct_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_direct_url_edit_field.format(direct_url=campaign_direct_url_edited[-1]))
            if not direct_url_field and passed:
                passed = False

        if "wildcard_string" in campaign["fields"]:
            wildcard_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_wildcard_strign_edit_field.format(wildcard=campaign_wildcard_string_edited[-1]))
            if not wildcard_field and passed:
                passed = False
        time.sleep(2)

        if "tier1_url" in campaign["fields"]:
            tier_1_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_tier1_url_edit_field.format(tier_url=campaign_tier1_url_edited[-1]))
            if not tier_1_url_field and passed:
                passed = False
        time.sleep(2)
        
        if "tier2_url" in campaign["fields"]:
            tier_2_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_tier2_url_edit_field.format(tier_url=campaign_tier2_url_edited[-1]))
            if not tier_2_url_field and passed:
                passed = False
        time.sleep(2)

        if "destination_url" in campaign["fields"]:
            destination_url_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_destination_url_edit_field.format(destination_url=campaign_destination_url_edited[-1]))
            if not destination_url_field and passed:
                passed = False
        time.sleep(2)
        
        if "brand_name" in campaign["fields"]:
            brand_name_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_brand_name_edit_field.format(brand=campaign_brand_name_edited))
            if not brand_name_field and passed:
                passed = False
        time.sleep(2)
        
        campaign_edited = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_view_check.format(campaign_name=campaign_name_edited))
        if not campaign_edited and passed:
            passed = False
            
        average_session_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_average_session_edit_field_check.format(average_session=campaign_average_session_edited))
        if not average_session_field and passed:
            passed = False
            
        # country_field = base_page.wait(resources.OldTrafficModuleLocator.campaign_country_edit_field_check.format(country=campaign_country_edited))
        # if not country_field and passed:
        #     passed = False
        
        return passed

class CE_Traffic_TestCases(TrafficBase):
    def __init__(self):
        self.driver = initialize_and_navigate(data.ce_traffic_url)
        self.base_page = page.HomePage(self.driver)
        self.base_page.make_csv('CE_traffic_must_haves.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    
    def login_test_cases(self):
        try:
            # Test Case 1: Invalid Login (Invalid Username and Password)
            self.driver.get(data.ce_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid credentials"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password),Fail\n', new=False)
        
        try:
            # Test Case 2: Valid Username, Invalid Password
            self.driver.get(data.ce_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys(data.ce_login_username)
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid password"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password),Fail\n', new=False)
        
        try:
            # Test Case 3: Invalid Username, Valid Password
            self.driver.get(data.ce_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys(data.ce_login_password)
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid username"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password),Fail\n', new=False)
        
        try:
            # Test Case 4: Valid Login
            self.driver.get(data.ce_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys(data.ce_login_username)
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys(data.ce_login_password)
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login failed with valid credentials"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password), {"Pass" if login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password),Fail\n', new=False)

    def crud_test_cases(self):
        try:
            self.driver.get(data.ce_project_listing_page)
        
            # Test Case 1: Create Project
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_btn)
            time.sleep(2)
            self.base_page.wait(resources.TrafficModuleLocator.project_create_name_input).send_keys(project_name)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_modal_btn)
            project_created = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project creation failed"
            project_id = self.driver.current_url.split("/")[-2]
            self.driver.get(data.ce_project_listing_page)
            project_found_in_listing = self.base_page.wait(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id)), "Project creation failed"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Create Project, {"Pass" if project_created[0] and project_found_in_listing[0] else f"Fail - {project_created[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Create Project,Fail\n', new=False)  
        
        try:
            # Test Case 2: Edit Project
            time.sleep(2)
            self.driver.get(data.ce_project_listing_page)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_edit_btn.format(project_id=project_id))
            project_edit_input = self.base_page.wait(resources.TrafficModuleLocator.project_edit_name_input.format(project_name=project_name))
            project_edit_input.clear()
            project_edit_input.send_keys(edited_project_name)
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_edit_modal_btn.format(project_id=project_id))
            project_edited = self.base_page.wait(resources.TrafficModuleLocator.project_edit_check.format(edited_project_name=edited_project_name)), "Project edit failed"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Edit Project, {"Pass" if project_edited[0] else f"Fail - {project_edited[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Edit Project,Fail\n', new=False)
        
        try:
            # Test Case 3: View Project
            time.sleep(2)
            self.driver.get(data.ce_project_listing_page)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id))
            project_viewed = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project view failed"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, View Project,Fail\n', new=False)

        try:
            self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_btn)

            campaign_types = [
                {
                    "campaign_type": "Turing",
                    "campaign_sub_type": "Turing",
                    "fields": ["image_base64_code", "image_url", "keyword_modifiers"]
                },
                {
                    "campaign_type": "Google Search No Click",
                    "campaign_sub_type": "Google Search No Click",
                    "fields": ["keyword_modifiers"]
                },
                {
                    "campaign_type": "Multiple Session",
                    "campaign_sub_type": "Multiple Session",
                    "fields": ["direct_url", "is_spread_session"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "Organic Keyword",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "Organic Direct",
                    "fields": ["direct_url", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "Organic Brand",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Spreadsheet",
                    "campaign_sub_type": "Spreadsheet",
                    "fields": [ "direct_url", "keyword_modifiers"]
                },
                {
                    "campaign_type": "Squidoosh",
                    "campaign_sub_type": "Squidoosh",
                    "fields": [ "wildcard_string", "keyword_modifiers", "select_wildcard_type_option"]
                },
                {
                    "campaign_type": "Tiered",
                    "campaign_sub_type": "Tiered",
                    "fields": [ "wildcard_string", "tier1_url", "tier2_url", "destination_url"]
                },
                {
                    "campaign_type": "Wordpress",
                    "campaign_sub_type": "Wordpress",
                    "fields": [ "wildcard_string", "tier1_url", "is_product", "keyword_modifiers", "brand_name"]
                },
                {
                    "campaign_type": "Youtube",
                    "campaign_sub_type": "Youtube",
                    "fields": [ "keyword_modifiers", "tier1_url", "tier2_url", "brand_name"]
                },
                {
                    "campaign_type": "Squidoosh",
                    "campaign_sub_type": "Local Squidoosh",
                    "fields": ["brand_name", "wildcard_string"]
                },
                # {
                #     "campaign_type": "Website Specific",
                #     "campaign_sub_type": "aitomation.com",
                #     "fields": ["brand_name", "wildcard_string", "keyword_modifiers", "is_product"]
                # },
            ]

            selected_campaign = random.choice(campaign_types)

            def fill_campaign_form(campaign):
                self.base_page.wait(resources.TrafficModuleLocator.campaign_name).send_keys(campaign_name)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_category)
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_category_option.format(campaign_type=campaign["campaign_type"]))
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_sub_category)
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_sub_category_option.format(campaign_sub_type=campaign["campaign_sub_type"]))
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_country)
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_country_option.format(country=campaign_country))
                
                self.add_input_field_data(self.base_page, campaign, self.driver)
                self.add_tagify_data(self.base_page, campaign, self.driver)

            try:
                # Test Case 1: Create Campaign
                time.sleep(2)
                fill_campaign_form(selected_campaign)
                time.sleep(5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_submit_btn)
                campaign_created = self.base_page.wait(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign creation failed"
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Create Campaign, {"Pass" if campaign_created[0] else f"Fail - {campaign_created[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Create Campaign,Fail\n', new=False)
                
            try:
                # Test Case 2: View Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name))
                campaign_viewed = self.base_page.wait(resources.TrafficModuleLocator.capmaign_view_check.format(campaign_name=campaign_name)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, View Campaign, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, View Campaign,Fail\n', new=False)

            try:
                # Test Case 3: Edit Campaign
                time.sleep(2)
                self.driver.get(data.ce_campaing_listing_page.format(project_id=project_id))
                self.base_page.click_btn(resources.TrafficModuleLocator.campaing_edit_btn.format(campaign_id=campaign_id))
                
                self.edit_tagify_data(self.base_page, selected_campaign, self.driver)
                self.edit_input_field_data(self.base_page, selected_campaign, self.driver)

                save_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(3)
                cancel_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_cancel_btn)
                self.driver.execute_script("arguments[0].click();", cancel_btn)
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited))
                campaign_edited = self.edit_campaign_check(self.base_page, selected_campaign, self.driver), "Campaign edit failed"
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
                  
            try:
                # Test Case 2: View Campaign
                self.driver.get(data.ce_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited))
                campaign_viewed = self.base_page.wait(resources.TrafficModuleLocator.capmaign_view_check.format(campaign_name=campaign_name_edited)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, View Campaign after edit, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, View Campaign after edit,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
                self.driver.get(data.ce_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                campaign_live = self.base_page.wait(resources.TrafficModuleLocator.live_status), "Campaign live failed"
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Live Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Live Campaign,Fail\n', new=False)
        
            try:
                # Test Case 5: Cancel Live Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                campaign_live = self.base_page.wait(resources.TrafficModuleLocator.cancel_status), "Campaign live failed"
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Cancel Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Cancel Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Delete Campaign
                time.sleep(2)
                delete_btn = self.base_page.wait(resources.TrafficModuleLocator.campaing_delete_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(2)
                delete_modal_btn = self.base_page.wait(resources.TrafficModuleLocator.capmaign_delete_modal_btn)
                self.driver.execute_script("arguments[0].click();", delete_modal_btn)
                campaign_deleted = not self.base_page.wait(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign deletion failed"
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Delete Campaign, {"Pass" if campaign_deleted else f"Fail - {campaign_deleted[1]}"}\n', new=False)
                
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Delete Campaign,Fail\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, CRUD Test Cases,Fail\n', new=False)
            
        try:
            # Test Case 4: Delete Project
            self.driver.get(data.ce_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
            project_deleted = not self.base_page.wait(resources.TrafficModuleLocator.project_deleted_list_check.format(project_id=project_id)), "Project deletion failed"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Delete Project, {"Pass" if project_deleted else f"Fail - {project_deleted[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, Delete Project,Fail\n', new=False)
            
            
    def report_test_cases(self):
        
        try:
            # Test Case 2: Select a project, a campaign, and filter records
            table_rows = None
            self.driver.get(data.ce_report_page)
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.report_project_filter)
            time.sleep(0.5)
            project_filter_options = self.base_page.wait_all(resources.TrafficModuleLocator.report_project_filter_option)
            for index, option in enumerate(project_filter_options):
                if index == 0:
                    continue
                option.click()
                time.sleep(5)

                self.base_page.click_btn(resources.TrafficModuleLocator.report_campaign_filter)
                time.sleep(0.5)
                campaign_filter_options = self.base_page.wait_all(resources.TrafficModuleLocator.report_campaign_filter_option)
                for campaign_index, option in enumerate(campaign_filter_options):
                    if campaign_index == 0:
                        continue
                    option.click()
                    time.sleep(5)
                
                    table_rows = self.base_page.wait(resources.TrafficModuleLocator.report_result_row)
                    if table_rows:
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all)
                        time.sleep(5)
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all_failed_option)
                        time.sleep(5)
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all)
                        time.sleep(5)
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all_success_option)
                        time.sleep(5)
                        table_rows = self.base_page.wait(resources.TrafficModuleLocator.report_result_row)
                        if table_rows:
                            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Pass\n', new=False)
                            break
                if table_rows:
                    break
                if index == 7:
                    self.base_page.make_csv("CE_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail - No results found\n', new=False)
                    break
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail\n', new=False)
            
    def campaign_error_and_graph_stats(self):
        try:
            self.driver.get(data.ce_campaign_error_page)
            time.sleep(5)
            error_page_row = self.base_page.wait(resources.TrafficModuleLocator.campaign_error_page_row).text
            data_list_24_days = error_page_row.split('\n')
            data_dict_24_days = {
                "campaing_id": data_list_24_days[0],
                "total_failed": data_list_24_days[1],
                "google_recaptcha": data_list_24_days[2],
                "wildcard_not_found": data_list_24_days[3],
                "product_wildcard_not_found": data_list_24_days[4],
                "page_not_loaded": data_list_24_days[5],
                "other_errors": data_list_24_days[6]
            }
            print(data_dict_24_days)
            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_7_day_option)
            time.sleep(30)
            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_30_day_option)
            time.sleep(30)
            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_today_option)

            time.sleep(30)
            error_page_row = self.base_page.wait(resources.TrafficModuleLocator.campaign_error_page_row).text
            data_list = error_page_row.split('\n')
            data_dict = {
                "campaing_id": data_list[0],
                "total_failed": data_list[1],
                "google_recaptcha": data_list[2],
                "wildcard_not_found": data_list[3],
                "product_wildcard_not_found": data_list[4],
                "page_not_loaded": data_list[5],
                "other_errors": data_list[6]
            }
            print(data_dict)
            
            filter_check = int(data_dict["total_failed"]) != int(data_dict_24_days["total_failed"])
            
            if filter_check:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Pass\n', new=False)
            else:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Fail\n', new=False)
            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaign_link)
            time.sleep(5)
            raw_data = self.driver.page_source
            page_src = raw_data.split('rawData = ')
            for part in page_src:
                if part.startswith("JSON"):
                    data_string = part
                    data_json = data_string.split(";")[0]

            json_string = data_json.split("JSON.parse('")[1].split("')")[0]
            json_data = json.loads(json_string)[-1]
            print(json_data)
            
            google_recaptcha_check = int(data_dict["google_recaptcha"]) == int(json_data["google_recaptcha"])
            wildcard_not_found_check = int(data_dict["wildcard_not_found"]) == int(json_data["wildcard_not_found"])
            product_wildcard_not_found_check = int(data_dict["product_wildcard_not_found"]) == int(json_data["product_wildcard_not_found"])
            total_failed_check = int(data_dict["total_failed"]) == int(json_data["failed"])
            
            if google_recaptcha_check and wildcard_not_found_check and product_wildcard_not_found_check and total_failed_check:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Pass\n', new=False)
            else:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            
            time.sleep(2)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            print(e)
            
    def full_dashboard_must_haves(self):
        self.login_test_cases()
        self.crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Full CE Dashboard Must Haves Test Cases Completed")
        
class Tiger_Traffic_TestCases(TrafficBase):    
    def __init__(self):
        self.driver = initialize_and_navigate(data.tiger_traffic_url)
        self.base_page = page.HomePage(self.driver)
        self.base_page.make_csv('Tiger_traffic_must_haves.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    
    
    def login_test_cases(self):
        try:
            # Test Case 1: Invalid Login (Invalid Username and Password)
            self.driver.get(data.tiger_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid credentials"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password),Fail\n', new=False)
        
        try:
            # Test Case 2: Valid Username, Invalid Password
            self.driver.get(data.tiger_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys(data.tiger_login_username)
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid password"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password),Fail\n', new=False)
        
        try:
            # Test Case 3: Invalid Username, Valid Password
            self.driver.get(data.tiger_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys(data.tiger_login_password)
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login succeeded with invalid username"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password),Fail\n', new=False)
        
        try:
            # Test Case 4: Valid Login
            self.driver.get(data.tiger_traffic_url)
            self.base_page.wait(resources.TrafficModuleLocator.login_user).send_keys(data.tiger_login_username)
            self.base_page.wait(resources.TrafficModuleLocator.login_password).send_keys(data.tiger_login_password)
            self.base_page.click_btn(resources.TrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.TrafficModuleLocator.main_content), "Login failed with valid credentials"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password), {"Pass" if login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password),Fail\n', new=False)

    def crud_test_cases(self):
        try:
            self.driver.get(data.tiger_project_listing_page)
        
            # Test Case 1: Create Project
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_btn)
            time.sleep(2)
            self.base_page.wait(resources.TrafficModuleLocator.project_create_name_input).send_keys(project_name)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_modal_btn)
            project_created = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project creation failed"
            project_id = self.driver.current_url.split("/")[-2]
            self.driver.get(data.tiger_project_listing_page)
            project_found_in_listing = self.base_page.wait(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id)), "Project creation failed"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, Create Project, {"Pass" if project_created[0] and project_found_in_listing[0] else f"Fail - {project_created[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, Create Project,Fail\n', new=False)  
        
        try:
            # Test Case 2: Edit Project
            time.sleep(2)
            self.driver.get(data.tiger_project_listing_page)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_edit_btn.format(project_id=project_id))
            project_edit_input = self.base_page.wait(resources.TrafficModuleLocator.project_edit_name_input.format(project_name=project_name))
            project_edit_input.clear()
            project_edit_input.send_keys(edited_project_name)
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_edit_modal_btn.format(project_id=project_id))
            project_edited = self.base_page.wait(resources.TrafficModuleLocator.project_edit_check.format(edited_project_name=edited_project_name)), "Project edit failed"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, Edit Project, {"Pass" if project_edited[0] else f"Fail - {project_edited[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, Edit Project,Fail\n', new=False)
        
        try:
            # Test Case 3: View Project
            time.sleep(2)
            self.driver.get(data.tiger_project_listing_page)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id))
            project_viewed = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project view failed"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, View Project,Fail\n', new=False)

        try:
            self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_btn)

            campaign_types = [
                {
                    "campaign_type": "Birthday",
                    "campaign_sub_type": "Birthday",
                    "fields": ["image_base64_code", "image_url", "keyword_modifiers"]
                },
                {
                    "campaign_type": "Birthday Amazon",
                    "campaign_sub_type": "Birthday Amazon",
                    "fields": ["image_base64_code", "image_url", "keyword_modifiers"]
                },
                {
                    "campaign_type": "Bsr Booster",
                    "campaign_sub_type": "Bsr Booster",
                    "fields": ["brand_name", "keyword_modifiers", "is_product", "gmb_cid"]
                },
                {
                    "campaign_type": "Lookey",
                    "campaign_sub_type": "Lookey",
                    "fields": ["direct_url", "radius"]
                },
                {
                    "campaign_type": "Pathfinder",
                    "campaign_sub_type": "Pathfinder",
                    "fields": ["wildcard_string", "keyword_modifiers", "gmb_website_percentage"]
                },
                {
                    "campaign_type": "Rocket",
                    "campaign_sub_type": "Rocket",
                    "fields": ["gmb_cid", "keyword_modifiers", "gmb_website_percentage", "geo_latitude", "geo_longitude", "radius"]
                },
                {
                    "campaign_type": "Shopify",
                    "campaign_sub_type": "Shopify",
                    "fields": ["brand_name", "keyword_modifiers", "is_product", "wildcard_string", "tier1_url"]
                },
                {
                    "campaign_type": "Walmart",
                    "campaign_sub_type": "Walmart",
                    "fields": ["gmb_website_percentage", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Squidoosh",
                    "campaign_sub_type": "Local Squidoosh",
                    "fields": ["brand_name", "wildcard_string"]
                },
                {
                    "campaign_type": "Website Specific",
                    "campaign_sub_type": "aitomation.com",
                    "fields": ["brand_name", "wildcard_string", "keyword_modifiers", "is_product"]
                },
                {
                    "campaign_type": "Google Search No Click",
                    "campaign_sub_type": "Google Search No Click",
                    "fields": ["keyword_modifiers"]
                },
                {
                    "campaign_type": "Multiple Session",
                    "campaign_sub_type": "Multiple Session",
                    "fields": ["direct_url", "is_spread_session"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "Organic Keyword",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "Organic Direct",
                    "fields": ["direct_url", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "Organic Brand",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Spreadsheet",
                    "campaign_sub_type": "Spreadsheet",
                    "fields": [ "direct_url", "keyword_modifiers"]
                },
                {
                    "campaign_type": "Squidoosh",
                    "campaign_sub_type": "Squidoosh",
                    "fields": [ "wildcard_string", "keyword_modifiers", "select_wildcard_type_option"]
                },
                {
                    "campaign_type": "Tiered",
                    "campaign_sub_type": "Tiered",
                    "fields": [ "wildcard_string", "tier1_url", "tier2_url", "destination_url"]
                },
                {
                    "campaign_type": "Wordpress",
                    "campaign_sub_type": "Wordpress",
                    "fields": [ "wildcard_string", "tier1_url", "is_product", "keyword_modifiers", "brand_name"]
                },
                {
                    "campaign_type": "Youtube",
                    "campaign_sub_type": "Youtube",
                    "fields": [ "keyword_modifiers", "tier1_url", "tier2_url", "brand_name"]
                },
            ]

            selected_campaign = random.choice(campaign_types)

            def fill_campaign_form(campaign):
                self.base_page.wait(resources.TrafficModuleLocator.campaign_name).send_keys(campaign_name)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_category)
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_category_option.format(campaign_type=campaign["campaign_type"]))
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_sub_category)
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_sub_category_option.format(campaign_sub_type=campaign["campaign_sub_type"]))
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_country)
                time.sleep(0.5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_country_option.format(country=campaign_country))
                
                self.add_input_field_data(self.base_page, campaign, self.driver)
                self.add_tagify_data(self.base_page, campaign, self.driver)

            try:
                # Test Case 1: Create Campaign
                time.sleep(2)
                fill_campaign_form(selected_campaign)
                time.sleep(5)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_submit_btn)
                campaign_created = self.base_page.wait(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign creation failed"
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Create Campaign, {"Pass" if campaign_created[0] else f"Fail - {campaign_created[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Create Campaign,Fail\n', new=False)
                
            try:
                # Test Case 2: View Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name))
                campaign_viewed = self.base_page.wait(resources.TrafficModuleLocator.capmaign_view_check.format(campaign_name=campaign_name)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, View Campaign, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, View Campaign,Fail\n', new=False)


            try:
                # Test Case 3: Edit Campaign
                time.sleep(2)
                self.driver.get(data.tiger_campaing_listing_page.format(project_id=project_id))
                self.base_page.click_btn(resources.TrafficModuleLocator.campaing_edit_btn.format(campaign_id=campaign_id))
                
                self.edit_tagify_data(self.base_page, selected_campaign, self.driver)
                self.edit_input_field_data(self.base_page, selected_campaign, self.driver)

                save_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(3)
                cancel_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_cancel_btn)
                self.driver.execute_script("arguments[0].click();", cancel_btn)
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited))
                campaign_edited = self.edit_campaign_check(self.base_page, selected_campaign, self.driver), "Campaign edit failed"
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
                
                
            try:
                # Test Case 2: View Campaign
                self.driver.get(data.tiger_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited))
                campaign_viewed = self.base_page.wait(resources.TrafficModuleLocator.capmaign_view_check.format(campaign_name=campaign_name_edited)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                time.sleep(5)
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, View Campaign after edit, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, View Campaign after edit,Fail\n', new=False)
                
        
            try:
                # Test Case 4: Live Campaign
                self.driver.get(data.tiger_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                campaign_live = self.base_page.wait(resources.TrafficModuleLocator.live_status), "Campaign live failed"
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Live Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Live Campaign,Fail\n', new=False)
        
            try:
                # Test Case 5: Cancel Live Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                campaign_live = self.base_page.wait(resources.TrafficModuleLocator.cancel_status), "Campaign live failed"
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Cancel Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Cancel Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Delete Campaign
                time.sleep(2)
                delete_btn = self.base_page.wait(resources.TrafficModuleLocator.campaing_delete_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(2)
                delete_modal_btn = self.base_page.wait(resources.TrafficModuleLocator.capmaign_delete_modal_btn)
                self.driver.execute_script("arguments[0].click();", delete_modal_btn)
                campaign_deleted = not self.base_page.wait(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign deletion failed"
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Delete Campaign, {"Pass" if campaign_deleted else f"Fail - {campaign_deleted[1]}"}\n', new=False)
                
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Delete Campaign,Fail\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, CRUD Test Cases,Fail\n', new=False)
            
        try:
            # Test Case 4: Delete Project
            self.driver.get(data.tiger_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
            project_deleted = not self.base_page.wait(resources.TrafficModuleLocator.project_deleted_list_check.format(project_id=project_id)), "Project deletion failed"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, Delete Project, {"Pass" if project_deleted else f"Fail - {project_deleted[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, Delete Project,Fail\n', new=False)
            
            
    def report_test_cases(self):
        
        try:
            # Test Case 2: Select a project, a campaign, and filter records
            table_rows = None
            self.driver.get(data.tiger_report_page)
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.report_project_filter)
            time.sleep(0.5)
            project_filter_options = self.base_page.wait_all(resources.TrafficModuleLocator.report_project_filter_option)
            for index, option in enumerate(project_filter_options):
                if index == 0:
                    continue
                option.click()
                time.sleep(5)

                self.base_page.click_btn(resources.TrafficModuleLocator.report_campaign_filter)
                time.sleep(0.5)
                campaign_filter_options = self.base_page.wait_all(resources.TrafficModuleLocator.report_campaign_filter_option)
                for campaign_index, option in enumerate(campaign_filter_options):
                    if campaign_index == 0:
                        continue
                    option.click()
                    time.sleep(5)
                
                    table_rows = self.base_page.wait(resources.TrafficModuleLocator.report_result_row)
                    if table_rows:
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all)
                        time.sleep(5)
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all_failed_option)
                        time.sleep(5)
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all)
                        time.sleep(5)
                        self.base_page.click_btn(resources.TrafficModuleLocator.filter_all_success_option)
                        time.sleep(5)
                        table_rows = self.base_page.wait(resources.TrafficModuleLocator.report_result_row)
                        if table_rows:
                            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Pass\n', new=False)
                            break
                if table_rows:
                    break
                if index == 7:
                    self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail - No results found\n', new=False)
                    break
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail\n', new=False)
            
    def campaign_error_and_graph_stats(self):
        try:
            self.driver.get(data.tiger_campaign_error_page)
            time.sleep(5)
            error_page_row = self.base_page.wait(resources.TrafficModuleLocator.campaign_error_page_row).text
            data_list_24_days = error_page_row.split('\n')
            data_dict_24_days = {
                "campaing_id": data_list_24_days[0],
                "total_failed": data_list_24_days[1],
                "google_recaptcha": data_list_24_days[2],
                "wildcard_not_found": data_list_24_days[3],
                "product_wildcard_not_found": data_list_24_days[4],
                "page_not_loaded": data_list_24_days[5],
                "other_errors": data_list_24_days[6]
            }
            print(data_dict_24_days)

            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_7_day_option)
            time.sleep(100)
            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_30_day_option)
            time.sleep(100)
            
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_today_option)

            time.sleep(130)
            error_page_row = self.base_page.wait(resources.TrafficModuleLocator.campaign_error_page_row).text
            data_list = error_page_row.split('\n')
            data_dict = {
                "campaing_id": data_list[0],
                "total_failed": data_list[1],
                "google_recaptcha": data_list[2],
                "wildcard_not_found": data_list[3],
                "product_wildcard_not_found": data_list[4],
                "page_not_loaded": data_list[5],
                "other_errors": data_list[6]
            }
            print(data_dict)
            filter_check = int(data_dict["total_failed"]) != int(data_dict_24_days["total_failed"])
            
            if filter_check:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Pass\n', new=False)
            else:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Fail\n', new=False)
            
            time.sleep(5)
            self.base_page.click_btn(resources.TrafficModuleLocator.campaign_link)
            time.sleep(5)
            raw_data = self.driver.page_source
            page_src = raw_data.split('rawData = ')
            for part in page_src:
                if part.startswith("JSON"):
                    data_string = part
                    data_json = data_string.split(";")[0]

            json_string = data_json.split("JSON.parse('")[1].split("')")[0]
            json_data = json.loads(json_string)[-1]
            print(json_data)
            
            google_recaptcha_check = int(data_dict["google_recaptcha"]) == int(json_data["google_recaptcha"])
            wildcard_not_found_check = int(data_dict["wildcard_not_found"]) == int(json_data["wildcard_not_found"])
            product_wildcard_not_found_check = int(data_dict["product_wildcard_not_found"]) == int(json_data["product_wildcard_not_found"])
            total_failed_check = int(data_dict["total_failed"]) == int(json_data["failed"])
            
            if google_recaptcha_check and wildcard_not_found_check and product_wildcard_not_found_check and total_failed_check:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Pass\n', new=False)
            else:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            
            time.sleep(2)   
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            print(e)
        
        try:
            self.driver.get(data.tiger_campaign_error_page)
            time.sleep(2)
            self.base_page.click_btn('//button[@id="btnProjectErrors"]')
            time.sleep(2)
            error_page_row = self.base_page.wait('//div[./div[./a[contains(@href, "/project")]]]').text
            
            data_list_24_days = error_page_row.split('\n')
            data_dict_24_days = {
                "campaing_id": data_list_24_days[0],
                "total_failed": data_list_24_days[1],
                "google_recaptcha": data_list_24_days[2],
                "wildcard_not_found": data_list_24_days[3],
                "product_wildcard_not_found": data_list_24_days[4],
                "page_not_loaded": data_list_24_days[5],
                "other_errors": data_list_24_days[6]
            }
            print(data_dict_24_days)
            
            day_filter = self.base_page.wait_all(resources.TrafficModuleLocator.campaing_error_filter)
            day_filter[1].click()
            time.sleep(0.5)
            day_7_filter = self.base_page.wait_all(resources.TrafficModuleLocator.campaing_error_filter_7_day_option)
            day_7_filter[1].click()
            time.sleep(100)
            
            day_filter = self.base_page.wait_all(resources.TrafficModuleLocator.campaing_error_filter)
            day_filter[1].click()
            time.sleep(0.5)
            day_30_filter = self.base_page.wait_all(resources.TrafficModuleLocator.campaing_error_filter_30_day_option)
            day_30_filter[1].click()
            time.sleep(100)
            
            day_filter = self.base_page.wait_all(resources.TrafficModuleLocator.campaing_error_filter)
            day_filter[1].click()
            time.sleep(0.5)
            day_today_filter = self.base_page.wait_all(resources.TrafficModuleLocator.campaing_error_filter_today_option)
            day_today_filter[1].click()
            time.sleep(130)
            
            error_page_row = self.base_page.wait('//div[./div[./a[contains(@href, "/project")]]]').text
            data_list = error_page_row.split('\n')
            data_dict = {
                "campaing_id": data_list[0],
                "total_failed": data_list[1],
                "google_recaptcha": data_list[2],
                "wildcard_not_found": data_list[3],
                "product_wildcard_not_found": data_list[4],
                "page_not_loaded": data_list[5],
                "other_errors": data_list[6]
            }
            print(data_dict)
            filter_check = int(data_dict["total_failed"]) != int(data_dict_24_days["total_failed"])
            
            if filter_check:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project error and graph stats, Data Filtering, Pass\n', new=False)
            else:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project error and graph stats, Data Filtering, Fail\n', new=False)
                
            time.sleep(5)
            self.base_page.click_btn('//a[contains(@href, "/projects/") and @class="text-muted"]')
            time.sleep(5)
            raw_data = self.driver.page_source
            page_src = raw_data.split('rawData = ')
            for part in page_src:
                if part.startswith("JSON"):
                    data_string = part
                    data_json = data_string.split(";")[0]

            json_string = data_json.split("JSON.parse('")[1].split("')")[0]
            json_data = json.loads(json_string)[-1]
            print(json_data)
            
            google_recaptcha_check = int(data_dict["google_recaptcha"]) == int(json_data["google_recaptcha"])
            wildcard_not_found_check = int(data_dict["wildcard_not_found"]) == int(json_data["wildcard_not_found"])
            product_wildcard_not_found_check = int(data_dict["product_wildcard_not_found"]) == int(json_data["product_wildcard_not_found"])
            total_failed_check = int(data_dict["total_failed"]) == int(json_data["failed"])
            
            if google_recaptcha_check and wildcard_not_found_check and product_wildcard_not_found_check and total_failed_check:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project error and graph stats, Error and Graph Stats, Pass\n', new=False)
            else:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project error and graph stats, Error and Graph Stats, Fail\n', new=False)
            
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project error and graph stats, Error and Graph Stats, Fail\n', new=False)
            print(e)
        
        
    def full_dashboard_must_haves(self):
        self.login_test_cases()
        self.crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Full Tiger Dashboard Must Haves Test Cases Completed")
 
class Torrential_Traffic_TestCases(TrafficBase):
    def __init__(self):
        self.driver = initialize_and_navigate(data.torrential_traffic_url)
        self.base_page = page.HomePage(self.driver)
        self.base_page.make_csv('Torrential_traffic_must_haves.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    
    def login_test_cases(self):
        try:
            # Test Case 1: Invalid Login (Invalid Username and Password)
            self.driver.get(data.torrential_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login succeeded with invalid credentials"
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password),Fail\n', new=False)

        try:
            # Test Case 2: Valid Username, Invalid Password
            self.driver.get(data.torrential_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys(data.torrential_login_username)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login succeeded with invalid password"
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password),Fail\n', new=False)
        
        try:
            # Test Case 3: Invalid Username, Valid Password
            self.driver.get(data.torrential_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys(data.torrential_login_password)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login succeeded with invalid username"
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password),Fail\n', new=False)
        
        try:
            # Test Case 4: Valid Login
            self.driver.get(data.torrential_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys(data.torrential_login_username)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys(data.torrential_login_password)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login failed with valid credentials"
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password), {"Pass" if login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password),Fail\n', new=False)

    def crud_test_cases(self):
        try:
            self.driver.get(data.torrential_project_listing_page)
        
            # Test Case 1: Create Project
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_btn)
            time.sleep(3)
            self.base_page.wait(resources.OldTrafficModuleLocator.project_create_name_input).send_keys(project_name)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_modal_btn)
            project_created = self.base_page.wait(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name)), "Project creation failed"
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, Create Project, {"Pass" if project_created[0] else f"Fail - {project_created[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, Create Project,Fail\n', new=False)
        
        try:
            # Test Case 2: View Project
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name))
            project_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.project_view_check.format(project_name=project_name)), "Project view failed"
            project_id = self.driver.current_url.split("/")[-2]
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, View Project,Fail\n', new=False)
        
        try:
            # Test Case 3: Edit Project
            time.sleep(2)
            self.driver.get(data.torrential_project_listing_page)
            time.sleep(6)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_edit_btn.format(project_id=project_id))
            time.sleep(2)
            project_edit_input = self.base_page.wait(resources.OldTrafficModuleLocator.project_edit_name_input)
            time.sleep(2)
            project_edit_input.clear()
            time.sleep(2)
            project_edit_input.send_keys(edited_project_name)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_edit_modal_btn)
            time.sleep(6)
            project_edited = self.base_page.wait(resources.OldTrafficModuleLocator.project_edit_check.format(edited_project_name=edited_project_name)), "Project edit failed"
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, Edit Project, {"Pass" if project_edited[0] else f"Fail - {project_edited[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, Edit Project,Fail\n', new=False)
        
        try:
            # Test Case 2: View Project
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=edited_project_name))
            project_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.project_view_check.format(project_name=edited_project_name)), "Project view failed"
            project_id = self.driver.current_url.split("/")[-2]
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, View Project after edit, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, View Project after edit,Fail\n', new=False)


        try:

            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_create_btn)
        

            campaign_types = [
                {
                    "campaign_type": "google_search_no_click",
                    "campaign_sub_type": "google_search_no_click",
                    "fields": ["keyword_modifiers"]
                },
                {
                    "campaign_type": "multiple_session",
                    "campaign_sub_type": "multiple_session",
                    "fields": ["direct_url", "is_spread_session"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "organic_keyword",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "organic_direct",
                    "fields": ["direct_url", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "organic_brand",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Spreadsheet",
                    "campaign_sub_type": "Spreadsheet",
                    "fields": [ "direct_url", "keyword_modifiers"]
                },
                {
                    "campaign_type": "Squidoosh",
                    "campaign_sub_type": "Squidoosh",
                    "fields": [ "wildcard_string", "keyword_modifiers", "select_wildcard_type_option"]
                },
                {
                    "campaign_type": "Tiered",
                    "campaign_sub_type": "Tiered",
                    "fields": [ "wildcard_string", "tier1_url", "tier2_url", "destination_url"]
                },
                {
                    "campaign_type": "Youtube",
                    "campaign_sub_type": "Youtube",
                    "fields": [ "keyword_modifiers", "tier1_url", "brand_name"]
                },
            ]

            selected_campaign = random.choice(campaign_types)

            def fill_campaign_form(campaign):
                self.base_page.wait(resources.OldTrafficModuleLocator.campaign_name).send_keys(campaign_name)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_category)
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_category_option.format(campaign_type=campaign["campaign_type"].lower()))
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_sub_category)
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_sub_category_option.format(campaign_sub_type=campaign["campaign_sub_type"].lower()))
                time.sleep(2)
                country_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_country)
                self.driver.execute_script("arguments[0].innerHTML = arguments[1];", country_field, resources.OldTrafficModuleLocator.country_inner_html)
                time.sleep(2)
                self.base_page.wait(resources.OldTrafficModuleLocator.campaign_average_session).send_keys(campaign_average_session)
                time.sleep(2)
                if "keyword_modifiers" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_keyword_modifiers)
                    self.base_page.send_key_with_action_chain(wildcard_field, campaign_keyword_modifiers)

                if "direct_url" in campaign["fields"]:
                    direct_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_direct_url)
                    self.base_page.send_key_with_action_chain(direct_url_field, campaign_direct_url)
                    
                if "wildcard_string" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_wildcard_strign)
                    self.base_page.send_key_with_action_chain(wildcard_field, campaign_wildcard_string)

                if "tier1_url" in campaign["fields"]:
                    tier_1_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier1_url)
                    self.base_page.send_key_with_action_chain(tier_1_url_field, campaign_tier1_url)

                    
                if "tier2_url" in campaign["fields"]:
                    tier_2_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier2_url)
                    self.base_page.send_key_with_action_chain(tier_2_url_field, campaign_tier2_url)

                if "destination_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_destination_url)
                    self.base_page.send_key_with_action_chain(wildcard_field, campaign_destination_url)

                if "brand_name" in campaign["fields"]:
                    self.base_page.wait(resources.OldTrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
                
            try:
                # Test Case 1: Create Campaign
                time.sleep(2)
                fill_campaign_form(selected_campaign)
                time.sleep(5)
                submit_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_submit_btn)
                self.driver.execute_script("arguments[0].click();", submit_btn)
                time.sleep(8)

                campaign_created = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign creation failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Create Campaign, {"Pass" if campaign_created[0] else f"Fail - {campaign_created[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Create Campaign,Fail\n', new=False)

            try:
                # Test Case 2: View Campaign
                time.sleep(10)
                campaign_create_check_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name))
                self.driver.execute_script("arguments[0].click();", campaign_create_check_btn)
                campaign_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_view_check.format(campaign_name=campaign_name)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                print(f"Campaign ID: {campaign_id}")
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, View Campaign, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                    self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, View Campaign,Fail\n', new=False)

            try:
                # Test Case 3: Edit Campaign
                time.sleep(2)
                self.driver.get(data.torrential_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                edit_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_edit_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", edit_btn)
                time.sleep(2)
                self.old_traffic_edit_fields(self.base_page, selected_campaign, self.driver)

                save_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(6)
                campaign_edited = self.old_traffic_edit_fields_check(self.base_page, selected_campaign, self.driver), "Campaign edit failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
                

            try:
                # Test Case 2: View Campaign
                self.driver.get(data.torrential_campaing_listing_page.format(project_id=project_id))
                time.sleep(10)
                campaign_create_check_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited))
                self.driver.execute_script("arguments[0].click();", campaign_create_check_btn)
                campaign_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_view_check.format(campaign_name=campaign_name_edited)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                print(f"Campaign ID: {campaign_id}")
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, View Campaign after edit, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                    self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, View Campaign after edit,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
                self.driver.get(data.torrential_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                live_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", live_btn)
                time.sleep(3)
                live_modal_confirmation_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_live_modal_confirmation)
                self.driver.execute_script("arguments[0].click();", live_modal_confirmation_btn)
                time.sleep(10)
                self.driver.get(data.torrential_campaing_listing_page.format(project_id=project_id))
                time.sleep(10)
                campaign_live = self.base_page.wait(resources.OldTrafficModuleLocator.live_status), "Campaign live failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Live Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Live Campaign,Fail\n', new=False)
        
            try:
                # Test Case 5: Cancel Live Campaign
                time.sleep(2)
                stop_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_stop_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", stop_btn)
                time.sleep(3)
                stop_modal_confirmation_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_stop_modal_confirmation)
                self.driver.execute_script("arguments[0].click();", stop_modal_confirmation_btn)
                time.sleep(10)
                self.driver.get(data.torrential_campaing_listing_page.format(project_id=project_id))
                time.sleep(10)
                campaign_live = self.base_page.wait(resources.OldTrafficModuleLocator.stop_status), "Campaign live failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Cancel Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Cancel Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Delete Campaign
                time.sleep(2)
                delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_delete_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(2)
                delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.capmaign_delete_modal_btn)
                time.sleep(2)
                self.driver.execute_script("arguments[0].click();", delete_modal_btn)
                time.sleep(6)
                campaign_deleted = not self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign deletion failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Delete Campaign, {"Pass" if campaign_deleted else f"Fail - {campaign_deleted[1]}"}\n', new=False)
                
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Delete Campaign,Fail\n', new=False)
                
            try:
                # Test Case 4: Delete Project
                self.driver.get(data.torrential_project_listing_page)
                time.sleep(2)
                delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_btn.format(project_id=project_id))
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(2)
                delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_modal_btn)
                self.driver.execute_script("arguments[0].click();", delete_modal_btn)
                time.sleep(6)
                project_deleted = not self.base_page.wait(resources.OldTrafficModuleLocator.project_deleted_list_check.format(edited_project_name=edited_project_name)), "Project deletion failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, Delete Project, {"Pass" if project_deleted else f"Fail - {project_deleted[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Project, Delete Project,Fail\n', new=False)
                
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, CRUD Test Cases,Fail\n', new=False)

            
    def report_test_cases(self):
        
        try:
            # Test Case 2: Select a project, a campaign, and filter records
            table_rows = None
            self.driver.get(data.torrential_report_page)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.report_project_filter)
            time.sleep(0.5)
            project_filter_options = self.base_page.wait_all(resources.OldTrafficModuleLocator.report_project_filter_option)
            for index, option in enumerate(project_filter_options):
                if index == 0:
                    continue
                option.click()
                time.sleep(5)

                self.base_page.click_btn(resources.OldTrafficModuleLocator.report_campaign_filter)
                time.sleep(2)
                campaign_filter_options = self.base_page.wait_all(resources.OldTrafficModuleLocator.report_campaign_filter_option)
                for campaign_index, option in enumerate(campaign_filter_options):
                    if campaign_index == 0:
                        continue
                    option.click()
                    time.sleep(10)
                
                    table_rows = self.base_page.wait(resources.OldTrafficModuleLocator.report_result_row)
                    if table_rows:
                        self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Pass\n', new=False)
                        break
                if table_rows:
                    break
                if index == 7:
                    self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail - No results found\n', new=False)
                    break
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail\n', new=False)
            
    def campaign_error_and_graph_stats(self):
        try:
            self.driver.get(data.torrential_campaign_error_page)
            time.sleep(5)
            error_page_row = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_error_page_row).text
            data_list_24_days = error_page_row.split(' ')
            data_dict_24_days = {
                "campaing_id": data_list_24_days[0],
                "total_failed": data_list_24_days[1],
                "google_recaptcha": data_list_24_days[2],
                "wildcard_not_found": data_list_24_days[3],
                "product_wildcard_not_found": data_list_24_days[4],
                "page_not_loaded": data_list_24_days[5],
                "other_errors": data_list_24_days[6]
            }
            print(data_dict_24_days)
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_1_month_option)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_error_filter_btn)
            time.sleep(10)
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_7_day_option)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_error_filter_btn)
            time.sleep(10)
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_1_day_option)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_error_filter_btn)
            time.sleep(10)
            error_page_row = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_error_page_row).text
            data_list = error_page_row.split(' ')
            data_dict = {
                "campaing_id": data_list[0],
                "total_failed": data_list[1],
                "google_recaptcha": data_list[2],
                "wildcard_not_found": data_list[3],
                "product_wildcard_not_found": data_list[4],
                "page_not_loaded": data_list[5],
                "other_errors": data_list[6]
            }
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_link)
            time.sleep(5)
            cleaned_data = []
            graph_data_list = []
            raw_data = self.driver.page_source
            page_src = raw_data.split('var options')[1]
            data_splited = page_src.split('],')[0]
            fixed_string = data_splited.replace("'", '"')
            fixed_string = fixed_string.split('=', 1)[1].strip()
            splited_data_by_new_line = fixed_string.split('\n')
            for data_values in splited_data_by_new_line:
                if "data" in data_values:
                    graph_data_list.append(data_values)
            for values in graph_data_list:
                values_splited = int(values.split(',')[-1].replace(' ', '').replace(']', '').replace('"', ''))
                cleaned_data.append(values_splited)
            print(cleaned_data)
                    
            google_recaptcha_check = int(data_dict["google_recaptcha"]) == int(cleaned_data[4])
            wildcard_not_found_check = int(data_dict["wildcard_not_found"]) == int(cleaned_data[2])
            product_wildcard_not_found_check = int(data_dict["product_wildcard_not_found"]) == int(cleaned_data[3])
            total_failed_check = int(data_dict["total_failed"]) == int(cleaned_data[1])
            
            if google_recaptcha_check and wildcard_not_found_check and product_wildcard_not_found_check and total_failed_check:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Pass\n', new=False)
            else:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            
            time.sleep(2)
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            print(e)
            
        
        
    def full_dashboard_must_haves(self):
        self.login_test_cases()
        self.crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Torrential Dashboard Must Haves Test Cases Completed")
        
        
        
class BS_Traffic_TestCases(TrafficBase):
    def __init__(self):
        self.driver = initialize_and_navigate(data.torrential_traffic_url)
        self.base_page = page.HomePage(self.driver)
        self.base_page.make_csv('BS_traffic_must_haves.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
    
    def login_test_cases(self):
        try:
            # Test Case 1: Invalid Login (Invalid Username and Password)
            self.driver.get(data.bs_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login succeeded with invalid credentials"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Invalid Login (Invalid Username and Password),Fail\n', new=False)

        try:
            # Test Case 2: Valid Username, Invalid Password
            self.driver.get(data.bs_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys(data.bs_login_username)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys("invalid_pass")
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login succeeded with invalid password"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Invalid Login (valid Username and invalid Password),Fail\n', new=False)
        
        try:
            # Test Case 3: Invalid Username, Valid Password
            self.driver.get(data.bs_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys("invalid_user")
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys(data.bs_login_password)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login succeeded with invalid username"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password), {"Pass" if not login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Invalid Login (invalid Username and valid Password),Fail\n', new=False)
        
        try:
            # Test Case 4: Valid Login
            self.driver.get(data.bs_traffic_url)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_user).send_keys(data.bs_login_username)
            self.base_page.wait(resources.OldTrafficModuleLocator.login_password).send_keys(data.bs_login_password)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.login_btn)
            login_result = self.base_page.wait(resources.OldTrafficModuleLocator.main_content), "Login failed with valid credentials"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password), {"Pass" if login_result[0] else f"Fail - {login_result[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Login, Valid Login (valid Username and Password),Fail\n', new=False)

    def crud_test_cases(self):
        try:
            self.driver.get(data.bs_project_listing_page)
        
            # Test Case 1: Create Project
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_btn)
            time.sleep(3)
            self.base_page.wait(resources.OldTrafficModuleLocator.project_create_name_input).send_keys(project_name)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_modal_btn)
            project_created = self.base_page.wait(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name)), "Project creation failed"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Create Project, {"Pass" if project_created[0] else f"Fail - {project_created[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Create Project,Fail\n', new=False)
        
        try:
            # Test Case 2: View Project
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name))
            project_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.project_view_check.format(project_name=project_name)), "Project view failed"
            project_id = self.driver.current_url.split("/")[-2]
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, View Project,Fail\n', new=False)
        
        try:
            # Test Case 3: Edit Project
            time.sleep(10)
            self.driver.get(data.bs_project_listing_page)
            time.sleep(6)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_edit_btn.format(project_id=project_id))
            time.sleep(2)
            project_edit_input = self.base_page.wait(resources.OldTrafficModuleLocator.project_edit_name_input)
            time.sleep(2)
            project_edit_input.clear()
            time.sleep(2)
            project_edit_input.send_keys(edited_project_name)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_edit_modal_btn)
            time.sleep(20)
            self.driver.get(data.bs_project_listing_page)
            project_edited = self.base_page.wait(resources.OldTrafficModuleLocator.project_edit_check.format(edited_project_name=edited_project_name)), "Project edit failed"
            if not project_edited[0]:
                self.base_page.click_btn(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name))
                time.sleep(10)
                project_edited = self.base_page.wait(resources.OldTrafficModuleLocator.project_edit_check_2.format(edited_project_name=edited_project_name)), "Project edit failed"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Edit Project, {"Pass" if project_edited[0] else f"Fail - {project_edited[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Edit Project,Fail\n', new=False)


        try:

            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_create_btn)
        

            campaign_types = [
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "organic_keyword",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "organic_direct",
                    "fields": ["direct_url", "wildcard_string"]
                },
                {
                    "campaign_type": "Organic",
                    "campaign_sub_type": "organic_brand",
                    "fields": [ "brand_name", "keyword_modifiers", "wildcard_string"]
                },
                {
                    "campaign_type": "Tiered",
                    "campaign_sub_type": "Tiered",
                    "fields": [ "wildcard_string", "tier1_url", "tier2_url", "destination_url"]
                },
                {
                    "campaign_type": "multiple_session",
                    "campaign_sub_type": "multiple_session",
                    "fields": ["direct_url", "is_spread_session"]
                },
                {
                    "campaign_type": "google_search_no_click",
                    "campaign_sub_type": "google_search_no_click",
                    "fields": ["keyword_modifiers"]
                },
                # {
                #     "campaign_type": "Birthday",
                #     "campaign_sub_type": "Birthday",
                #     "fields": ["image_base64_code", "keyword_modifiers"]
                # },
                {
                    "campaign_type": "Rocket",
                    "campaign_sub_type": "Rocket",
                    "fields": ["gmb_cid", "keyword_modifiers", "gmb_website_percentage", "geo_latitude", "geo_longitude", "radius"]
                },
            ]

            selected_campaign = random.choice(campaign_types)

            def fill_campaign_form(campaign):
                self.base_page.wait(resources.OldTrafficModuleLocator.campaign_name).send_keys(campaign_name)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_category)
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_category_option.format(campaign_type=campaign["campaign_type"].lower()))
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_sub_category)
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_sub_category_option.format(campaign_sub_type=campaign["campaign_sub_type"].lower()))
                time.sleep(2)
                country_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_country)
                self.driver.execute_script("arguments[0].innerHTML = arguments[1];", country_field, resources.OldTrafficModuleLocator.country_inner_html)
                time.sleep(2)
                self.base_page.wait(resources.OldTrafficModuleLocator.campaign_average_session).send_keys(campaign_average_session)
                time.sleep(2)
                if "keyword_modifiers" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_keyword_modifiers)
                    self.base_page.send_key_with_action_chain(wildcard_field, campaign_keyword_modifiers)

                if "direct_url" in campaign["fields"]:
                    direct_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_direct_url)
                    self.base_page.send_key_with_action_chain(direct_url_field, campaign_direct_url)
                    
                if "wildcard_string" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_wildcard_strign)
                    self.base_page.send_key_with_action_chain(wildcard_field, campaign_wildcard_string)

                if "tier1_url" in campaign["fields"]:
                    tier_1_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier1_url)
                    self.base_page.send_key_with_action_chain(tier_1_url_field, campaign_tier1_url)

                    
                if "tier2_url" in campaign["fields"]:
                    tier_2_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier2_url)
                    self.base_page.send_key_with_action_chain(tier_2_url_field, campaign_tier2_url)

                if "destination_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_destination_url)
                    self.base_page.send_key_with_action_chain(wildcard_field, campaign_destination_url)

                if "brand_name" in campaign["fields"]:
                    self.base_page.wait(resources.OldTrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
                
            try:
                # Test Case 1: Create Campaign
                time.sleep(2)
                fill_campaign_form(selected_campaign)
                time.sleep(5)
                submit_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_submit_btn)
                self.driver.execute_script("arguments[0].click();", submit_btn)
                time.sleep(8)

                campaign_created = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign creation failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Create Campaign, {"Pass" if campaign_created[0] else f"Fail - {campaign_created[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Create Campaign,Fail\n', new=False)

            try:
                # Test Case 2: View Campaign
                time.sleep(10)
                campaign_create_check_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name))
                self.driver.execute_script("arguments[0].click();", campaign_create_check_btn)
                campaign_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_view_check.format(campaign_name=campaign_name)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                print(f"Campaign ID: {campaign_id}")
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, View Campaign, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                    self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, View Campaign,Fail\n', new=False)

            try:
                # Test Case 3: Edit Campaign
                time.sleep(2)
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                edit_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_edit_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", edit_btn)
                time.sleep(2)
                self.old_traffic_edit_fields(self.base_page, selected_campaign, self.driver)

                save_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(70)
                campaign_edited = self.old_traffic_edit_fields_check(self.base_page, selected_campaign, self.driver), "Campaign edit failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
                

            try:
                # Test Case 2: View Campaign
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(0)
                campaign_create_check_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited))
                self.driver.execute_script("arguments[0].click();", campaign_create_check_btn)
                campaign_viewed = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_view_check.format(campaign_name=campaign_name_edited)), "Campaign view failed"
                campaign_id = self.driver.current_url.split("/")[-2]
                print(f"Campaign ID: {campaign_id}")
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, View Campaign after edit, {"Pass" if campaign_viewed[0] else f"Fail - {campaign_viewed[1]}"}\n', new=False)
            except Exception as e:
                    self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, View Campaign after edit,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(2)
                live_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", live_btn)
                time.sleep(3)
                live_modal_confirmation_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_live_modal_confirmation)
                self.driver.execute_script("arguments[0].click();", live_modal_confirmation_btn)
                time.sleep(10)
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(20)
                campaign_live = self.base_page.wait(resources.OldTrafficModuleLocator.live_status), "Campaign live failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Live Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Live Campaign,Fail\n', new=False)
        
            try:
                # Test Case 5: Cancel Live Campaign
                time.sleep(2)
                stop_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_stop_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", stop_btn)
                time.sleep(3)
                stop_modal_confirmation_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_stop_modal_confirmation)
                self.driver.execute_script("arguments[0].click();", stop_modal_confirmation_btn)
                time.sleep(10)
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(20)
                campaign_live = self.base_page.wait(resources.OldTrafficModuleLocator.stop_status), "Campaign live failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Cancel Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Cancel Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Delete Campaign
                time.sleep(2)
                delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaing_delete_btn.format(campaign_id=campaign_id))
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(2)
                delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.capmaign_delete_modal_btn)
                time.sleep(2)
                self.driver.execute_script("arguments[0].click();", delete_modal_btn)
                time.sleep(6)
                campaign_deleted = not self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name)), "Campaign deletion failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Delete Campaign, {"Pass" if campaign_deleted else f"Fail - {campaign_deleted[1]}"}\n', new=False)
                
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Delete Campaign,Fail\n', new=False)
                
            try:
                # Test Case 4: Delete Project
                self.driver.get(data.bs_project_listing_page)
                time.sleep(2)
                delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_btn.format(project_id=project_id))
                self.driver.execute_script("arguments[0].click();", delete_btn)
                time.sleep(2)
                delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_modal_btn)
                self.driver.execute_script("arguments[0].click();", delete_modal_btn)
                time.sleep(6)
                project_deleted = not self.base_page.wait(resources.OldTrafficModuleLocator.project_deleted_list_check.format(edited_project_name=edited_project_name)), "Project deletion failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Delete Project, {"Pass" if project_deleted else f"Fail - {project_deleted[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Delete Project,Fail\n', new=False)
                
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, CRUD Test Cases,Fail\n', new=False)

            
    def report_test_cases(self):
        
        try:
            # Test Case 2: Select a project, a campaign, and filter records
            table_rows = None
            self.driver.get(data.bs_report_page)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.report_project_filter)
            time.sleep(0.5)
            project_filter_options = self.base_page.wait_all(resources.OldTrafficModuleLocator.report_project_filter_option)
            for index, option in enumerate(project_filter_options):
                if index == 0:
                    continue
                option.click()
                time.sleep(5)

                self.base_page.click_btn(resources.OldTrafficModuleLocator.report_campaign_filter)
                time.sleep(2)
                campaign_filter_options = self.base_page.wait_all(resources.OldTrafficModuleLocator.report_campaign_filter_option)
                for campaign_index, option in enumerate(campaign_filter_options):
                    if campaign_index == 0:
                        continue
                    option.click()
                    time.sleep(90)
                
                    table_rows = self.base_page.wait(resources.OldTrafficModuleLocator.report_result_row)
                    if table_rows:
                        self.base_page.make_csv("BS_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Pass\n', new=False)
                        break
                if table_rows:
                    break
                if index == 7:
                    self.base_page.make_csv("BS_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail - No results found\n', new=False)
                    break
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Report, Filter by Project and Campaign, Fail\n', new=False)
            
    def campaign_error_and_graph_stats(self):
        try:
            self.driver.get(data.bs_campaign_error_page)
            time.sleep(5)
            error_page_row = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_error_page_row).text
            data_list_24_days = error_page_row.split(' ')
            data_dict_24_days = {
                "campaing_id": data_list_24_days[0],
                "total_failed": data_list_24_days[1],
                "google_recaptcha": data_list_24_days[2],
                "wildcard_not_found": data_list_24_days[3],
                "product_wildcard_not_found": data_list_24_days[4],
                "page_not_loaded": data_list_24_days[5],
                "other_errors": data_list_24_days[6]
            }
            print(data_dict_24_days)
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_1_month_option)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_error_filter_btn)
            time.sleep(40)
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_7_day_option)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_error_filter_btn)
            time.sleep(40)
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter)
            time.sleep(0.5)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_1_day_option)
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_error_filter_btn)
            time.sleep(40)
            error_page_row = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_error_page_row).text
            data_list = error_page_row.split(' ')
            data_dict = {
                "campaing_id": data_list[0],
                "total_failed": data_list[1],
                "google_recaptcha": data_list[2],
                "wildcard_not_found": data_list[3],
                "product_wildcard_not_found": data_list[4],
                "page_not_loaded": data_list[5],
                "other_errors": data_list[6]
            }
            
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_link)
            time.sleep(5)
            cleaned_data = []
            graph_data_list = []
            raw_data = self.driver.page_source
            page_src = raw_data.split('var options')[1]
            data_splited = page_src.split('],')[0]
            fixed_string = data_splited.replace("'", '"')
            fixed_string = fixed_string.split('=', 1)[1].strip()
            splited_data_by_new_line = fixed_string.split('\n')
            for data_values in splited_data_by_new_line:
                if "data" in data_values:
                    graph_data_list.append(data_values)
            for values in graph_data_list:
                values_splited = int(values.split(',')[-1].replace(' ', '').replace(']', '').replace('"', ''))
                cleaned_data.append(values_splited)
            print(cleaned_data)
                    
            google_recaptcha_check = int(data_dict["google_recaptcha"]) == int(cleaned_data[4])
            wildcard_not_found_check = int(data_dict["wildcard_not_found"]) == int(cleaned_data[2])
            product_wildcard_not_found_check = int(data_dict["product_wildcard_not_found"]) == int(cleaned_data[3])
            total_failed_check = int(data_dict["total_failed"]) == int(cleaned_data[1])
            
            if google_recaptcha_check and wildcard_not_found_check and product_wildcard_not_found_check and total_failed_check:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Pass\n', new=False)
            else:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            
            time.sleep(2)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign error and graph stats, Error and Graph Stats, Fail\n', new=False)
            print(e)
            
        
        
    def full_dashboard_must_haves(self):
        self.login_test_cases()
        self.crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("BS Dashboard Must Haves Test Cases Completed")