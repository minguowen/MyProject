# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2019/03/16
# 淘宝秒杀脚本，扫码登录版
from selenium import webdriver
import datetime
import time
  
  
def login():
  # 打开淘宝登录页，并进行扫码登录
  browser.get("https://www.taobao.com")
  time.sleep(3)
  if browser.find_element_by_link_text("亲，请登录"):
    browser.find_element_by_link_text("亲，请登录").click()
    print("请在15秒内完成扫码")
    time.sleep(15)
    browser.get("https://cart.taobao.com/cart.htm")
  time.sleep(3)
  
  now = datetime.datetime.now()
  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
  
  
def buy(times):

  while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 对比时间，时间到的话就点击结算
    if now > times:
      # 秒杀

      try:
        if browser.find_element_by_id("J_Go"):
          browser.find_element_by_id("J_Go").click()
        if browser.find_element_by_link_text("提交订单"):
          browser.find_element_by_link_text("提交订单").click()    
      except:
        pass
          
    time.sleep(0.01)
  
if __name__ == "__main__":
  browser = webdriver.Chrome()
  browser.maximize_window()
  login()
  # 时间格式："2018-09-06 11:20:00.000000"
  buy("2020-02-09 19:37:00.000000")
  #buy("0")
