from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""

    def __init__(self,driver: WebDriver = None):
        if driver == None:
            #复用浏览器，需要cmd启动浏览器，先登录chrome --remote-debugging-port=9222
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            #隐式等待10s
            self.driver.implicitly_wait(10)
        else:
            self.driver =driver

        if self.base_url !="":
            self.driver.get(self.base_url)

    #定义find方法
    def find(self,locator, value):
        return self.driver.find_element(locator,value)

    #定义finds方法
    def finds(self,locator, value):
        return self.driver.find_elements(locator,value)

    #定义显示等待，等待元素可以点击
    def wait_for_click(self,timeout,locator):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.driver.quit()