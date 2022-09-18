from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import threading
import time

TIME_OUT = 1000

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(
    r'--user-data-dir=C:/Users/owen/Library/Application Support/Google/Chrome/Default')
options.add_argument(
    r'--profile-directory=Default')

browser = webdriver.Chrome(options=options, service=Service(
    ChromeDriverManager().install()))

browser.get("https://play.typeracer.com/")


def type_quote():
    try:
        # Wait until quote appears
        quote = WebDriverWait(browser, TIME_OUT).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inputPanel"))).text
        quote = [*quote[:len(quote)-21]]

        textInput = browser.find_element(By.CLASS_NAME, "txtInput")
        # Wait until text input is interactable
        while not textInput.is_enabled():
            pass

        # Type the quote letter by letter
        for word in quote:
            textInput.send_keys(word)
            time.sleep(0.06)  # Change delay to change wpm
    except Exception as e:
        # Keep on searching for the button, even when page switches and quotes aren't on screen.
        type_quote()


threading.Thread(target=type_quote).start()
