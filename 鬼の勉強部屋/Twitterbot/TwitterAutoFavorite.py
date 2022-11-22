import tweepy

"""認証準備"""
APIkye = "H5laHIA3RwHMA5JfHW2nh9BwC"
APIkyeSecret = "BayKiU8UVb364eSWp0PMS9hd8SgZ7kbp3bnpnLbB9OHSLdXRCB"
AccessToken = "1144240754442637312-kegAORVDbnMn9g2sKYrJNlYQxokAwh"
AccessTokenSecret = "QpIJg45hBXzrlGG5U4MY7wd0SSUjRAsiH6bpLo1J7P7Sq"

auth = tweepy.OAuthHandler(APIkye,APIkyeSecret)
auth.set_access_token(AccessToken,AccessTokenSecret)

api = tweepy.API(auth)
"""認証準備"""

keyword = "メンズエステ"

objects = api.search_tweets(q="keyword",result_type="recent",count=5)
# print(object)

for object in objects:
    
    try:
        favoriteId =object.id
        api.create_favorite(favoriteId)
        
    
    except tweepy.error.tweepError as e:  # type: ignore
        print(e)



