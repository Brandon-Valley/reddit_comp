# from selenium import webdriver
# 
# 
# driver = webdriver.Chrome(executable_path="C:/Users/Brandon/Downloads/chromedriver_win32/chromedriver.exe")
# driver.get('https://www.youtube.com/watch?v=RNZGJEd1YWE')
# 
# duration = driver.find_element_by_class_name('ytp-time-duration')
# 
# print(duration)
# print(duration.text)









from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/Brandon/Downloads/chromedriver_win32/chromedriver.exe")
driver.get('https://www.reddit.com/r/dankvideos/comments/bthlor/the_kook_aids_man/')

duration = driver.find_element_by_css_selector('.s1toz0wv-6.aiUF')

print(duration.get_property("attributes"))
print(duration.value_of_css_property('.s1toz0wv-6.aiUF'))



