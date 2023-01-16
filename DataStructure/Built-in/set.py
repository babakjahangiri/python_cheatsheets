import time

myset = {"apple", "banana", "cherry"}

set_from_list = set([1, 2, 3, 4])
print(set_from_list)


word1 = "abbcccdddddeeefffdddd"

set1 = set(word1)
#return unique characters
for i in set1:
    print(i)

new_list1 = list(set1)
new_list1 = sorted(list((x.upper() for x in new_list1)),reverse=False)
print(new_list1)
 

set_names = {'Smith', 'Babak', 'Rose', 'Ali'}

print(len(set_names)) # 4



find_smith = True if 'smith' in set_names else False
print(find_smith) # False



for i,value in enumerate(set_names):
    if value.upper() == 'SMITH' :
        print('yaahhhh, I found Smith in the list')
else:
    print('Smith not found')


# use the set constructor 
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # {'cherry', 'apple', 'banana'}

#Once a set is created, you cannot change its items, but you can add new items

print("banana" in thisset) # True


thisset.add("orange")

print('-------------------')

#merge two set 
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) # {'mango', 'cherry', 'pineapple', 'orange', 'papaya', 'banana', 'apple'}


thisset1 = {"Bijan", "Sohiel", "Meherdad"}
mylist1 = ["nazi", "sepideh"]

thisset1.update(mylist1) 

print(thisset1) # {'sohiel', 'bijan', 'sepideh', 'meherdad', 'nazi'}

thisset1.remove("Meherdad")
print(thisset1) # {'sepideh', 'nazi', 'sohiel', 'bijan'}
thisset1.add("Hamid")
print(thisset1)
random_person = thisset1.pop()
print(random_person) # Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

set_m = {"m1", "m2", "m3","m4"}
set_m.clear()
print(set_m) # set()

print('--------MMMMMMMMM-----------')
for x in thisset1:
  print(x)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

# The union() method returns a new set with all items from both sets:
set3 = set1.union(set2)
print(set3) # {'b', 1, 2, 3, 'a', 'c'}

# ----------------------------------------------
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# keep both x . y as it was
z = x.intersection(y)
print(f'----- intersection :-------> {z}')


# rewrite to x 
x.intersection_update(y)
print(x) # {'apple'}


# Keep All, But NOT the Duplicates
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

# make a new set and not changing the previous sets
z1 = x1.symmetric_difference(y1)
print(f' symmetric_difference : ----> {z1}') # {'cherry', 'banana', 'microsoft', 'google'}
# update the x1
x1.symmetric_difference_update(y1)
print(f'update the x1 for symmetric difference update ---> {x1}') #  {'microsoft', 'cherry', 'banana', 'google'}

x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "facebook"}

# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
z2 = x2.isdisjoint(y2)

print(f' isdisjoint ---> : {z2}')

# ------------------------------------

m = {"a", "b", "d"}
n = {"f", "e", "d", "c", "b", "a"}

v = m.issubset(n)
print(f' issubset : ---->{v}') # True


t = {"f", "e", "d", "c", "b", "a"}
u = {"a", "b", "c"}

v1 = t.issuperset(u)

print(f' issuperset : ---->{v1}') # True


#The discard() method removes the specified item from the set.
m.discard("b")
print(f'm after discarding b : {m}')



# more about sets  --> https://python-reference.readthedocs.io/en/latest/docs/sets/