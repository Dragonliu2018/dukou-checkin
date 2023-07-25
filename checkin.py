import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

def signin():
    # 设置Chrome浏览器选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无界面模式，不弹出浏览器窗口

    # 创建Chrome浏览器实例
    browser = webdriver.Chrome('./chromedriver_linux64/chromedriver', options=chrome_options)

    # 登陆
    browser.implicitly_wait(20) # 如果找不到元素，每隔半秒钟再去界面上查看一次， 直到找到该元素， 或者过了20秒最大时长。
    url = 'https://dukou.icu/user/index' # 目标网站
    browser.get(url)
    print("登陆成功")
    sleep(5)

    browser.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(os.environ.get('EMAIL')) # 输入框
    browser.find_element(by=By.XPATH, value='//*[@id="passwd"]').send_keys(os.environ.get('PASSWD'))
    browser.find_element(by=By.XPATH, value='//*[@id="formLogin"]/div[3]/div/div/span/button').click() # 点击登陆按钮

    # 进行签到
    sleep(5)
    browser.find_element(by=By.XPATH, value='//*[@id="app"]/section/section/main/div/div[2]/div/div/div/div[2]/div[3]'
    '/div/div/button[1]').click() # 点击签到
    print("签到成功")

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

