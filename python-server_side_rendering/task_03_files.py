from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read JSON file
def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}.")
        return []

# Function to read CSV file
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

# Route for displaying products
@app.route('/products')
def products():
    # Get query parameters
    source = request.args.get('source', '').lower()  # Default to empty string if not provided
    product_id = request.args.get('id', None)        # Optional id parameter

    # Read data based on source
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source")

    # Convert price to float for CSV (since all values are read as strings)
    if source == 'csv':
        for product in products_data:
            product['price'] = float(product['price'])

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [product for product in products_data if product['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Invalid id format")

    # Pass data to the template
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
