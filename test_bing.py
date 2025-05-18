import allure
import requests

@allure.title("访问必应首页")
def test_访问必应():
    # Step 1: 发送 GET 请求
    response = requests.get("https://www.bing.com")
    
    # Step 2: 提取状态码
    code = response.status_code

    # Step 3: 验证状态码等于 200
    assert code == 200, f"断言失败，实际状态码为: {code}"
