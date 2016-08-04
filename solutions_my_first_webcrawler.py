
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
	categories=[]
	soup=bsoup(starting_url)
	# now I need to save URLs of every category into a list and return that list (categories)
	for link in soup.findAll("a", {"class":"top-level-genre"}):
		href=link.get("href")
		categories.append(href)
	return categories

list_of_categories=get_categories (starting_url)
print(" Listed Categories", list_of_categories)
print("______________________________________________________________________________________")

# this function needs to return randomly picked category
# from list of categories

def get_random_category(categories):
	#One of the ways to randomly select a category from a list
	#is to pick a random value which is between 0 and len(list_of_categories)-1
	#and treat it as an index of the list.
	#Now the ony thing that I need to do is to retrieve the corresponding element (to the index) of the list
	number_of_categories=len(categories)
	random_number=random.randint(0, number_of_categories-1)
	return (categories[random_number])

random_category=get_random_category(list_of_categories)
print (" Randomly picked category is ", random_category)
print("______________________________________________________________________________________")

# this function takes URL of a randomly picked category
# and returns a list of links that correspond to the applications
# listed on the first page 

def apps(category):
	app_links=[]
	soup=bsoup(category)
	for app_link in soup.findAll("a",href = re.compile( '^https://itunes.apple.com/us/app' )):
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
	paid_apps=[]
	for app in app_links:
		soup=bsoup(app)
		price=soup.find("div", {"class":"price"})
		if price.text!="Free":
			paid_apps.append(app)
			#print(app)
	return (paid_apps)

paid_applications=paid_apps(app_links)
print(" List of paid apps (URLs): ", paid_applications)
print("______________________________________________________________________________________")
