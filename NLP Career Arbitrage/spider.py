from urllib.request import urlopen # module that allows us to connect to webpages witth python
from link_finder import LinkFinder
from general import *



# this will get links, check the waiting list to see if the link was crawled already, and if not it will put it in the waiting list
# if the link was crawled, it will move link from waiting to crawled list
class Spider:

  # class variable (shared among all instances)
  project_name = ''
  base_url = ''
  domain_name = ''
  queue_file = '' # waiting list (this'll be the text file we save data in long term)
  crawled_file = '' # all pages we've crawled
  queue = set() # these 2 set variables are bc we dont want to store every single link we come across for long term
  crawled = set()

  def __init__(self, project_name, base_url, domain_name):
    Spider.project_name = project_name
    Spider.base_url = base_url
    Spider.domain_name = domain_name
    Spider.queue_file = Spider.project_name + '/queue.txt'
    Spider.crawled_file = Spider.project_name + '/crawled.txt'
    self.boot()
    self.crawl_page('First spider', Spider.base_url) # this'll connect to some webpage, crawl it, gather it, etc

  @staticmethod
  def boot():
    create_project_directory(Spider.project_name)
    create_data_files(Spider.project_name, Spider.base_url)
    Spider.queue = file_to_set(Spider.queue_file)
    Spider.crawled = file_to_set(Spider.crawled_file)

  @staticmethod
  def crawl_page(thread_name, page_url):
    if page_url not in Spider.crawled:
      print(thread_name + ' now crawling ' + page_url)
      print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
      Spider.add_links_to_queue(Spider.gather_links(page_url)) # connects to webpage and returns set of links found on webpage, then adds links to waiting list that all spiders can see
      Spider.queue.remove(page_url) # once ur done crawling a page move from queue list to crawled
      Spider.crawled.add(page_url)
      Spider.update_files() # once done with all that, then we update the file

  @staticmethod
  def gather_links(page_url):
    html_string = ''
    try: 
      response = urlopen(page_url)
      if 'text/html' in response.getheader('Content-Type'):
        html_bytes = response.read()
        html_string = html_bytes.decode('utf-8')
      finder = LinkFinder(Spider.base_url, page_url)
      finder.feed(html_string)
    except Exception as e:
      print('Error: cannot crawl page', e)
      return set()
    return finder.page_links()
  
  @staticmethod
  def add_links_to_queue(links):
    for url in links:
      if url in Spider.queue:
        continue
      if url in Spider.crawled:
        continue
      if Spider.domain_name not in url:
        continue
      Spider.queue.add(url)

  @staticmethod
  def update_files():
    set_to_file(Spider.queue, Spider.queue_file)
    set_to_file(Spider.crawled, Spider.crawled_file)
