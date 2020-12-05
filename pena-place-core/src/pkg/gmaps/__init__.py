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
            output_writer.writerow(["Name", "Address", "Phone Number", "Latitude", "Longitude", "Category", "Rating", "Reviewer", "Location"])

        for x in range(10):
            result_list = driver.find_elements_by_class_name("section-result")  
            div_number = 1
            name_of_bengkel = None
            phone_number = None
            rating = None
            number_of_reviews = None
            category = None
            places = None
            for j in range(len(result_list)):                    
                try:
                    category = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[2]/span[4]".format(div_number))
                except Exception:
                    category = None
                else:
                    category = category.text
                    if category.lower() in no_use_category_list:
                        continue
                    try:
                        name_of_bengkel = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[2]/h3/span".format(div_number))
                    except Exception:
                        name_of_bengkel = None
                    else:
                        name_of_bengkel = name_of_bengkel.text
                    
                    try:
                        phone_number = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[5]/span[3]/span[1]".format(div_number))
                    except Exception:
                        phone_number = None
                    else:
                        phone_number = phone_number.text

                    try:
                        rating = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[2]/span[3]/span[1]/span[1]/span".format(div_number))
                    except Exception :
                        rating = None
                    else:
                        rating = rating.text

                    try:
                        number_of_reviews = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[2]/span[3]/span[1]/span[2]".format(div_number))
                    except Exception:
                        number_of_reviews = None
                    else:
                        number_of_reviews = number_of_reviews.text
                        number_of_reviews = number_of_reviews.rstrip(')')
                        number_of_reviews = number_of_reviews.lstrip('(')
            
                    try:
                        bengkel = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]".format(div_number))
                        time.sleep(3)
                    except Exception:
                        places = None
                    else:
                        bengkel.click()
                        time.sleep(7)
                        #Getting longitude and latitude
                        url_in_browser = str(driver.current_url)
                        pos1 = url_in_browser.find("!3d")
                        pos2 = url_in_browser.find("!4d")
                        longitude = ""
                        latitude = ""

                        try:
                            latitude = str(url_in_browser[pos1 + 3: pos2])
                        except Exception:
                            latitude = None

                        try:
                            longitude = str(url_in_browser[pos2 + 3:])
                        except Exception:
                            longitude = None

                        try:
                            sharePlaceBtn = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[5]/div[5]/div") 
                        except Exception:
                            places = None
                        else:
                            sharePlaceBtn.click()
                            time.sleep(10)
                            try:
                                linkPlace = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[3]/div/div/div[1]/div[4]/div[2]/div[1]/input")
                                fullAddress = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[3]/div/div/div[1]/div[3]/div[2]/div[2]")
                            except Exception:
                                places = None
                                fullAddress = None
                                modalExit = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[2]/button")
                                modalExit.click()
                                time.sleep(3)
                                back = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/button")
                                back.click()
                            else:
                                places = linkPlace.get_attribute('value')
                                fullAddress = fullAddress.text
                                modalExit = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[2]/button")
                                modalExit.click()
                                time.sleep(3)
                                back = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/button")
                                back.click()
                    
                    with open(result_filename, mode='a') as output:
                        output_writer = csv.writer(output, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        output_writer.writerow([name_of_bengkel, fullAddress, phone_number, latitude, longitude, category, rating, number_of_reviews, places])
                time.sleep(5)
                div_number += 2
            driver.find_element_by_xpath("//*[@id='n7lv7yjyC35__section-pagination-button-next']/img").click()
            time.sleep(5)
    driver.close()
    driver.quit()


