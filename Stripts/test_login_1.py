import sys, os

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from Page.page import Page
from Base.get_driver import get_driver
import pytest


class Test_Login():
    def __init__(self):
        text = '此用户'
        self.mess = (By.XPATH, "//*[contains(@text,'{}')]".format(text))
    def setup_class(self):
        self.driver = get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope='class', autouse=True)
    def click_login_btu(self):
        # 点击我的
        self.page_obj.get_home_page_obj().click_my_btu()
        # 点击已有账号 去登录
        self.page_obj.get_sign_page_obj().click_exits_login_btu()

    def test_login(self):
        self.page_obj.get_login_page_obj().login("1111", '1234')


    def test_get_result(self):
        text = self.page_obj.get_login_page_obj().search_element(self.mess, timeout=5, poll_frequency=0.5).text
        print(text)
