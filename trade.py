from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

## @param: WebDriver  -  The webdriver to be used
## @returns: An array - Returns the 15 minutes, 1 hour and 1 day recommendation values for Oscillators, Summary and Moving Averages
##                  indicators
def fetch_data(driver):
    temp = []
    values = []
    numrical_data = []
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div:nth-child(1) > div.countersWrapper-1TsBXTyc- > div:nth-child(1) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div:nth-child(1) > div.countersWrapper-1TsBXTyc- > div:nth-child(2) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div:nth-child(1) > div.countersWrapper-1TsBXTyc- > div:nth-child(3) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div.speedometerWrapper-1SNrYKXY-.summary-72Hk5lHE- > div.countersWrapper-1TsBXTyc- > div:nth-child(1) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div.speedometerWrapper-1SNrYKXY-.summary-72Hk5lHE- > div.countersWrapper-1TsBXTyc- > div:nth-child(2) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div.speedometerWrapper-1SNrYKXY-.summary-72Hk5lHE- > div.countersWrapper-1TsBXTyc- > div:nth-child(3) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div:nth-child(3) > div.countersWrapper-1TsBXTyc- > div:nth-child(1) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div:nth-child(3) > div.countersWrapper-1TsBXTyc- > div:nth-child(2) > span.counterNumber-3l14ys0C-")
    numrical_data.append("#technicals-root > div > div > div.speedometersContainer-1EFQq-4i- > div:nth-child(3) > div.countersWrapper-1TsBXTyc- > div:nth-child(3) > span.counterNumber-3l14ys0C-")

    speedometers = []
    speedometers.append("#technicals-root > div > div > div.elementWrap-1QD4r5YL- > div > div:nth-child(1) > div")
    speedometers.append("#technicals-root > div > div > div.elementWrap-1QD4r5YL- > div > div:nth-child(2) > div")
    speedometers.append("#technicals-root > div > div > div.elementWrap-1QD4r5YL- > div > div:nth-child(3) > div")

    driver.get("https://www.tradingview.com/symbols/EURUSD/technicals/")
    assert "Technical Analysis of Euro / U.S. Dollar (FX:EURUSD) — TradingView" in driver.title

    for j in range(len(speedometers)):
        elem = driver.find_element_by_css_selector(speedometers[j])
        actions = ActionChains(driver)
        actions.move_to_element(elem)
        actions.click()
        actions.perform()
        time.sleep(3)
        for i in range(len(numrical_data)):
            data = driver.find_element_by_css_selector(numrical_data[i])
            print(data.text)
            values.append(data.text)
        time.sleep(3)
    return(values)

driver = webdriver.Chrome(executable_path=r"C:\Users\Sameeh\Downloads\chromedriver_win32\chromedriver.exe")

values = fetch_data(driver)

time.sleep(600)

driver.close()

