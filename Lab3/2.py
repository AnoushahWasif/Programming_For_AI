def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
length_of_fruits = len(fruits)
Fruits = tuple(fruits)

for i in range(1, length_of_fruits, 2):
   print("At even length: " , Fruits[i], end=" ")

for i in range(0,length_of_fruits,2):
   print("At odd length: " , Fruits[i], end=" ")
