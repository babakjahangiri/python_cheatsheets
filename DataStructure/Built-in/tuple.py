
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