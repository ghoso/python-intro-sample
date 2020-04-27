#  word_count.py
#

def word_count(words):
    wnum = 0
    word_list = words.split(' ')
    for word in word_list:
        wnum += 1

    return wnum

#main
s = "This is my first Python program."
word_num = word_count(s)
print("単語数は", word_num)