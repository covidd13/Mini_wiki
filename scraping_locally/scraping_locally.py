from bs4 import BeautifulSoup
from requests import get

def main():
    #lets first open file in read only mode
    f=open('/workspaces/109335985/scrapy/example.html','r')
    s=f.read()

    soup=BeautifulSoup(s,'html.parser')

    list_=soup.find_all('li')

    details= [d.string for d in list_]
    print(details)


if __name__ == "__main__":
    main()