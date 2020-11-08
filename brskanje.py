from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller
import pyautogui
import autoit
import time
import random
# Using Chrome to access web


def is_element_focus(id):
    return driver.find_element_by_id(id) == driver.switch_to.active_element


def youtube(input, driver, wait):
    keyboard = Controller()
    # Open the website
    driver.get('https://www.youtube.com')
    print("odpiram youtube")
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located
    # znebi se okna
    time.sleep(1)
    # autoit.send('{TAB}{TAB}{ENTER}')
    keyboard.press(Key.tab, Key.tab, Key.enter)

    time.sleep(1)
    # autoit.send('{TAB}')
    keyboard.press(Key.tab)
    time.sleep(1)
    keyboard.press(Key.tab, Key.tab)
    a  # utoit.send('{TAB}{TAB}')
    time.sleep(1)
    keyboard.press(Key.enter)

    # išči
    time.sleep(1)
    wait.until(visible((By.NAME, "search_query")))
    driver.find_element_by_name("search_query").click()
    driver.find_element_by_name("search_query").send_keys(input)
    driver.find_element_by_id("search-icon-legacy").click()

    i = random.randint(1, 3)
    time.sleep(i)
    for i in range(1, 9):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/{})".format(10-i))
        time.sleep(2)
    # Play the video.

    videos = driver.find_elements_by_xpath(
        '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-vertical-list-renderer/div[1]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a')
    i = random.randint(0, 1)
    videos[i].click()


# youtube("idoli")

def wiki(input, driver):
    keyboard = Controller()
    geek = "https://www.geeksforgeeks.org"
    stackOver = "https://stackoverflow.com"
    wiki = "https://en.wikipedia.org"
    github = "https://github.com"
    strani = [geek, stackOver, wiki, github]
    driver.get('http://www.google.com')

    for i in input:

        keyboard.press(i)
        time.sleep(.3)
    time.sleep(2)
    search = driver.find_element_by_name('q')
    search.send_keys(Keys.RETURN)

    while True:
        j = random.randint(0, 3)
        try:
            results = driver.find_element_by_xpath(
                '//a[starts-with(@href,"{}")]'.format(strani[j])).click()
            break
        except:
            print(strani[j])
            pass

    if strani[j] == geek:
        keyboard.press(Key.tab)
        keyboard.press(Key.tab)
        keyboard.press(Key.tab)
        keyboard.press(Key.enter)

    for i in range(1, 9):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight/{})".format(10-i))
        time.sleep(random.randint(1, 3))


def kao_brskam(input):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    keyboard = Controller()

    pyautogui.moveTo(1280, 150, duration=1)
    pyautogui.click(1280, 150)
    driver.maximize_window()

    wait = WebDriverWait(driver, 3)
    driver.get('http://www.google.com')
    time.sleep(3)
    # autoit.send('{TAB}{TAB}{ENTER}')
    # keyboard.press(Key.tab)
    # keyboard.press(Key.tab)
    # keyboard.press(Key.enter)
    pyautogui.moveTo(1190, 860, duration=1.2)
    pyautogui.click(1190, 860)
    time.sleep(1)

    wiki(input, driver)
    #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    #youtube(input, driver, wait)

    keyboard.press(Key.esc)
    for i in range(5):
        rand = random.randint(0, 10)
        if rand % 10 == 1:
            driver.find_element_by_tag_name(
                'body').send_keys(Keys.COMMAND + 't')
            youtube(input, driver, wait)
            if rand % 3 == 0:
                driver.find_element_by_tag_name(
                    'body').send_keys(Keys.COMMAND + 'w')

        else:
            driver.find_element_by_tag_name(
                'body').send_keys(Keys.COMMAND + 't')
            wiki(input, driver)


if __name__ == "__main__":
    kao_brskam("selenium python")
