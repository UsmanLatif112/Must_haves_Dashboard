# Imports
import json
import random
from lib.driver import *
from lib import data, page, resources



# Sample Data
project_name = "-AI-TEST-PROJECT-SQA"
edited_project_name = "-AI-TEST-PROJECT-SQA-EDITED"
project_id = None

campaign_name = "-AI-TEST-Campaign-SQA"
campaign_name_edited = "-AI-TEST-Campaign-SQA-Edited"
campaign_country = "US"
campaign_average_session = "10"
campaign_image_base64 = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8NDw4QEBAPDxAVDhAPERUYDhYQEBEQIB0bFhcSGBUaHigsGB0lHhYVITEjJSs3Li4vGSIzOT8sNygtLi4BCgoKDg0OGhAQGi0lHyUtLSsvLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0vLSsuKy0tLS0tLS0tLS0tLS4tLS0tLf/AABEIAMgAyAMBEQACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAABgcBBAUDAv/EADgQAAICAQIDBgUCBQIHAAAAAAABAgMEBREGEiETMVFhcYEHFCJBkSMyQnKCobEV0WKDkrLBwvD/xAAbAQEAAgMBAQAAAAAAAAAAAAAABAUBAwYCB//EACkRAQACAQMEAgEDBQAAAAAAAAABAgMEERIFITFBE1EyFGGhBkJxgbH/2gAMAwEAAhEDEQA/ALxAAAAAAAAAAAAABgAAAMDIAAAAAAAAAAAAAAAAAAAAAAABhsH7IVrfxAqx7JV01du4tqUuflhv4Lo9yJk1UUXel6LkzV5XnaH3pHxBxrto3Rljy8W+eH/Uu73Qpqq28vOo6Lmx96d4S3HyIWxUq5RnF9zUlJP3RKi0T4VFqTSdpju9jLyAAAAAAAAAAAAAAAAAAAAAAAOFxjqvyeHbNPacl2dfjzv7+y3fsac9+NN03p+n+fPFVLFRLvKxtEQGGdt23p+p34suam2db8n9L9V3P3Nlcs1Rs2lw542vC1uCeInqFUudJXVtKe3dJPukvw/wWWDLzhyHUtD+mydvE+EkRIVrIAAAAAAAAAAAAAAAAAAAAAFVfEvVO2yY0Rf0VLr52Pv9dlt+WVurvvbi63oem445yT5lDiGvv2B4Ayf4WN8KsKUYZF76Rk41x89t23/df3LDR02jdynXs+9q09wn5Nc+yAAAAAAAAAAAAAAAAAAAGANPV86OLRbdLuhBvbxf2Xu9keL24xybdPinNkike1FZF0rZznJ7ylJyk/NvdlPa287voODFGOsRDzPENnsM+9x90VSslGEVvKUlGK8W3shWu9tnjLeMUTafC9NF0+OJj00x/ggk3ttvL+J+73ZdY68YfP8AUZpzZbXn23j20MgAAAAAAAAAAAAAAAAAABgCvvilquyqxYvv/Vs9F0ivzu/ZELWZO3F0XQtNvacs+vCuyu2dRsA8AJjdLvhtpXb5TukvopW687H0ivb6n+CZpab23UfXNTwxfHHmVrlk5EAyAAAAAAAAAAAAAAAAAAAHnbYoRcpNKKTbf2SRiftmtZtMRCi9d1F5eTdc/wCKf0rwgukV+NinzX5X5O+0Wn+HDFGiaksACCZ2XPwVpXymHXFrac/1bPHmf2fotl7Fxgpxq4TqWo+bPM+nfNyAAAAAAAAAAAAAAAAAAAAAAiPxH1XsMTsov67nyf8ALXWf/hf1EbU3412+1t0fT/Lm5T4hU5VO127AYAO3wdpfzmZVBreEX2lnhyrrt7vZe5v09OVlb1TU/DgnbzPhdSLdw7IAAAAAAAAAAAAAAAAAAAYAAU1xzqnzeZZs94V/pQ8On7n+d/wiq1N+Vna9J004cET7lHyOtt+4AMMePC0/hppfY40r5L6rX08q10X5e7/BZ6WnGu7jutan5M3CPEJkS1MyAAAAAAAAAAAAAAAAAAAGAONxbqnyeJbYntNrkr/nfRfjq/Y1Zr8a7pmg0/zZq1UmU897O+pHGNgT5NtgMtvSMGWVfVTHvnNR9F3t+y3Z7xV5SjarNGDDa8r1x6I1QjCK2jGKjFeCXRIuaxtGz5/e03mZl6mXlkAAAAAAAAAAAAAAAAAAAMAVb8TdU7XIhjxf01LeXnY/9lt+WV2rybzx+nVdC03GnyT7QwhOgAAkT/4XaVu7cqS7v0q/Xvk/8L8k/SU/ucz13U94xR/tYxPc2wOxsJmN4NtmTIyAAAAAAAAAAAAAAAAAaeqZscam26X7YQcn4vwXq+483txjdtwYpyXike1FZWRK6ydk3vKc3OXq3uUtp5Tu+g4ccYscVh5HlsAPqqtzlGMVvKUlFLxb7keqxvbZ4yXilZtK89C0+OJjU0r+GC3fjJ9ZP3e5cY6ca7Pn+qzTmy2vPtzeLuJo6fWkkp3ST5I/Zf8AFLy/yeMuaMcJPT9DbU2+oVbqOuZWVJytum/JS5YLyUV0K22a15ddg0OHFG1avHD1TIoadV1kH5Tez9YvoxXLaveHvLo8OT8oWXwXxd87+jdtG9LeLXRWL7vb7PyJ+DUfJ2s5XqXTZ0886/j/AMTAlKgAAAAAAAAAAAAAAAAQD4o6rtCrFi+sn2ln8q/an6vr/SQ9XfavF0HQ9NyvOWfSuCudVt7DAASz4caV8xl9rJbwpXN62PpFf5fsS9JTe3JSdb1PDFwjzK2SzcgpTjHMd+dkt90bHVFeCj9O35TfuVOptveYdx0rFFNNWY9uKR1nAPEnf02NOy5Y91Vsd04TjL1271/k2Y7cbbo+pxRlxWrZfkHuk/JF0+ezHd9BgAAAAAAAAAAAAAB8WTUU23skm2/BBmsbztCjeINSeZk3XfaUtoeUF0j6dOpTZb87zLvdDg+DBWrnGpN8wBgMkztG65OB9K+Uw601tZZ+rPx3fcvZbL8ltgpxo4Xqep+bPM+o7QkJvV6luNMF4+dkJrpObti/FS6/53XsVOprteZdv0nLGTT1iPThkdZg8yzG/ps6Xhyyb6qY77zmo+i+79l1NmOvK2yLqssYcVrWX3FbJehdPn8z3fQYAAAAAAAAAAAAAwGEV+ImqfL4bri/rubrXjyfxv8AHT+ojam/Gu32tukab5c8T6hUhVu1DABl2OEtL+cy6q2t4J9pZ/Ivt7vZe5vwU53V3U9T8OGZ9z4XalsW7hWQODxTw5XqNaTfJbHd1z2328n4o05cVbx3TtFrr6W28ePpV+o8MZuNJqVE5L7ShF2Rfn07vcrrae9Z7Osw9T0+WPy2n6eWFw/mXy5YY9vq4OEV/U+h5jBeZe8vUMGPzZZHB/CUcBdrY1O9rbdftrXhH/cscOCtIct1DqM6mdo7VSskKsAAAAAAAAAAAAABgCnOPNV+azJpPeureqPhuv3P89PZFVqMnK2307XpGm+LBvPmUdIy1AAPe60PhlpfZY8siS+q17R8VWun93u/wWelptXk5DrWp+TLw9QmxLUgBjYAY2+zdjYz4N2QMgAAAAAAAAAAAAAAfE+5+jDMeVAZNUq5zhNNTjJxlv3qSfUo7RO87vomntF6Ravh5nlu7yCNzZ3OFuHbNQtS2caYv9Sf/qvFm/Dhm87yq+odQpp6du9pXJj0xrhGEEoxjFRil3JLuRbRG0bOKvab2mbe3sZeQAAAAAAAAAAAAAAAAAAAAGAwjuvcI4udJ2SUq7XtvOL2b/mXczRlwRdY6XqWbBHGvj6Ryfwzlv0ylt509f8AuI/6KPta1/qCdu9P5dDTvhzj1tO6yd/lt2cH67bv+5srpawi5ut5r/hG38pfi40KYxhXGMIJbJJbJIlRER4U2TJa872l7GXlkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB8ykkm30XeB4YGdTk1xtosruqlvyzhNThLZ7PaS7+qa9gNkAAAAAAAAAA1cjPpqnTXZbXCy1yjVCU1Gdkkt2op/u2XgBtAAAAAAAAAAAAAAg/F2u6np6yL1bpEaa1KyuiyVkcm+qPVpTcklNpPZKL6+IEo03UIZeJTkwX0XY0L4p9fplHm5X+QOF8Oc95WjYt1VONjSnC9wrrrdeNCSnOK+nfdJtbv1YEf+Fz1J5OrOyWG6VrOXHJ2jb2vbKMV+k3LZQ35Okuu24Ei1/iDK+dq03ArplkyoeVdZdzOjHo35E3GPWcm+5boD50LiHLWfPTdQhQr/l/mqLaeZU3078slySbcJp/bd/7h8cT8R5uPqGFg4lNFssii+alY5RjXODX1yafWKXN0S3b2W6A5uLxJrUsy/S5U4Hzka45MchdqsT5Z9N3VvzOfNstt9u/w6h2uCeIMjMebj5ddVeXiZHY29m5djOLXNCyCl1Sa+zA+uJ8vUaZOVF+lY1CguV5Pac1ln3i2pRUV3derA9uCuIf9WwKcrkVc5c8JxUuaMbIycHs/uum/owIhwE9Ueq6zzzwnFZlCyto27/s6KneX0r+YCR8U58atS0Op0Y9rtvyoqydfNbRtXzb1S/hb7n6AbfGPEMtProjTUr8rIyIYuNW5ckHY+rnOX2jFLd//MDlW8Qalp2Rhw1KOHbj5N8cWNuPGyt0ZEv2RnGyT5ovZrdbAdDj7iK3Ssam+qqN0pZlFDg995Qk2movdbS6dG+gHKs4h1XBy8GGoV4Lxsu9Y0HQ7e0x72t4Rk59Jp7bbpLufuE7AAAAAAAAAVBHRMqNOrY92kzy9Rvsy+TMkqpUOqaarkrZS5ocq7q4r7Lu+wWFwjh2UaVg02RcLYYNNU4vbeM1BRcenmBo/C7Tb8LR8KjIrdV0I2qcHtvHeycl3eTQGhwdTk4GfqePbiXuvJ1G/OqyYqEsdQlFPlm+beL+nbu737gfeuYWVharHU8fHnmU2YfyeVVW49vDaXPC6EZNc/g1uBnRsPKztV/1O/Hnh0VYksXFqscfmJylLmnbNRbUF02S38wNjVtMvnrumZMa5OivEy4WT6csZS25V7gMbTL1xBkZTrkseWk10Rs6crtVnM4euwDhTTL6NT126yuUK778WVMnttYo18smvRgcTM0+6rVs+7J0u3VFbGlYE1GqyqiCjtKp9pJKn6urlt1A7Hws0rIwtO7HJq7G1ZOTJxW3LyubacfLwA1tCpycHWNTU8S+yjMvpuqvhySphtDlkrN5Jx6+TA3OK9Mvv1PQrq65TrovypXSW21alXyxb9WBnj3R8m/5HLxIK3Iw8pZEanJQ7etrlsrUn0jJrbZsDmapHM1y/T6/ksnCxaMyrNyJ39nGc517uFNcIylzJt9ZdAOl8SdMvy8bFhRXKyUdSxLpJbdK4y3lL0QDj7TL8qejOmuVip1nFyLdtvopipc036boCXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//Z"
campaign_image_url = "http://image.url"
campaign_gmb_cid = "1234567890"
campaign_geo_latitude = "10"
campaign_geo_longitude = "10"
campaign_radius = "10"
campaign_gmb_website_percentage = "100"
campaign_keyword_modifiers = "keyword"
campaign_direct_url = "http://direct.url"
campaign_brand_name = "Brand"
campaign_wildcard_string = "http://wildcard.url"
campaign_tier1_url = "http://tier1.url"
campaign_tier2_url = "http://tier2.url"
campaign_destination_url = "http://destination.url"

class CE_Traffic_TestCases:
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

    def project_crud_test_cases(self):
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
            # Test Case 2: View Project
            time.sleep(2)
            self.driver.get(data.ce_project_listing_page)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id))
            project_viewed = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project view failed"
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("CE_traffic_must_haves.csv", f'Project, View Project,Fail\n', new=False)
        
        try:
            # Test Case 3: Edit Project
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
            # Test Case 4: Delete Project
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

    def campaign_crud_test_cases(self):
        try:
            self.driver.get(data.ce_project_listing_page)
        
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_btn)
            time.sleep(2)
            self.base_page.wait(resources.TrafficModuleLocator.project_create_name_input).send_keys(project_name)
            
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_modal_btn)
            time.sleep(2)
            print(f"Project Created- Getting project id {self.driver.current_url}")
            project_id = self.driver.current_url.split("/")[-2]
            print(f"Project ID: {project_id}")
            time.sleep(5)
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
                {
                    "campaign_type": "Website Specific",
                    "campaign_sub_type": "aitomation.com",
                    "fields": ["brand_name", "wildcard_string", "keyword_modifiers", "is_product"]
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
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_country_option)

                if "image_base64_code" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_image_base64).send_keys(campaign_image_base64)
                if "image_url" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_image_url).send_keys(campaign_image_url)
                if "keyword_modifiers" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers)
                    new_inner_html = f'''
                        <tag title="{campaign_keyword_modifiers}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_keyword_modifiers}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_keyword_modifiers}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_keyword_modifiers)

                if "direct_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_direct_url)
                    new_inner_html = f'''
                        <tag title="{campaign_direct_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_direct_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_direct_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_direct_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_direct_url)
                if "is_spread_session" in campaign["fields"]:
                    self.base_page.click_btn(resources.TrafficModuleLocator.campaign_is_spread_session)
                if "brand_name" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
                if "wildcard_string" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_strign)
                    new_inner_html = f'''
                        <tag title="{campaign_wildcard_string}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_wildcard_string}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_wildcard_string}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_strign_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_wildcard_string)

                if "tier1_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url)
                    new_inner_html = f'''
                        <tag title="{campaign_tier1_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_tier1_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_tier1_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_tier1_url)

                if "tier2_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url)
                    new_inner_html = f'''
                        <tag title="{campaign_tier2_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_tier2_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_tier2_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_tier2_url)

                if "destination_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_destination_url)
                    new_inner_html = f'''
                        <tag title="{campaign_destination_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_destination_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_destination_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_destination_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_destination_url)
                
                if "select_wildcard_type_option" in campaign["fields"]:
                    self.base_page.click_btn(resources.TrafficModuleLocator.campaign_select_wildcard_type_option)
                if "is_product" in campaign["fields"]:
                    self.base_page.click_btn(resources.TrafficModuleLocator.campaign_is_product)

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
                input_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_edit_name_input.format(campaign_name=campaign_name))
                input_field.clear()
                input_field.send_keys(campaign_name_edited)
                save_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(3)
                cancel_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_cancel_btn)
                self.driver.execute_script("arguments[0].click();", cancel_btn)
                campaign_edited = self.base_page.wait(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited)), "Campaign edit failed"
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("CE_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
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
            self.driver.get(data.ce_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
        except Exception as e:
            print(e)
            
            
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
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_option)
            time.sleep(10)
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
        self.project_crud_test_cases()
        self.campaign_crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Full CE Dashboard Must Haves Test Cases Completed")

class Tiger_Traffic_TestCases:
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

    def project_crud_test_cases(self):
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
            # Test Case 2: View Project
            time.sleep(2)
            self.driver.get(data.tiger_project_listing_page)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_created_list_check.format(project_id=project_id))
            project_viewed = self.base_page.wait(resources.TrafficModuleLocator.project_view_check), "Project view failed"
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, View Project, {"Pass" if project_viewed[0] else f"Fail - {project_viewed[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Project, View Project,Fail\n', new=False)
        
        try:
            # Test Case 3: Edit Project
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
            # Test Case 4: Delete Project
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

    def campaign_crud_test_cases(self):
        try:
            self.driver.get(data.tiger_project_listing_page)
        
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_btn)
            time.sleep(2)
            self.base_page.wait(resources.TrafficModuleLocator.project_create_name_input).send_keys(project_name)
            
            time.sleep(2)
            self.base_page.click_btn(resources.TrafficModuleLocator.project_create_modal_btn)
            time.sleep(2)
            print(f"Project Created- Getting project id {self.driver.current_url}")
            project_id = self.driver.current_url.split("/")[-2]
            print(f"Project ID: {project_id}")
            time.sleep(5)
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
                self.base_page.click_btn(resources.TrafficModuleLocator.campaign_country_option)

                if "image_base64_code" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_image_base64).send_keys(campaign_image_base64)
                if "image_url" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_image_url).send_keys(campaign_image_url)
                if "gmb_cid" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_gmb_cid).send_keys(campaign_gmb_cid)
                if "geo_latitude" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_geo_latitude).send_keys(campaign_geo_latitude)
                if "geo_longitude" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_geo_longitude).send_keys(campaign_geo_longitude)
                if "keyword_modifiers" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers)
                    new_inner_html = f'''
                        <tag title="{campaign_keyword_modifiers}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_keyword_modifiers}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_keyword_modifiers}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_keyword_modifiers_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_keyword_modifiers)

                if "direct_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_direct_url)
                    new_inner_html = f'''
                        <tag title="{campaign_direct_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_direct_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_direct_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_direct_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_direct_url)
                if "is_spread_session" in campaign["fields"]:
                    self.base_page.click_btn(resources.TrafficModuleLocator.campaign_is_spread_session)
                if "brand_name" in campaign["fields"]:
                    self.base_page.wait(resources.TrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
                if "wildcard_string" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_strign)
                    new_inner_html = f'''
                        <tag title="{campaign_wildcard_string}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_wildcard_string}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_wildcard_string}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_wildcard_strign_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_wildcard_string)

                if "tier1_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url)
                    new_inner_html = f'''
                        <tag title="{campaign_tier1_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_tier1_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_tier1_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier1_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_tier1_url)

                if "tier2_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url)
                    new_inner_html = f'''
                        <tag title="{campaign_tier2_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_tier2_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_tier2_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_tier2_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_tier2_url)

                if "destination_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_destination_url)
                    new_inner_html = f'''
                        <tag title="{campaign_destination_url}" contenteditable="false" spellcheck="false" tabindex="-1" class="tagify__tag " value="{campaign_destination_url}">
                            <x title="" class="tagify__tag__removeBtn" role="button" aria-label="remove tag"></x>
                            <div><span class="tagify__tag-text">{campaign_destination_url}</span></div>
                        </tag>
                        <span contenteditable="" tabindex="0" data-placeholder="&ZeroWidthSpace;" aria-placeholder="" class="tagify__input" role="textbox" aria-autocomplete="both" aria-multiline="false"></span>
                        &ZeroWidthSpace;
                    </tags>
                    '''
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, new_inner_html)
                    # Update the hidden textarea value
                    hidden_textarea = self.base_page.wait(resources.TrafficModuleLocator.campaign_destination_url_textarea)
                    self.driver.execute_script("arguments[0].value = arguments[1];", hidden_textarea, campaign_destination_url)
                
                if "select_wildcard_type_option" in campaign["fields"]:
                    self.base_page.click_btn(resources.TrafficModuleLocator.campaign_select_wildcard_type_option)
                if "is_product" in campaign["fields"]:
                    self.base_page.click_btn(resources.TrafficModuleLocator.campaign_is_product)

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
                time.sleep(10)
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
                input_field = self.base_page.wait(resources.TrafficModuleLocator.campaign_edit_name_input.format(campaign_name=campaign_name))
                input_field.clear()
                input_field.send_keys(campaign_name_edited)
                save_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(3)
                cancel_btn = self.base_page.wait(resources.TrafficModuleLocator.campaign_cancel_btn)
                self.driver.execute_script("arguments[0].click();", cancel_btn)
                campaign_edited = self.base_page.wait(resources.TrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited)), "Campaign edit failed"
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Tiger_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
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
            self.driver.get(data.tiger_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.TrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
        except Exception as e:
            print(e)
            
            
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
            self.base_page.click_btn(resources.TrafficModuleLocator.campaing_error_filter_option)
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
            
        
        
    def full_dashboard_must_haves(self):
        self.login_test_cases()
        self.project_crud_test_cases()
        self.campaign_crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Tiger Dashboard Must Haves Test Cases Completed")
        
        
        
class Torrential_Traffic_TestCases:
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

    def project_crud_test_cases(self):
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
            # Test Case 4: Delete Project
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

    def campaign_crud_test_cases(self):
        try:
            self.driver.get(data.torrential_project_listing_page)
        
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_btn)
            time.sleep(2)
            self.base_page.wait(resources.OldTrafficModuleLocator.project_create_name_input).send_keys(project_name)
            
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_modal_btn)
            time.sleep(2)

            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name))
            time.sleep(5)
            print(f"Project Created- Getting project id {self.driver.current_url}")
            project_id = self.driver.current_url.split("/")[-2]
            print(f"Project ID: {project_id}")
            
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
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, resources.OldTrafficModuleLocator.keyword_inner_html.format(keyword=campaign_keyword_modifiers))

                if "direct_url" in campaign["fields"]:
                    direct_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_direct_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", direct_url_field, resources.OldTrafficModuleLocator.direct_url_inner_html.format(direct_url=campaign_direct_url))
                    
                if "brand_name" in campaign["fields"]:
                    self.base_page.wait(resources.OldTrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
                    
                if "wildcard_string" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_wildcard_strign)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, resources.OldTrafficModuleLocator.wildcard_url_inner_html.format(wildcard_url=campaign_wildcard_string))

                if "tier1_url" in campaign["fields"]:
                    tier_1_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier1_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", tier_1_url_field, resources.OldTrafficModuleLocator.tier_1_url_inner_html.format(tier_url=campaign_tier1_url))

                    
                if "tier2_url" in campaign["fields"]:
                    tier_2_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier2_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", tier_2_url_field, resources.OldTrafficModuleLocator.tier_2_url_inner_html.format(tier_2_url=campaign_tier2_url))

                if "destination_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_destination_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, resources.OldTrafficModuleLocator.destination_inner_html.format(destination_url=campaign_destination_url))
                
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
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name))
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
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_edit_btn.format(campaign_id=campaign_id))
                time.sleep(2)
                input_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_name_input.format(campaign_name=campaign_name))
                input_field.clear()
                input_field.send_keys(campaign_name_edited)
                save_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(6)
                self.driver.get(data.torrential_campaing_listing_page.format(project_id=project_id))
                time.sleep(3)
                campaign_edited = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited)), "Campaign edit failed"
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                time.sleep(3)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_live_modal_confirmation)
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
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_stop_btn.format(campaign_id=campaign_id))
                time.sleep(3)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_stop_modal_confirmation)
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
        except Exception as e:
            self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign, CRUD Test Cases,Fail\n', new=False)
            
        try:
            self.driver.get(data.torrential_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
        except Exception as e:
            print(e)
            
            
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
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_option)
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
            print(data_dict)
            filter_check = int(data_dict["total_failed"]) != int(data_dict_24_days["total_failed"])
            
            if filter_check:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Pass\n', new=False)
            else:
                self.base_page.make_csv("Torrential_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Fail\n', new=False)
            
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
        self.project_crud_test_cases()
        self.campaign_crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Torrential Dashboard Must Haves Test Cases Completed")
        
        
        
        
class BS_Traffic_TestCases:
    def __init__(self):
        self.driver = initialize_and_navigate(data.bs_traffic_url)
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

    def project_crud_test_cases(self):
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
            time.sleep(10)
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
            # Test Case 4: Delete Project
            self.driver.get(data.bs_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
            time.sleep(20)
            self.driver.get(data.bs_project_listing_page)
            project_deleted = not self.base_page.wait(resources.OldTrafficModuleLocator.project_deleted_list_check.format(edited_project_name=edited_project_name)), "Project deletion failed"
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Delete Project, {"Pass" if project_deleted else f"Fail - {project_deleted[1]}"}\n', new=False)
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Project, Delete Project,Fail\n', new=False)

    def campaign_crud_test_cases(self):
        try:
            self.driver.get(data.bs_project_listing_page)
        
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_btn)
            time.sleep(2)
            self.base_page.wait(resources.OldTrafficModuleLocator.project_create_name_input).send_keys(project_name)
            
            time.sleep(2)
            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_create_modal_btn)
            time.sleep(2)

            self.base_page.click_btn(resources.OldTrafficModuleLocator.project_created_list_check.format(project_name=project_name))
            time.sleep(5)
            print(f"Project Created- Getting project id {self.driver.current_url}")
            project_id = self.driver.current_url.split("/")[-2]
            print(f"Project ID: {project_id}")
            
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
                {
                    "campaign_type": "Birthday",
                    "campaign_sub_type": "Birthday",
                    "fields": ["image_base64_code", "keyword_modifiers"]
                },
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
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, resources.OldTrafficModuleLocator.keyword_inner_html.format(keyword=campaign_keyword_modifiers))

                if "direct_url" in campaign["fields"]:
                    direct_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_direct_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", direct_url_field, resources.OldTrafficModuleLocator.direct_url_inner_html.format(direct_url=campaign_direct_url))
                    
                if "brand_name" in campaign["fields"]:
                    self.base_page.wait(resources.OldTrafficModuleLocator.campaign_brand_name).send_keys(campaign_brand_name)
                    
                if "wildcard_string" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_wildcard_strign)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, resources.OldTrafficModuleLocator.wildcard_url_inner_html.format(wildcard_url=campaign_wildcard_string))

                if "tier1_url" in campaign["fields"]:
                    tier_1_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier1_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", tier_1_url_field, resources.OldTrafficModuleLocator.tier_1_url_inner_html.format(tier_url=campaign_tier1_url))

                    
                if "tier2_url" in campaign["fields"]:
                    tier_2_url_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_tier2_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", tier_2_url_field, resources.OldTrafficModuleLocator.tier_2_url_inner_html.format(tier_2_url=campaign_tier2_url))

                if "destination_url" in campaign["fields"]:
                    wildcard_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_destination_url)
                    self.driver.execute_script("arguments[0].innerHTML = arguments[1];", wildcard_field, resources.OldTrafficModuleLocator.destination_inner_html.format(destination_url=campaign_destination_url))
                
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
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name))
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
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_edit_btn.format(campaign_id=campaign_id))
                time.sleep(2)
                input_field = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_name_input.format(campaign_name=campaign_name))
                input_field.clear()
                input_field.send_keys(campaign_name_edited)
                save_btn = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_edit_save_btn)
                self.driver.execute_script("arguments[0].click();", save_btn)
                time.sleep(6)
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(3)
                campaign_edited = self.base_page.wait(resources.OldTrafficModuleLocator.campaign_create_check.format(campaign_name=campaign_name_edited)), "Campaign edit failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Edit Campaign, {"Pass" if campaign_edited[0] else f"Fail - {campaign_edited[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Edit Campaign,Fail\n', new=False)
        
            try:
                # Test Case 4: Live Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_live_btn.format(campaign_id=campaign_id))
                time.sleep(3)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_live_modal_confirmation)
                time.sleep(10)
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(10)
                campaign_live = self.base_page.wait(resources.OldTrafficModuleLocator.live_status), "Campaign live failed"
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Live Campaign, {"Pass" if campaign_live[0] else f"Fail - {campaign_live[1]}"}\n', new=False)
            except Exception as e:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, Live Campaign,Fail\n', new=False)
        
            try:
                # Test Case 5: Cancel Live Campaign
                time.sleep(2)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaign_stop_btn.format(campaign_id=campaign_id))
                time.sleep(3)
                self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_stop_modal_confirmation)
                time.sleep(10)
                self.driver.get(data.bs_campaing_listing_page.format(project_id=project_id))
                time.sleep(10)
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
        except Exception as e:
            self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign, CRUD Test Cases,Fail\n', new=False)
            
        try:
            self.driver.get(data.bs_project_listing_page)
            time.sleep(2)
            delete_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_btn.format(project_id=project_id))
            self.driver.execute_script("arguments[0].click();", delete_btn)
            time.sleep(2)
            delete_modal_btn = self.base_page.wait(resources.OldTrafficModuleLocator.project_delete_modal_btn)
            self.driver.execute_script("arguments[0].click();", delete_modal_btn)
        except Exception as e:
            print(e)
            
            
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
                    time.sleep(60)
                
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
            self.base_page.click_btn(resources.OldTrafficModuleLocator.campaing_error_filter_option)
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
            print(data_dict)
            filter_check = int(data_dict["total_failed"]) != int(data_dict_24_days["total_failed"])
            
            if filter_check:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Pass\n', new=False)
            else:
                self.base_page.make_csv("BS_traffic_must_haves.csv", f'Campaign error and graph stats, Data Filtering, Fail\n', new=False)
            
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
        self.project_crud_test_cases()
        self.campaign_crud_test_cases()
        self.report_test_cases()
        self.campaign_error_and_graph_stats()
        print("Torrential Dashboard Must Haves Test Cases Completed")