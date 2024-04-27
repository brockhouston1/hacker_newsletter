
def get_top_show_stories():
    data_shows = []
    response = requests.get('https://hacker-news.firebaseio.com/v0/showstories.json')
    show_story_ids = response.json()[:10]  # Limit to the top 10 for demonstration purposes
    for top_story_id in show_story_ids:
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json')
        story_data = story_response.json()
        if story_data:
            # Ensure all keys exist, provide defaults if not
            data_shows.append((
                story_data.get('id', 0),
                story_data.get('title', 'N/A'),
                story_data.get('url', 'N/A'),
                story_data.get('by', 'N/A'),
                story_data.get('score', 0),
                story_data.get('time', 0),
                story_data.get('descendants', 0)  # This is the comments count
            ))
    print(data_shows)

get_top_show_stories()
