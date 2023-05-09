#!usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Ftn that returns a list containing
    all hot articles
    """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
                    Safari/537.36 Brave/94.1.23.1 Chrome/94.0.4606.61'
                    }
    params = {
            "limit": 50,
            "after": after
            }
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        response = response.json()['data']
        after = response['after']
        response = response['children']

        for post in response:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
