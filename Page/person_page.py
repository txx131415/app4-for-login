import allure

from Base.base import Base
import Page


class Person_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title='获取我的优惠卷')
    def get_person_coupons_text(self):
        # 返回我的优惠卷文本
        return self.search_element(Page.person_coupons_id).text

    @allure.step(title='点击设置')
    def click_setting(self):
        self.click_element(Page.setting_btn_id)
