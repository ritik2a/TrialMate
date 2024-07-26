import tweepy
import json
# from textblob import TextBlob
access_token = "1462461291319087104-ciVLbaC1fOF6ojBzY0KfqhhdFfaXYB"
access_token_secret = "u84vXennP14Q5oZ786QRnaWAgJH95Bn4zTWdxgUYHVARE"
consumer_key ="yUreKpcY6PIxfNAcuuHZjzsbf" 
consumer_secret = "7bEmEEh3IZjh0V9vL8XGGSx465B2i2yyxKaHiGggHbw2Qiz2ay"
auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def _init_(self,api=None):
        super(MyStreamListener,self)._init_()
        self.num_tweets=0
        self.file=open("tweets.txt","w")
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<100:
            return True
        else:
            return False
        self.file.close()
    

##convert into csv file 

#create streaming object and authenticate
l = MyStreamListener()
stream = tweepy.Stream(auth,l)
#this line filters twiiter streams to capture data by keywords
stream.filter(track=['covid','corona','covid19','coronavirus','facemask','sanitizer','social-distancing'],languages=['en'])
print("Done extracting tweets.")