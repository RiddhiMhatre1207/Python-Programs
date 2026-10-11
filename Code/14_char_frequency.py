
def count_frequency(text):
    frequency = {}

    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    return frequency

print(count_frequency("hello"))
