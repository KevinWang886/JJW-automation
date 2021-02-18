from appium import webdriver
import time
import yaml
import os
from base import config
from page.guide_page import GuidePage
from base.base_page import BasePage


class StartAPP:   # 打开APP

    def start_appium(self, port, bootstrap, udid):   # 启动appium服务
        a = os.popen('netstat -ano | findstr "%s" ' % port)
        time.sleep(2)
        t1 = a.read()
        if "LISTENING" in t1:
            BasePage.log.info("appium服务已经启动：%s" % t1)
        else:
            # 启动appium服务
            # appium -a 127.0.0.1 -p 4740 -U emulator-5554 127.0.0.1:62001 --no-reset
            # os.system("start /b appium -a 127.0.0.1 -p %s -U %s --no-reset" % (port, udid))
            # appium -a 127.0.0.1 -p 4724 -bp 4725 -U 127.0.0.1:62001
            os.system("start /b appium -a 127.0.0.1 -p %s -bp %s -U %s" % (port, bootstrap, udid))

    # def stop_appium(self):  # 关闭所有的appium进程
    #     os.system("start /b taskkill /F /t /IM node.exe")

    def get_desired_caps(self, devices_name):
        """
        从yaml读取desired_caps配置信息
        参数name:设备名称,如：夜神1/夜神2
        :return: desired_caps字典格式

        """
        yamlpath = os.path.join(config.YMAL_FILE, "app.yaml")
        f = open(yamlpath, "r", encoding="utf-8")
        a = f.read()
        f.close()
        # 把yaml文件转字典
        d = yaml.safe_load(a)
        for ii in d:
            if devices_name in ii["desc"]:  # 判断输入的设备名称是否存在
                # 启动服务
                StartAPP.start_appium(self, port=ii['port'], bootstrap=ii['bootstrap-port'], udid=ii['desired_caps']['udid'])
                return ii['desired_caps'], ii['port']

    def run_app(self, devices_name):    # 启动app
        # 配置参数
        try:
            desired_caps = StartAPP.get_desired_caps(self, devices_name)
        # 执行代码
            driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' % desired_caps[1], desired_caps[0])
        # 设置隐式等待时间
            driver.implicitly_wait(2)
            return GuidePage(driver)
        except:
            raise

    def end(self, devices_name):   # 退出app
        StartAPP.run_app(self, devices_name).driver.quit()
