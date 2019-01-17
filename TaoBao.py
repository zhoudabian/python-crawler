# -*- coding=UTF-8 -*-
from selenium import webdriver
import time
import datetime
from tkinter import *
import threading
import tkinter.messagebox
def make_app():
    app = Tk()
    app.geometry('300x250')
    Label().pack()
    Label(text='请务必按照格式输入抢单时间').pack()
    Label(text='2018-10-30 20:44:26.463135').pack()
    Entry(name='ipt').pack()
    Label(text='请输入买家备注(如不填写可提高抢单速度)').pack()
    Entry(name='ipt2').pack()
    Label(name='lb1', text='抢单中').pack()
    Button(text='点击开始抢单', command=login).pack()
    return app

def login():
    # driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    th = threading.Thread(target=sign_up)
    th.start()

def sign_up():

    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    time.sleep(3)
    if driver.find_element_by_link_text('亲，请登录'):
        driver.find_element_by_link_text('亲，请登录').click()
        tkinter.messagebox.showinfo('提示', '请在15秒内完成登录二维码扫描')
        time.sleep(15)
        driver.get("https://cart.taobao.com/cart.htm")
        while tkinter.messagebox.askokcancel('提示', '请选择抢购的商品。打勾后点击确定') == False:
            tkinter.messagebox.askokcancel('提示', '请选择抢购的商品。打勾后点击确定')
        tkinter.messagebox.showinfo('提示', '请勿关闭网页')
        if app.children['ipt2'].get() == '':
             while True:
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                if now >= app.children['ipt'].get():
                    try:
                        if app.children['lb1']['text'] == '抢单中':
                            if driver.find_element_by_id('J_Go'):
                                driver.find_element_by_id('J_Go').click()
                                app.children['lb1']['text'] = '商品上线'
                        if app.children['lb1']['text'] != '抢单中':
                            driver.find_element_by_link_text('提交订单').click()
                            tkinter.messagebox.showinfo('提示', '抢单成功')
                    except:
                        time.sleep(0.001)
                time.sleep(0.001)
        else:
            while True:
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                if now >= app.children['ipt'].get():
                    try:
                        if app.children['lb1']['text'] == '抢单中':
                            if driver.find_element_by_id('J_Go'):
                                driver.find_element_by_id('J_Go').click()
                                app.children['lb1']['text'] = '商品上线'
                        if app.children['lb1']['text'] != '抢单中':
                            input_text = driver.find_elements_by_tag_name('textarea')[0]
                            if input_text:
                                text = app.children['ipt2'].get()
                                input_text.send_keys(text)
                                driver.find_element_by_link_text('提交订单').click()
                                tkinter.messagebox.showinfo('提示', '抢单成功')
                    except:
                        time.sleep(0.001)
                time.sleep(0.001)

if __name__ == '__main__':
    app = make_app()
    app.mainloop()

