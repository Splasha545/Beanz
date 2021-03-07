from bs4 import BeautifulSoup

soup = BeautifulSoup(open("War and Peace, by Leo Tolstoy.html", encoding="utf8"), features="lxml")

links = soup.find_all('p')

file1 = open("WarAndPeace.txt", "w", encoding="utf8")

for link in links:
    string = link.text
    file1.write(string)