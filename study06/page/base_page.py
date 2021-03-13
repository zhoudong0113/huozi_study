import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from typing import List, Dict

class BasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find(self,locator,value):
        return self.driver.find_element(locator,value)

    def find_click(self,locator,value):
        return self.find(locator,value).click()

    def send(self,locator,value,text):
        return self.find(locator,value).send_keys(text)

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"],step["value"])
            elif step["action"] == "find":
                self.find(step["locator"],step["value"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "send":
                self.send(step["locator"],step["value"],step["text"])
