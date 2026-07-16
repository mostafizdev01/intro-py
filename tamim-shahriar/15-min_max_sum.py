li = [1, 3, 6, 7, 10, 14, 100, 9, 5, 12]

max_number = float("-inf")
for num in li:
    if num > max_number:
        max_number = num
        
print(max_number)


# print sum number

result = sum(li)
print(result)

# get sum number useing loop

final_result = 0

for num in li:
    final_result = final_result + num
    
    print(final_result)
    
# print min number

min_number = min(li)
print("min_number: ", min_number)