import allure
from base.base_page import BasePage
from page.private_info import PrivateInfo
from page.public_methods import PublicMethod


class TestPrivateAnnounce:

    private_ann = PublicMethod()

    @allure.severity("normal")
    @allure.story("测试隐私协议")
    @allure.title("查看隐私页面的标题和内容")
    def test_private_announce(self):
        self.private_ann.setup(BasePage(self).get_data()['test_private_announce']["_device_name"])
        self.private_ann.swap_guide_and_go_to_different_pages(0)
        assert PrivateInfo.get_title(self.private_ann.ll) == \
               BasePage(self).get_data()['test_private_announce']["_title"]
        self.private_ann.teardown()

