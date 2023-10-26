import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@then('Add few items to cart and click on “checkout”')
def checkout_button(self):
    products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    time.sleep(5)
    fs = self.driver.find_element(By.XPATH, "//div[@class = 'sc-124al1g-3 bHJSNa']").text
    product_details = {}
    i = 0
    z = 0
    j = 0
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
            product_details[name] = price
        elif fs not in product.text and j == 0:
            self.driver.find_elements(By.XPATH, "//button[@class = 'sc-124al1g-0 jCsgpZ']")[z].click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
            j = j + 1
            time.sleep(2)
            name_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(z + 1) + "]/p[1]"
            value_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(
                z + 1) + "]/div[2]/p[1]"
            name = self.driver.find_element(By.XPATH, name_element).text
            price = self.driver.find_element(By.XPATH, value_element).text
            product_details[name] = price
        else:
            pass
        z = z + 1
    print("product_details=============================================", product_details)
    cart_button = self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']")
    cart_button.click()
    time.sleep(10)

    self.total_cart_amount = float((self.driver.find_element(By.CSS_SELECTOR, ".sc-1h98xa9-9.jzywDV").text).replace("$ ", ""))
    print(self.total_cart_amount)
    time.sleep(5)
    self.driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
    time.sleep(5)


@then('verify alert message is displayed with correct price same as cart')
def verify_alert(self):
    alert = self.driver.switch_to.alert
    # sleep for a second
    time.sleep(1)
    # accept the alert
    alerts_msg = alert.text

    alerts_msg_price = float((alerts_msg.split("$ "))[1])
    print("alerts_msg_price----------------------------------------------------------", alerts_msg_price)
    alert.accept()
    assert self.total_cart_amount == alerts_msg_price

@then('Verify items in cart is reset on refreshing the page')
def step_impl(self):
    self.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
    self.driver.maximize_window()
    time.sleep(5)
    ###### Add products from prodiuct list & get the details in dict #################
    products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    time.sleep(5)
    fs = self.driver.find_element(By.XPATH, "//div[@class = 'sc-124al1g-3 bHJSNa']").text
    product_details = {}
    i = 0
    z = 0
    j = 0
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
            product_details[name] = price
        elif fs not in product.text and j == 0:
            self.driver.find_elements(By.XPATH, "//button[@class = 'sc-124al1g-0 jCsgpZ']")[z].click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
            j = j + 1
            time.sleep(2)
            name_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(z + 1) + "]/p[1]"
            value_element = "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[" + str(
                z + 1) + "]/div[2]/p[1]"
            name = self.driver.find_element(By.XPATH, name_element).text
            price = self.driver.find_element(By.XPATH, value_element).text
            product_details[name] = price
        else:
            pass
        z = z + 1
    print("product_details=============================================", product_details)

    self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
    time.sleep(10)

    total_cart_amount = int(self.driver.find_element(By.CSS_SELECTOR, ".sc-1h98xa9-3.VLMSP").text)
    print("total_cart_amount----------------------------------------------------------", total_cart_amount)

    self.driver.refresh()

    self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
    time.sleep(10)

    products_in_cart = int(self.driver.find_element(By.CSS_SELECTOR, ".sc-1h98xa9-3.VLMSP").text)
    print("products_in_cart----------------------------------------------------------", products_in_cart)

    assert products_in_cart == 0
