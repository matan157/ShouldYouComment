#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import sys
import time
import ConfigParser

# Initialize ConfigParser
config = ConfigParser.ConfigParser()
config.read("config.ini")

# set keys
CONSUMER_KEY = config.get("consumer", "key")
CONSUMER_SECRET = config.get("consumer", "secret")
ACCESS_KEY = config.get("access", "key")
ACCESS_SECRET = config.get("access", "secret")

# Set Authentication for Tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Runes in the Background
while True:
    api.update_status("Yes. #ShouldYouComment")
    time.sleep(3600)

