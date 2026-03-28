#import all the required Selenium classes and tools
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

#create object
o = ChromeOptions()

#to keep the browser open after code finishes executing
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

#implicit wait
driver.implicitly_wait(25)

#opening the website
driver.get("https://www.shoppersstack.com/")

#open browser in maximized window mode
driver.maximize_window()

#finds the xpath of the image that we need to open
driver.find_element(By.XPATH, "//img[@src='https://m.media-amazon.com/images/I/71ZDY57yTQL._AC_UY327_FMwebp_QL65_.jpg']").click()

#locate the pincode textbox and adding the pincode
driver.find_element(By.ID, "Check Delivery").send_keys("248001")
sleep(5)

#explicit wait
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.ID, "Check")))

#finding the element to check by ID method.
btn = driver.find_element(By.ID, "Check")
#clicking the check button
btn.click()
#sleep to observe results and then quit the browser window.
sleep(20)
driver.quit()

