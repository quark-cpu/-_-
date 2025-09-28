from selenium import webdriver
import time
import os
url1='https://kaoshi.wjx.top/vm/mimVyAk.aspx#'
# 打开测试浏览器并修改ua
custom_user_agent = "Mozilla/5.0 (Linux; Android 10; CDY-AN90 Build/HUAWEICDY-AN90; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200801 Mobile Safari/537.36 MMWEBID/4006 MicroMessenger/7.0.18.1740(0x2700123B) Process/toolsmp WeChat/arm64 NetType/4G Language/zh_CN ABI/arm64"

option = webdriver.EdgeOptions()
option.add_argument(f'--user-agent={custom_user_agent}') # 修改ua
option.add_experimental_option('excludeSwitches', ['enable-automation']) #关闭浏览器的自动化
option.add_experimental_option('useAutomationExtension', False) #关闭浏览器的自动化扩展
option.add_experimental_option("detach", True) #进程结束不会关浏览器
driver = webdriver.Edge(options=option)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                       {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}) # 禁用webdriver

driver.get(url1)

