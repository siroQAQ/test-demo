import allure
import requests

@allure.title("访问必应首页")
def test_访问必应():
    with allure.step("发送 GET 请求"):
        response = requests.get("https://www.bing.com")

    with allure.step("校验响应状态码"):
        code = response.status_code
        assert code == 200, f"断言失败，实际状态码为: {code}"
