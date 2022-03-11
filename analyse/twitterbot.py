import tweepy
from . import settings


class TwitterBot:
    """
    A simple class that abstracts away boilerplate code for accessing twitter API and makes life easier
    """

    def __init__(self):
        """
        Create a .env file in the root directory and fill in these values in the same
        """
        self.consumerKey = settings.API_KEY
        self.consumerSecret = settings.API_KEY_SECRET
        self.accessToken = settings.ACCESS_TOKEN
        self.accessTokenSecret = settings.ACCESS_TOKEN_SECRET
        self.__authenticated = False

    def authenticate(self):
        """
        Authenticates the instance
        """
        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken, self.accessTokenSecret)
        self.api = tweepy.API(auth)
        self.__authenticated = True

    def isAuthenticated(self):
        """
        Checks whether the bot is authenticated.

        Returns:
            A boolean value that signifies the authentication status
        """
        return self.__authenticated

    def getTweetsByUser(self, userID):
        """
        Gets all the tweets in the timeline of a user by their user ID

        Args:
            userID (string): A string which is the Twitter user ID

        Returns:
            tweets (list): A list of strings containing the tweets of the given user
        """
        tweets = self.api.user_timeline(
            screen_name=userID, count=10, include_rts=False, tweet_mode="extended"
        )
        return tweets
