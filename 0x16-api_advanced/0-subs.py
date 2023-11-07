#!/usr/bin/python3
""" Write a function that queries the Reddit
API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """ functions to return subscribers to a subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
            "User-Agent": "Linux:subredditcheck:v1"
            # Replace with your custom User-Agent
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    except (requests.RequestException, KeyError):
        return 0
