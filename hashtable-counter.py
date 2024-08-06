
# Python dict has a convenient subclass Counter for counting hashable objects. When you pass an iterable object, such as a list or a string, to Counter(), it will return a new dict with elements as keys and their counts as values.

from  collections import Counter

word = "occur"
counter = Counter(word)
# counter = {'o': 1, 'c': 2, 'u': 1, 'r': 1}

print(counter['c'])    # prints out 2
print(counter['y'])    # prints out 0 for a non-existent element

# the number of unique elements in word can be obtained by the length of its counter
num_of_unique_elements = len(counter)
# num_of_unique_elements = 4