# Python's dict is an implementation of a hash table. For a dictionary d = {},

# get using a key: d[key], O(1), gives KeyError if key isn't in the dictionary
# set a key, value: d[key] = value, O(1)
# remove a key: del d[key], O(1)
# size: len(d), O(1), returns the number of items in the dictionary.

# A hash table's worst time complexity is actually O(N) due to hash collision and others. For the vast majority of the cases and certainly most coding interviews, the assumption of constant time lookup/insert/delete is valid.
# Use a hash table if you want to create a mapping from A to B. Many starter interview problems can be solved with a hash table.



d = {"hello" : "world"}

print("Setting a key...")
d["foo"] = "bar"

print("Current hashtable: " + str(d))

print("The value of 'hello' is: " + str(d["hello"]))

print("Deleting 'hello' from hashtable...")
del d["hello"]

print("Result: " + str(d))

print("Length of the hashtable is now: " + str(len(d)))