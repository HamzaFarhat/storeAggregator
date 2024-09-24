from flask import Flask, jsonify
from data1 import scrape_website

app = Flask(__name__)

@app.route('/api/items', methods=['GET'])
def get_items():
    urls = [
    'https://oldnavy.gapcanada.ca',
    'https://www.gapcanada.ca',
    #'https://website3.com/clothing'
    ]
    all_items = []
    for url in urls:
        all_items.extend(scrape_website(url))
    return jsonify(all_items)

if __name__ == '__main__':
    app.run(debug=True)
