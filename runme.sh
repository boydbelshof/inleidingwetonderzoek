#!/bin/bash
# A program that opens the corpus files from 1 march 2017 12 o'clock. It read the numbers of tweet, unique tweets, the retweets and it prints the first 20 tweets
#Run this file for sample data
zless /net/corpora/twitter2/Tweets/2017/03/201703*.out.gz | /net/corpora/twitter2/tools/tweet2tab user.location text | sort -u | python code.py

