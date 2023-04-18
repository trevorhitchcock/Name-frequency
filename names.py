# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 20:17:02 2023

Trevor Hitchcock
Programming Languages Lab 4
names.py
This program uses a names dataset that allows the user to search a name and see the name's
most popular year, the name's publicity over time, and the top 10 names of a decade.
"""

def main():
    # load in text file
    file = open("names-data.txt","r")
    
    # stores it in dictionary
    # dict key is str name
    # dict value list frequency
    # index 0 of list corresponds to 1910, 1 to 1920, ... , 11 to 2010
    names_dict = {}
    for line in file:
        split = line.split()
        if(len(split) > 1): # the first 2 lines of the file are weird so I needed this condition
            name = split.pop(0)
            names_dict.update({name:split})
    file.close()
    
    # enter menu
    print("\nWelcome to the name game!")
    menu(names_dict)

def search(names_dict):
    name_to_search = input("\nEnter the name you would like to search: ")
    capital_name_to_search = name_to_search.capitalize() # only first letter of name in data can be capital
    match = False
    for key in names_dict:
        if(key.__contains__(name_to_search))or(key.__contains__(capital_name_to_search)): # match
            match = True
            # change 0s in dict to 1001 so min function finds most popular year
            pop_array = names_dict[key]
            for i in range(len(pop_array)):
                if(pop_array[i] == '0'):
                    pop_array[i] = 1001
                    
            int_pop_array = [int(ele) for ele in pop_array] # converts strings in list to int so min function works
            
            min_value = min(int_pop_array)
            index = int_pop_array.index(min_value) # index of most popular year for the name
            
            year = -1 # for error purposes
            
            # assigns the year for printing
            if(index == 0):
                year = 1900
            elif(index == 1):
                year = 1910
            elif(index == 2):
                year = 1920
            elif(index == 3):
                year = 1930
            elif(index == 4):
                year = 1940
            elif(index == 5):
                year = 1950
            elif(index == 6):
                year = 1960
            elif(index == 7):
                year = 1970
            elif(index == 8):
                year = 1980
            elif(index == 9):
                year = 1990
            elif(index == 10):
                year = 2000
            elif(index == 11):
                year = 2010                
            
            print("The name "+key+" was most popular in the year "+str(year))
            
            for i in range(len(pop_array)):
                if(pop_array[i] == 1001):
                    pop_array[i] = 0
    if(match == False):
        print("\nThat name wasn't found.")
    menu(names_dict)

def popularity(names_dict):
    name_to_search = input("\nEnter the name you would like to search: ")
    match = False
    for key in names_dict:
        if(key == name_to_search): # match
            match = True
            print("Publicity is ranked out top 1000 names. If 0, the name did not appear on the list.")
            print("Publicity: " + str(names_dict[key][0]) + " Year: 1900")
            print("Publicity: " + str(names_dict[key][1]) + " Year: 1910")
            print("Publicity: " + str(names_dict[key][2]) + " Year: 1920")
            print("Publicity: " + str(names_dict[key][3]) + " Year: 1930")
            print("Publicity: " + str(names_dict[key][4]) + " Year: 1940")
            print("Publicity: " + str(names_dict[key][5]) + " Year: 1950")
            print("Publicity: " + str(names_dict[key][6]) + " Year: 1960")
            print("Publicity: " + str(names_dict[key][7]) + " Year: 1970")
            print("Publicity: " + str(names_dict[key][8]) + " Year: 1980")
            print("Publicity: " + str(names_dict[key][9]) + " Year: 1990")
            print("Publicity: " + str(names_dict[key][10]) + " Year: 2000")
            print("Publicity: " + str(names_dict[key][11]) + " Year: 2010")
    if(match == False):
        print("\nThat name wasn't found.")
    menu(names_dict)
    
def top_ten(names_dict):
    try:
        year = int(input("\nEnter the year you would like to see the most popular names for: "))
        if(year > 2010)or(year < 1900)or(year%10 != 0): # invalid input
            print("Enter a year that ends in 0 between 1900 and 2010")
            top_ten(names_dict)
        else: # valid input
            print("\nMost popular names for the year "+str(year) + " are..")
            if(year == 1900):
                index = 0
            elif(year == 1910):
                index = 1
            elif(year == 1920):
                index = 2
            elif(year == 1930):
                index = 3
            elif(year == 1940):
                index = 4
            elif(year == 1950):
                index = 5
            elif(year == 1960):
                index = 6
            elif(year == 1970):
                index = 7
            elif(year == 1980):
                index = 8
            elif(year == 1990):
                index = 9
            elif(year == 2000):
                index = 10
            elif(year == 2010):
                index = 11
            
            look = 1 # the index to be looked for
            i =0
            
            while(i < len(names_dict.keys()))and(look != 11):
                
                key = list(names_dict.keys())[i]
                value = names_dict[key]
            
                if(int(value[index]) == look):# name at publicity look was found
                    print(str(look)+". "+ key)
                    look +=1
                    i = 0 # reset loop
                else:
                    i += 1 # increment loop variable
        menu(names_dict)     
    except ValueError:
        print("Enter an integer")
        top_ten(names_dict)
    
def menu(names_dict):
    print("\nEnter what you would like to do:")
    print("1. Search")
    print("2. Popularity over time")
    print("3. Top ten")
    print("4. Quit")
    
    try:
        choice = int(input("Enter a number: "))
        if(choice == 1):
            search(names_dict)
        elif(choice == 2):
            popularity(names_dict)
        elif(choice == 3):
            top_ten(names_dict)
        elif(choice == 4):
            print("Quitting the program")
        else:
            print("Enter a valid integer")
            menu(names_dict)
    except ValueError:
        print("Enter an integer")
        menu(names_dict)

main()