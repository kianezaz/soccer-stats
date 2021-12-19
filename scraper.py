from bs4 import BeautifulSoup
import requests
import urllib 

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type'
}

def scrape_for(query, location):
    url = "https://www.yelp.com/search?"
    params = {"cflt": query, "find_loc": location, "start": 0}
    url += urllib.parse.urlencode(params)

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    prices = soup.find_all("span", class_="priceRange__09f24__mmOuH css-18qxe2r")
    for i in range(len(prices)):
        prices[i] = prices[i].text.strip()

    stars = soup.find_all("div", class_="i-stars__09f24__foihJ")
    for i in range(len(stars)):
        stars[i] = float(stars[i]["aria-label"][:-12])

    images = soup.find_all("img", class_="css-xlzvdl")
    for i in range(len(images)):
        images[i] = images[i]["src"]

    return (prices, stars, images)