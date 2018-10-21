from appium import webdriver


def get_driver(pag, act):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    desired_caps['appPackage'] = pag
    desired_caps['appActivity'] = act
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote("http://192.168.45.32:4723/wd/hub", desired_caps)


