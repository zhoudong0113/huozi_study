import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from typing import List, Dict
import json
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging


class BasePage:

    _params = {}  #传参字典
    _blacklist = {} #黑名单字典
    _max_num = 3 #错误上限
    _error_num = 0 #错误计算器

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def setup_implicitly_wait(self, timeout):
        self.driver.implicitly_wait(timeout)

    def waits(self,time,locator):
        locate = (MobileBy.XPATH,locator)
        ele = WebDriverWait(self.driver,time).until(expected_conditions.element_to_be_clickable(locate))
        return ele.find_click()

    def find(self, locator, value):
        # return self.driver.find_element(locator, value)
        logging.info(f"find: locator={locator} , value = {value}")
        try:
            # 没有异常情况下直接return继续运行下去
            element = self.driver.find_element(locator, value)
            self._error_num = 0
            self.setup_implicitly_wait(10)
            return element
        except Exception as e:
            logging.error("未查到元素")
            # 处理黑名单逻辑
            self.setup_implicitly_wait(5)
            # 设置最大查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                self.setup_implicitly_wait(5)
                raise True
            # 每次进except 一次都执行+1操作
            self._error_num += 1
            for ele in self._blacklist:
                # find_elements 会返回元素的列表[ele1,ele2.....]，如果没有元素会返回一个空列表
                elves = self.driver.find_elements(*ele)
                if len(elves) > 0:
                    elves[0].click()
                    return self.find(locator, value)
            # 如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e

    def find_click(self, locator, value):
        return self.find(locator, value).click()

    def send(self, locator, value, text):
        return self.find(locator, value).send_keys(text)

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
        # json 序列化与反序列化
        # json.dumps() 序列化  python 对象转化成字符串
        # json.loads() 反序列化  python 字符串转化为python对象
        raw = json.dumps(steps)
        for key,value in self._params.items():
            raw = raw.replace("${" + key + "}", value)
        steps = json.loads(raw)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"], step["value"])
            elif step["action"] == "find":
                self.find(step["locator"], step["value"])
            elif step["action"] == "swip_click":
                self.swip_click(step["text"])
            elif step["action"] == "send":
                self.send(step["locator"], step["value"], step["text"])

