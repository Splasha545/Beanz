import random

import numpy as py

# dictionary holding every word, in a {word : options} pair where options is a dictionary holding {word : integer} pairs
word_connections = {}

# Decide which book the data is taken from
input1 = input()

if input1 == "Hamlet":
    file = open("HamletClean.txt")

if input1 == "War and Peace":
    file = open("cleanWar.txt", "r")


# Creating the word connections
def update_word_connections( current: str, nextWord: str):
    # if the current word is not in the dictionary yet
    if current not in word_connections:
        word_connections.update({current: {nextWord: 1}})

    options = word_connections[current]

    # if the current word does not hold next word in its options yet
    if nextWord not in options:
        options.update({nextWord: 1})
    # otherwise increase probability for that word - so increase what it already is by 1
    else:
        options.update({nextWord : options[nextWord] + 1})


# reading the data
for line in file:
    words = line.split(' ')
    while (words[len(words) - 1] == " "):
        words = words[:-1]
    # taking every word from each sentence
    for currentWordIndex in range(len(words)):
        for i in range(len(words)):
            if i != currentWordIndex:
                update_word_connections(words[currentWordIndex], words[i])   

# the word the user wishes to look up
searchString = input()

if searchString not in word_connections:
    print('Word not found')
else:
    secondary_dictionary = word_connections.copy()

    options2 = secondary_dictionary[searchString]

    n = 10 # variable for how many words to show

    top10 = {}  
    # Creating the top10 dictionary holding the top 10 most common words and their weights
    while n > 0 and len(options2.items()) != 0:
        maximum = max(options2, key=options2.get)
        if maximum == '\n':
            del options2[maximum]
        else:
            top10.update({maximum : options2[maximum]})
            del options2[maximum]
        n = n - 1
    print(top10)


# This part of the program creates a top5 list for every word in the book to make a dictionary and exports that to a txt file
fileOutput = open("Connections.txt", "w")
    
top5 = {}
for currentWord in word_connections:
    options = word_connections[currentWord]
    if currentWord.endswith("\n"):
        currentWord = currentWord[:-1]
    fileOutput.write(currentWord + ": ")
    top5 = sorted(options, key=options.get, reverse=True)
    for i in range(len(top5) - 1):
        if top5[i] == "\n" or top5[i] == " ":
            del top5[i]

    rangee = min(5, len(top5))
    for i in range(rangee):
        fileOutput.write(top5[i] + " ")
    fileOutput.write("\n")
   








