import time
from flask import Flask, request, jsonify

app = Flask(__name__)

#initial connection test
@app.route('/time')
def get_time():
    return {'time': time.time()}

#testing the connection
@app.route('/api/stores', methods=['POST'])
def search_stores():
    data = request.get_json()
    selected_item = data.get('item')

    if selected_item:
        print("Selected item:", selected_item)
        return "Selected item printed on the server", 200
    else:
        return "Invalid request", 400

if __name__ == '__main__':
    app.run(debug=True)