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
    
    def click_btn(self, xpath: str):
        self.driver.find_element(By.XPATH, xpath).click()
        
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
            raise e
        
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


    # # def click_random_elements(self, xpath: str, num_clicks=3):
    # #     try:
    # #         keywords = self.driver.find_elements(By.XPATH, xpath)
    # #         total_elements = len(keywords)
    
    
    
    
    
            
            
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
  