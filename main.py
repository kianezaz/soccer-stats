import sys
import traceback
import webbrowser
import os

from scraper import scrape_for
from convert import avg_price, avg_rating
from generate import generate

if __name__ == "__main__":
    print("Welcome to the location comparator app! Please enter the item you'd like to compare:\n")
    item = input()
    print("Ah, {}! Excellent choice. Please enter the first of two locations to compare:\n".format(item))
    location1 = input()
    print("Second of two locations:\n")
    location2 = input()
    print("Generating report...\n\n")

    try:
        (prices1, stars1, images1) = scrape_for(item, location1)
        (prices2, stars2, images2) = scrape_for(item, location2)

        location1_avg_price = avg_price(prices1)
        location1_avg_rating = avg_rating(stars1)

        location2_avg_price = avg_price(prices2)
        location2_avg_rating = avg_rating(stars2)

    except Exception as e:
        print("Bad input, the program has ended")
        print(traceback.format_exc())
        sys.exit()

    cheaper = None
    if location1_avg_price < location2_avg_price:
        cheaper = location1
    elif location2_avg_price < location1_avg_price:
        cheaper = location2

    higher_rating = None
    if location1_avg_rating > location2_avg_rating:
        higher_rating = location1
    elif location2_avg_rating > location1_avg_rating:
        higher_rating = location2

    print("In {p1}, the average rating for {item} is {ra}"
    .format(p1 = location1, item = item, ra = location1_avg_rating))

    print("In {p2}, the average rating for {item} is {ra}"
    .format(p2 = location2, item = item, ra = location2_avg_rating))

    if cheaper != None:
        print("Based on Yelp, we can conclude that {} is cheaper".format(cheaper))
    else:
        print("Based on Yelp, we can conclude that their average ratings are equal")

    if higher_rating != None:
        print("and {} is higher rated!".format(higher_rating))
    else:
        print("and their average ratings are equal!")

    generate(item, [
        {"location": location1, "rating": location1_avg_rating, "price": location1_avg_price, "images": images1},
        {"location": location2, "rating": location2_avg_rating, "price": location2_avg_price, "images": images2}
    ])
    webbrowser.open("file://" + os.path.realpath("out.html"))