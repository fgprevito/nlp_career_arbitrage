from html.parser import HTMLParser #generic html parser, can go through html file and sift through it
from urllib import parse



# when we connect to a page and gather that HTML this class will give us all the links in that HTML
class LinkFinder(HTMLParser): # going to inherit HTMLParser so we can customize
    
  def __init__(self, base_url, page_url):
    super().__init__()
    self.base_url = base_url
    self.page_url = page_url
    self.links = set()

  def handle_starttag(self, tag, attrs):
    if tag == 'a':
      for (attribute, value) in attrs:
        if attribute == 'href' and '/en-us/job-detail/' in value:
          url = parse.urljoin(self.base_url, value)
          self.links.add(url)

  def page_links(self):
    return self.links

  def error(self, message):
    pass

