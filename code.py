from __future__ import division
import sys

# Name: Boyd Belshof
# Student: S3012158
# Date: 18-03-17
# Description: This program checks which gender uses the most swearing words on twitter.
# The program consists out of 4 files, the code.py, the vrouwen_namen.txt, the mannen_namen.txt and scheldwoorden.txt.
# The scheldwoorden and namenfiles contains the swearing words and names so that there are can
# easily be added more swearing words and names to it. The program used input data from Twitter.

def get_swear_words():
    """Opens the schelwoorden.txt file and places this in a string. Then returns
    it so it can be used later on."""
    swear_words = []
    f = open("scheldwoorden.txt", "r")
    for line in f:
        stripped_line = line.strip()
        swear_words.append(stripped_line)
    return swear_words

def get_man_names():
    man_names = {}
    f = open("mannen_namen.txt", "r")
    for line in f:
        new_line = line.strip()
        new_line_lower = new_line.lower()
        man_names[new_line_lower] = 0
    return man_names

def get_woman_names():
    woman_names = {}
    f = open("vrouwen_namen.txt", "r")
    for line in f:
        new_line = line.strip()
        new_line_lower = new_line.lower()
        woman_names[new_line_lower] = 0
    return woman_names


def main():
    """The main function, this is where all the help functions are runned and the checks for
    swear words and there location. """
    #Gets the swear words
    swear_words = get_swear_words()
    #The counter for all the tweets that the program has checked
    total_tweets = 0
    #Gets the mens names
    man_names = get_man_names()
    # Gets the womens names
    woman_names = get_woman_names()
    #The counter for all the tweets send by men
    man_names_counter = 0
    #The counter for all the tweets send by women
    woman_names_counter = 0
    #The counter for all the tweets send by men that contain swearwords
    man_names_swear_counter = 0
    #The counter for all the tweets send by women that contain swearwords
    woman_names_swear_counter = 0
    #The Dictionary to check which swear words are used the most
    woman_swear_words = {}
    #The Dictionary to check which swear words are used the most.
    man_swear_words = {}
    for line in sys.stdin:
        total_tweets += 1
        #Splits the input
        two_parts = line.split("\t")
        #Seperates the text part
        text = two_parts[1]
        #SEperates the names part
        name = two_parts[0]
        #Lowers the name and replaces punctuation with a space.
        stripped_name = name.lower()
        stripped_name.replace(",.!-?/", " ")
        stripped_text = text.lower()
        #Creates a word and name list for iteration.
        splitted_words = stripped_text.split(" ")
        splitted_name = stripped_name.split(" ")
        #Check if the name is in the name list
        for name in splitted_name:
            if name in man_names:
                man_names_counter += 1
            elif name in woman_names:
                woman_names_counter += 1

        #Check for swearing words in the text
        for word in splitted_words:
            #Checks if the tweet is a retweet. If it is, the tweet is skipped
            if word == "RT":
                print(line)
                print('removed')
                break;
            elif word in swear_words:
                for name in splitted_name:
                    if name in man_names:
                        if word in man_swear_words:
                            man_swear_words[word] += 1
                        else:
                            man_swear_words[word] = 1
                        man_names[name] += 1
                        man_names_swear_counter += 1
                    elif name in woman_names:
                        if word in woman_swear_words:
                            woman_swear_words[word] += 1
                        else:
                            woman_swear_words[word] = 1
                        woman_names[name] += 1
                        woman_names_swear_counter += 1


    #The printing function.
    print(sorted(woman_swear_words.items(), key=lambda x: x[1]))
    print(sorted(man_swear_words.items(), key=lambda x: x[1]))
    print(total_tweets)
    print(woman_names_counter, "\n", woman_names_swear_counter)
    print(man_names_counter, "\n", man_names_swear_counter)


main()


