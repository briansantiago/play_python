from selenium import webdriver
import pandas as pd 

chromedriver = './chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http://ridibooks.com/')

find_some = input("뭘 찾고 있나요?")
find_some = find_some + '\n'

search = driver.find_element_by_css_selector("input[id='book_search_input']")
search.send_keys(find_some)
searches = driver.find_element_by_id('books_contents')

book_lists = []

for l in searches.find_elements_by_css_selector("span.title_text"):
    book_lists.append(l.text)

easy_index = pd.Series(0, index = range(1, len(book_lists) +1))
book_series = pd.Series(book_lists, index = easy_index.index)

print(book_series)