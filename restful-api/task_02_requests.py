#!/usr/bin/python3
"""Module for fetch_and_print_posts and fetch_and_save_posts methods"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder API and prints their titles.
    """
    # Send GET request to JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        posts = response.json()

        # Iterate through posts and print titles
        for post in posts:
            print(post["title"])
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder API and saves them to a CSV file.
    """
    # Send GET request to JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        all_posts = response.json()

        # Create a list of dictionaries with only the required fields
        posts_data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in all_posts
        ]

        # Write to CSV file
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            # Define fieldnames for the CSV
            fieldnames = ["id", "title", "body"]

            # Create DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Write all rows of data
            writer.writerows(posts_data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
