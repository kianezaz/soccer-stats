HTML_FORMAT = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Yelp Comparator App</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
	<h1 id="title">Yelp Comparator for {}</h1>
    <div id="board">{}</div>
  </body>
</html>
"""

ITEM_FORMAT = """
<div class="slide">
    <h2>{location}</h2>
    <div><strong>Average rating: </strong>{rating}</div>
    <div><strong>Average price: </strong>{price}</div>
    <div class="images-container">{images}</div>
</div>
"""

def generate(item, datalist):
    body_string = ""
    for data in datalist:
        images_string = ""
        for url in data['images']:
            images_string += """<img src={}>\n""".format(url)
        
        body_string += ITEM_FORMAT.format(location = data["location"],
                       rating = data["rating"],
                       price = data["price"],
                       images = images_string)

    with open("out.html", "w+") as output_file:
        output_file.write(HTML_FORMAT.format(item, body_string))
    