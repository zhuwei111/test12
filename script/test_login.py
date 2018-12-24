import allure


class TestLogin:
    def test_a(self):
        print("\n111")
        assert 1


    @allure.step('测试登录的步骤')
    def test_b(self):
        print("\n2222")
        assert 0