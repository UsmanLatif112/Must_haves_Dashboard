from imports import *
from lib.resources import *
import os,csv




def random_click_elements(driver, xpath, num_clicks=3):
    try:
        # Find all elements matching the given XPath
        elements = driver.find_elements(By.XPATH, xpath)

        # Get the total number of elements
        num_elements = len(elements)

        # Make sure there are enough elements to click on
        if num_elements < num_clicks:
            raise ValueError("Not enough elements to click on")

        # Randomly select and click on num_clicks elements
        random_elements = random.sample(elements, num_clicks)
        for element in random_elements:
            time.sleep(0.5)
            element.click()

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
    
    
class BasePage:
    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):

    def wait_for_element(self, xpath, timeout=180):
        locator = (By.XPATH, xpath)
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f"Timeout occurred while waiting for element: {locator}")
            return None
    
    def click_button(self, button_name):
        """Click a button by its name"""
        xpath = f'//button[contains(text(), "{button_name}")]'
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        button.click()
        time.sleep(1)
    
    def handle_date_picker(self, input_element, date_value):
        """
        Handle date picker selection for input type='date'
        Uses JavaScript to set the value directly
        """
        # Set the date value using JavaScript
        self.driver.execute_script(f"arguments[0].value = '{date_value}';", input_element)
        # Trigger change event to ensure any listeners are notified
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", input_element)
        time.sleep(0.5)

    def select_and_wait_for_option(self, select_element, option_value=None):
        """
        Select an option from select dropdown and wait
        If option_value is None, it will iterate through all options
        """

        
        select = Select(select_element)
        
        if option_value:
            # Select specific option
            select.select_by_value(option_value)
            time.sleep(2)
            return
        
        # Iterate through all options
        options = select.options
        for index, option in enumerate(options):
            if option.get_attribute("value"):  # Skip empty options
                print(f"Selecting option: {option.text}")
                select.select_by_index(index)
                time.sleep(4)
                self.scroll_and_return()

    def click_and_validate_campaign(self, project_Xpath, data_dict):
        """Click a campaign link and validate the data"""
        try:
            # Wait for campaign links to be present
            campaign_links = WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, project_Xpath))
            )
            
            if campaign_links:
                campaign_links[0].click()
                time.sleep(2)
                
            self.slow_scroll_to_bottom()
            raw_data = self.driver.page_source
            page_src = raw_data.split('rawData = ')
            data_string = None
            for part in page_src:
                if part.startswith("JSON"):
                    data_string = part
                    data_json = data_string.split(";")[0]
                    break
            
            if not data_string:
                print("Could not find JSON data in page source")
                return False, {"error": "JSON data not found"}
            
            json_string = data_json.split("JSON.parse('")[1].split("')")[0]
            json_data = json.loads(json_string)[-1]
            print(json_data)
            
            google_recaptcha_check = int(data_dict["google_recaptcha"]) == int(json_data["google_recaptcha"])
            wildcard_not_found_check = int(data_dict["wildcard_not_found"]) == int(json_data["wildcard_not_found"])
            product_wildcard_not_found_check = int(data_dict["product_wildcard_not_found"]) == int(json_data["product_wildcard_not_found"])
            total_failed_check = int(data_dict["total_failed"]) == int(json_data["failed"])
            
            all_checks_passed = google_recaptcha_check and wildcard_not_found_check and product_wildcard_not_found_check and total_failed_check
            
            # Return results
            result_dict = {
                "google_recaptcha_check": google_recaptcha_check,
                "wildcard_not_found_check": wildcard_not_found_check,
                "product_wildcard_not_found_check": product_wildcard_not_found_check,
                "total_failed_check": total_failed_check,
                "json_data": json_data
            }
            
            return all_checks_passed, result_dict
        
        except Exception as e:
            print(f"Error in click_and_validate_campaign: {str(e)}")
            return False, {"error": str(e)}

    def scroll_and_return(self):
        # Scroll down by 300 pixels
        self.driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(3)
        
        # Scroll back to the absolute top (0,0)
        self.driver.execute_script("window.scrollTo(0, 0);")

    def slow_scroll_to_bottom(self, step_size=500, delay=1.5):
        """
        step_size: How many pixels to move per jump
        delay: Seconds to wait between jumps
        """
        current_position = 0
        # Get the total height of the page
        total_height = self.driver.execute_script("return document.body.scrollHeight")

        while current_position < total_height:
            current_position += step_size
            self.driver.execute_script(f"window.scrollTo(0, {current_position});")
            
            # Update total height in case the page expanded (infinite scroll)
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            
            time.sleep(delay)


    def get_elements_by_tag_name(self, element, tag_name):
        """
        Finds child elements by tag name from a parent element
        
        Args:
            element: The parent web element
            tag_name: The tag name to search for (e.g., "option", "li", "div")
        
        Returns:
            list: List of web elements with the specified tag name
        """
        try:
            elements = element.find_elements(By.TAG_NAME, tag_name)
            return elements
        except Exception as e:
            print(f"Error finding elements by tag name '{tag_name}': {str(e)}")
            return []
        
    def click_btn(self, xpath: str):
        element = self.wait_for_element(xpath)
        time.sleep(1)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)


    def click_with_chains(self, locator):
        """Clicks an element using ActionChains."""
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def select_from_search_dropdown(self, dropdown_locator, input_locator, text):
        """
        Handles a searchable dropdown (like Select2).
        Clicks the dropdown, types the text, and presses Enter.
        """
        # 1. Click the dropdown to open it
        self.click_with_chains(dropdown_locator)
        
        # 2. Wait for the input field and type the search term
        input_field = self.wait_for_element(input_locator)
        ActionChains(self.driver).move_to_element(input_field).click().send_keys(text).perform()
        
        # 3. Select the result (Down Arrow + Enter is highly reliable for Select2)
        input_field.send_keys(Keys.ARROW_DOWN)
        input_field.send_keys(Keys.ENTER)
        
    def enter_Name(self, xpath: str, clientname: str):
        self.driver.find_element(By.XPATH, xpath).send_keys(clientname)
        
    def enter_name_delay(self, xpath: str, clientname: str, delay=0.2):
        element = self.wait(xpath)
        element.clear()
        for char in clientname:
            element.send_keys(char)
            time.sleep(delay)
            
    def wait(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            return None
    def wait5(self, xpath, timeout=500):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            return None
    def wait5e(self, xpath, timeout=5000):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            return None
        
    def wait_all(self, xpath, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            )
            return elements
        except Exception as e:
            print(f"Elements with XPath '{xpath}' not found within {timeout} seconds.")
            return None
        
    def waitx(self, xpath, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
    
    def waitt(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
        
    def waiiitt(self, xpath, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
    
    def waittt(self, xpath, timeout=60):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
    def waitte(self, xpath, timeout=30):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
        except Exception as e:
            print(f"Element with XPath '{xpath}' not found within {timeout} seconds.")
            raise e
        
    def make_csv(self, filename: str, data, new=True):
        mode = 'w' if new else 'a'
        with open(filename, mode, newline='') as f:
            f.writelines(data)

    def select_Client(self, dropdown_xpath: str):
        dropdown = self.driver.find_element(By.XPATH, dropdown_xpath)
        options = self.driver.find_elements(By.XPATH, f"{dropdown_xpath}/option")

        if len(options) > 1:
            random_index = random.randint(1, len(options) - 1)
            options[random_index].click()
        else:
            print("Dropdown does not have enough options to select from.")


    def get_key_words(
        driver,
        # xpath="div.potential-keywords:not(.Local-keywords)  ul.potential-keyword-list li",
        xpath=QuickAnalysispage.Keyword_list,
        ):
        select_Keyword = driver.find_elements(By.XPATH, xpath)
        rand_option = random.choice(select_Keyword)
        try:
            rand_option.click()
            time.sleep(0.5)
            rand_option.click()
            return rand_option
                
            
        except:
            pass
        
        
    def send_key_with_action_chain(self, element, text):
        
        actions = ActionChains(self.driver)
        actions.click(element).send_keys(text[-1]).send_keys(Keys.ENTER).perform()
        
    def remove_text(self, element, text):
        
        actions = ActionChains(self.driver)
        for _ in range(len(text)):
            actions.click(element).send_keys(Keys.BACKSPACE).perform()
            actions = ActionChains(self.driver)
            actions.click(element)
            actions.key_down(Keys.CONTROL)
            actions.send_keys('a')
            actions.key_up(Keys.CONTROL)
            actions.send_keys(Keys.BACKSPACE).perform()
        

    
    
    
    
            
            
row_limit_file = "row_limit.txt"            
# Function to read the row limit from the file
def read_row_limit():
    if os.path.exists(row_limit_file):
        with open(row_limit_file, 'r') as file:
            return int(file.read().strip())
    return 8  # Default value

# Function to write the row limit to the file
def write_row_limit(value):
    with open(row_limit_file, 'w') as file:
        file.write(str(value))            
            
# def make_csv(filename: str, data, new=True):
#         """make a csv file with the given filename
#         and enter the data
#         """
#         mode = 'w' if new else 'a'
#         with open(filename, mode, newline='') as f:
#             f.writelines(data)
  