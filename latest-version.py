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

  index = -1
  while True:
    a_tag = bs(html, 'html.parser').find("span", {"id":"Download"}).parent.find_next("table").find_all("td")[index].find("a")
    if "Linux" == a_tag.text and "preview" not in a_tag['href']:
      break
    index = index - 1

  version = re.compile('.*bedrock-server-(.*).zip').match(a_tag['href']).group(1)
  print(version)

if __name__ == '__main__':
  main()
