myset = {"apple", "banana", "cherry"}
print(type(myset))


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
  
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
  
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)


