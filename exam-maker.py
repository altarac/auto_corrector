import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup as bs


chromedriver = '/Users/samuelaltarac/Desktop/python programs/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.reddit.com/r/ScienceGIFs/')
