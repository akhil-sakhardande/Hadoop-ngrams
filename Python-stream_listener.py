# Importing the necessary libraries
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
from pymongo import MongoClient
import json

# Authorization variables
ckey = 'aOJM1Ez1vmhlVPX3ihzPBa5WQ'
consumer_secret = 'ZtapCJfAGyRB2AT3K0u94IHcVvqymBG80bV2PxSh07tPEHP30c'
access_token_key = '55590423-utuGkNI3cqRVI39GlAXy2DtT84Dnp1dUfIIySoqBI'
access_token_secret = 'p8jDr8RLaOMFa6cDwP89OzCiE07DaAwQvcnpCn2lGZA79'

# Keywords to fetch data
start_time = time.time() #grabs the system time
keyword_list = ['IPL'] #track list

class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
 
		self.time = start_time
		self.limit = time_limit
 
	def on_data(self, data):
 
		while (time.time() - self.time) < self.limit:
 
			try:
 
		# Saving to a local directory	
				#saveFile = open('raw_tweets.json', 'a')
				#saveFile.write(data)
				#saveFile.write('\n')
				#saveFile.close()
				
				#return True
				
		# Storing the data directly in MongoDB	
				client = MongoClient('localhost', 27017)
				db = client['twitter_db']
				collection = db['twitter_collection']
				tweet = json.loads(data)

				collection.insert(tweet)

				return True
 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
 
		exit()
 
	def on_error(self, status):
 
		print statuses

auth = OAuthHandler(ckey, consumer_secret) #OAuth object
auth.set_access_token(access_token_key, access_token_secret)
 
twitterStream = Stream(auth, listener(start_time, time_limit=500000)) #initialize Stream object with a time out limit
twitterStream.filter(track=keyword_list, languages=['en'])  #call the filter method
