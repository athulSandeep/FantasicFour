import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_perf_log_on_load(url, headless=True, filter=None):
    # init Chrome driver (Selenium)
    options = Options()
    options.add_experimental_option('w3c', False)
    options.headless = headless
    cap = DesiredCapabilities.CHROME
    cap["loggingPrefs"] = {"performance": "ALL"}
    driver = webdriver.Chrome(r"C:\Users\hp\Desktop\misc\SE Project\FantasticFour\chromedriver\chromedriver.exe", desired_capabilities=cap, options=options)
    # record and parse performance log
    driver.get(url)
    time.sleep(5)
    if filter:
        log = [item for item in driver.get_log("performance") if filter in str(item)]
    else:
        log = driver.get_log("performance")
    driver.close()
    return log

url = "https://soundcloud.com/sukhman-brar-881966732/yaaran-nal-de-gur-sidhu"
netlog = (get_perf_log_on_load(url))
for i in netlog:
    print(i, "\n")
f = open(r'C:\Users\hp\Desktop\misc\SE Project\FantasticFour\Temp\log.txt', 'wt')
f.write(str(netlog))
f.close()
