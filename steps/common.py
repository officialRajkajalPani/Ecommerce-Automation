from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@given('lunch chrome browser')
def lunchBrowser(self):
    service_obj = Service()
    self.driver = webdriver.Chrome(service=service_obj)
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)


@when('open shopping page')
def openApp(self):
    self.driver.get("https://react-shopping-cart-67954.firebaseapp.com/")


@then('close browser')
def closeBrower(context):
    context.driver.close()