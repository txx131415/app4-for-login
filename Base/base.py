from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, loc, timeout=10, poll_frequency=0.5):
        """元组（类型 属性 ）
        显式等待 时间 频率
        """
        return WebDriverWait(self.driver, timeout, poll_frequency). \
            until(lambda x: x.find_element(*loc))

    def search_elements(self, loc, timeout=10, poll_frequency=0.5):
        """元组（类型 属性 ）
        显式等待 时间 频率
        """
        return WebDriverWait(self.driver, timeout, poll_frequency). \
            until(lambda x: x.find_elements(*loc))

    def click_element(self, loc, timeout=10, poll_frequency=0.5):
        self.search_element(loc, timeout, poll_frequency).click()

    def send_element(self, loc, text, timeout=10, poll_frequency=0.5):
        input_text = self.search_element(loc, timeout, poll_frequency)
        input_text.clear()
        input_text.send_keys(text)

    @allure.step(title='滑动操作')
    def sreen_scrool(self, tag):
        """页面滑动
         tag  1---向上滑动  2--向下滑动 3--向左滑动 4--向右滑动
         """

        # 屏幕分辨率 ('width', 'height')
        screen_size = self.driver.get_window_size()

        width = screen_size.get("width")
        height = screen_size.get("height")

        if tag == 1:
            allure.attach('tag=1', '向上滑动')
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:
            allure.attach('tag=2', '向下滑动')
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:
            allure.attach('tag=3', '向左滑动')
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:
            allure.attach('tag=4', '向右滑动')
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    @allure.step(title='获取toast消息操作')
    def get_toast(self, mess):
        """
        获取toast消息
        :param mess: tost消息text文本
        :return: toast 消息
        """
        # 定位错误提示消息
        toast_xpath = "//*[contains(@text,'{}')]".format(mess)
        toast_message = self.search_element((By.XPATH, toast_xpath), timeout=5, poll_frequency=0.1).text
        allure.attach('toast文本为,{}'.format(toast_message))
        return toast_message
