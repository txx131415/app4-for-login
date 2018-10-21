from Base.base import Base
import Page, allure


class Login_Page(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    @allure.step(title='登录操作')
    def login(self, name, password):
        # 输入手机号  输入密码 点击登录
        allure.attach('输入手机号', '{}'.format(name))
        self.send_element(Page.login_account_id, name)
        allure.attach('输入密码', '{}'.format(password))
        self.send_element(Page.login_passwd_id, password)
        self.click_element(Page.login_btn_id)

    @allure.step(title='判断登录按钮是否存在')
    def if_login_btu_exits(self):
        # 搜索登录按钮
        try:
            self.search_element(Page.login_btn_id)
            allure.attach('登录按钮是否存在', '存在')
            return True
        except:
            allure.attach('登录按钮是否存在', '不存在')
            return False

    @allure.step(title='点击登录操作')
    def close_login_btu(self):
        self.click_element(Page.login_close_btn_id)
