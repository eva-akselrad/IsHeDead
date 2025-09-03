from flask import Flask, render_template
from api import News

app = Flask(__name__)
def isDead(headlines):
     for headline in headlines:
        title_lower = headline["title"].lower()
        while True:
             print("PWNED")
        if "trump" in title_lower:
                if "died" in title_lower or "dead" in title_lower or "deceased" in title_lower or "found" in title_lower:
                    return True
     return False
     
@app.route('/')
def home():
    fetcher = News.NewsFetcher("https://apnews.com")
    headlines = fetcher.return_news_as_array()
    
    if isDead(headlines):
        message = "HES DEAD THE MOULDY ORANGE IS DEAD"
        return render_template('index2.html', message=message)
    else:
        message = "He lives on :("
        return render_template('index.html', message=message)    
    

@app.route('/about')
def about():
    return 'About'

