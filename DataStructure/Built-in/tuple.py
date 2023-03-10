
tuple1 = ("mike", "tom", "rebekah")
print(tuple1) # ("mike", "tom", "rebekah")

# * -- Duplicates Allowed in tuples

tuple2 = ("mike", "tom", "rebekah","tom")
print(tuple2) # ('mike', 'tom', 'rebekah', 'tom')

# Tuple Length
print(len(tuple2)) #4

# one item tuple
thistuple = ("apple",)
print(type(thistuple)) # <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # <class 'str'>


# ---- Access Tuple Items
 
# access to second item
print(tuple2[1]) # tom

print(tuple1[-1]) # rebekah

tuple3 = ("mike", "tom", "rebekah","katy","jerry","patrik")

# create new tuple from second item until sixth item (means from index 1 untill index 5)
print(tuple3[1:5]) # ('tom', 'rebekah', 'katy', 'jerry')

#from start value untill index 4 (include 3 but not fifth item)
print(tuple3[:4]) # ('mike', 'tom', 'rebekah', 'katy')

# new tuple from fifth item from end to last item
print(tuple3[-4:]) # ('rebekah', 'katy', 'jerry', 'patrik')

# To determine if a specified item is present in a tuple use the in keyword:
if "babak" not in tuple3:
  print("correct, 'babak' is not in the tuple3")

# Tuples are unchangeable, or immutable 
myfriends = ("farnam", "amir", "sufi","sarah","alireza","ali")

# to change a value, convert to list & add 'fati' to the end of the list
myfriends_list = list(myfriends)
myfriends_list[-1] = "fati"
myfriends = tuple(myfriends_list)
print(myfriends) #('farnam', 'amir', 'sufi', 'sarah', 'alireza', 'fati')

# to Add Items, need to be changed to list

myfriends_list = list(myfriends)
myfriends_list.append("erfan")
myfriends = tuple(myfriends_list)
print(myfriends) # ('farnam', 'amir', 'sufi', 'sarah', 'alireza', 'fati', 'erfan')

new_friends= ("roya","mahsa","bijan","oliver")
myfriends += new_friends 
print(myfriends) # ('farnam', 'amir', 'sufi', 'sarah', 'alireza', 'fati', 'erfan', 'roya', 'mahsa', 'bijan', 'oliver')

# --------- Remove Items
# *** You cannot remove items in a tuple (because tuples are unchangeable), therefore; changing them to lists

myfriends_list = list(myfriends)
myfriends_list.remove("roya")
myfriends = tuple(myfriends_list)
print(myfriends) # ('farnam', 'amir', 'sufi', 'sarah', 'alireza', 'fati', 'erfan', 'mahsa', 'bijan', 'oliver')



del tuple2 
#print(tuple2) #NameError: name 'tuple2' is not defined.


# --- unpack tuples

friend1, friend2, friend3 = tuple1  
print(friend1) #mike
print(friend2) #tom
print(friend3) #rebekah


# if the number of items in tuples not match the number of variable you can collect the rest as list
best_friend1, best_friend2, *other_firends = tuple3
print(best_friend1) #mike
print(best_friend2) #tom
print(other_firends) #['rebekah', 'katy', 'jerry', 'patrik']


(right_one, *others , left_one) = myfriends
print(right_one) # farnam
print(others) # ['amir', 'sufi', 'sarah', 'alireza', 'fati', 'erfan', 'mahsa', 'bijan']
print(left_one) # oliver

*good_buddies, = 'reza','arshiya','sarah' 
print(good_buddies) # ['reza', 'arshiya', 'sarah']

#tuple maker function
def names_tuple(*args):
    return args

print(names_tuple('Michael', 'John', 'Nancy')) # ('Michael', 'John', 'Nancy')


# --- loop through a tuple
for x in good_buddies:
  print(x)

# -- loop through the tuple items by referring to their index number
myfriends = ('amir', 'sufi', 'sarah', 'alireza', 'fati', 'erfan', 'mahsa', 'bijan')
print('---- loop through the tuple items ----')
for i in range(5,len(myfriends)):
  print(myfriends[i],end="\f")

# -- while loop
print('\n')
print('---- Using a While Loop ----')
i = 0
while i < len(myfriends):
  print(i+1,'-',myfriends[i])
  i+=1


print('\n')
#---- join two or more tuples with + operator

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)


# --- multiply the content of a tuple
fruits = ("blueberry", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) #('blueberry', 'banana', 'cherry', 'blueberry', 'banana', 'cherry')

num_banana = mytuple.count('banana')
print(num_banana)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 7)
index_seven= thistuple.index(7)
print(index_seven) #2   it returns the first occurrence 

#thistuple.index(700)
#ValueError: tuple.index(x): x not in tuple