from Base.base import Base
import Page


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name, password):
        # 输入手机号  输入密码 点击登录
        self.send_element(Page.login_account_id, name)
        self.send_element(Page.login_passwd_id, password)
        self.click_element(Page.login_btn_id)

    def if_login_btu_exits(self):
        # 搜索登录按钮
        try:
            self.search_element(Page.login_btn_id).text
            return True
        except:
            return False

    def close_login_btu(self):
        self.click_element(Page.login_close_btn_id)