
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

    they now each loop until the end of the response data and add all
    attributes in order in tuples to a single list -> now we need to create a
    new list per posting and not just have one entire list of tuples.

=================================================================================
"""

def get_top_show_story():
    data_show = []
    response = requests.get('https://hacker-news.firebaseio.com/v0/showstories.json')
    print(response.json())
    for top_story_id in response.json():  # top_story_id is each item in the list
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json')
        story_response = story_response.json()
        print(story_response)

        for key in story_response:
            if( key == "by" or key == "descendants" or key == "title" or key == "id" or key == "url"):
                data_show.append((key, story_response[key]))
    print(data_show)
    print("\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n")

get_top_show_story()

def get_job_posting():
    data_jobs = []
    response = requests.get('https://hacker-news.firebaseio.com/v0/jobstories.json')
    for job_posting_id in response.json():
        job_response =  requests.get(f'https://hacker-news.firebaseio.com/v0/item/{job_posting_id}.json')
        job_response = job_response.json()

        for key in job_response:
            if( key != "score" and  key != "type" ):
                data_jobs.append((key, job_response[key]))
    print(data_jobs)

get_job_posting()

