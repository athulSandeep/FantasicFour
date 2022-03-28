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
    driver = webdriver.Chrome(r"C:\Users\hp\Desktop\misc\FantasticFour\chromedriver\chromedriver.exe", desired_capabilities=cap, options=options)
    # record and parse performance log
    driver.get(url)
    time.sleep(5)
    if filter:
        log = [item for item in driver.get_log("performance") if filter in str(item)]
    else:
        log = driver.get_log("performance")
    driver.close()
    return log

url = "https://soundcloud.com/hu-nh-l-ng-duy-thi-n/double-take?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing"
netlog = (get_perf_log_on_load(url))
for i in netlog:
    print(i, "\n")
f = open(r'C:\Users\hp\Desktop\misc\FantasticFour\Temp\log.txt', 'wt')
f.write(str(netlog))
f.close()
