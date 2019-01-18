from bs4 import BeautifulSoup
from util import environment_check
import requests

base_url = 'http://www.jmrenti.org'


def get_soup():
    soup = BeautifulSoup(environment_check.gethtml(base_url), "html.parser")
    return soup


# s=soup.prettify()
def get_page_url():
    for link in get_soup().find_all('a'):
        print(link.get('href'))
        if str(link.get('href')).endswith('.html') and str(link.get('href')).startswith('/'):
            # print(link.get('href'))
            url = []
            if str(link.get('href')) not in url:
                url.append(str(link.get('href')))
                for ur in url:
                    print(ur)


# print(soup.find_all('a'))
def get_image_url():
    for img in get_soup().find_all('img'):
        print(img.get('src'))
        # if str(img.get('src')).endswith('.jpg'): #and str(img.get('src')).startswith('/'):
        if img.get('src').endswith('.jpg'):
            # print (img.get('src'))
            imgg = []
            if str(img.get('src')) not in imgg:
                imgg.append(str(img.get('src').endswith('.jpg')))
                for im in imgg:
                    print(im)
               # return imgg
def create_url():
    pass


def save_img():
    i = 1
    for imagepath in get_image_url():
        try:
            f = open('../images/' + str(i) + '.jpg', 'wb')
            f.write(requests.get('http://www.jmrenti.org/uploads/allimg/140401/1-140401192442.jpg').content)
            f.close()
        except Exception as e:
            print(imagepath + e)
        # i+1


# for url in get_image_url():
#   print(url)
#save_img()
get_image_url()