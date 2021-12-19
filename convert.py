def avg_price(prices):
    total_price = 0
    for price in prices:
        total_price += len(price)
    average = total_price / len(prices)
    return average

def avg_rating(ratings):
    total_rating = 0
    for rating in ratings:
        total_rating += rating
    average = total_rating / len(ratings)
    return average