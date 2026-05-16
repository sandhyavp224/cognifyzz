file  = open("sample.txt" , "r")
text = file.read()
text = text.lower()
text = text.replace("," , "")
text = text.replace("." , "")
text = text.replace("!" , "")
text = text.replace("?" , "")
words = text.split()
word_occurences = {}
for word in words:
    if word in word_occurences:
        word_occurences[word] += 1
    else:
        word_occurences[word] = 1

for word , count in word_occurences.items():
    print(word , ":"  , count)
    