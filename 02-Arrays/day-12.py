# Question 1: Reverse an array without using any inbuilt function, i.e, reversed() or [::-1]
#array = [1, 2, 3, 4, 5]
#temp = []
#for i in range(len(array)-1, -1 , -1):
 #   temp.append(array[i])
#print(temp)

# Question 2: Find the second largest number in an array without using any inbuilt function, i.e, max() or sort()
#array = [10, 20, 40, 80, 160]
#largest = second_largest = float('-inf')
#for num in array:
 #   if num > largest:
  #      second_largest = largest
   #     largest = num
    #elif num > second_largest and num != largest:
     #   second_largest = num

#print("Second largest number is:", second_largest)

# Question 3: Check whether if the given array is sorted in ascending order or not.

#array = [33, 66, 77, 44, 55]
#is_sorted = True
#for i in range(len(array) -1):
 #   if array[i] > array[i+1]:
  #      is_sorted = False
   #     break

#if is_sorted:
 #   print("true")
#else:
 #   print("false")

# Question 4: Count how many even and odd numbers are there in an array.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0

for num in array:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)