import time
from flask import Flask, request, jsonify
from WalMart_scraper import get_WM_items

app = Flask(__name__)

#initial connection test
@app.route('/time')
def get_time():
    return {'time': time.time()}

@app.route('/api/search', methods=['POST'])
def search_groceries():
    data = request.get_json()
    item =  data.get('query')

    # Just a test
    # print("The item: " + item)
    
    search_results = get_WM_items(item)
    return jsonify(search_results), 200

if __name__ == '__main__':
    app.run(debug=True)