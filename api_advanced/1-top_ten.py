#!/usr/bin/python3
""" module for function to return top 10 hot posts of a given subreddit """
import requests
import sys


def top_ten(subreddit):
    """Returns: top ten post titles
       or None if queried subreddit is invalid

    Args:
        subreddit title
    """
headers = {'User-Agent': 'test'}
url = f"https://www.reddit.com/r/{subreddit}/hot.json"
parameters = {'limit': 10}
response = requests.get(url, headers=headers, 
                        allow_redirects=False, params=parameters)

if response.status_code == 200:
    titles_ = response.json().get('data').get('children')
    for title_ in titles_:
        print(title_.get('data').get('title'))
else:
    print(None)
