import time
from selenium.webdriver.common.by import By
from lib.page import HomePage


class HelperFuncs:
    """Helper class for handling dropdown operations across test cases"""
    

    @staticmethod
    def click_all_dropdown_options(base_page,select_element_xpath, wait_between_options=3, 
                                   wait_before_click=1.5, wait_after_close=0.5):
        """
        Clicks the select dropdown and iterates through all options
        Returns:
            list: List of option texts that were clicked
        """
        clicked_options = []
        
        try:
            # Find the select element
            select_element = HomePage.wait_for_element(select_element_xpath)
            
            # Get all options from the select element
            options = HomePage.get_elements_by_tag_name(select_element, "option")
            
            # Iterate through each option
            for index in range(len(options)):
                # Re-find the select element to avoid stale element reference
                select_element = HomePage.wait_for_element(select_element_xpath)
                
                # Get all options again
                options = select_element.find_elements(By.TAG_NAME, "option")
                
                # Click the select to open dropdown
                HomePage.click_btn(select_element_xpath)
                time.sleep(wait_before_click)
                
                # Click the current option
                HomePage.click_btn(options[index])
                clicked_options.append(options[index].text)
                
                # Wait after clicking the option
                time.sleep(wait_between_options)
                
                # Close the dropdown (if needed for next iteration)
                HomePage.click_btn(select_element_xpath)
                time.sleep(wait_after_close)
            
            return clicked_options
            
        except Exception as e:
            raise Exception(f"Failed to click dropdown options: {str(e)}")
    
    def click_specific_options(self, select_element_xpath, option_xpaths=None, 
                               option_texts=None, wait_after_click=3):
        """
        Clicks specific options in a dropdown
        
        Args:
            select_element_xpath: XPath of the select element
            option_xpaths: List of XPaths for specific options to click
            option_texts: List of option text values to click (alternative to xpaths)
            wait_after_click: Time to wait after clicking each option
            
        Returns:
            list: List of option values/texts that were clicked
        """
        clicked_items = []
        
        try:
            # Click using provided XPaths
            if option_xpaths:
                for option_xpath in option_xpaths:
                    # Open dropdown
                    select_element = self.base_page.wait_for_element(select_element_xpath)
                    select_element.click()
                    time.sleep(1)
                    
                    # Click the specific option
                    option = self.base_page.wait_for_element(option_xpath)
                    option.click()
                    clicked_items.append(option.text)
                    
                    # Wait after click
                    time.sleep(wait_after_click)
            
            # Click using option text values
            elif option_texts:
                for option_text in option_texts:
                    # Open dropdown
                    select_element = self.base_page.wait_for_element(select_element_xpath)
                    select_element.click()
                    time.sleep(1)
                    
                    # Find and click option by text
                    option_xpath = f"//option[text()='{option_text}']"
                    option = self.base_page.wait_for_element(option_xpath)
                    option.click()
                    clicked_items.append(option_text)
                    
                    # Wait after click
                    time.sleep(wait_after_click)
            
            return clicked_items
            
        except Exception as e:
            raise Exception(f"Failed to click specific dropdown options: {str(e)}")