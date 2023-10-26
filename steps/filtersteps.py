import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then(u'find the total products in the the shopping page')
def all_products(self):
    products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    self.total_count = len(products)

@then(u'add filter for XS size and verify product count')
def xs_products(self):
    xs_size = self.driver.find_element(By.XPATH, "//span[contains(text(),'XS')]")
    xs_size.click()
    time.sleep(5)
    xs_products = self.driver.find_elements(By.XPATH, "//div[@class = 'sc-uhudcz-0 iZZGui']/div")
    self.xscount = len(xs_products)

@then('add filter for xl size and verify product count')
def xl_products(self):
    xl_size = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/div[1]/div[6]/label[1]/span[1]")))
    xl_size.click()
    time.sleep(5)
    xlproducts = self.driver.find_elements(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/main[1]/div[1]/div")
    time.sleep(5)
    self.xlcount = len(xlproducts)

@then('find total count of xs products and xl products')
def multisize_products(self):
    self.multiproduct_count = self.xlcount + self.xscount

@then('compare the total products with sum of xs products and xl size products')
def compare_products(self):
    assert self.total_count > self.multiproduct_count
