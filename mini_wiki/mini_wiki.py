from bs4 import BeautifulSoup
from requests import get

def main():
    # take user input
    # get the wikipedia page
    # scape the page using loops and if else statements

    q = str(input("What's the title?"))


    # oblviously the input will contain white space so first get rid of the
    url_q=add_underscore(q)

    # now lets get the wikipedia page to scrape
    page=get("https://en.wikipedia.org/wiki/" + url_q)


    # now convert this page to beautiful soup object
    soup=BeautifulSoup(page.content,'html.parser')

    # after locating the title in html page lets bring it here using python
    title=soup.find('h1',id='firstHeading').get_text()

    # now lets bring thr image url
    image=soup.find('a',class_="image")
    if not image:
        img="No image present here"

    else:
        img=image.find('img').get("src")
        if not img:
            print("No image available")

    # now its time we locate the description
    body=soup.find('div',id='mw-content-text')
    if not body:
        print("No wikipedia page available"+q)
        return 1

    body_text=body.find_all('p',limit=5)

    print("Title: " ,title)
    print("Description: ",first_sentence(body_text,q.split("p")[0]))
    print("image url: ",img)

def first_sentence(b,q):
    for p in b:
        sentences=p.get_text().split(".")

        for s in sentences:
            if q.lower() in s.lower():
                return s
    return b[0].get_text().split(".")[0]

def add_underscore(s):
    return s.replace(" ","_")

if __name__=="__main__":
    main()