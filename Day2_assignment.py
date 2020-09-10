#List default functions..................................................

# Adds List Element as value of List. 
List = ['Mathematics', 'chemistry', 1997, 2000] 
List.append(20544) 
print(List) 

#insert
List = ['Mathematics', 'chemistry', 1997, 2000] 
# Insert at index 2 value 10087 
List.insert(2,10087)      
print(List)

#extend
List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
List1.extend(List2)         
print(List1) 
List2.extend(List1)  
print(List2) 

#sum
List = [1, 2, 3, 4, 5] 
print(sum(List)) 

#count
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1)) 

#length
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(len(List)) 

#index
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.index(2)) 

#minimum
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(min(List)) 

#maximum
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(max(List)) 

#sort and reverse
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
List.sort(reverse=True)
print(List)		 

#pop
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(List.pop()) 

#delete
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
del List[0] 
print(List) 

#remove
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
List.remove(3) 
print(List) 



#Dictionary default functions......................................

#clear
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)

#get
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)

#item
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

#popcar = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

#update
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


#Sets default functions...............................

#Addsfruits = {"apple", "banana", "cherry"}

fruits.add("orange")

print(fruits)

#clearfruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

#copy
fruits = {"apple", "banana", "cherry"}

x = fruits.copy()

print(x)

#popfruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

#removefruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)


#Tuple default functions........................................................

#count
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

#index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)


#String default functions........................................................

#capitalize
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#count
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

#index
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#isalpha
txt = "CompanyX"

x = txt.isalpha()

print(x)

#islower
txt = "hello world!"

x = txt.islower()

print(x)
