from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome()
driver.get("https://leetcode.com/problemset/?page=1&topicSlugs=dynamic-programming")
wait = WebDriverWait(driver, 10)

time.sleep(5)
i = 0
for i in range(11):
    time.sleep(3)
    elements = driver.find_elements(By.CSS_SELECTOR, '.odd\\:bg-layer-1, .even\\:bg-overlay-1, .dark\\:odd\\:bg-dark-layer-bg, .dark\\:even\\:bg-dark-fill-4')
    for element in elements:
        acceptance = element.find_element(By.TAG_NAME,'span').text
        percentage = float(acceptance.replace('%',''))
        title = element.find_element(By.TAG_NAME,'a').text
        if percentage < 40:
            with open('problems.txt','a') as f:
                f.write(title)
                f.write('\n')
    with open('problems.txt','a') as f:
        f.write('-'*50)
        f.write('\n')

    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='next']")))
    button.click()

driver.close()