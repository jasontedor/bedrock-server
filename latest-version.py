import re
import urllib.request as ulr
from bs4 import BeautifulSoup as bs

def main():
  html = ulr.urlopen('https://minecraft.fandom.com/wiki/Bedrock_Dedicated_Server').read()

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
