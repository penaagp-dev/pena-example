from selenium import webdriver



def setup():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def set_url(url=None):
    if url is None:
        url = "https://www.google.com/maps"
    driver = setup()
    driver.get(url)
    return driver