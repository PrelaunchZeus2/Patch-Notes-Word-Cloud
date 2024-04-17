import requests
import praw
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import datetime
import os

#Reddit Api Cridentials
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = os.getenv('REDDIT_USER_AGENT')

def main():
    testurl = 'https://www.reddit.com/r/leagueoflegends/comments/1c5mymo/patch_148_notes/'
    url = input("Enter the URL of Reddit Post:")
    redditpage = praw.Reddit(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, user_agent=USER_AGENT)
    submission = redditpage.submission(url=url)

    comments = []
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments.append(comment.body)
    
    text = ' '.join(comments)
    wordclout = WordCloud(max_words=1000).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    current_date = datetime.tatetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    plt.savefig(f'wordcloud_{date_string}.png')

    

    


if __name__ == '__main__':
    main()

    