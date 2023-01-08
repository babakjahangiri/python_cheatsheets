# ----------------------- create a new dictionary -----------------------

person = {
  "name": "Mike",
  "lastname": "Ford",
  "dob": 1990,
  "married" : True,
  "balance" : 1500.95
}


print(person)


print(person["lastname"]) #Ford


# * -- Duplicates Not Allowed
person = {
  "name": "Mike",
  "lastname": "Ford",
  "dob": 1990,
  "married" : True,
  "balance" : 1500.95,
  "balance" : 1600.00
}

print(person) # new balance replaced

print(len(person)) # 5    

print(type(person)) # <class 'dict'>

# -- Create a new dictionary with constructor

person2 = dict(name ="maria", lastname ="Bello", dob= 1995)

print(person2) 

# -- access to dictionary key with <get> method
name = person2.get("name") 
print(name) # maria

# -- get all keys in person dictioanry
print(person.keys()) # dict_keys(['name', 'lastname', 'dob', 'married', 'balance'])


# -- get all values in person dictioanry
print(person.values()) # dict_values(['Mike', 'Ford', 1990, True, 1600.0])


person["dob"] = 1988
print(person)



print(person.items()) # dict_items([('name', 'Mike'), ('lastname', 'Ford'), ('dob', 1988), ('married', True), ('balance', 1600.0)])


# -- add new item to person2 dict

person2["married"] = True
print(person2.items()) # dict_items([('name', 'maria'), ('lastname', 'Bello'), ('dob', 1995), ('married', True)])

if "married" in person2:
  print("Yes, we may know marriage status")

# clone person2 to person3
person3 = dict(person2)

# shallow copy
# person3 = person2  >> don't do this

# -- update item(s) of person2 dict
person2.update({"name": "rosa" , "married": False, "balance": 10000})
print("person2 : ", person2)
print("person3 : ", person3)


# -- remove an item
person2.pop("married")
print("person2 : ", person2)


del person2["balance"]
print("person2 : ", person2)


# -- delete the whole dictionary
del person3 
# print("person3 : ", person3)  #NameError: name 'person3' is not defined. Did you mean: 'person'?

person2.clear()
print(person2) # {}


# -- simple loop through a dictionary
for x in person:
  print(x)


# -- simple loop but get values
for x in person:
  print(person[x] , end=" ")

# ===================== get keys and values =====================
# -- simple loop but get keys with reading keys method
for x in person.keys():
  print(x)

# -- simple loop but get values with reading values method
for x in person.values():
  print(x)


# -- simple loop with keys & values
for k, v in person.items():
  print(k,":", v)


# -- make a new dictionary
persons = {}

# -- add a child dictionary
persons.update({"person1" : dict(person)})
print(persons)

# not effected on persons because its a deep clone(new dictonary)
person["name"] = "Tom"
print(persons)
print(person)


# change child value in nested dictionary
persons["person1"]["name"] = "Akbar"
print(persons)

# -- if the key exist it return the key otherwise it set a key=id with value=1000 
x = person.setdefault("id", "1000")
print(x)

print(person) #{'name': 'Tom', 'lastname': 'Ford', 'dob': 1988, 'married': True, 'balance': 1600.0, 'id': '1000'}