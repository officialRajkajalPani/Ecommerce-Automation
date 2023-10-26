import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Add few items to cart and verify the total count and price is displayed correctly')
def total_count_verification(self):
    products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    time.sleep(5)
    fs = self.driver.find_element(By.XPATH, "//div[@class = 'sc-124al1g-3 bHJSNa']").text
    print(fs)

    self.product_details = {}
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
            self.product_details[name] = price
        elif fs not in product.text and j == 0:
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
        z = z + 1
    self.product_details = {x: v.replace('$', '') for x, v in self.product_details.items()}
    cart_button = self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']")
    cart_button.click()
    time.sleep(10)

    items = self.product_details.keys()
    print(items)
    total_items_added = len(items)
    print(total_items_added)
    # time.sleep(5)
    cart_items = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").text
    # print(cart_items)

    prices = self.product_details.values()
    print(prices)
    y = []
    for i in prices:
        y.append(i)
    print(y)
    z = [float(string.replace("$", "")) for string in y]
    print(z)
    all_added_value = sum(z)
    # print(all_added_value)

    total_cart_value = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[1]").text
    total_cart_value = float(total_cart_value.replace("$ ", ""))
    print(total_cart_value)

    # conditions
    assert total_items_added == int(cart_items)
    assert total_cart_value == all_added_value

@then('Clear all items in cart and verify price & count is reset to 0')
def delete_items(self):

    items = self.product_details.keys()
    print(items)
    total_items_added = len(items)
    print(total_items_added)
    # self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/button[1]/div[1]").click()
    time.sleep(5)
    for i in range(int(total_items_added)):
        remove_button = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/button[1]")
        remove_button.click()
    time.sleep(2)
    cart_items = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]").text
    cart_items = int(cart_items)
    print(cart_items)
    assert cart_items == 0


