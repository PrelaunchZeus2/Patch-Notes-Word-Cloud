import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import datetime

def main():

    url = input("Enter the URL of Reddit Post:")
    create_word_cloud(url)

    
def create_word_cloud(reddit_url):
    response = requests.get(reddit_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    wordcloud = WordCloud(max_words=1000).generate(text)  # Increase max_words to 1000
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    current_date = datetime.datetime.now()
    date_string = current_date.strftime("%Y-%m-%d")
    plt.savefig(f'wordcloud_{date_string}.png')

if __name__ == '__main__':
    main()

    