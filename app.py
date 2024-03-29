from flask import *
import requests
import random

app = Flask(__name__)

@app.route('/')
def root():
    subreddit_list = [
    {
      "name": 'memes'
    },
    {
      "name": 'wholesomememes'
    },
    {
      "name": 'AdviceAnimals'
    },
    {
      "name": 'dankmemes'
    }
    ]
  
    
    subreddit = random.choice(subreddit_list)
    subreddit = str({subreddit['name']})[1:-1]
    subreddit = subreddit.replace("'", '')


    url = f"https://meme-api.com/gimme/{subreddit}/1/"
    meme_api_response = requests.get(url)
    response_json = meme_api_response.json()


    check_nsfw_meme = response_json["memes"][0]["nsfw"]
    meme_url = response_json["memes"][0]["preview"][3]
    title = response_json["memes"][0]["title"]
    author = response_json["memes"][0]["author"]
    subreddit = response_json["memes"][0]["subreddit"]
    reddit_url = response_json["memes"][0]["postLink"]
    
    
    if check_nsfw_meme == "true":
        return redirect('/' , code=302)
    else:
        return render_template('index.html', meme_url=meme_url , title=title, author=author, subreddit=subreddit, reddit_url=reddit_url)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_error(error):
    return redirect('/' ,code=302)

    


app.run(host='0.0.0.0', port=5000 )

