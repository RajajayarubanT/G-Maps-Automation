from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random
import time
import win32clipboard

def sleep_for_period_of_time():
    limit = random.randint(7,10)
    time.sleep(limit)


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=en") #default
    # userdatadir = "C:/Users/rajaj/AppData/Local/Google/Chrome/User Data" #existing chrome account
    
    # options.add_argument(f"--user-data-dir={userdatadir}")
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    
    base_search = "stockmarket teaching centers near me"
    base_search_input_xpth = "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/form/input[1]"
    base_search_btn_xpth = "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button"
    
    browser.get("https://www.google.com/maps/")
    
    time.sleep(2)
        
    base_search_res = browser.find_element(By.XPATH, base_search_input_xpth)
    base_search_res.send_keys(base_search)
    
    base_search_btn = browser.find_element(By.XPATH, base_search_btn_xpth)
    
    base_search_btn.click()
        
    sleep_for_period_of_time()
    
    # result processing
    
    results_base_xpath = "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{}]/div/a"
        
    res_limit = 10
    
    data = []
    
    last_ind = 1
    
    while True:
            
        _i =  last_ind + 2
        
        last_ind = _i        

        print(_i, 'index', '\n')
        
        result_xpath = results_base_xpath.format(_i)
        print(result_xpath, '\n')
                
        result = browser.find_element(By.XPATH, result_xpath)
        result.click()
        sleep_for_period_of_time()
        
        res_content_xpath =  "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]"
        res_content = browser.find_element(By.XPATH, res_content_xpath)
        
        name = res_content.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[1]/h1/span[1]')
        rating = res_content.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span[1]/span/span[1]')
        address = res_content.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[3]/button/div[1]/div[2]/div[1]')
        link = res_content.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]/div[5]/a')
        
        name = name.text
        rating = rating.text
        address = address.text
        link = link.get_attribute('href')
        
        _res = {
            "name": name,
            "rating": rating,
            "address": address,
            "link": link,
        }
        print(_res, '\n')
        
        data.append(_res)
            
    
if __name__ == "__main__":
    main()
