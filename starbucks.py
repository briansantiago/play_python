from selenium import webdriver
import random

chromedriver = './chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http://first.wifi.olleh.com/starbucks/index_new.html')

check_box = driver.find_element_by_css_selector("input[id='stCheck']")
check_box.click()
use_box = driver.find_element_by_css_selector("img[src='img_new/bt_wifi_use.gif']")
use_box.click()

name = driver.find_element_by_name('userNm')
email = driver.find_element_by_name('cust_email_addr')
new_id = []
for i in range(7):
    text = ['1', '6','7','8','9','0', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'j', 'z', 'w', 'y']
    random.shuffle(text)
    new_id.append(text[i])
random_name = "".join(new_id)
random_email = "".join(new_id) + "@gail.com"
name.send_keys(random_name)
email.send_keys(random_email)

agree_box = driver.find_element_by_css_selector("input[id='agree1']")
agree_box.click()
agree_box2 = driver.find_element_by_css_selector("input[id='agree2']")
agree_box2.click()
last_box = driver.find_element_by_css_selector("img[src='img_new2/bt_agree.gif']")
last_box.click()

