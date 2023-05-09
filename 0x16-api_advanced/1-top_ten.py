#!/usr/bin/python3
"""script that queries the Reddit API
and prints the titles of the first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """
    ftn that prints the top ten posts
    listed for a given subreddit
    """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
                    Safari/537.36 Brave/94.1.23.1 Chrome/94.0.4606.61'
                    }
    response = requests.get("https://www.reddit.com/r/{}/about.json?limit=10".
                            format(subreddit), headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        results = response.json()
        for post in results['data']['children']:
            print(post['data']['title'])
