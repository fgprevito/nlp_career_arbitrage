# making functions repsonsible for extracting domain name so we dont crawl the entire web
from urllib.parse import urlparse

# Get domain name (example.com)
def get_domain_name(url):
  try:
    results = get_sub_domain_name(url).split('.')
    return results[-2] + '.' + results[-1]
  except:
    return ''

# Get sub domain name (careers.example.com)
def get_sub_domain_name(url):
  try: # anytime we work with networking or connecting to a server put into a try catch so we dont crash our program if we get booted
    return urlparse(url).netloc
  except:
    return ''
