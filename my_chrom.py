import requests
from bs4 import BeautifulSoup
import eel
import link_class




campus = "https://campus.gov.il"
back,url,soup2 = [],'',''

def print_urls(url): # returns all url in the page in html pormat with id.
    global  soup2
    a = "the url you visit is: " + url
    result = ""
    for j in range(len(soup2) - 1):
        try:
            if soup2[j].text:
                soup2[j]['href'] = soup2[j]['href'].replace("/url?q=", "")[:soup2[j]['href'].find('&')]
                link = link_class.LINK(j, soup2[j]['href'], soup2[j].text)
                result += str(link)
        except:
            j += 1
    return a + result


@eel.expose()
def go(first_url=campus, is_back=False): # go to the url page.
    global back
    global url
    global soup2


    try:
        i= int(first_url)
        url = str(soup2[i]['href'])
        r = requests.get(url)

    except:

        try:
            url = first_url
            r = requests.get(url)
        except:
            try:
                url = url+first_url # if the new link is in this website. like "/page2"
                r = requests.get(url)

            except:
                try:
                    url = 'https://www.google.com/search?q=' + first_url
                    r = requests.get(url)
                except:
                    return('error :',url ,go_back())
    if not is_back:
        if url:
            back += [url] # add the url to the memory.

    soup = BeautifulSoup(r.content)
    soup3 = soup.find_all('link')
    print(soup3)
    soup2 = soup.find_all('a')
    return print_urls(url)






@eel.expose()
def go_back(i): # go to the passed pages.
    try:
        return go(back[-1 - i], is_back=True)
    except:
        return """hello! insert a url or word to search in google to see only the links inside and to get right to the page you need.
        it's help my for my slowly internet. after you send url put the number of url you need...
        if you find your wonted page click on it and go out of my chrom."""


app_options = {
        'mode': "chrome",
        'host': "localhost",
        'port': 0   # python will select free ephemeral ports.
    }
eel.init('web')

try:
    eel.start('index.html',  options=app_options ,suppress_error=True)

except (SystemExit, MemoryError, KeyboardInterrupt):
    print("Program Exit, Save Logs if Needed")