import requests
from bs4 import BeautifulSoup

item = 'roma tomato organic'
item.replace(" ", "%20")
target_url=f"https://www.walmart.com/search?q={item}"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}


html_text = requests.get(target_url, headers=headers).text



if("Robot or human" in html_text):
     print(True)
else:
     print(False)

soup = BeautifulSoup(html_text,'html.parser')
#print(soup)

name_price = soup.find_all("span", {"class": "w_iUH7"})

# get names and prices into separate lists
names = [element.text.strip() for element in name_price[::2]]  # Extracting even indexed elements (names)
prices = [element.text.strip().replace("current price ", "") for element in name_price[1::2]]  # Extracting odd indexed elements (prices)

# get all image elements
images = soup.find_all("img", {"class": "absolute top-0 left-0"})

# combine names, prices, and image url into a list of dictionaries
products = []

for name, price, image in zip(names, prices, images):
    product = {
        "name": name,
        "price": price,
        "image_src": image.get("src")
    }
    products.append(product)
print(products)
# print each product dictionary, for testing
for product in products:
    print(product)



