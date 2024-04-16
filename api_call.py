
import json
import requests
import random
"""
=================================================================================

    Both get_top_show_story and get_job_posting return the desired values from
    the appropriate hacker news api get requests. In each function the response
    is turned into a python dictionary and looped over adding key value pairs
    as tuples into a python list. After the list is created the fields we dont
    desire to enter into our table are popped out of the list by index.

    next steps: do this looping over more objects not just one

=================================================================================
"""

def get_top_show_story():
    response = requests.get('https://hacker-news.firebaseio.com/v0/showstories.json?print=pretty')
    top_story_id = response.json()[0]  # Get the first top show story ID
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json')
    story_response = story_response.json()

    data = []
    for i in story_response:
        data.append((i, story_response[i]))
    data.pop(4)
    data.pop(4)
    data.pop(4)
    data.pop(5)
    print(data)

get_top_show_story()

def get_job_posting():
    response = requests.get('https://hacker-news.firebaseio.com/v0/jobstories.json')
    job_posting_id = response.json()[0]
    job_response =  requests.get(f'https://hacker-news.firebaseio.com/v0/item/{job_posting_id}.json')
    job_response = job_response.json()

# This creates a list of tuples where ( key, value) of the "job_response"
# dictionary. then it pops the thrird item off of the list which is "score"
    data = []
    for i in job_response:
        data.append((i, job_response[i]))
    data.pop(2)
    print(data)

get_job_posting()

