import markdown
from bs4 import BeautifulSoup as bs

def gettitles(md_string):
    html = markdown.markdown(md_string)
    soup = bs(html)
    titles = []
    for tag in soup.find_all('h1'):
        titles.append(tag.text)
    for tag in  soup.find_all('h2'):
        titles.append(tag.text)
    return titles
