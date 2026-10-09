import json
import re
import urllib.request as ulr

def main():
  response = ulr.urlopen(
               ulr.Request(
                 'https://net-secondary.web.minecraft-services.net/api/v1.0/download/links',
                 headers={'User-Agent': 'Mozilla'}
               )
             ).read()

  links = json.loads(response)['result']['links']
  url = next(link['downloadUrl'] for link in links if link['downloadType'] == 'serverBedrockLinux')

  version = re.compile(r'.*/bin-linux/bedrock-server-(\d+(?:\.\d+)+)\.zip$').match(url).group(1)
  print(version)

if __name__ == '__main__':
  main()
