import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

# think of a factory, each thread is like a worker, each queue is like a job

PROJECT_NAME = 'careerscraper'
HOMEPAGE = 'https://careers.bankofamerica.com/en-us/job-search?ref=search&start=0&rows=895&search=jobsByKeyword&keywords=risk'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
  for _ in range(NUMBER_OF_THREADS):
    t = threading.Thread(target=work)
    t.daemon = True 
    t.start()

# Do the next job in the queue
def work():
  while True:
    url = queue.get() # get the next item from the thread queue
    Spider.crawl_page(threading.current_thread().name, url)
    queue.task_done() # tells os to free up memory and that worker is done with its job

# Each queued link is a new job
def create_jobs():
  for link in file_to_set(QUEUE_FILE):
    queue.put(link)
  queue.join()
  crawl() # after function is done creating a job and doing its thing, we want updated version of it

# Check if there are items (links) in the queue that need to be crawled. if so crawl them
def crawl():
  queued_links = file_to_set(QUEUE_FILE)
  if len(queued_links) > 0:
    print(str(len(queued_links)) + ' links in the queue')
    create_jobs()

create_workers()
crawl()
