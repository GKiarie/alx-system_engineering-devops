#!usr/bin/python3
"""recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
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
            "after": after,
            "count": count
            }
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count = count + results.get("dist")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
