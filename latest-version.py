import re
import urllib.request as ulr
from bs4 import BeautifulSoup as bs

def main():
  html = ulr.urlopen('https://minecraft.fandom.com/wiki/Bedrock_Dedicated_Server').read()
  version = bs(html, 'html.parser').find("span", {"id":"Download"}).parent.find_next("table").find_all("th")[-1].text.strip()
  print(version)

if __name__ == '__main__':
  main()
