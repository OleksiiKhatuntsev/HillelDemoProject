import allure


class TestAllure:
    @allure.suite("auth_test")
    @allure.description("always failed, just to fail green diagram")
    @allure.issue("https://google.com", "Test issue: willn't be fix in the nearest future")
    def test_always_fail(self):
        assert 1 == 2
