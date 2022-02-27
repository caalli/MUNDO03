import time
import requests
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1. Pegar conteúdo HTML a partir da URL

url = "https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular Season&sort=PLAYER"

option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)

driver.quit()




# 2. Parsear o conteúdo HTML - BeautifulSoup
# 3. Estruturar conteúdo em um Data Frame - Pandas
# 4. Transformar os Dados em um Dicionário de dados próprio
# 5. Converter e salvar em um arquivo JSON
