import re
import urllib.request as ulr
from bs4 import BeautifulSoup as bs

def main():
  html = ulr.urlopen('https://minecraft.fandom.com/wiki/Bedrock_Dedicated_Server').read()
  version = bs(html, 'html.parser').find_all(title=re.compile("Bedrock Dedicated Server"))[-1].text
  print(version)

if __name__ == '__main__':
  main()
