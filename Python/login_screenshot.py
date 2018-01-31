#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time


def login_website():
	browser = webdriver.Chrome()
	browser.get('http://10.180.0.201')
	browser.maximize_window() 
	username = browser.find_element_by_id("login_input_username")
	password = browser.find_element_by_id("login_input_password")
	username.send_keys("admin")
	password.send_keys("admin")
	browser.find_element_by_id("button-login").click()
	time.sleep(20)
	browser.find_element_by_id("button-fullscreen").click()
	time.sleep(20)
	#browser.find_element_by_xpath("//select[@name='button-image-mode']/option[text()='IR']").click()
	#time.sleep(20)
	#browser.save_screenshot("/home/raj/Pictures/{}.png".format( datetime.now()))
	select = Select(browser.find_element_by_id('popup-image-mode'))
	select.select_by_visible_text('IR')
	select.select_by_value("on")

	return 0

def main():
	login_website()
	return 0


main()