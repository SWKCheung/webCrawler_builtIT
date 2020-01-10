import requests
from bs4 import BeautifulSoup
# import pandas as pd
import time

baseurl = "https://wiprodigital.com"
URL_4_Visits = [baseurl]
level = 1
exclude_list = ["facebook.com", "twitter.com", "linkedin.com", "google.com", "statista.com", "ecommercedb.com", "ehi.org"]
visited = ["x"]

def getAndParseURL(current_url):
    if current_url not in 'mailto:info@wipro.com':
        result = requests.get(current_url)
        soup = BeautifulSoup(result.content, 'html.parser')
        url_list = soup.find_all('a', href=True)
        return url_list


#def processURL(URL_4_Visits):
while len(URL_4_Visits) != 0:
    for visiting in URL_4_Visits:
        links = []
        df = {}
        for link in set(getAndParseURL(visiting)):
            url = link['href']
            if not any(x in url for x in exclude_list) and not any(url in v for v in visited) and url.startswith('http'):
               links.append(url)
               print(" visited : " + url)
               visited.append(url)
            else:
               print(" skipped : " + url)
    # df["level" + str(level)] = pd.DataFrame(set(links), columns=['url'])
    level += 1
    URL_4_Visits = links
    print("process level" + str(level))
