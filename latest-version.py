import re
import urllib.request as ulr
from bs4 import BeautifulSoup as bs

def main():
  html = ulr.urlopen(
           ulr.Request(
             'https://minecraft.wiki/w/Bedrock_Dedicated_Server',
             headers={'User-Agent': 'Mozilla'}
           )
         ).read()

  table = bs(html, 'html.parser').find("h3", {"id":"Release_versions"}).find_next("table")
  a_tag = table.find_all("tr")[-1].find("a", string="Linux")

  version = re.compile('.*bedrock-server-(.*).zip').match(a_tag['href']).group(1)
  print(version)

if __name__ == '__main__':
  main()
