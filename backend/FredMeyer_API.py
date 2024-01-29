import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

# authentication
auth_url = "https://api.kroger.com/v1/connect/oauth2/token"

# Client credentials
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
item = "tomato"

data = {
    "grant_type": "client_credentials",
    "scope": "product.compact"
}

# Encode client ID and client secret for authorization header
auth_header = {
    "Authorization": f"Basic {base64.b64encode(f'{client_id}:{client_secret}'.encode()).decode()}"
}

# Make token request
response = requests.post(auth_url, data=data, headers=auth_header)

# Parse response
if response.status_code == 200:
    access_token = response.json()["access_token"]

    # Product search endpoint
    product_search_url = "https://api.kroger.com/v1/products"

    # API request headers with access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    # Query parameters for product search
    params = {
        "filter.term": f"{item}",  # Example search term
        "filter.limit": 10,  # Limiting to 10 results
        "filter.locationId": 70100603 # Shelton, WA location ID
    }

    # Make API request to search for products
    search_response = requests.get(product_search_url, headers=headers, params=params)

    # Parse search response
    items = {}
    if search_response.status_code == 200:
        product_data = search_response.json()["data"]

        # Process product data
        for product in product_data:

            if "productId" in product:

                id = str(product["productId"])
                product_details_url = f"https://api.kroger.com/v1/products/{id}"

                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Accept": "application/json"
                }

                # Make the API request
                product_response = requests.get(product_details_url, headers=headers, params=params)

                # Check if the request was successful (status code 200)
                if product_response.status_code == 200:
                        product_data = product_response.json()

                        # Extract price information from the response
                        items = product_data["data"]["items"]
                        item_info = product_data["data"]["description"]

                        if items:
                            for item in items:
                                price_info = item.get("price")
                                item_name = item_info + " " + item.get("size")
                                print(item_name)
                                
                                if price_info:
                                    regular_price = price_info.get("regular")
                                    promo_price = price_info.get("promo")
                                    print(f"Regular Price: ${regular_price}, Promo Price: ${promo_price}")
                                else:
                                    print("Price information not available.")
                        else:
                            print("No items found for the specified product ID.")
                else:
                    print("Error:", product_response.status_code)
            images = product['images']
            for image in images:
                sizes = image['sizes']
                for size in sizes:
                    if size['size'] == 'thumbnail':
                        thumbnail_url = size['url']
                        print("Thumbnail URL:", thumbnail_url)
                        break  # Exit the loop once thumbnail URL is found
                break

    else:
        print("Error:", search_response.status_code)
else:
    print("Error:", response.status_code)


"""
                items_data = product_data["data"]
                item_info = items_data["description"]
                item_name = item_info + " " + item.get("size")

                # Extract thumbnail URL
                images = items_data.get("images", [])
                thumbnail_url = None
                for image in images:
                    sizes = image.get("sizes", [])
                    for size in sizes:
                        if size["size"] == "thumbnail":
                            thumbnail_url = size["url"]
                            break
                    if thumbnail_url:
                        break

                # Extract item details
                items[item_name] = {
                    "price": None,
                    "promo_price": None,
                    "img_url": thumbnail_url
                }
                items_list = items_data.get("items", [])
                for item in items_list:
                    price_info = item.get("price")
                    if price_info:
                        regular_price = price_info.get("regular")
                        promo_price = price_info.get("promo")
                        items[item_name]["price"] = regular_price
                        items[item_name]["promo_price"] = promo_price
                    else:
                        print("Price information not available.")

"""