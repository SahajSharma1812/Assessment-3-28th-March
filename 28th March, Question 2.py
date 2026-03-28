#import all the needed classes and tools
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#create object
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
#used to maximize the window
driver.maximize_window()
#implicit wait
wait = WebDriverWait(driver, 20)
#open myntra and let myntra load
driver.get("https://www.myntra.com/")
sleep(2)
#wait until the GenZ part of Myntra website is visible and then select it
genz = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Genz']")))

ActionChains(driver).move_to_element(genz).perform()
#wait until jackets under 899 is visible andf clickable and then click it clickable
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Jackets Under')]"))).click()
#locate the filters part of the page and press on the first and second one.
filters = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "common-customCheckbox")))
filters[0].click()
filters[1].click()

#wait until Sort by is visible and then click on popularity
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Sort by')]"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Popularity')]"))).click()

#then click on the first element with class name product-base because we can select any item
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-base"))).click()
#switch to the new page that opens
driver.switch_to.window(driver.window_handles[1])
#wait until or if size button is selectable and then click
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "size-buttons-size-button"))).click()
#press on add to bag
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='ADD TO BAG']"))).click()
#wait to observe changes and then quit windows
sleep(20)
driver.quit()

