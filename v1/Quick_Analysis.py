import requests
import csv,os,fitz
from csv import reader
import time
from flask import  request
from lib.driver import *
from imports import *
from lib.resources import *
from lib.page import *
from lib.data import *
from pdf2image import convert_from_path
import shutil


def init_the_testing(GMB_cid, User_name, Pass_word):
    try:
        urll = "https://app.brandsignals.io/"
        driver = initialize_and_navigate(urll)
        actions = ActionChains(driver)
        try:
            Login_Pagee = HomePage(driver)
            Login_Pagee.wait(Login.login_page)
        except:
            pass
        csvv = HomePage(driver)
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Test Case,Use Case / Scenario,Result\n', new=True)
        
        # Enter Username.
        time.sleep(2)
        Username = HomePage(driver)
        Username.click_btn(Login.USERNAME)
        time.sleep(1)
        Username = HomePage(driver)
        Username.enter_Name(Login.USERNAME, User_name)
        
        # Enter Password.
        time.sleep(1)
        Password = HomePage(driver)
        Password.click_btn(Login.PASSWORD)
        time.sleep(1)
        Password = HomePage(driver)
        Password.enter_Name(Login.PASSWORD, Pass_word)
    
        # Enter Password.
        time.sleep(1)
        Login_btn = HomePage(driver)
        Login_btn.click_btn(Login.LOGIN_BTN)
        
        # main page s
        try:
                
            mainpage = HomePage(driver,)
            mainpage.wait5(MainPage.Main_Page)
            if mainpage:
                print("Successfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Pass\n', new=False)
            else:
                print("UnSuccessfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
            
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Login,Login with correct username and password,Fail\n', new=False)
        
        main_buttion = HomePage(driver)
        main_buttion.click_btn(QuickAnalysispage.main_buttion) 
        try:
                
            create_q_cam_page = HomePage(driver)
            create_q_cam_page.wait5(QuickAnalysispage.create_q_cam_page)
            
            if create_q_cam_page:
                print("Successfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis button,Pass\n', new=False)
            else:
                print("UnSuccessfull")
                csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis button,Fail\n', new=False)
            
        except:
            print("UnSuccessfull")
            csvv.make_csv("BSWA Quick Analysis Report.csv", 'Create quick analysis campaign,Click on quick analysis button,Fail\n', new=False)
        
        gmb_cid_feild = HomePage(driver)
        gmb_cid_feild.click_btn(QuickAnalysispage.gmb_cid_feild)
        
        time.sleep(1)
        gmb_cid_feild = HomePage(driver)
        gmb_cid_feild.enter_name_delay(QuickAnalysispage.gmb_cid_feild, GMB_cid)
        
        time.sleep(1)
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
            
        time.sleep(2)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        try:
            time.sleep(2)
            Keyword_list = HomePage(driver)
            Keyword_list = HomePage.get_key_words(driver)
        except:
            time.sleep(1)
            key_feild = HomePage(driver)
            key_feild.click_btn(QuickAnalysispage.key_feild)
            
            time.sleep(1)
            key_feild = HomePage(driver)
            key_feild.enter_name_delay(QuickAnalysispage.key_feild, keyword)
            
        business_name = HomePage(driver)
        business_name.wait5(QuickAnalysispage.business_location)
        business_name = driver.find_element(By. XPATH, QuickAnalysispage.business_location)
        print(business_name.text)
        business = business_name.text
        print(business)
        submit_btn = HomePage(driver)
        submit_btn.click_btn(QuickAnalysispage.submit_btn)
        
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        
        try:
            while True:
                Quick_tab_btn = HomePage(driver)
                Quick_tab_btn.click_btn(QuickAnalysispage.Quick_tab)
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
                Noti = HomePage(driver)
                Noti.click_btn(QuickAnalysispage.Notification)
                time.sleep(2)
                try:
                    Notifications = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {business} quick analysis completed.')]/h6")
                    time.sleep(2)
                    if Notifications:
                        time.sleep(2)
                        print("Successfull")
                        print(Notifications.text)
                        time.sleep(2)
                        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Create quick analysis campaign,Create quick analysis campaign ({Notifications.text}),Pass\n', new=False)
                        break
                    else:
                        time.sleep(2)
                        print("Fail")
                except:
                    Notificationss = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), '1 minute ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {business} quick analysis completed.')]/h6")
                    time.sleep(2)
                    if Notificationss:
                        time.sleep(2)
                        print("Successfull")
                        print(Notificationss.text)
                        time.sleep(2)
                        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Create quick analysis campaign,Create quick analysis campaign ({Notificationss.text}),Pass\n', new=False)
                        break
                    else:
                        time.sleep(2)
                        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Create quick analysis campaign,Create quick analysis campaign with correct data,Fail\n', new=False)
                        print("Fail")     
        except:
            time.sleep(2)
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Create quick analysis campaign,Create quick analysis campaign with correct data,Fail\n', new=False)
            pass
        
        
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        
        Quick_tab = HomePage(driver)
        Quick_tab.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(2)
        while True:
            try:
                Quick_tab_table = HomePage(driver)
                Quick_tab_table.waitte(QuickAnalysispage.Quick_tab_table)
                if Quick_tab_table:
                    print("loop breaked")
                    break
            except:
                pass
        try:
            time.sleep(2)
            formatted_textt = business.capitalize()
            actionn = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{formatted_textt}")]//td/div[@class="assign-campaign-box"])[1]').click()
            time.sleep(2)   
            edit_camm = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{formatted_textt}")]//td/div[@class="assign-campaign-box"]//li[contains(normalize-space(), "Edit Campaign")]/a)[1]').click()
            time.sleep(2)
        except:
            time.sleep(2)
            actionn = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{business}")]//td/div[@class="assign-campaign-box"])[1]').click()
            time.sleep(2)   
            edit_camm = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{business}")]//td/div[@class="assign-campaign-box"]//li[contains(normalize-space(), "Edit Campaign")]/a)[1]').click()
            time.sleep(2)
        Edit_Quick_tab = HomePage(driver)
        Edit_Quick_tab.waitte(QuickAnalysispage.Edit_Quick_tab)
        
        if Edit_Quick_tab:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Pass\n', new=False)
        else:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Fail\n', new=False)
        time.sleep(2)
        Quick_report = HomePage(driver)
        Quick_report.click_btn(QuickAnalysispage.Quick_report_btn)
        try:
            while True:
                Quick_report = HomePage(driver)
                Quick_report.waitte(QuickAnalysispage.Quick_report_btn)
                break
            try:
                # Define paths
                downloads_path = os.path.expanduser("~/Downloads")  # Adjust if necessary
                pdf_base_name = 'edit-report'  # The base name of the PDF file without dynamic parts
                static_folder = os.path.join('v1', 'static')
                pdf_file_name = None

                # Check if the file exists, considering dynamic filenames
                for file in os.listdir(downloads_path):
                    if file.startswith(pdf_base_name) and file.endswith('.pdf'):
                        pdf_file_name = file
                        break

                # Step 1: Wait for the file to download (if not found immediately)
                if pdf_file_name is None:
                    timeout = 30  # Max wait time of 30 seconds
                    while timeout > 0:
                        for file in os.listdir(downloads_path):
                            if file.startswith(pdf_base_name) and file.endswith('.pdf'):
                                pdf_file_name = file
                                break
                        
                        if pdf_file_name:
                            break
                        else:
                            print("Waiting for PDF to download...")
                            time.sleep(2)  # Wait 1 second before re-checking
                            timeout -= 1

                # After waiting, check if the PDF file was found
                if pdf_file_name:
                    pdf_file_path = os.path.join(downloads_path, pdf_file_name)
                    print(f"Found PDF: {pdf_file_path}")

                    # Step 2: Ensure the static folder exists
                    os.makedirs(static_folder, exist_ok=True)

                    # Step 3: Move the downloaded PDF to the static folder
                    static_pdf_path = os.path.join(static_folder, pdf_file_name)
                    shutil.move(pdf_file_path, static_pdf_path)
                    print(f"Moved '{pdf_file_name}' to '{static_folder}'.")

                    # Step 4: Convert the PDF to PNG
                    png_filename = 'edit-report.png'  # Output PNG file name
                    png_output_path = os.path.join(static_folder, png_filename)
                    
                    # Open the PDF document and convert it
                    pdf_document = fitz.open(static_pdf_path)  # Open the PDF document
                    page = pdf_document.load_page(0)  # Get the first page (assuming single-page PDF)
                    pix = page.get_pixmap()  # Convert page to pixel map
                    pix.save(png_output_path)  # Save the image as PNG
                    print(f"PDF converted and saved as PNG at {png_output_path}")

                    # Close the PDF document
                    pdf_document.close()

                    # Step 5: Remove the original PDF file
                    os.remove(static_pdf_path)
                    print(f"Original PDF '{static_pdf_path}' deleted.")

                else:
                    print("PDF file not found in Downloads after waiting.")
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        time.sleep(2)
        Edit_Quick_Cam = HomePage(driver)
        Edit_Quick_Cam.click_btn(QuickAnalysispage.Edit_Quick_Cam)
        time.sleep(2)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        actions.send_keys(Keys.BACKSPACE).perform()
        time.sleep(2)
        campaign_name = driver.find_element(By.XPATH, QuickAnalysispage.Edit_Quick_Cam).send_keys(f"{campaign_nam}")
        time.sleep(2)
        keywords = driver.find_element(By.XPATH, '//*[@class="selected-box"]//div[@class="bootstrap-tagsinput"]')
        time.sleep(2)
        time.sleep(2)
        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(2)
        try:
            # import pdb; pdb.set_trace()
            div_element = driver.find_element(By.XPATH, '//*[@class="campaign-field-wrapper mb-3"]//label[contains(normalize-space(), "Keywords")]')
            driver.execute_script("arguments[0].scrollIntoView(true);", div_element)
            time.sleep(2)
            Key_countt = driver.find_element(By.XPATH, "//*[@class='bootstrap-tagsinput']/input").click()
            time.sleep(2)
            Keyword_list = HomePage(driver)
            Keyword_list = HomePage.get_key_words(driver)
        except:
            pass
        
        time.sleep(2)
        re_button = HomePage(driver)
        re_button.click_btn(QuickAnalysispage.re_button)
        
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        
        time.sleep(2)
        Cam_tab_button = HomePage(driver)
        Cam_tab_button.click_btn(QuickAnalysispage.Cam_tab_button)
        
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        
        try:
            while True:
                Quick_tab_btn = HomePage(driver)
                Quick_tab_btn.click_btn(QuickAnalysispage.Quick_tab)
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
                Noti = HomePage(driver)
                Noti.click_btn(QuickAnalysispage.Notification)
                time.sleep(2)
                try:
                    Notifications = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), 'few seconds ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {campaign_nam} quick analysis completed.')]/h6")
                    time.sleep(2)
                    if Notifications:
                        time.sleep(2)
                        print("Successfull")
                        print(Notifications.text)
                        time.sleep(2)
                        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign ({Notifications.text}),Pass\n', new=False)
                        break
                    else:
                        time.sleep(2)
                        print("Fail")
                except:
                    Notificationss = driver.find_element(By.XPATH, f"//*[@class='card text-white notification-unread-bg mb-3 nf-card  '][contains(normalize-space(), '1 minute ago')]/*[@class='card-body'][contains(normalize-space(), 'Your campaign {campaign_nam} quick analysis completed.')]/h6")
                    time.sleep(2)
                    if Notificationss:
                        time.sleep(2)
                        print("Successfull")
                        print(Notificationss.text)
                        time.sleep(2)
                        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign ({Notificationss.text}),Pass\n', new=False)
                        break
                    else:
                        time.sleep(2)
                        csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign with correct data,Fail\n', new=False)
                        print("Fail")     
        except Exception as e:
            time.sleep(2)
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Edit quick analysis campaign with correct data,Fail\n', new=False)
            print(e)
            
        time.sleep(2)
        Quick_tabb = HomePage(driver)
        Quick_tabb.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(2)
        while True:
            try:
                Quick_tabb_table = HomePage(driver)
                Quick_tabb_table.waitte(QuickAnalysispage.Quick_tab_table)
                if Quick_tabb_table:
                    print("loop breaked")
                    break
            except:
                pass
        try:
            time.sleep(2)
            formatted_textt = campaign_nam.capitalize()
            actionn = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{formatted_textt}")]//td/div[@class="assign-campaign-box"])[1]').click()
            time.sleep(2)   
            edit_camm = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{formatted_textt}")]//td/div[@class="assign-campaign-box"]//li[contains(normalize-space(), "Edit Campaign")]/a)[1]').click()
            time.sleep(2)
        except:
            time.sleep(2)
            actionn = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{campaign_nam}")]//td/div[@class="assign-campaign-box"])[1]').click()
            time.sleep(2)   
            edit_camm = driver.find_element(By.XPATH, f'(//div[@id="campaign-tab-content06"]//tbody/tr[contains(normalize-space(), "{campaign_nam}")]//td/div[@class="assign-campaign-box"]//li[contains(normalize-space(), "Edit Campaign")]/a)[1]').click()
            time.sleep(2)
        Edit_Quick_tab = HomePage(driver)
        Edit_Quick_tab.waitte(QuickAnalysispage.Edit_Quick_tab)
        
        if Edit_Quick_tab:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Pass\n', new=False)
        else:
            csvv.make_csv("BSWA Quick Analysis Report.csv", f'Edit quick analysis campaign,Click on edit campaign button,Fail\n', new=False)
        time.sleep(2)
        Quick_report = HomePage(driver)
        Quick_report.click_btn(QuickAnalysispage.Quick_report_btn)
        try:
            while True:
                Quick_report = HomePage(driver)
                Quick_report.waitte(QuickAnalysispage.Quick_report_btn)
                break
            try:
                # Define paths
                downloads_path = os.path.expanduser("~/Downloads")  # Adjust if necessary
                pdf_base_name = 'edit-report'  # The base name of the PDF file without dynamic parts
                static_folder = os.path.join('v1', 'static')
                pdf_file_name = None

                # Check if the file exists, considering dynamic filenames
                for file in os.listdir(downloads_path):
                    if file.startswith(pdf_base_name) and file.endswith('.pdf'):
                        pdf_file_name = file
                        break

                # Step 1: Wait for the file to download (if not found immediately)
                if pdf_file_name is None:
                    timeout = 30  # Max wait time of 30 seconds
                    while timeout > 0:
                        for file in os.listdir(downloads_path):
                            if file.startswith(pdf_base_name) and file.endswith('.pdf'):
                                pdf_file_name = file
                                break
                        
                        if pdf_file_name:
                            break
                        else:
                            print("Waiting for PDF to download...")
                            time.sleep(2)  # Wait 1 second before re-checking
                            timeout -= 1

                # After waiting, check if the PDF file was found
                if pdf_file_name:
                    pdf_file_path = os.path.join(downloads_path, pdf_file_name)
                    print(f"Found PDF: {pdf_file_path}")

                    # Step 2: Ensure the static folder exists
                    os.makedirs(static_folder, exist_ok=True)

                    # Step 3: Move the downloaded PDF to the static folder
                    static_pdf_path = os.path.join(static_folder, pdf_file_name)
                    shutil.move(pdf_file_path, static_pdf_path)
                    print(f"Moved '{pdf_file_name}' to '{static_folder}'.")

                    # Step 4: Convert the PDF to PNG
                    png_filename = 'edit-reportt.png'  # Output PNG file name
                    png_output_path = os.path.join(static_folder, png_filename)
                    
                    # Open the PDF document and convert it
                    pdf_document = fitz.open(static_pdf_path)  # Open the PDF document
                    page = pdf_document.load_page(0)  # Get the first page (assuming single-page PDF)
                    pix = page.get_pixmap()  # Convert page to pixel map
                    pix.save(png_output_path)  # Save the image as PNG
                    print(f"PDF converted and saved as PNG at {png_output_path}")

                    # Close the PDF document
                    pdf_document.close()

                    # Step 5: Remove the original PDF file
                    os.remove(static_pdf_path)
                    print(f"Original PDF '{static_pdf_path}' deleted.")

                else:
                    print("PDF file not found in Downloads after waiting.")
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        time.sleep(2)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        
        time.sleep(2)
        Cam_tab_button = HomePage(driver)
        Cam_tab_button.click_btn(QuickAnalysispage.Cam_tab_button)
        
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        
        time.sleep(2)
        Quick_tabb = HomePage(driver)
        Quick_tabb.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(2)
        while True:
            try:
                Quick_tabb_table = HomePage(driver)
                Quick_tabb_table.waitte(QuickAnalysispage.Quick_tab_table)
                if Quick_tabb_table:
                    print("loop breaked")
                    break
            except:
                pass
        try:
            time.sleep(2)
            formatted_textt = campaign_nam.capitalize()
            actionnn = driver.find_element(By.XPATH, f"(//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{formatted_textt}')]//td/div[@class='assign-campaign-box'])[1]").click()
            time.sleep(2)
            edit_camm = driver.find_element(By.XPATH, f"(//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{formatted_textt}')]//td/div[@class='assign-campaign-box']//li[contains(normalize-space(), 'Delete')]/a)[1]").click()
            time.sleep(2)
        except:
            time.sleep(2)
            actionnn = driver.find_element(By.XPATH, f"(//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box'])[1]").click()
            time.sleep(2)
            edit_camm = driver.find_element(By.XPATH, f"(//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']//li[contains(normalize-space(), 'Delete')]/a)[1]").click()
            time.sleep(2)
        
        
        delete_modal = HomePage(driver)
        delete_modal.wait(QuickAnalysispage.delete_modal)
        time.sleep(2)
        delete_modal_btn = HomePage(driver)
        delete_modal_btn.click_btn(QuickAnalysispage.delete_modal_btn)
        
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        Quick_tabb = HomePage(driver)
        Quick_tabb.click_btn(QuickAnalysispage.Quick_tab)
        time.sleep(2)
        try:
            while True:
                try:
                    Quick_tabb_table = HomePage(driver)
                    Quick_tabb_table.waitte(QuickAnalysispage.Quick_tab_table)
                    if Quick_tabb_table:
                        print("loop breaked")
                        break
                except:
                    pass
            
            try:
                time.sleep(2)
                Campaignnn = driver.find_element(By.XPATH, f"//div[@id='campaign-tab-content06']//tbody/tr[contains(normalize-space(), '{campaign_nam}')]//td/div[@class='assign-campaign-box']")
                if Campaignnn:
                    csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign, Quick Analysis Campaign not deleted,Fail\n', new=False)    
            except:
                csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign,Quick Analysis Campaign ({campaign_nam}) Deleted Successfully,Pass\n', new=False)
                pass        
        except Exception as e:
            print(e)
            csvv.make_csv('BSWA Quick Analysis Report.csv', f'Delete Quick Analysis Campaign, Quick Analysis Campaign ({campaign_nam}) Deleted Successfully,Pass\n', new=False)
    
    except Exception as e:
        print(f"An exception occurred: {e}")
        csvv.make_csv('BSWA Quick Analysis Report.csv', f'Quick Analysis Campaign test, Test quick analysis campaign create/edit/delete,Fail\n', new=False)
        pass
    time.sleep(2)
    driver.quit()
    result_file = 'BSWA Quick Analysis Report.csv'
    with open(result_file, "r", encoding="utf-8") as file:
        result_content = list(reader(file))

    # Skip the header row (first row of the CSV)
    result_content = result_content[1:]
    return result_content
    