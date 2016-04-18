# Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.pythonlearn.com/code/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#    Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
#    Actual data: http://python-data.dr-chuck.net/comments_245083.html (Sum ends with 26)

import urllib	
from BeautifulSoup import *

# url = raw_input('Enter - ')
url = "http://python-data.dr-chuck.net/comments_245083.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs

# using list comprehension to create a list out of the comment counts
contents = [int(tag.contents[0]) for tag in tags]
sum(contents)