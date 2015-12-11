import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'aOJM1Ez1vmhlVPX3ihzPBa5WQ'
consumer_secret = 'ZtapCJfAGyRB2AT3K0u94IHcVvqymBG80bV2PxSh07tPEHP30c'
access_token = '55590423-utuGkNI3cqRVI39GlAXy2DtT84Dnp1dUfIIySoqBI'
access_token_secret = 'p8jDr8RLaOMFa6cDwP89OzCiE07DaAwQvcnpCn2lGZA79'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status(status='Next two-three weeks are gonna be hectic. #Exams #AgigatedSchedule #TweetedusingPython')
print "Posted."
