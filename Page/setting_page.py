import time

from Base.base import Base
import Page


class Setting_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login_out(self, tag):
        time.sleep(2)
        # 先滑倒最底部 点击退出 再点击确定(默认退出)
        self.sreen_scrool(1)
        self.click_element(Page.logout_btn_id)
        # 在弹窗中点击确定
        if tag == 1:
            self.click_element(Page.logout_acc_btn_id)
        else:
            self.click_element(Page.logout_miss_btn_id)
