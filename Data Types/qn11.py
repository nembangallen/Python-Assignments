"""
11. Write a Python program to count the occurrences of each word in a given
sentence.
"""
def word_count(sentence):
    word_counts = dict()
    words = sentence.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

print(word_count('Love the way you love you'))
