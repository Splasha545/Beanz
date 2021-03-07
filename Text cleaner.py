import re

fileInput = open("WarAndPeace.txt", encoding="utf8")
fileOutput = open("CleanWar.txt", "w")

# List of common words we dont want to consider
articulates = ["the", "and", "or", "so", "with", "because", "it", "his", "her", 
                "he", "she", "they", "but", "a", "was", "had", "on", "in", "by", 
                "to", "too", "at", "is", "of", "i", "if", "this", "what", "these",
                "then", "that", "were", "you", "has", "here", "while", "which", "by"
                "who", "how", "for", "have", "hath", "them", "not", "any", "", "o", "no"
                "be", "we", "some", "my", "an", "him", "who", "its", "pierre", "karat"]

line2 = ""
string = ""

for line in fileInput:
    line = line.lower()
    line = re.sub(r"[^a-zA-Z0-9\.]", '-', line)
    line2 += line

sentences = line2.split('.')
for sentence in sentences:
    words = sentence.split('-')
    if len(words) > 10:
        for word in words:
            word = re.sub(r"[^a-zA-Z0-9\.]", '', word)
            if len(word) <= 2 or word in articulates:
                word = ""
            if words[len(words) - 1] == word or word == "":
                fileOutput.write(word)
            else:
                fileOutput.write(word + " ")
        fileOutput.write("\n")

