from Base.base import Base
import Page,allure


class Home_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
    @allure.step(title='点击我的按钮')
    def click_my_btu(self):
        """点击 首页-我的 按钮"""
        self.click_element(Page.my_btn_id)