
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from unittest.util import _count_diff_all_purpose
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

repeating_count = 0
url = input('Enter link - ')
count =  input('Enter count - ')
count = int(count)
position = input('Enter position - ')
position = int(position)

def parse_html(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags 

# Retrieve all of the anchor tags

while repeating_count < count:
    print('Retrieving: ', url)
    tags = parse_html(url)
    for index, item in enumerate(tags):
        if index == position - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    repeating_count += 1

print('Last Url: ', url)    

# for num in count:
#     print('Retrieving:  ', url)
#     tags = parse_html(url)
#     for index, item in enumerate(tags):
#         if index == position - 1:
#             url = item.get('href', None)
#             name = item.contents[0]
#             break
#         else:
#             continue
    

   

    