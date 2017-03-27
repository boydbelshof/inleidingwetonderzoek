from __future__ import division
import sys
import copy
import operator

# Name: Boyd Belshof
# Student: S3012158
# Date: 18-03-17
# Description: This program checks in which place in the Netherlands the most swearing words
# are used. The program consists out of 3 files, the code.py, the plaatsnamen.txt and schelwoorden.txt.
# The scheldwoorden and plaatsnamen contains the swearing words and places so that there are can
# easily be added more swearing words and places to it. The program used input data from Twitter.

def check_for_province(lines, active):
    """The helper for places_to_province, this function checks in which province the
    places should be."""
    if lines == "Overijssel":
        return 1
    elif lines == "Drenthe":
        return 2
    elif lines == "Flevoland":
        return 3
    elif lines == "Utrecht":
        return 4
    elif lines == "Groningen":
        return 5
    elif lines == "Friesland":
        return 6
    elif lines == "Zuid Holland":
        return 7
    elif lines == "Gelderland":
        return 8
    elif lines == "Noord Holland":
        return 9
    elif lines == "Zeeland":
        return 10
    elif lines == "Limburg":
        return 11
    elif lines == "Noord Brabant":
        return 12
    else:
        return active

def places_to_province():
    """Places the right place in the right province, so at the end there is a
    possibility to check in which place the most people tweet."""
    #The list that is returned with al the provinces in it.
    province_list = []
    #Opens  the plaatsnamen.txt file
    f = open("plaatsnamen.txt", "r")
    #This are all the dictionaries containing the places.
    active_province = 1
    overijssel = {}
    drenthe = {}
    flevoland = {}
    utrecht = {}
    groningen = {}
    friesland = {}
    zuidholland = {}
    gelderland = {}
    noordholland = {}
    zeeland = {}
    limburg = {}
    noordbrabant = {}
    total = {}
    #Iterates over all the lines in the input file.
    for lines in f:
        #Strips all the non needed Enters in the file.
        new_line = lines.rstrip()
        #Checks for the province
        active_province = check_for_province(new_line, active_province)
        #Makes all the words lowercase and removes the '-' so that it could be easier found.
        new_line2 = new_line.lower()
        new_line3 = new_line2.replace('-', ' ')
        lower_line = new_line3.rstrip()
        if active_province == 1:
            overijssel[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 2:
            drenthe[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 3:
            flevoland[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 4:
            utrecht[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 5:
            groningen[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 6:
            friesland[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 7:
            zuidholland[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 8:
            gelderland[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 9:
            noordholland[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 10:
            zeeland[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 11:
            limburg[lower_line] = 0
            total[lower_line] = 0
        elif active_province == 12:
            noordbrabant[lower_line] = 0
            total[lower_line] = 0
    province_list = [overijssel, drenthe, flevoland, utrecht, groningen, friesland, zuidholland, gelderland, noordholland, zeeland, limburg, noordbrabant, total]
    return province_list

def total_to_province(total_dict, province_dict):
    """Gets the Dictionary with all the places in it and then places it in the right province."""
    for place in total_dict:
        for province2 in province_dict:
            if place in province2:
                province2[place] = total_dict[place]
    return province_dict;

def get_swear_words():
    """Opens the schelwoorden.txt file and places this in a string. Then returns
    it so it can be used later on."""
    swear_words = []
    f = open("scheldwoorden.txt", "r")
    for line in f:
        new_line = line.strip()
        swear_words += new_line
    return swear_words

def main():
    """The main function, this is where all the help functions are runned and the checks for
    swear words and there location. """
    #Gets the swear words
    swear_words = get_swear_words()
    #Gets the provinces
    province_list = places_to_province()
    #Duplicates the list for later percentage check.
    province_list_counter = copy.deepcopy(province_list)
    for line in sys.stdin:
        #Splits the input
        two_parts = line.split("\t")
        #Seperates the text part
        text = two_parts[1]
        #SEperates the location part
        location = two_parts[0]
        #Lowers the location and replaces puncuation with a space.
        stripped_location = location.lower()
        stripped_location.replace(",.!-?/", " ")
        stripped_text = text.lower()
        #Creates a word and location list for iteration.
        splitted_words = stripped_text.split(" ")
        splitted_location = stripped_location.split(" ")
        #Check if the location is in the location list
        for location in splitted_location:
            if location in province_list[12]:
                province_list_counter[12][location] += 1
        #Check for swearing words in the text
        for word in splitted_words:
            if word in swear_words:
                for location in splitted_location:
                    if location in province_list[12]:
                        #Counts the swearing words on their location
                        province_list[12][location] += 1
                        break
    #Removes unwanted spaces
    for dict in province_list:
        if "" in dict:
            dict.pop("")
    #Seperates all the provinces
    new_dict = total_to_province(province_list[12], province_list)
    #Sorts the data so the biggest cities can be easliy found (this is for printing purposes)
    sorted_total = sorted(province_list[12].items(), key=operator.itemgetter(1))
    for keys,values in sorted_total:
        if values is not 0:
            #Prints all the data if the value in the dictionary is not 0
            print(keys + ":\t" + str(values) + '\t'+ str(province_list_counter[12][keys]) + "\t "+ str((values / province_list_counter[12][keys]) * 100) + "%")
    #The total counters so at the end we can see what the average swearing percentage is
    total_total_counter = 0
    total_total_swear_counter = 0
    dict_counter = 0
    #This loop prints the right statistics per Province
    for dict in new_dict:
        dict_counter += 1
        #Removes the total dict
        if dict_counter == 13:
            break
        #The counter for each province
        total_swear_counter = 0
        total_counter = 0
        #The for loop for each province
        for keys in dict:
                total_counter += dict[keys]
                total_swear_counter += province_list_counter[12][keys]

        #Prints the right province for the data
        if "overijssel" in dict:
            print("Overijssel:\t")
        elif "utrecht" in dict:
            print("Utrecht:\t")
        elif "drenthe" in dict:
            print("Drenthe:\t")
        elif "noord holland" in dict:
            print("Noord Holland:\t")
        elif "zuid holland" in dict:
            print("Zuid Holland:\t")
        elif "groningen" in dict:
            print("Groningen:\t")
        elif "noord brabant" in dict:
            print("Noord Brabant:\t")
        elif "limburg" in dict:
            print("Limburg:\t")
        elif "friesland" in dict:
            print("Friesland:\t")
        elif "zeeland" in dict:
            print("Zeeland:\t")
        elif "flevoland" in dict:
            print("Flevoland:\t")
        elif "gelderland" in dict:
            print("Gelderland:\t")

        #Prints the swearing words, the total tweets and the percentage
        print(str(total_swear_counter) + "\t" + str(total_counter) + "\t" + str((total_counter / total_swear_counter) * 100) + "%")

        #This is for the final report to check for the average of all the tweets
        total_total_counter += total_counter
        total_total_swear_counter += total_swear_counter

main()


