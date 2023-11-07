#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:subredditcheck:v1"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    results = response.json()["data"]
    after = results["after"]
    count += results["dist"]
    for c in results["children"]:
        hot_list.append(c["data"]["title"])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
