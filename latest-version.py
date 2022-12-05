import re
import urllib.request as ulr
from bs4 import BeautifulSoup as bs

def main():
  html = ulr.urlopen('https://minecraft.fandom.com/wiki/Bedrock_Dedicated_Server').read()
  href = bs(html, 'html.parser').find("span", {"id":"Download"}).parent.find_next("table").find_all("td")[-1].find("a")['href']
  if "preview" not in href:
    version_index = -1
  else:
    version_index = -2
  version = bs(html, 'html.parser').find("span", {"id":"Download"}).parent.find_next("table").find_all("th")[version_index].text.strip()
  print(version)

if __name__ == '__main__':
  main()
