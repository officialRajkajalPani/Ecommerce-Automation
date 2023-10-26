import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then('Add a same item more than 1 times using ‘Add to cart’ button')
def add_products_by_button(self):
    self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[1]/button[1]").click()
    time.sleep(5)
    self.x = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/p[2]").text
    self.a = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[1]").text
    previous_value = float(self.a.replace("$ ", ""))
    previous_quantity = (self.x.split("Quantity: ")[1])
    print(previous_quantity)
    print(previous_value)
    self.previous_value = float(self.a.replace("$ ", ""))
    self.previous_quantity = (self.x.split("Quantity: ")[1])
    print(previous_quantity)
    print(previous_value)

    self.driver.find_element(By.XPATH, "//button[@class = 'sc-1h98xa9-0 gFkyvN']").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[1]/button[1]").click()
    time.sleep(2)
    y = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/p[2]").text
    self.new_quantity = (y.split("Quantity: ")[1])
    b = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[1]").text
    self.new_value = float(b.replace("$ ", ""))
    print(self.new_quantity)
    print(self.new_value)

@then('verify the count & price is increased in cart accordingly')
def compare_both_values(self):
    assert int(self.new_quantity) > int(self.previous_quantity) and float(self.new_value) > float(self.previous_value)

@then('Add an item which is already present in the cart using ‘+’ button')
def step_impl(self):
    self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div[1]/button[1]").click()
    time.sleep(5)
    x = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/p[2]").text
    a = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[1]").text
    self.previous_value = float(a.replace("$ ", ""))
    self.previous_quantity = (x.split("Quantity: ")[1])

    self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/button[2]").click()
    time.sleep(2)
    y = self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/p[2]").text
    self.new_quantity = (y.split("Quantity: ")[1])
    b = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/p[1]").text
    self.new_value = float(b.replace("$ ", ""))
    print(self.new_quantity)
    print(self.new_value)

@then('verify the count & price is increased in cart accordingly after that')
def compare_both_values(self):
    assert int(self.new_quantity) > int(self.previous_quantity) and float(self.new_value) > float(
        self.previous_value)