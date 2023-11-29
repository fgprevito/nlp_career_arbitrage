from bs4 import BeautifulSoup
import requests

def scrape_job_description(url):
  response = requests.get(url)

  if response.status_code == 200:
    document = BeautifulSoup(response.text, 'html.parser')
    job_description = document.find('div', class_='job-description-body__internal job__external js-job-description-body-internal')

    if job_description:
      return job_description.get_text(separator='\n', strip=True)
    else:
      return None
  else:
    print(f'Failed to access {url}')
    return None

# Main script to read URLs and write the scraped text to a file
with open('NLP Career Arbitrage/careerscraper/crawled.txt', 'r') as links_file, open('NLP Career Arbitrage/careerscraper/scraped_text.txt', 'a') as output_file:
  for url in links_file:
    url = url.strip()  # Remove any leading/trailing whitespace
    if url:  # Check if URL is not empty
      print(f'Scraping {url}')
      job_description_text = scrape_job_description(url)
      if job_description_text:
        output_file.write(job_description_text + '\n\n---\n\n')

print('Scraping complete.')