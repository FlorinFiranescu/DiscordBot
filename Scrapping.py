from bs4 import BeautifulSoup
import requests

specs = ("dungeon", "tank", "melee", "healer", "ranged")

def request2BfSoupObj(URL):
    page = requests.get("{}".format(URL))
    print("\nRequesting Page URL: {}\n".format(URL))
    if page.status_code == 200: print("\nRequest OK: Status code {}\n".format(page.status_code))
    else:
        print("\nError with the request:response: {}\n".format(page.status_code))
        raise ConnectionError("\nError with the request:response: {}\n".format(page.status_code))
        return 0
    page.encoding = 'ISO-885901'
    soup = BeautifulSoup(page.text, 'html.parser')      #using the html parser, easier to search in browser
    return soup

def getAffixes(URL, spec = None):

    soup = request2BfSoupObj(URL)
    try:
        affixes = soup.body.find("h1")
    except Exception as e:
        print(e)
        return "Hm, there is something wrong. I can't find them for you"
    if spec == None:
        return "Oh, ok. Here are your affixes:\n{}".format(affixes.get_text().strip())
    elif spec.lower() not in specs:
        return "I don't know who is this guy {} but.. Here are your affixes:\n{}".format(spec, affixes.get_text().strip())
    else:
        tiers = soup.body.find_all("div", class_="col-xl-4")
        for tier in tiers:
            if spec.lower() in tier.h2.string.lower():
                soupTier = tier
                break
    currentAffixes = affixes.get_text().strip()
    tier = ""
    classes = ""
    message = "Oh, ok. Here are your affixes:\n{}".format(affixes.get_text().strip())
    for tr in soupTier.find_all("tr"):
        tier = tr.find(class_="tier")
        scrappedTierName = tier.string.strip()
        message = "{}\n{}:".format(message, scrappedTierName)
        for iconWithText in tr.find_all(class_="icon-with-text"):
            scrappedClass = iconWithText.img['title']
            message = "{} {}".format(message, scrappedClass)
            #print(iconWithText.img['title'])
    return message
        #Scrapping the spec



getAffixes("https://mplus.subcreation.net/")