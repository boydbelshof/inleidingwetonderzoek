#!/bin/bash
# A program that opens the corpus files.
echo "Number of tweets in the file:"
 zless /net/corpora/twitter2/Tweets/2017/03/20170301\:12.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | wc -l
echo "Unique tweets in the file:"
zless /net/corpora/twitter2/Tweets/2017/03/20170301\:12.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | sort -u |wc -l
echo "Number of retweets:"
zless /net/corpora/twitter2/Tweets/2017/03/20170301\:12.out.gz  | /net/corpora/twitter2/tools/tweet2tab rt.id | sort -u |wc -l
echo "The first 20 tweets":
zless /net/corpora/twitter2/Tweets/2017/03/20170301\:12.out.gz  | /net/corpora/twitter2/tools/tweet2tab text | sort -u | head -20
