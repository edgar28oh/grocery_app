import requests
from bs4 import BeautifulSoup

# Need to fix the data processing. 
# When an item is on sale it throws off the names and prices

def get_WM_items(item):
    item.replace(" ", "%20")
    target_url=f"https://www.walmart.com/search?q={item}"

    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}

    html_text = requests.get(target_url, headers=headers).text
    #print(html_text)

    # handles check for walmart robot blocker
    if("Robot or human" in html_text):
        print(True)
    else:
        print(False)

    soup = BeautifulSoup(html_text,'html.parser')

    name_price = soup.find_all("span", {"class": "w_iUH7"})
  
    # get names and prices into separate lists
    names = []
    prices = []
    sale_price = []


    for i in range(len(name_price)):

        current_text = name_price[i].text.strip()

        if current_text.startswith("current price Now $"):
            names.append(name_price[i-1].text.strip())
            sale_price.append(current_text.replace("current price Now $", ""))
        elif current_text.startswith("current price $"):
            names.append(name_price[i-1].text.strip())
            prices.append(current_text.replace("current price $", ""))
            sale_price.append("")
        elif current_text.startswith("Was $"):
            prices.append(current_text.replace("Was $", ""))
    print(sale_price)
    # get all image elements
    images = soup.find_all("img", {"class": "absolute top-0 left-0"})

    # combine names, prices, and image url into a list of dictionaries
    products = []

    for name, price, sale, image in zip(names, prices, sale_price, images):
        product = {
            "store": "Walmart",
            "name": name,
            "price": price,
            "sale_price": sale,
            "image_src": image.get("src")
        }
        products.append(product)

    return products


    





