import re
from collections import Counter


def word_frequency(sentence):
    words = re.findall(r"\b[\w']+\b", sentence.lower())
    return dict(Counter(words))


# Example
sentence = "Hello world! Hello Python."
print(word_frequency(sentence))
