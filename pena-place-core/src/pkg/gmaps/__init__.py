from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pkg.selenium import set_url
import time


def setup_maps(url, search):
    driver = set_url(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchboxinput")))
    time.sleep(5)
    return driver

def maximize_window(driver=set_url):
    driver.maximize_window()

def search_place(driver=set_url, keyword_list=[]):
    for i in range(len(keyword_list)):
        input = driver.find_element_by_class_name("tactile-searchbox-input")
        driver.find_element_by_class_name("tactile-searchbox-input").clear()
        input.send_keys(keyword_list[i])
        input.send_keys(Keys.ENTER)
        time.sleep(8)
        for x in range(10):
            result_list = driver.find_elements_by_class_name("section-result")  
            div_number = 1
            name_of_bengkel = None
            phone_number = None
            address = None
            rating = None
            number_of_reviews = None
            category = None
            places = None
            for j in range(len(result_list)):    
                try:
                    name_of_bengkel = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[2]/h3/span".format(div_number))
                except Exception as e:
                    name_of_bengkel = None
                    print("Name:> None") 
                else:
                    name_of_bengkel = name_of_bengkel.text 
                    print("Name:> ",name_of_bengkel)
                
                try:
                    phone_number = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[5]/span[3]/span[1]".format(div_number))
                except Exception as e:
                    phone_number = None
                    print("Phone:> ",phone_number)
                else:
                    phone_number = phone_number.text
                    print("Phone:> ",phone_number)

                try:
                    address = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[2]/span[6]".format(div_number))
                except Exception as e:
                    address = None
                    print("Address:> ",address)
                else:
                    address = address.text
                    print("Address:> ",address)

                try:
                    rating = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[2]/span[3]/span[1]/span[1]/span".format(div_number))
                except Exception as e:
                    rating = None
                    print("Rating:> ", rating)
                else:
                    rating = rating.text
                    print("Rating:> ", rating)

                try:
                    number_of_reviews = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[1]/div[1]/div[2]/span[3]/span[1]/span[2]".format(div_number))
                except Exception as e:
                    number_of_reviews = None
                    print("Review:> ",number_of_reviews) 
                else:
                    number_of_reviews = number_of_reviews.text
                    number_of_reviews = number_of_reviews.rstrip(')')
                    number_of_reviews = number_of_reviews.lstrip('(')
                    print("Review:> ",number_of_reviews) 
                
                try:
                    category = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]/div[2]/div[1]/div[2]/span[4]".format(div_number))
                except Exception as e:
                    category = None
                    print("Category:> ",category) 
                else:
                    category = category.text
                    print("Category:> ",category) 
                
                try:
                    bengkel = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[4]/div[1]/div[{}]".format(div_number))
                    time.sleep(3)
                except Exception as e:
                    places = None
                    print("Places:> ", places)
                    print("Click Detail Error:> ", e)
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
                    except Exception as e:
                        latitude = None
                        print("Latitude:>", latitude)
                    else:
                        print("Latitude:>", latitude)

                    try:
                        longitude = str(url_in_browser[pos2 + 3:])
                    except Exception as e:
                        longitude = None
                        print("Longitude:>", longitude)
                    else:
                        print("Longitude:>", longitude)

                    try:
                        sharePlaceBtn = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[5]/div[5]/div") 
                    except Exception as e:
                        places = None
                        print("Places:> ", places)
                    else:
                        sharePlaceBtn.click()
                        time.sleep(10)
                        try:
                            linkPlace = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[3]/div/div/div[1]/div[4]/div[2]/div[1]/input")
                            fullAddress = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[3]/div/div/div[1]/div[3]/div[2]/div[2]")
                        except Exception as e:
                            places = None
                            fullAddress = None
                            modalExit = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[2]/button")
                            modalExit.click()
                            time.sleep(3)
                            back = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/button")
                            back.click()
                        else:
                            places = linkPlace.get_attribute('value')
                            print("Places:> ", places)
                            fullAddress = fullAddress.text
                            print("FullAddress: > ", fullAddress)
                            modalExit = driver.find_element_by_xpath("//*[@id='modal-dialog-widget']/div[2]/div/div[2]/button")
                            modalExit.click()
                            time.sleep(3)
                            back = driver.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/button")
                            back.click()
                time.sleep(5)
                print("________________________________________________")
                div_number += 2
        driver.find_element_by_xpath("//*[@id='n7lv7yjyC35__section-pagination-button-next']/img").click()
        time.sleep(8)
        div_number += 2
    driver.close()
    driver.quit()


