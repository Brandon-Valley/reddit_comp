# # import time
# # from urllib.parse import quote_plus
# # from selenium import webdriver
# # import threading
# # 
# # from PIL import Image
# # 
# # PATH = 'C:/Users/Brandon/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe' ## SET YOU PATH TO phantomjs
# # 
# # driver = webdriver.PhantomJS(PATH)
# # driver.get('https://old.reddit.com/r/videomemes/comments/btf30h/when_your_mom_finds_you_casually_playing/')
# # driver.save_screenshot('screenshot.png')
# # 
# # image = Image.open('screenshot.png')
# # image.show()
# # 
# # vid_duration = driver.find_element_by_id('duration-overlay')#duration-overlay
# # 
# # print(vid_duration.get_attribute('elapsedTime'))
# 
# 
# 
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:/Users/Brandon/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://old.reddit.com/r/videomemes/comments/btf30h/when_your_mom_finds_you_casually_playing/')

s = driver.page_source.spl
# print(driver.page_source)
# 
# vid_duration = driver.find_element_by_class_name('duration-overlay')#duration-overlay
# print(vid_duration.get_attribute('data-action'))
# 
# print('<div class="duration-overlay">0:23</div>' in driver.page_source)


# 
# from selenium import webdriver
# from pprint import pprint
# driver = webdriver.Chrome(executable_path="C:/Users/Brandon/Downloads/chromedriver_win32/chromedriver.exe")
# driver.get('https://old.reddit.com/r/videomemes/comments/btf30h/when_your_mom_finds_you_casually_playing/')
# 
# element = driver.find_element_by_id('read-next-link-t3_btf30h')#duration-overlay
# attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', element)
# pprint(attrs)
# print(element.get_attribute('duration-overlay'))
# print(element.get_property('attributes'))

