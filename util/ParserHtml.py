from bs4 import BeautifulSoup
from util import environment_check
import requests

base_url = 'http://www.jmrenti.org'


def get_soup(url):
    soup = BeautifulSoup(environment_check.gethtml(url), "html.parser")
    return soup


# s=soup.prettify()
def get_page_all_url(url):
    page_url=[]
    link_url=[]
    for link in get_soup(url).find_all('a'):
        #print(link.get('href'))

        if str(link.get('href')).endswith('.html') and str(link.get('href')).startswith('/'):
            # print(link.get('href'))
            url = []
            if str(link.get('href')) not in url:
                url.append(str(link.get('href')))
                for ur in url:
                    print(ur)


# print(soup.find_all('a'))
def get_image_url(url):
    imgs = []
    src_url = []
    for img in get_soup(url).find_all('img'):
        # print(img.get('src'))
        imgs.append(img.get('src'))
        for src in imgs:
            if str(src).endswith('.jpg') and str(src).startswith('/'):
                imgurl = base_url + str(src)
                if imgurl not in src_url:
                    src_url.append(imgurl)
                # print(imgurl)
    return src_url


#def get_union_image_url(str):
 #   union_url = []
  #  for url in str:
   #     if url not in get_image_url():
    #        union_url.append(url)
    #return union_url
    # return src_url
    # if img.get('src').endswith('.jpg'):
    # print (img.get('src'))
    #  imgg = []
    #  if str(img.get('src')) not in imgg:
    #       imgg.append(str(img.get('src').endswith('.jpg')))
    #      for im in imgg:
    #          print(im)
    # return imgg


def create_url():
    pass


def save_img():
    i = 1
    for imagepath in get_image_url():
        try:
            f = open('../images/' + str(i) + '.jpg', 'wb')
            f.write(requests.get(imagepath).content)
            f.close()
        except Exception as e:
            print(imagepath + e)
        # i+1


# for url in get_image_url():
#   print(url)
# save_img()
#for sre in get_image_url():
##    print(sre)
ls='python'
print(ls[::2])

for s in 'stingdg':
    print(s)