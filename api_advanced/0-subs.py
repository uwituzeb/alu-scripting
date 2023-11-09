#!/usr/bin/python3
"""Module to get the number of subscribers for a subreddit"""
import requests
from sys import argv

def number_of_subscribers(subreddit):
    """Returns:
            number of subscribers,
            0 if subreddit is invalid
        Args:
            subreddit: subreddit name
    """
    
    headers = {'User-Agent': 'test'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
