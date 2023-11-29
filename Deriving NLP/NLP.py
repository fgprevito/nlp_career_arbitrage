# Start with simulating the data 
# I want to start by trying to solve for the following: 
# There are 2 realities
  # 1: the model I have in mind makes sense
  # 2: it doesn't 
# What does this mean? Not interested in getting into a philosophical debate about the 'truth' of NLP techniques
# start with bare minimum: grammar structure
# let's pretend descriptive adjectives actually can explain text data well
# how do I know I am actually explaining data well and not just fooling myself into the relevancy of the factors I think are important? (descriptive adjectives in this case)
# easiest way to do this is using 2 kinds of fake data 
  # Fake data that uses my model to make fake data
  # fake data that obviously violates the assumption of my model
    # NOTE: DOES THIS TRANSFER OVER TO NLP? 

# I am assuming that each job description has a number of descriptive adjectives that'll tell me everything I want to know (what skills the bank emphasizes, the tone)
  # Basically, there's a set of information from job posts that'll tell me how a co. fairs risk wise
  # Suppose I deliberately genereate this data, will my model recover what I am intending? That's a sanity check
  # Reality is language is likely very nonlinear, random, posts probably just copy phrasing based on hiring culture so there's some BS 
  # I'm just trying to form a coherent, simple logic here

# Then I will have another chunk of data that totally violates my models assumptions
  # jsut a bunch of random incoherent words, maybe use sarcasm, idk 
  # i should get a senseless result
  # point of this is, recognize the biases of the model and try to eliminate as many variables as I can (words that don't matter, maybe paragraphs that dont matter, etc)
  # ke to being a good quant: dont want to find new variables, want a disciplined process where I can eliminate irrelevant variables

# So, make a set of fake data with:
# a job_title, date_posted, job_description, country, bank_name etc
# NOTE ???

# NOTE: IMPORTANT 
  # if i make data that's generated from an honest to God model, under what assumptions does my model recapitulate that structure
  # shoudl realize theres a specific set of conditions where I can recapitulate that data

# Know how to make data to truly understand how to manipulate the processes (do i actually know what I think I'm doing)
# Even tho fake data wont model reality exactly its good to know what parts of reality I cant control 
# Are my models sensitive to 1 time deviations?

# NOTE: GOAL: Take a complicated a problem, and do things to prove to myself that whatever I'm actually doing makes sense
# NOTE: GOAL: Achieve intuition about NLP 
  # If I can learn to go through the process of achieving intuition around NLP here and all its facets, this'll help me leanr how to solve problems with clear high quality thinking
  # think carefully about each step and why I'm doing it, what it means, and when it's useful
  # How Will changes in the process affect my results (more data, more factors, different grammar structures, different descriptive adjectives)

# NOTE: There are few things which we know which aren't capable of being reduced to a mathematical reasoning. 
  # And when they cannot, it is a sign that our knowldge of them is very small and confused. 
  # Where a math reasoning can be had, it is a great folly to make use of any other type of reasoning, 
  # as that would be like groping for a thing in the dark when you have a candle standing by you
    # Be able to process reality mathematically

###########################################################################

# So, I want to prove I understand this text data. How do I go about this? First what's the simplest expression I can use to simulate real data? 
  # Keep in mind the nature of this data: Job title, data posted, description, responsibilities, requirements, qualifications
  # Let's start with just a job desription 

# NOTE: ROSS ADVICE
  # look at a job ad for Lloyds and NWG
  # look at the subtle differences between the 2
  # - Lloyds used more exaggerated descriptive adjectives and paragraphs of inclusion and persuasive language. NWG  was more direct, communicated with bulleted lists
  # Bingo. NWG > Lloyds in regards to loan book management. Now try to find how you automate this. Lloyds uses veil lang. NWG also shit but a bit better. 
  # Read SEC securities law about future statement wordings

import re
import nltk
from nltk.corpus import stopwords
from nltk.corpus import state_union
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
# JJ  adjective              | big
# JJR comparative adjective  | bigger
# JJS superlative adjective  | biggest
# MD modal 

forward_looking_words = {'believes', 'will', 'shall', 'may', 'might', 'can', 'continue', 'could', 'should', 'would', 'expect', 'expects', 'estimates', 'anticipate', 'anticipates', 'predict', 'project', 'intend', 'intends', 'plan', 'plans', 'hope', 'seeks', 'seeks'}

def read_file(text):
  with open(text, 'r', encoding='utf-8') as file:
    content = file.read()
    return str(content)

def count_words(text):
  words = text.split()
  return len(words)
  # except FileNotFoundError:
  #   print(f'could not find the {text} file :(')
  # except Exception as e:
  #   print(f'An error occured :O {e}')

def count_adjectives(text):
  adjectives = 0
  words = word_tokenize(text)
  pos_tags = nltk.pos_tag(words)
  for word, tag in pos_tags:
    if tag == 'JJ':
      adjectives += 1
  return adjectives

def count_bullets(text):
  bullets = re.findall(r'\n[•\-]', text)
  return len(bullets)

def count_forward_looking_statements(text):
  forward_looking_count = 0
  words = word_tokenize(text)
  for word in words:
    if word.lower() in forward_looking_words:
      forward_looking_count += 1
  return forward_looking_count

def list_unique_adjectives(text):
  return set()

# TODO: FIX THIS
def list_forward_looking_statements(text):
  sentences = sent_tokenize(text)

  def contains_forward_looking_word(sentence):
    words = word_tokenize(sentence)
    for word in words:
      if word.lower() in forward_looking_words:
        return True
    return False

  forward_looking_statements = [sentence for sentence in sentences if contains_forward_looking_word(sentence)]

  print('\nForward-looking Statements:\n')
  for statement in forward_looking_statements:
    print(statement)

def sentiment_analysis(text):
  return None
  
# how I want to group my words
  # what does that mean group words? How do I define that?
def group_by_word(text):
  words = word_tokenize(text)
  return words

def group_by_sentence(text):
  sentences = sent_tokenize(text)
  return sentences

# TODO: FIX THIS
# preprocessing step: remove pointless words to clean up the data
def remove_unnecessary_words(text):
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(text)
  filtered_sentence = []
  for w in words:
    if w not in stop_words:
      filtered_sentence.append(w)
  return filtered_sentence

# evaluate model
def evaluate_model():
  return None

# SANITY CHECK
# sample_text = 'simulated_data.txt'
train = state_union.raw('2005-GWBush.txt')
sample = state_union.raw('2006-GWBush.txt')
small_example = 'We expect great things from this person and that person. It is my birthday.'
# sample_text = 'Our people work differently depending on their jobs and needs. From hybrid working to flexible hours, we have plenty of options that help our people to thrive. This role is based in the United Kingdom and as such all normal working days must be carried out in the United Kingdom.Join us as a Risk Modelling Lead Analyst. You’ll be developing and maintaining compliant and fit for purpose models used in the bank’s risk framework. With your skills and expertise, you’ll be able to provide clear and well-presented analysis. Join a collaborative and supportive team environment, where you’ll be valued for sharing your ideas and learning from others'
bullet_example = '''Job Description:
At Bank of America, we are guided by a common purpose to help make financial lives better through the power of every connection. Responsible Growth is how we run our company and how we deliver for our clients, teammates, communities and shareholders every day.
One of the keys to driving Responsible Growth is being a great place to work for our teammates around the world. We’re devoted to being a diverse and inclusive workplace for everyone. We hire individuals with a broad range of backgrounds and experiences and invest heavily in our teammates and their families by offering competitive benefits to support their physical, emotional, and financial well-being.
Bank of America believes both in the importance of working together and offering flexibility to our employees. We use a multi-faceted approach for flexibility, depending on the various roles in our organization.
Working at Bank of America will give you a great career with opportunities to learn, grow and make an impact, along with the power to make a difference. Join us!
Job Description:
This role is responsible for engaging clients in the lobby to educate and assist with conducting transactions through self-service resources such as mobile banking, online banking, or ATM. This role also accurately and efficiently processes cash transactions for clients as needed. Relationship bankers have deep conversations with clients to gain in-depth knowledge of their financial and life priorities.
A Relationship Banker (responsibilities):
- Executes the bank's risk culture and strives for operational excellence 
• Builds relationships with individual clients to meet their financial needs
• Follows established processes and guidelines in daily activities to do what is right for clients and the bank, adhering to all applicable laws and regulations
• Grows business knowledge and network by partnering with experts in small business, lending and investments
• Manages financial center traffic, appointments and outbound calls effectively
• Drives the client experience
• Manages cash responsibilities'''

text = read_file('NLP Career Arbitrage/careerscraper/scraped_text.txt')

jobs = text.split('---')
jobs = [job for job in jobs if job]
for job in jobs:
  job = job.strip()
  words = job.split()
  word_count = len(words)

# print('Total # of words: ', count_words(text))
# print('Total # of descriptive adjectives: ', count_adjectives(text))
# print('Total # of forward looking words: ', count_forward_looking_statements(text))
# print('Total # of bullets: ', count_bullets(text))

# custom_sentence_tokenizer = PunktSentenceTokenizer(train)
# tokenized = custom_sentence_tokenizer.tokenize(sample)

# def process_content():
#   try:
#     for i in tokenized:
#       words = nltk.word_tokenize(i)
#       tagged = nltk.pos_tag(words)
#       print(tagged)
#   except Exception as e:
#     print(f'An error occured :O {e}')

# process_content()
