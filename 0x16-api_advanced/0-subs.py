#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Return total no of subscribers
    on a given subreddit
    """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
                    Safari/537.36 Brave/94.1.23.1 Chrome/94.0.4606.61'
                    }
    response = requests.get("https://www.reddit.com/r/{}/about.json".
                            format(subreddit), headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json().get("data")
    return results.get("subscribers")
