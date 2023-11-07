#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, hot_list=[], after="", count=0):
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

    if after is None:
        wrd = {val: 0 for val in word_list}
        for item in hot_list:
            new_str = item.lower().split(' ')
            for key in new_str:
                if key in wrd:
                    wrd[key] += 1
        srd = sorted(wrd.items(), key=lambda item: (-item[1], item[0]))
        [print("{}: {}".format(key, val)) for key, val in srd if val]
        return hot_list
    else:
        return count_words(subreddit, word_list, hot_list, after, count)
