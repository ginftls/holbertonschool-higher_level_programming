from flask import Flask, render_template
import json

app = Flask(__name__)

# Route for the home page (optional, if you want to keep it)
@app.route('/')
def home():
    return render_template('index.html')

# Route for displaying the list of items
@app.route('/items')
def items():
    # Read the JSON file
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])  # Default to an empty list if "items" key is missing
    except FileNotFoundError:
        print("Error: items.json file not found.")
        items_list = []

    # Pass the list of items to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
