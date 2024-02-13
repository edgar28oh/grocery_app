import time
from flask import Flask, request, jsonify
from WalMart_scraper import get_WM_items
from FredMeyer_API import getFredMeyer

app = Flask(__name__)

#initial connection test
@app.route('/time')
def get_time():
    return {'time': time.time()}

@app.route('/api/search', methods=['POST'])
def search_groceries():
    data = request.get_json()
    print(data)
    item =  data.get('query')
    stores = data.get('selectedStores')

    if len(stores) < 2:
        if "Wal-Mart" in stores:
            return jsonify(get_WM_items(item)), 200
        elif "Fred-Meyer" in stores:
            return jsonify(getFredMeyer(item)), 200
    else:
        if "Wal-Mart" in stores and "Fred-Meyer" in stores:
            search_results = getFredMeyer(item) +  get_WM_items(item)
            return jsonify(search_results), 200

if __name__ == '__main__':
    app.run(debug=True)