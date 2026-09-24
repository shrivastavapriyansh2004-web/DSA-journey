# dsa = data structures and algorithms
# data structures are the way of storing data in a computer so that it can be used efficiently.
# algorithms are the step by step procedure to solve a problem.

# Time Complexity tells us how fast our code runs when input size grows.

# Question 1 :Create an array of 5 numbers and print all elements using a loop.

#arr = [10, 20, 30, 40, 50]
#for i in range(len(arr)):
    #print(arr[i])

# Question 2 : print the sum of all elements in the array.

#arr = [33, 66, 99, 165, 222]
#total = 0
#for i in range(len(arr)):
    #total += arr[i]
#print(total)

# Question 3 : print the largest element in the array without using max() function.

#arr = [888, 555, 1596, 222, 17856]
#largest = arr[0]
#for i in range(1, len(arr)):
 #   if arr[i] > largest:
  #      largest = arr[i]
#print(largest)

# Question 4 : print the smallest element in the array without using min() function.

arr = [888, 555, 1596, 222, 17856]
smallest = arr[0]
for i in range(1, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]
print(smallest)