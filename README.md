# Word Connections

This program uses a Markov Chain to find relation between words in the literary piece "War and Peace" by Tolstoy.
It allows the user to search for the top 10 most related words to the entered words.
It also creates a text file holding the top 5 related words to every word in the book.

The "War and Peace, by Leo Tolstoy" file is the raw HTML file of the book which we then converted into the cleaner "WarAndPeace" file. The "CleanWar.txt" file is the file we got after cleaning it with the "Text Cleaner.py". And "WordConnections.txt" is the dictionary made by "Word Connections.py".

beautifulSoup is a python program to extract the text of the book from the raw HTML of the book.

Text Cleaner is a python program which converts the text of the book into data which we can feed to the main program.

Word Connections is the main pythong program which creates the dictionary of associated words.
