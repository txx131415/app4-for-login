from Base.base import Base
import Page

class Sign_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_exits_login_btu(self):
        # 点击已有账号去登录按钮
        self.click_element(Page.exits_account_id)