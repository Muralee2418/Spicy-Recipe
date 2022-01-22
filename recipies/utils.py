from bs4 import BeautifulSoup
import requests

def get_link_data(url):
    print("inside get link")
    page2=requests.get(url)
    print(url)
    soup2 = BeautifulSoup(page2.content, 'html.parser')
    tit=soup2.find('h1',class_='nheadingrs')
    title=tit.text
    image=soup2.find('img',class_='postSlikeLoadImage')
    imageurl=image['src']
    print("image url")
    print(imageurl)
    des_div=soup2.find('div',class_='summeryhtcontentin')
    art=des_div.find('artsyn')
    des=art.find('p')
    description=''
    if des != None:
        description=des.text
    else:
        description="Description is not available"
    print(description)
    return title,description,imageurl
   

