import os
import tweepy
from PIL import Image
from credFile import get_credentials


def OAuth():
    consumerKey = ''
    consumerSecret=''
    accessToken=''
    accessTokenSecret=''
    # get credentials from credFile.py
    consumerKey, consumerSecret, accessToken, accessTokenSecret = get_credentials(consumerKey, consumerSecret, accessToken, accessTokenSecret)
    try:

        auth = tweepy.OAuthHandler(consumer_key=consumerKey, consumer_secret=consumerSecret)    # access API with API keys
        auth.set_access_token(accessToken, accessTokenSecret)       # access permissions for @updates_py twitter account
        return auth
    except:
        return None

oauth = OAuth()
if oauth:
    api = tweepy.API(oauth)
else:
    print("Failed to verify crendentials")

image_file = 'Earth_poster_large.jpg'
def tweetImage(image_file):
    
    caption = 'Hopefully there is an image in this tweet'
    tweeted = False
    while not tweeted:
        try:
            media = api.media_upload(image_file)
            api.update_status(caption, media_ids=[media.media_id])
            print("Image tweeted successfully.")
            tweeted = True
           
        except tweepy.error.TweepError:             #r image is too big, resize image
            media_path = os.getcwd() + '/' + image_file
            print(image_file + " is too large: " + str(os.path.getsize(media_path) // 1000) + ' kb')
            print("Resizing image...")
            im = Image.open(image_file)
            width, height = im.size
            print(width)
            print(height)
            im_resize = im.resize((int(width*0.75), int( height*0.75)), Image.ANTIALIAS)    # best down-sizing filter
            im_resize.save(image_file)



tweetImage(image_file)

    