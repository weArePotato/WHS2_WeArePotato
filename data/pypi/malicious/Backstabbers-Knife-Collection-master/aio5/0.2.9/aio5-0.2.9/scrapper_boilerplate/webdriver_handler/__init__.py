import logging
from time import sleep
from scrapper_boilerplate.setup import setSelenium
from scrapper_boilerplate.parser_handler import init_parser


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def scrolldown(driver, element=None):
    """
    Scroll down the page
    args:
        - driver: Selenium Webdriver
    return: void
    """

    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    if element:
        last_height = driver.execute_script("return arguments[0].scrollHeight", element)

    else:
        last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        if element:
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", element)

        else: 
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page and increments one more second
        SCROLL_PAUSE_TIME += 1
        sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        if element:
            new_height = driver.execute_script("return arguments[0].scrollHeight", element)
        
        else:
            new_height = driver.execute_script("return document.body.scrollHeight")


        if new_height == last_height:
            break
        last_height = new_height


def smooth_scroll(driver, element=None):
    """
    Smooth scroll the page
    args:
        - driver: Selenium Webdriver
    returns:
        - void
    """

    scroll = .1
    while scroll < 9.9:
        if not element:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scroll)
        
        else:
            driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight/%s);" % (element, scroll))
        scroll += .01


def load_dynamic_page(url, headless=True):
    """
    Load a dynamic page
    args:
        - url: str, the url of the page you want to load
        - headless: bool, True if you want to run the browser in headless mode
    returns:
        - driver: Selenium Webdriver
    """

    with setSelenium(headless=headless) as driver:
        driver.get(url)
        driver.implicitly_wait(220)
        html = driver.find_element(By.TAG_NAME, 'html')
        return init_parser(html.get_attribute('outerHTML'))


def load_code(driver, full_page=False):
    """
    Load code from a page

    args:
        - driver: Selenium Webdriver
    
    returns:
        - code: Beautifulsoap Obj, the code from the page
    """
    if full_page:
        code = driver.page_source
        return init_parser(code)

    code = driver.get_attribute('outerHTML')
    return init_parser(code)


def check_tag(tag):
    """
    Check if the tag is valid
    args:
        - tag: str, the tag you want to check
    returns:
        - bool: True if the tag is valid, 'Não localizado...':str otherwise
    """
    try:
        handler = tag
        return handler

    except Exception as error:
        print('Error')
        logging.error(error)
        return 'Não localizado...'


def explicit_wait(driver, tag, element, timeout=10):
    """
    Explicit wait for a tag
    args:
        - driver: Selenium Webdriver
        - tag: str, the tag you want to wait for
        - timeout: int, the timeout of the wait
    returns:
        - handler: str, the tag handler
    """
    try:
        handler = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((tag, element))
        )
        return handler
    
    except Exception as error:
        logging.error(error)
        return
