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


def init_the_testing(GMB_cid, User_name, Pass_word):
    try:
        driver = initialize_and_navigate(url)
        actions = ActionChains(driver)
        try:
            Login_Pagee = HomePage(driver)
            Login_Pagee.wait(Login.login_page)
        except:
            pass
        csvv = HomePage(driver)
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
        
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
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Pass\n', new=False)
            else:
                print("UnSuccessfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
            
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
        
        
        time.sleep(1.5)
        main_buttion = HomePage(driver)
        main_buttion.click_btn(QuickAnalysispage.main_buttion)
        
        # main page 
        try:
                
            create_q_cam_page = HomePage(driver)
            create_q_cam_page.wait(QuickAnalysispage.create_q_cam_page)
            
            if create_q_cam_page:
                print("Successfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis page button,Pass\n', new=False)
            else:
                print("UnSuccessfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis page button,Fail\n', new=False)
            
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis page button,Fail\n', new=False)
        
        time.sleep(1.5)
        gmb_cid_feild = HomePage(driver)
        gmb_cid_feild.click_btn(QuickAnalysispage.gmb_cid_feild)
        
        time.sleep(1.5)
        gmb_cid_feild = HomePage(driver)
        gmb_cid_feild.enter_name_delay(QuickAnalysispage.gmb_cid_feild, GMB_cid)
        
        time.sleep(1.5)
        check_gmb_cid = HomePage(driver)
        check_gmb_cid.click_btn(QuickAnalysispage.check_gmb_cid)
        
        try:
            try:
                    
                check_gmb_cid_k = HomePage(driver)
                check_gmb_cid_k.waitte(QuickAnalysispage.check_gmb_cid_incorrect)
                
                if check_gmb_cid_k:
                    print("Successfull")
                    csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Pass\n', new=False)
                else:
                    print("UnSuccessfull")
                    csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Fail\n', new=False)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Incorect CID,Fail\n', new=False) 
                    driver.quit()
                
            except:
                
                check_gmb_cid_k = HomePage(driver)
                check_gmb_cid_k.waitte(QuickAnalysispage.check_gmb_cid_k)
                
                if check_gmb_cid_k:
                    print("Successfull")
                    csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Pass\n', new=False)
                else:
                    print("UnSuccessfull")
                    csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Fail\n', new=False)    
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Click on check button to check GMB CID,Fail\n', new=False)
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Check GMB CID,Incorect CID,Fail\n', new=False) 
            driver.quit()
            
        time.sleep(2.5)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        try:
            time.sleep(5)
            Keyword_list = HomePage(driver)
            Keyword_list = HomePage.get_key_words(driver)
        except:
            time.sleep(1.5)
            key_feild = HomePage(driver)
            key_feild.click_btn(QuickAnalysispage.key_feild)
            
            time.sleep(1.5)
            key_feild = HomePage(driver)
            key_feild.enter_name_delay(QuickAnalysispage.key_feild, keyword)
        
        time.sleep(3)
        business_name = driver.find_element(By. XPATH, QuickAnalysispage.business_location)
        time.sleep(3)
        print(business_name.text)
        business = business_name.text
        print(business)
        submit_btn = HomePage(driver)
        submit_btn.click_btn(QuickAnalysispage.submit_btn)
        
        time.sleep(1.5)
        driver.refresh()
        time.sleep(1.5)
        
        try:
            time.sleep(5)
            time.sleep(1.5)
            driver.refresh()
            time.sleep(1.5)
            Noti = HomePage(driver)
            Noti.click_btn(QuickAnalysispage.Notification)
            time.sleep(2.5)
            try:
                Notifications = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {business} quick analysis completed.')]/h6")
                time.sleep(2.5)
                if Notifications:
                    time.sleep(2.5)
                    print("Successfull")
                    print(Notifications.text)
                    time.sleep(2.5)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign {Notifications.text},Pass\n', new=False)
                else:
                    time.sleep(2.5)
                    print("fail")
            except:
                Notificationss = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), '1 minute ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {business} quick analysis completed.')]/h6")
                time.sleep(2.5)
                if Notificationss:
                    time.sleep(2.5)
                    print("Successfull")
                    print(Notificationss.text)
                    time.sleep(2.5)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign {Notificationss.text},Pass\n', new=False)
                else:
                    time.sleep(2.5)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign with correct data,fail\n', new=False)
                    print("fail")     
        except:
            time.sleep(2.5)
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign with correct data,fail\n', new=False)
            pass
        
        
        time.sleep(1.5)
        driver.refresh()
        
        time.sleep(2.5)
        Quick_tab = HomePage(driver)
        Quick_tab.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(1.5)
        Quick_tab_table = HomePage(driver)
        Quick_tab_table.waittt(QuickAnalysispage.Quick_tab_table)
    
        
        time.sleep(1.5)
        
        actionn = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{business}')]//td/div[@class='assign-campaign-box']").click()
        time.sleep(1.5)
        edit_camm = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{business}')]//td/div[@class='assign-campaign-box']//li[contains(normalize-space(), 'Edit Campaign')]/a").click()
        
        time.sleep(1.5)
        Edit_Quick_tab = HomePage(driver)
        Edit_Quick_tab.waitte(QuickAnalysispage.Edit_Quick_tab)
        
        if Edit_Quick_tab:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Pass\n', new=False)
        else:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Fail\n', new=False)
        time.sleep(3)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        # screenshot_path = 'v1/screenshot.png'
        # driver.save_screenshot(screenshot_path)
        # Wait for the page to load
        time.sleep(3)

        # Get the dimensions of the entire page
        page_width = driver.execute_script("return document.body.scrollWidth")
        page_height = driver.execute_script("return document.body.scrollHeight")

        # Set the width of the window to match the page width
        driver.set_window_size(page_width, 600)  # Window height can be set to 600 or according to your needs

        # Start with an empty image
        stitched_image = Image.new('RGB', (page_width, page_height))

        # Scroll through the page and take screenshots
        y_offset = 0
        while y_offset < page_height:
            # Scroll the page to the new position
            driver.execute_script(f"window.scrollTo(0, {y_offset})")
            time.sleep(2.5)  # Wait for the page to load the new content

            # Take a screenshot and open it with PIL
            png = driver.get_screenshot_as_png()
            screenshot = Image.open(io.BytesIO(png))

            # Calculate the position where to paste the screenshot slice
            position = (0, y_offset)

            # Paste the screenshot slice into the stitched image
            stitched_image.paste(screenshot, position)

            # Calculate the offset for the next screenshot
            y_offset += screenshot.size[1]

        # Resize the stitched image to the actual page height (if there is extra space at the bottom)
        stitched_image = stitched_image.crop((0, 0, page_width, page_height))

        # Save the stitched image to a file
       # screenshot_path = os.path.join('v1/static', 'screenshot.png')
        #stitched_image.save(screenshot_path)
        # screenshot_path = os.path.join('static', 'screenshot.png')
        file_name = 'screenshot.png'

        # Define the path to the static folder
        static_folder = os.path.join('v1', 'static')

        # Join the path components using os.path.join
        screenshot_path = os.path.join(static_folder, file_name)
        stitched_image.save(screenshot_path)
        time.sleep(2.5)
        driver.maximize_window()
        div_elementt = driver.find_element(By.XPATH, QuickAnalysispage.Edit_Quick_Cam)
        driver.execute_script("arguments[0].scrollIntoView(true);", div_elementt)
        time.sleep(2.5)
        Edit_Quick_Cam = HomePage(driver)
        Edit_Quick_Cam.click_btn(QuickAnalysispage.Edit_Quick_Cam)
        time.sleep(1.5)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(1.5)
        actions.send_keys(Keys.BACKSPACE).perform()
        time.sleep(3)
        campaign_name = driver.find_element(By.XPATH, QuickAnalysispage.Edit_Quick_Cam).send_keys(f"{campaign_nam}")
        time.sleep(2.5)
        keywords = driver.find_element(By.XPATH, '//*[@class="selected-box"]//div[@class="bootstrap-tagsinput"]')
        time.sleep(2.5)
        time.sleep(1.5)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1.5)
        try:
            # import pdb; pdb.set_trace()
            div_element = driver.find_element(By.XPATH, '//*[@class="campaign-field-wrapper mb-3"]//label[contains(normalize-space(), "Keywords")]')
            driver.execute_script("arguments[0].scrollIntoView(true);", div_element)
            time.sleep(2.5)
            Key_countt = driver.find_element(By.XPATH, "//*[@class='bootstrap-tagsinput']/input").click()
            time.sleep(2.5)
            Keyword_list = HomePage(driver)
            Keyword_list = HomePage.get_key_words(driver)
        except:
            pass
        
        time.sleep(3)
        re_button = HomePage(driver)
        re_button.click_btn(QuickAnalysispage.re_button)
        
        time.sleep(1.5)
        driver.refresh()
        time.sleep(1.5)
        
        time.sleep(1.5)
        Cam_tab_button = HomePage(driver)
        Cam_tab_button.click_btn(QuickAnalysispage.Cam_tab_button)
        
        time.sleep(1.5)
        driver.refresh()
        driver.refresh()
        time.sleep(1.5)
        
        try:
            time.sleep(5)
            time.sleep(1.5)
            driver.refresh()
            time.sleep(1.5)
            Noti = HomePage(driver)
            Noti.click_btn(QuickAnalysispage.Notification)
            time.sleep(2.5)
            try:
                Notifications = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {campaign_nam} quick analysis completed.')]/h6")
                time.sleep(2.5)
                if Notifications:
                    time.sleep(2.5)
                    print("Successfull")
                    print(Notifications.text)
                    time.sleep(2.5)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign {Notifications.text},Pass\n', new=False)
                else:
                    time.sleep(2.5)
                    print("fail")
            except:
                Notificationss = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), '1 minute ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {campaign_nam} quick analysis completed.')]/h6")
                time.sleep(2.5)
                if Notificationss:
                    time.sleep(2.5)
                    print("Successfull")
                    print(Notificationss.text)
                    time.sleep(2.5)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign {Notificationss.text},Pass\n', new=False)
                else:
                    time.sleep(2.5)
                    csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign with correct data,fail\n', new=False)
                    print("fail")     
        except:
            time.sleep(2.5)
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign with correct data,fail\n', new=False)
            pass
        
        time.sleep(2.5)
        Quick_tabb = HomePage(driver)
        Quick_tabb.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(1.5)
        Quick_tabb_table = HomePage(driver)
        Quick_tabb_table.waitte(QuickAnalysispage.Quick_tab_table)
        
        time.sleep(3)
        
        actionn = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']").click()
        time.sleep(1.5)
        edit_camm = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']//li[contains(normalize-space(), 'Edit Campaign')]/a").click()
        
        time.sleep(1.5)
        Edit_Quick_tab = HomePage(driver)
        Edit_Quick_tab.waitte(QuickAnalysispage.Edit_Quick_tab)
        
        if Edit_Quick_tab:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Pass\n', new=False)
        else:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Fail\n', new=False)
        time.sleep(3)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        # screenshot_path = 'v1/screenshot.png'
        # driver.save_screenshot(screenshot_path)
        # Wait for the page to load
        time.sleep(3)

        # Get the dimensions of the entire page
        page_width = driver.execute_script("return document.body.scrollWidth")
        page_height = driver.execute_script("return document.body.scrollHeight")

        # Set the width of the window to match the page width
        driver.set_window_size(page_width, 600)  # Window height can be set to 600 or according to your needs

        # Start with an empty image
        stitched_image = Image.new('RGB', (page_width, page_height))

        # Scroll through the page and take screenshots
        y_offset = 0
        while y_offset < page_height:
            # Scroll the page to the new position
            driver.execute_script(f"window.scrollTo(0, {y_offset})")
            time.sleep(2.5)  # Wait for the page to load the new content

            # Take a screenshot and open it with PIL
            png = driver.get_screenshot_as_png()
            screenshot = Image.open(io.BytesIO(png))

            # Calculate the position where to paste the screenshot slice
            position = (0, y_offset)

            # Paste the screenshot slice into the stitched image
            stitched_image.paste(screenshot, position)

            # Calculate the offset for the next screenshot
            y_offset += screenshot.size[1]

        # Resize the stitched image to the actual page height (if there is extra space at the bottom)
        stitched_image = stitched_image.crop((0, 0, page_width, page_height))

        # Save the stitched image to a file
       # screenshot_path = os.path.join('v1/static', 'screenshot.png')
        #stitched_image.save(screenshot_path)
                # Define the file name
        file_name = 'screenshott.png'

        # Define the path to the static folder
        static_folder = os.path.join('v1', 'static')

        # Join the path components using os.path.join
        screenshot_path = os.path.join(static_folder, file_name)
        # screenshot_path = os.path.join('static','screenshott.png')
        stitched_image.save(screenshot_path)
        time.sleep(2.5)
        driver.maximize_window()
        time.sleep(1.5)
        driver.execute_script("arguments[0].scrollIntoView(true);", QuickAnalysispage.Cam_tab_button)
        time.sleep(1.5)
        driver.refresh()
        time.sleep(1.5)
        
        time.sleep(1.5)
        Cam_tab_button = HomePage(driver)
        Cam_tab_button.click_btn(QuickAnalysispage.Cam_tab_button)
        
        time.sleep(1.5)
        driver.refresh()
        driver.refresh()
        time.sleep(1.5)
        
        time.sleep(2.5)
        Quick_tabb = HomePage(driver)
        Quick_tabb.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(1.5)
        Quick_tabb_table = HomePage(driver)
        Quick_tabb_table.waitte(QuickAnalysispage.Quick_tab_table)
        
        time.sleep(3)
        
        actionnn = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']").click()
        time.sleep(1.5)
        
        edit_camm = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']//li[contains(normalize-space(), 'Delete')]/a").click()
        time.sleep(1.5)
        
        delete_modal = HomePage(driver)
        delete_modal.wait(QuickAnalysispage.delete_modal)
        time.sleep(2.5)
        delete_modal_btn = HomePage(driver)
        delete_modal_btn.click_btn(QuickAnalysispage.delete_modal_btn)
        
        Quick_tabb_table = HomePage(driver)
        Quick_tabb_table.waittt(QuickAnalysispage.Quick_tab_table)
        
        time.sleep(3)
        try:
            time.sleep(1.5)
            Cam_tab_button = HomePage(driver)
            Cam_tab_button.click_btn(QuickAnalysispage.Cam_tab_button)
            time.sleep(2.5)
            Quick_tabb = HomePage(driver)
            Quick_tabb.click_btn(QuickAnalysispage.Quick_tab)
            time.sleep(1.5)
            Quick_tabb_table = HomePage(driver)
            Quick_tabb_table.waittt(QuickAnalysispage.Quick_tab_table)
        
            Campaignnn = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']")
            if Campaignnn:
                csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign {Campaignnn.text} not deleted,Fail\n', new=False)
            else:
                csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign {campaign_nam} Deleted Successfully,Pass\n', new=False)
        except:
            csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign {campaign_nam} Deleted Successfully,Fail\n', new=False)
            pass
        
    except Exception as e:
        print(f"An exception occurred: {e}")
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Quick Analysis Campaign test, Test quick analysis campaign create/edit/delete,Fail\n', new=False)
        pass

    driver.quit()

    result_file = 'BSWA Quick Analysis Report.csv'
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content
    