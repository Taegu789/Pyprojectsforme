from urllib import response
import requests


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm_notebook
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

momo = []

url ='https://kr.investing.com/currencies/usd-krw'
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.get(url)
body = driver.find_element(By.CSS_SELECTOR,'body')
money =driver.find_element(By.CSS_SELECTOR,'__next > div > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__3tg3t > main > div > div.instrument-header_instrument-header__1SRl8.mb-5.bg-background-surface.tablet\:grid.tablet\:grid-cols-2 > div:nth-child(2) > div.instrument-price_instrument-price__3uw25.flex.items-end.flex-wrap.font-bold > span')

momo.append(money)
print(momo)