#!/usr/bin/python3
""" get number of subcribers on subreddit """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid """
    
    headers = {'User-Agent': 'test'}
    url = "https://www.reddit.com/r/%7B%7D/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
