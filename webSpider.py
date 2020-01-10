import requests
from bs4 import BeautifulSoup
import sys


#import pandas as pd
"""
  Developer   : Sam Cheung
  Date        : 1/10/2020
  Version     : 1.0
  Purpose     : This program is simulating web crawler or robot agent scanning web page URLs until all 
                web pages are visited. Add any web site to the exclude_list if you want.
  Dependencies: Python 3.8
                BS4
                Pandas(only required for analysis)             
"""

# Initial block #
#baseurl = "https://wiprodigital.com"
#URL_4_Visits = [baseurl]
#level = 1

# exclusion list of sites
exclude_list = ["facebook.com", "twitter.com", "linkedin.com", "google.com", "youtube.com",
                "idc.com", "pega.com", "adobe.com", "statista.com", "ecommercedb.com",
                "ehi.org", "designit.com", "mckinsey.com", "onstar.com", "support.mozilla.org",
                "en.wikipedia.org", "s17776.pcdn.co", "aboutcookies.org", "support.microsoft.com", "cnbc.com"]

# set dummy value to make list comparison work
visited = ["x"]

def getAndParseURL(current_url):
    if current_url not in 'mailto:info@wipro.com':
        result = requests.get(current_url)
        soup = BeautifulSoup(result.content, 'html.parser')
        url_list = soup.find_all('a', href=True)
        img = soup.find_all('link', href=True)
        url_list.extend(img)
        return url_list

# Main loop until all pages are visited


def main():
    level = 1
    URL_4_Visits = [str(sys.argv[1])]
    while len(URL_4_Visits) != 0:
        for visiting in URL_4_Visits:
            links = []
            df = {}
            for link in set(getAndParseURL(visiting)):
                url = link['href']
                if not any(x in url for x in exclude_list) and not any(url in v for v in visited) and url.startswith('http'):
                   links.append(url)
                   print(" visited : " + url)

                else:
                   print(" skipped : " + url)
                visited.append(url)
        # df["level" + str(level)] = pd.DataFrame(set(links), columns=['url'])
        level += 1
        URL_4_Visits = links
        if len(URL_4_Visits) == 0:
            print("\n\n=====  visited pages ({}) =====".format(str(len(set(visited)))))
            for out in set(visited):
                if (out != 'x' or 'mailto' not in out) and out.startswith('http'):
                   print(out)
        else:
            print("process level" + str(level))


if __name__ == '__main__':
    main()
