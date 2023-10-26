import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Add random 4 items with free shipping tag (items labelled as Free shipping)')
def add4products(self):
    products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    fs = self.driver.find_element(By.XPATH, "//div[@class = 'sc-124al1g-3 bHJSNa']").text

    self.product_details = {}
    i = 0
    z = 0
    for product in products:
        if i >= 4:
            break
        if fs in product.text and i < 4:
            self.driver.find_elements(By.XPATH, "//button[@class = 'sc-124al1g-0 jCsgpZ']")[z].click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
            i = i + 1
            time.sleep(2)
            name_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(z + 1) + "]/p[1]"
            value_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(z + 1) + "]/div[3]/p[1]"
            name = self.driver.find_element(By.XPATH, name_element).text
            price = self.driver.find_element(By.XPATH, value_element).text
            self.product_details[name] = price
        else:
            pass
        z = z + 1


@then(u'Add 1 item without free shipping tag (items without Free shipping label)')
def add1product(self):
    products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    fs = self.driver.find_element(By.XPATH, "//div[@class = 'sc-124al1g-3 bHJSNa']").text
    print(fs)
    j = 0
    z = 0
    for product in products:
        if j >= 1:
            break
        if fs not in product.text and j == 0:
            self.driver.find_elements(By.XPATH, "//button[@class = 'sc-124al1g-0 jCsgpZ']")[z].click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
            j = j + 1
            time.sleep(2)
            name_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(z + 1) + "]/p[1]"
            value_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(z + 1) + "]/div[2]/p[1]"
            name = self.driver.find_element(By.XPATH, name_element).text
            price = self.driver.find_element(By.XPATH, value_element).text
            self.product_details[name] = price
        else:
            pass
        time.sleep(2)
        z = z + 1


@then('Verify the order of items in cart and the price')
def cart_verification(self):
    cart_button = self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']")
    cart_button.click()
    time.sleep(10)
    time.sleep(10)
    items = self.driver.find_element(By.CSS_SELECTOR, ".sc-1h98xa9-3.VLMSP").text
    cart_details = {}
    for i in range(int(items)):
        i = i + 1
        key_element = "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[" + str(i) + "]/div[1]/p[1]"
        value_element = "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[" + str(i) + "]/div[2]/p[1]"
        key = self.driver.find_element(By.XPATH, key_element).text
        value = self.driver.find_element(By.XPATH, value_element).text
        cart_details[key] = value
    print(cart_details, "cart_details=============")
    print(self.product_details, "product_details========")
    new_cart_details = {x: v.replace(' ', '')
                        for x, v in cart_details.items()}

    assert new_cart_details == self.product_details


