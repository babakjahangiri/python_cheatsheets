#collected by Babak Jahangiri

#create a new list
list1 = [1,2,3,4,5,6,7,8,9]
str1 = "strings are cool"

# list second element until seventh (range of indexs)
print(list1[1:6]) #[2, 3, 4, 5, 6] 
print(str1[1:6]) #tring

 #list second element until seventh element with step 2
print(list1[1:6:2]) #[2, 4, 6]


#returns the items from the beginning to 4
print(list1[:4]) #[1, 2, 3, 4]

#reverse the list
print(list1[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(str1[::-1]) #looc era sgnirts

#retrieve a certain portion of a list and make a new list
elements = slice(3 ,8 ,1)
list2 = list1[elements] #this is a new list
print(list2)

#similar operation on every element of the list
def double(el):
    return 2*el

print(list(map(double, list1))) #double all elements of a list 


# Iterating over multiple lists simultaneously
colour = ["red", "yellow", "green"]
fruits = ["apple", "banana", "mango"]
price = [60,20,80]
for colour, fruits, price in zip(colour, fruits, price ):
    print(colour, fruits,": $",price)


#add a new element to list 
list1.append(11)
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

#add a new list to the list
list1.append([22,33]) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, [22, 33]]
print(list1)

#remove last element of the list
list1.pop()
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 11]

#remove last element WITHOUT using pop
list1.remove(list1[len(list1)-1])
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#remove one element from second left of the list
del list1[-2]
print(list1) #[2, 3, 4, 5, 6, 7, 8, 9]

#Removes all the elements from the list
list1.clear()
print(list1) #[]

#create a fresh list with range function
list1 = list(range(1, 15))
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#Add Any Iterable , tupe or list 
list1.extend((14,15,14))
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 14, 15, 14]

#Returns the number of elements with the specified value
print(list1.count(14)) #3

#removes repeated elements in the list and makes all elements unique
list1 = sorted(set(list1))
print(list1)

#using list comprehension to append a new items where not in list1 from list2
list2 = [10,11,12,13,14,15,16,17,18,19,20]
[list1.append(item) for item in list2 if item not in list1]
print(list1)

list1.clear()
list3 = [10,21,1,5]
[list1.append(item) for item in list2 if item not in list1 and item in list3]
print(list1) #[10]

#length of the list
print(len(list3)) #4

#insert one item at the begining of list1
list1.insert(0, 5)
print(list1) #[5, 10]

#egative Indexing
print(list3[-3]) #21

#type of list
print(type(list3)) #<class 'list'

# ----------------------- sort in lists -----------------------

#sort the list
list3.sort()
print(list3) #[1, 5, 10, 21]

#sort descending 
list3.sort(reverse = True)
print(list3)

#customize sort  
def mysort(n):
    return n%5==1 and n > 5
list3.sort(key = mysort)
print(list3)

#sort based on the first charachter in the each element with lambda  
list4 = ['Babak','mike','4li','Bijan','2raj','1iam','Mori','Rose','3rah','0mid','00_after_0mid']
list4.sort(key = lambda x : x[0])
print(list4) #['0mid', '00_after_0mid', '1iam', '2raj', '3rah', '4li', 'Babak', 'Bijan', 'Mori', 'Rose', 'mike']


# ----------------------- copy lists -----------------------

awesome_fruits = ["blueberry", "apple", "cherry","Oo0o0o0orange"]

# change the last item
awesome_fruits[-1] = "orange"

print(awesome_fruits) # ['blueberry', 'apple', 'cherry', 'orange']
my_fruits = awesome_fruits.copy()
my_fruits_with_list = list(awesome_fruits)
 

# ----------------------- join lists -----------------------

team1 = ['mike','reza','ali','john','mitra','helen']
team2 = ['hamza','katherine','safa','nazi']

for x in team1:
    team2.append(x)

print(team2) # ['hamza', 'katherine', 'safa', 'nazi', 'mike', 'reza', 'ali', 'john', 'mitra', 'helen']

my_fruits_with_list.extend(team1)
print(team1) #['hamza', 'katherine', 'safa', 'nazi', 'mike', 'reza', 'ali', 'john', 'mitra', 'helen']
 

my_fruits.extend(team1) 
print(my_fruits) #['blueberry', 'apple', 'cherry', 'orange', 'mike', 'reza', 'ali', 'john', 'mitra', 'helen']

# exclude name of fruits from persons
with_out_fruits = [x for x in my_fruits if x not in awesome_fruits]
print(with_out_fruits)  #['mike', 'reza', 'ali', 'john', 'mitra', 'helen']


# merging lists
num_list1 = [1,2,3,4,5]
num_list_2 = [6,7,8,9,10]
print(*num_list1, *num_list_2, sep=',') # 1,2,3,4,5,6,7,8,9,10

#into new list
new_list = [*num_list1, *num_list_2]
print(new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]