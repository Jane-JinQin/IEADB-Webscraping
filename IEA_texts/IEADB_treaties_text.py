import requests
import urllib.request
import re
from bs4 import BeautifulSoup


#to run this code, you first need to create a folder where you will
# store the treaties texts.

list_text_id = [
    3059,
    8501,
    3100,
    5006] #add all treaties IDs in there


i = 0
inc = 0
n = len(list_text_id) #with n the total number of treaties

while i <= n-1:  
    treaty_id = list_text_id[inc]
    url_string='https://iea.uoregon.edu/treaty-text/'+str(treaty_id)
    print(url_string) #print the URL to test that the code is working
    
    website_url=requests.get(url_string)

    soup = BeautifulSoup(website_url.text,'lxml')
    myDiv = soup.find('div', {'class':'content clearfix'})
    myText = str(myDiv)  

    filename = "text_"+str(list_text_id[i])
    print(filename) #print the file name to test that the code is working
    location = "C:/Users/alice/Desktop/treaties/" + filename + ".doc"
    file = open(location, "w", encoding="utf-8")

    #Now we are going to write on our .doc file each element (define by the tag <p>) from our list
    #(mytext). But before adding a line to the .doc file, we are going to clean it from its html tag. 
    
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', myText)
    cleantext = cleantext + "\n"
    file.write(cleantext)    
    
    file.close()

    i += 1
    inc += 1
