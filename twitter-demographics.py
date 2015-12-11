import tweepy

## API keys look like:

consumer_key = 'aOJM1Ez1vmhlVPX3ihzPBa5WQ'
consumer_secret = 'ZtapCJfAGyRB2AT3K0u94IHcVvqymBG80bV2PxSh07tPEHP30c'
access_token = '55590423-utuGkNI3cqRVI39GlAXy2DtT84Dnp1dUfIIySoqBI'
access_token_secret = 'p8jDr8RLaOMFa6cDwP89OzCiE07DaAwQvcnpCn2lGZA79'

## Define user name
user='@hopeforbliss'

## Defining extract_twitter_data function which extracts data of twitter user
def extract_twitter_data(user):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    ## Call the API and get data from twitter user
    api = tweepy.API(auth)
    twitterData = api.get_user(user)

    ## Print data
    print 'Twitter user: ' + user
    print 'Number of followers: ' + str(twitterData.followers_count)
    print 'Number of tweets: ' + str(twitterData.statuses_count)
    print 'Favorites: ' + str(twitterData.favourites_count)
    print 'Friends: ' + str(twitterData.friends_count)
    print 'Appears on ' + str(twitterData.listed_count) + ' lists'

## Call function: extract_twitter_data
extract_twitter_data(user)
