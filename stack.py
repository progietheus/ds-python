
# Python's list also doubles as a stack. For a list l = []

# push: append, O(1)
# pop: pop,O(1)
# size: len(l), O(1)
# top: l[-1], O(1)

l = []

l.append(2);
l.append(3);
l.append(1);

l.pop(1)

print("Values are: " + str(l))
print("The length is: " + str(len(l)))
print("The top value is: " + str(l[-1]))



