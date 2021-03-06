#!/usr/bin/python3

'''
INSTRUCTIONS:
There are no pre-built functions and doctests for this lab.
This is to get you more experience writing entire python programs from scratch.
Step 1: Go to https://github.com/bpb27/trump_tweet_data_archive
Step 2: Download the files `condensed_*.json.zip`, where * is a year.
        There should be 10 total files (2009-2018).
        Trump has obviously sent tweets after 2018,
        but this particular archive of tweets has not been updated recently.
Step 3: Unzip each of these files to get files that look like `condensed_*.json`.
Step 4: Modify this `lab_part1.py` file so that it:
    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.
    2. Prints the total number of tweets.
    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.
       It's important to remember that each of these words can appear with many different capitalizations, 
       and your program should count the word no matter how it is capitalized.  
       For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.
    4. Prints out a count of each of these words.
My program gives the following output:
    len(tweets)= 36307
    counts= {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}
You'll know your program is correct if you get the same numbers.
'''

import glob
import json
len_tweets = []
# we need both the json and an index number so use enumerate()
files = glob.glob('trump_tweets/*')
for file in files:
    with open(file, 'r', encoding = 'ASCII') as d:
        tweets = d.read()
        len_tweets += json.loads(tweets)

num_obama = 0
num_mexico = 0
num_fake_news= 0
num_russia = 0
num_trump = 0
num_radical_left = 0
num_chicago = 0
num_china = 0
for tweet in len_tweets:
    lower_tweets = tweet['text'].lower()
    if lower_tweets.find('trump') != -1:
        num_trump += 1
    if lower_tweets.find('mexico') != -1:
        num_mexico += 1
    if lower_tweets.find('fake news') != -1:
        num_fake_news += 1
    if lower_tweets.find('obama') != -1:
        num_obama += 1
    if lower_tweets.find('china') != -1:
        num_china += 1
    if lower_tweets.find('radical left') != -1:
        num_radical_left += 1
    if lower_tweets.find('chicago') != -1:
        num_chicago += 1
    if lower_tweets.find('russia') != -1:
        num_russia += 1
percentage_obama = str(round((num_obama / len(len_tweets) * 100), 2))
percentage_obama_4d = percentage_obama.zfill(5)
percentage_trump = str(round((num_trump / len(len_tweets) * 100), 2))
percentage_trump_4d = percentage_trump.zfill(5)
percentage_mexico = str(round((num_mexico / len(len_tweets) * 100), 2))
percentage_mexico_4d = percentage_mexico.zfill(5)
percentage_russia = str(round((num_russia / len(len_tweets) * 100), 2))
percentage_russia_4d = percentage_russia.zfill(5)
percentage_fake_news = str(round((num_fake_news / len(len_tweets) * 100),2))
percentage_fake_news_4d = percentage_fake_news.zfill(5)
percentage_radical_left = str(round((num_radical_left / len(len_tweets) * 100), 2))
percentage_radical_left_4d = percentage_radical_left.zfill(5)
percentage_china = str(round((num_china / len(len_tweets) * 100), 2))
percentage_china_4d = percentage_china.zfill(5)
percentage_chicago = str(round((num_chicago / len(len_tweets) * 100), 2))
percentage_chicago_4d = percentage_chicago.zfill(5)
dis = "\tPercentage of tweets using word: \n\t       Obama {8} {0} \n\t       Trump {8} {1} \n\t      Mexico {8} {2} \n\t      Russia {8} {3} \n\t   Fake News {8} {4} \n\tRadical Left {8} {5} \n\t       China {8} {6} \n\t     Chicago {8} {7}".format(percentage_obama_4d, percentage_trump_4d,percentage_mexico_4d, percentage_russia_4d, percentage_fake_news_4d, percentage_radical_left_4d, percentage_china_4d, percentage_chicago_4d, ':','Obama', 'Trump', 'Mexico', 'Russia', 'Fake News', 'Radical Left', 'China', 'Chicago')
print('len(tweets)=',len(len_tweets))
print('counts= {''\'trump\': ', num_trump,', ' '\'russia\': ', num_russia,', ' '\'obama\': ', num_obama,', ' '\'fake news\': ', num_fake_news,', ' '\'mexico\': ', num_mexico,'}', sep='')

print(dis)


'''
========================================
EXTRA CREDIT:
You may earn 2 points of extra credit on this lab if you also:
    1. select at least 3 more interesting words/phrases to count in trump's tweets,
    2. calculate the percentage of tweets that contain each word, and
    3. display them nicely.
The display must have all words right justified and the percents printed with two 
significant figures (on both sides of the decimal) as shown in the example output below.
For example:
    percentage of tweets using phrase:
                  daca : 00.17
             fake news : 00.92
      mainstream media : 00.06
                mexico : 00.55
                 obama : 07.47
                russia : 01.13
                 trump : 38.35
                  wall : 00.91
HINT:
There are many ways to achieve this effect in python,
but I recommend using the .format string function.
Your python cheat sheet has instructions.
========================================
Submission
Upload your completed `lab_part1.py` file to sakai,
and copy and paste the output of running your program into sakai.
'''