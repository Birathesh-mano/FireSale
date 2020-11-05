import time

from flask import Flask, request, render_template, jsonify
import getting_price # custom scraping scripts
import addingItemDB # custom database script to add items to the database
app = Flask(__name__)

@app.route('/')
def get_data():
    return render_template("get_url.html")

@app.route('/confirmation', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        result = request.form
        url = result.get('URL')
        email = result.get('email')
        addingItemDB.addItem(url,email)
        while(True):
            getting_price.priceCheck(url)
            time.sleep(3600)
        return render_template("confirmation.html", result = result)

if __name__ == '__main__':
    app.run(debug=True)
