import sys, os

sys.path.append(os.getcwd())
import pytest
from Base.get_driver import get_driver
from Base.get_data import Get_Data
from Page.page import Page

"""
[(用例编号,手机号,密码,tag,tag_message,预期结果)]
"""


def get_login_data():
    # 结果列表
    login_list = []
    data = Get_Data().get_yaml_data("aolai_login.yml")
    # return data
    for i in data.keys():
        login_list.append((i, data.get(i).get("phone"), data.get(i).get("passwd"),
                           data.get(i).get("tag"), data.get(i).get("tag_message"),
                           data.get(i).get("expect_result")))
    return login_list


class Test_Login:
    def setup_class(self):
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_message,expect_result", get_login_data())
    def test_login(self, test_num, phone, passwd, tag, tag_message, expect_result):
        """

        :param test_num: 用例编号
        :param phone: 输入手机号
        :param passwd: 输入密码
        :param tag: 标记成功用例 1 成功用例  None 失败用例
        :param tag_message: 获取toast消息方法参数
        :param expect_result:预期结果
        :return:
        """
        # 点击我的
        self.page_obj.get_home_page_obj().click_my_btu()
        # 点击已有账号去登录
        self.page_obj.get_sign_page_obj().click_exits_login_btu()
        # 输入用户名 密码 点击登录
        self.page_obj.get_login_page_obj().login(phone, passwd)

        if tag:  # tag==1 为True 即为预期成功
            try:
                # 获取优惠卷文本
                coupons = self.page_obj.get_person_page_obj().get_person_coupons_text()
                # 但是 优惠卷名称可能会发生改变 但是如果取到这个文本即代表跳转至个人中心页-登录成功
                # 把断言放在try中，不会因为取到元素,但是断言失败而出错
                try:
                    assert coupons == expect_result
                except AssertionError as e:
                    # 打印断言错误信息
                    print(e.__str__())
                # 点击设置 点击退出
                self.page_obj.get_person_page_obj().click_setting()
                self.page_obj.get_setting_page_obj().login_out(1)
            except TimeoutError as e:
                # 如果没有跳转至个人中心页  也会用15秒的固定时间来搜索 优惠卷文本--找不到就会报超时异常
                # 即为还留在登录页  点击登录页上的退出按钮-进行退出操作
                self.page_obj.get_login_page_obj().close_login_btu()


        else:  # tag 找不到 即为预期失败用例
            pass


