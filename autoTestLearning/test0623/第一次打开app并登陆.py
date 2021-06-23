# -*- encoding=utf8 -*-
__author__ = "xmly"
from importlib import reload
from airtest.core.api import *
from aiautotest.core.decorator import run
from aiautotest.plugins.android.android import poco #导入poco api(用于元素识别，打开录制会自动导入)

time = 1
apk包名 = "com.ximalaya.ting.kid"
手机号 = "13000000181"
验证码 = "111111"

def 打开App():
    clear_app(apk包名);
    sleep(time);
    stop_app(apk包名);
    sleep(time);
    start_app(apk包名");
    sleep(time);
    
def 跳过欢迎页():
    sleep(time)

def 同意隐私条款():
    poco(text="同意").click();
    sleep(time)
    
def 跳过性别选择():
    poco(text="跳过").click()
    sleep(time)
    
def 同意权限():
    poco(text="允许").click()
    sleep(time)
    poco(text="允许").click()
    sleep(time)

def 关闭活动弹框():
    poco("com.ximalaya.ting.kid:id/img_firework_close").click()
    sleep(time)
    
def 去我的页面():
    poco("com.ximalaya.ting.kid:id/btn_me").click()
    sleep(time)
    poco("com.ximalaya.ting.kid:id/btn_me").click()
    sleep(time)
    
def 打开登陆页():
    poco("com.ximalaya.ting.kid:id/btn_login").click()
    sleep(time)
    
def 输入手机号并登陆():
    poco("com.ximalaya.ting.kid:id/et_txt").click()
    sleep(time)    
    text(手机号)
    sleep(time)
    poco("com.ximalaya.ting.kid:id/cbAgreement").click()
    sleep(time)    
    poco("com.ximalaya.ting.kid:id/ivSendSms").click()
    sleep(time)      
    text(验证码)
    sleep(time)
    
def test_login():
    打开App();
    跳过欢迎页();
    同意隐私条款();
    跳过性别选择();
    同意权限();
    关闭活动弹框();
    去我的页面();
    打开登陆页();
    输入手机号并登陆();
