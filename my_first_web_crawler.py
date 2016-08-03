# In this exercise you will need to write a 'spider'
# that crawls itunes website starting at https://itunes.apple.com/us/genre/ios/id36?mt=8
# It needs to return a list of the most popular paid apps ( URLs) that
# are available under a randomly picked category 

from bs4 import BeautifulSoup

import requests
import string 
import re
import random

starting_url="https://itunes.apple.com/us/genre/ios/id36?mt=8"

# converting specified web page into beautifulsoup format
def bsoup(url):
	source_code=requests.get(url)
        plain_text=source_code.text
        soup=BeautifulSoup(plain_text)
	return soup

# this function takes starting web page's url as an argument
# and returns a list of available categories

def get_categories(starting_url):
	"*** Your Code here ***"
	return categories

list_of_categories=get_categories (starting_url)
print(" Listed Categories", list_of_categories)
print("______________________________________________________________________________________")

# this function needs to return randomly picked category
# from list of categories

def get_random_category(list_of_categories):
	"*** Your Code here ***"

random_category=get_random_category(list_of_categories)
print (" Randomly picked category is ", random_category)
print("______________________________________________________________________________________")

# this function takes URL of a randomly picked category
# and returns a list of links that correspond to the applications
# listed on the first page 

def apps(category):
	app_links=[] #this is where I will store my app links
	soup=bsoup(category)# obtaining the content of the page
	for app_link in soup.findAll("a",href = re.compile( '^https://itunes.apple.com/us/app' )): #looping over links that start with 'https://itunes.apple.com/us/app'
			link_str=app_link.get("href")
			app_links.append(link_str)
	return app_links
app_links=apps(random_category)
print(" Apps( URLs) listed on",random_category, " : ", app_links)
print("______________________________________________________________________________________")

# this function takes a list of app links found in the previous function as an argument,
# and returns the list of links that correspond to Paid apps

# calculations may take quite some time. remember, you are downloading and checking contents of many pages!
# if you want to check whether your code is working, print the app's URL before appending it to a list!
def paid_apps(app_links):
	"*** Your Code here ***"

paid_applications=paid_apps(app_links)
print(" List of paid apps (URLs): ", paid_applications)
print("______________________________________________________________________________________")

