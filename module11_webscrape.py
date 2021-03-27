import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://www.textfiles.com/programming/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

soup.findAll('a')

line_count = 1 #variable to track what line you are on
for one_a_tag in soup.findAll('a'):  #'a' tags are for links
    if line_count >= 36: #code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://www.textfiles.com/programming/'+ link
        urllib.request.urlretrieve(download_url, ''+link) 
        time.sleep(1) #pause the code for a sec
    #add 1 for next line
    line_count +=1