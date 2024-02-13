import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def getFredMeyer(item):
    # authentication
    auth_url = "https://api.kroger.com/v1/connect/oauth2/token"

    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    #item = "tomato"

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
            "filter.term": f"{item}",  
            "filter.limit": 10,  
            "filter.locationId": 70100603 # Shelton, WA location ID
        }

        # Make API request
        search_response = requests.get(product_search_url, headers=headers, params=params)

        # Parse response
        items = {}
        products = []
        if search_response.status_code == 200:
            product_data = search_response.json()["data"]
            # Process  data

            for product in product_data:

                if "productId" in product:

                    id = str(product["productId"])
                    product_details_url = f"https://api.kroger.com/v1/products/{id}"

                    headers = {
                        "Authorization": f"Bearer {access_token}",
                        "Accept": "application/json"
                    }

                    # Make API request
                    product_response = requests.get(product_details_url, headers=headers, params=params)

                    # if the request was successful
                    if product_response.status_code == 200:
                            product_data = product_response.json()

                            # Extract price information from the response
                            items = product_data["data"]["items"]
                            item_info = product_data["data"]["description"]

                            if items:
                                for item in items:
                                    price_info = item.get("price")
                                    item_name = item_info + " " + item.get("size")
                                    #print(item_name)
                                    
                                    # Get price info
                                    if price_info:
                                        regular_price = price_info.get("regular")
                                        promo_price = price_info.get("promo")
                                        #print(f"Regular Price: ${regular_price}, Promo Price: ${promo_price}")
                                    else:
                                        print("Price information not available.")
                            else:
                                print("No items found for the specified product ID.")
                    else:
                        print("Error:", product_response.status_code)
                # Get image info
                images = product['images']
                for image in images:
                    sizes = image['sizes']
                    # Get thumbnail image
                    for size in sizes:
                        if size['size'] == 'medium':
                            img = size['url']
                            #print("Thumbnail URL:", thumbnail_url)
                            break 
                    break
                # add "promo_price": promo_price, back in
                products.append({"name": item_name, "price": regular_price, "image_src": img, "store": "Fred-Meyer"})
        else:
            print("Error:", search_response.status_code)
    else:
        print("Error:", response.status_code)

    return products
## Will get rid of print tests once the connection is made from backend to frontend