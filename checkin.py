import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def signin():
    # 设置Chrome浏览器选项
    service = Service(executable_path=r'./chromedriver_linux64/chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # 创建Chrome浏览器实例
    browser = webdriver.Chrome(service=service, options=options)

    # 登陆
    browser.implicitly_wait(20) # 如果找不到元素，每隔半秒钟再去界面上查看一次， 直到找到该元素， 或者过了20秒最大时长。
    url = 'https://dukou.icu/user/index' # 目标网站
    browser.get(url)
    print("登陆成功")
    sleep(5)

    username = os.environ.get('EMAIL')
    passwd = os.environ.get('PASSWD')
    browser.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(username) # 输入框
    browser.find_element(by=By.XPATH, value='//*[@id="passwd"]').send_keys(passwd)
    browser.find_element(by=By.XPATH, value='//*[@id="formLogin"]/div[3]/div/div/span/button').click() # 点击登陆按钮

    # 进行签到
    sleep(5)
    browser.find_element(by=By.XPATH, value='//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]'
                         '/div/div/button[1]').click() # 点击签到

    # 检查签到是否成功
    result_info = browser.find_element(by=By.XPATH, value='//*[@id="app"]/section/section/main/div/div[2]/div/div/'
                                       'div/div[2]/div[3]/div/div/div[3]/div[2]').text
    if browser.find_element(by=By.XPATH, value='//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/'
                             'div[3]/div/div/button[1]/span').text == '今日已签到':
        print("签到失败：今日已签到，", result_info)
    else:
        print("签到成功：", result_info)

    # 停止爬虫
    browser.quit()

# 主函数
def main():
    # 执行签到
    print("\n--------------dukou begin--------------")
    signin()
    print("--------------dukou end--------------\n")

if __name__ == "__main__":
    main()
