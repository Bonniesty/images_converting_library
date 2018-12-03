#!/usr/bin/env python
# encoding: utf-8
#Author - Tianyi Sun add to download prictures
#with database mysql and mongodb

import tweepy #https://github.com/tweepy/tweepy
import json
import urllib
import os

import pymysql
import pymongo
password = " "

#Twitter API credentials
consumer_key = " "
consumer_secret = " "
access_key = " "
access_secret = " "


def get_all_tweets(screen_name):

    #connect to mysql
    try:
        db = pymysql.connect("localhost","root", password,"db_proj");
    except Exception as e:
        print('connection error!')
        raise e

    #connect to mongodb
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mongo_proj"]
    mycol = mydb["user"]




    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=10)

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        if(len(alltweets) > 15):
            break
        print("...%s tweets downloaded so far" % (len(alltweets)))

    #write tweet objects to JSON
    file = open('tweet.json', 'w')
    print("Writing tweet objects to JSON please wait...")



    picSet = []
    for status in alltweets:
        #json.dump(status._json,file,sort_keys = True,indent = 4)
        tempData = status.entities.get('media',[])
        if(len(tempData)>0):
        	picSet.append(tempData[0]['media_url'])

    indexs = 0



    for i in picSet:
    	urllib.request.urlretrieve(i,"./pics/pic%03d.jpg"%indexs)
    	indexs=indexs+1
    	print(i+" has been downloaded!")
    picLog= "{0} imgs has been downloaded!".format(indexs)
    #if there's no images
    if len(picSet) == 0:
        print("No Pictures of this account!!!")
    #close the file
    print("Download done!")
    file.close()

    #mysql insert user info
    cursor = db.cursor()
    sql = """INSERT INTO user(twtaccount_id,log) VALUES (%s, %s)"""
    try:
        #pass
        cursor.execute(sql,(screen_name, picLog))
        db.commit()
    except:
        db.rollback()

    #mongo insert user info
    data = {'twtaccount_id':screen_name, 'log':picLog}
    mycol.insert(data)

    print("--------------------------------------------")
    print("Data stored into Database!")

    db.close()






if __name__ == '__main__':
    #pass in the username of the account you want to download

    try:
        get_all_tweets("SelenaActivity")
    except Exception:
        print("The account is invalid!!")
