from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pkg.selenium import set_url
import time, csv


def setup_maps(url):
    driver = set_url(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchboxinput")))
    time.sleep(5)
    return driver

def maximize_window(driver=set_url):
    driver.maximize_window()

def search_place(driver=set_url, keyword_list=[], no_use_category_list=[], result_path="", suffix=""):
    result_filename = "_".join([result_path+"/", suffix])+ '.csv'
    delimiter = ","

    for i in range(len(keyword_list)):
        input = driver.find_element_by_class_name("tactile-searchbox-input")
        driver.find_element_by_class_name("tactile-searchbox-input").clear()
        input.send_keys(keyword_list[i])
        input.send_keys(Keys.ENTER)
        
        time.sleep(8)
        # create csv
        with open(result_filename, mode='w') as output:
            output_writer = csv.writer(output, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
            output_writer.writerow(["name", "address", "description", "category", "rating", "reviewer", "link"])

        for x in range(10):
            try:
                listed_bengkel = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div")
                print(listed_bengkel.text)
            except Exception as e:
                print(e)
            
            div_number = 1
            name_of_bengkel = None
            phone_number = None
            rating = None
            number_of_reviews = None
            category = None
            places_link = None
            div_number_click = 1
            for j in range(int(20)): 
                try:
                    path = "//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/span[1]/jsl/span[2]".format(div_number)
                    category = driver.find_element_by_xpath(path)
                except Exception as e:
                    category = None
                    print(e)
                else:
                    category = category.text
                    print(category)
                    no_use_category_list = [each_string.lower() for each_string in no_use_category_list]
                    if category.lower() not in no_use_category_list:
                        try:
                            name_of_bengkel = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div/div[2]/div[2]/div[1]/div/div/div/div[1]".format(div_number))
                        except Exception:
                            name_of_bengkel = None
                            print("Error")
                            print(e)
                        else:
                            name_of_bengkel = name_of_bengkel.text
                        
                        try:
                            address = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[1]/span[2]/jsl/span[2]".format(div_number))
                        except Exception:
                            address = None
                        else:
                            address = address.text
                        
                        try:
                            phone_number = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div/div[2]/div[2]/div[1]/div/div/div/div[4]/div[2]/span[2]/jsl/span[2]".format(div_number))
                        except Exception:
                            phone_number = None
                        else:
                            phone_number = phone_number.text

                        try:
                            rating = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div/div[2]/div[2]/div[1]/div/div/div/div[3]".format(div_number))
                        except Exception :
                            rating = None
                        else:
                            rating = rating.text
                            rating = rating.split("(")
                            try:
                                number_of_reviews = rating[1].rstrip(')')
                            except Exception:
                                number_of_reviews = 0
                            rating = rating[0]
                        
                        try:
                            pathclick = "//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div/a".format(div_number_click)
                            sharePlaces = driver.find_element_by_xpath(pathclick)
                        except Exception as e:
                            print(e)
                            places_link = None
                        else:
                            sharePlaces.click()
                            time.sleep(5)
                            
                            try:
                                linkPlacePath = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[5]/button") 
                            except Exception as e:
                                print("error:> ")
                                print(e)
                                places_link = None
                            else:
                                linkPlacePath.click()
                                time.sleep(10)
                                link = driver.find_element_by_xpath("//*[@id='modal-dialog']/div/div[2]/div[1]/div/div/div/div[1]/div[4]/div[2]/div[1]/input")
                                places_link = link.get_attribute('value')
                                print("Places:> ", places_link)
                                driver.find_element_by_xpath("//*[@id='modal-dialog']/div/div/div/div[2]/button").click()
                                time.sleep(3)
                                
                            time.sleep(3)
                            back = driver.find_element_by_xpath("//*[@id='omnibox-singlebox']/div[1]/div[1]/button")
                            back.click()
                
                        result_list = [name_of_bengkel, address, phone_number, category, rating, number_of_reviews, places_link]
                        print("logging:> ", result_list)
                        with open(result_filename, mode='a') as output:
                            output_writer = csv.writer(output, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                            output_writer.writerow(result_list)
                    div_number_click += 2
                # scrollTarget = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div")
                # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", scrollTarget)
                time.sleep(8)
                div_number += 2
            driver.find_element_by_xpath("//*[@id='ppdPk-Ej1Yeb-LgbsSe-tJiF1e']").click()
            time.sleep(50)


