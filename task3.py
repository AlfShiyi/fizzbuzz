from string import *
books = ["Book1.txt","Book2.txt","Book3.txt"]
wordsbook = "20k.txt"
fr = open(wordsbook)
wordlst = list()
bookwords = list()
for line in fr:
        words = line.split()
        for word in words:
                word = word.strip(punctuation+whitespace)
                wordlst.append(word)
fr.close()
for i in books:
    bookwords.append(list())
    templst = bookwords[-1]
    fr = open(i)
    for line in fr:
        words = line.split()
        for word in words:
                word = word.strip(punctuation+whitespace)
                templst.append(word)
for i in range(len(books)):
    wset = set(wordlst)
    bset = set(bookwords[i])
    bset.difference_update(wset)
    fw = open(f"book{str(i+1)}uniqu.list","wt")
    for word in bset:
        fw.writelines(word+"\n")
    fw.close()

wset = set(wordlst)
for blst in bookwords:
    bset = set(blst)
    wset.difference_update(bset)
fw = open("rareword.list","wt")
for w in wset:
    fw.writelines(w+"\n")
fw.close()
