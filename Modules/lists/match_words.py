#function to check wether the first and the last letter of a word are the same

def match_word(words):
    ctr = 0
    lst = []
    for word in words:
        if word[0] == word[-1]:
            lst.append(word)
            ctr += 1
            lst.append(word)
        print("list of words with same first and last letter: ", lst)
        return ctr
count = match_word(['abc', 'xyz', 'aba', '1221'])
print("Number of words with same first and last letter: ", count)