SENTENSE = ('Привіт мене звати Гордій')
k = 0
j = 0 
s = ' '
words = []

for i in SENTENSE:
    if i == s:
        words.append(SENTENSE[k:j])
        k = j + 1
    j += 1
words.append(SENTENSE[k:j])
print (max(words, key=len))
print (words)