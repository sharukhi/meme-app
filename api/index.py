from flask import *
from init import *
import requests
import json 


app = Flask(__name__)

@app.route('/')
def root():


    url = "https://meme-api.com/gimme/1/"
    meme_api_response = requests.get(url)
    response_json = meme_api_response.json()


    check_nsfw_meme = response_json["memes"][0]["nsfw"]
    meme_url = response_json["memes"][0]["preview"][3]
    title = response_json["memes"][0]["title"]
    author = response_json["memes"][0]["author"]
    subreddit = response_json["memes"][0]["subreddit"]
    
    
    if check_nsfw_meme == "false":
        return redirect('/' , code=302)
    else:
        return render_template('index.html', meme_url=meme_url , title=title, author=author, subreddit=subreddit)
    

    


app.run(debug=True)

