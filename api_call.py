import requests
import sqlite3

def get_news_articles():
    data_news = []
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    news_article_ids = response.json()[:10]  # Limit to the top 10 for demonstration purposes
    count = 0
    for article_id in news_article_ids:
        article_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{article_id}.json')
        article_data = article_response.json()
        if article_data:
            count += 1
            # Ensure all keys exist, provide defaults if not
            data_news.append((
                article_data.get('id', 0),
                article_data.get('title', 'N/A'),
                article_data.get('url', 'N/A'),
                article_data.get('by', 'N/A'),
                article_data.get('score', 0),
                article_data.get('time', 0),
                article_data.get('descendants', 0)  # This is the comments count
            ))
    print(f"Total News Articles: {count}")
    return data_news

def get_top_show_stories():
    data_shows = []
    response = requests.get('https://hacker-news.firebaseio.com/v0/showstories.json')
    show_story_ids = response.json()[:10]  # Limit to the top 10 for demonstration purposes
    count = 0
    for top_story_id in show_story_ids:
        story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json')
        story_data = story_response.json()
        if story_data:
            count += 1
            data_shows.append((
                story_data.get('id', 0),
                story_data.get('title', 'N/A'),
                story_data.get('url', 'N/A'),
                story_data.get('by', 'N/A'),
                story_data.get('score', 0),
                story_data.get('time', 0),
                story_data.get('descendants', 0)
            ))
    print(f"Total Shows: {count}")
    return data_shows

def get_job_postings():
    data_jobs = []
    response = requests.get('https://hacker-news.firebaseio.com/v0/jobstories.json')
    job_posting_ids = response.json()[:10]  # Limit to the top 10 for demonstration purposes
    count = 0
    for job_posting_id in job_posting_ids:
        job_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{job_posting_id}.json')
        job_data = job_response.json()
        if job_data:
            count += 1
            data_jobs.append((
                job_data.get('id', 0),
                job_data.get('title', 'N/A'),
                job_data.get('url', 'N/A'),
                job_data.get('by', 'N/A'),
                job_data.get('time', 0),
                job_data.get('text', 'N/A')
            ))
    print(f"Total Jobs: {count}")
    return data_jobs

def insert_data_into_db():
    conn = sqlite3.connect('hacker_news.db')
    cursor = conn.cursor()

    # Insert news articles
    news_data = get_news_articles()
    cursor.executemany('INSERT INTO NewsArticles (id, title, url, author, points, time, comments_count) VALUES (?, ?, ?, ?, ?, ?, ?)', news_data)

    # Insert show stories
    show_data = get_top_show_stories()
    cursor.executemany('INSERT INTO Shows (id, title, url, author, points, time, comments_count) VALUES (?, ?, ?, ?, ?, ?, ?)', show_data)

    # Insert job postings
    job_data = get_job_postings()
    cursor.executemany('INSERT INTO JobPostings (id, title, url, author, time, text) VALUES (?, ?, ?, ?, ?, ?)', job_data)

    conn.commit()
    conn.close()

