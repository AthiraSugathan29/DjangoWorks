# print(dir(list))
# print(dir(dict))

lst = [
       [1,34],
       [40,5],
       [5,70]
      ]
# for ls in lst:
#     for num in ls:
#         if num > 50:
#             print(num)

# List Comprehension
# numbers = [num for ls in lst for num in ls]
# print(numbers)
print([num for ls in lst for num in ls if num > 50]) # Flattened list

# To find largest number in list.
# lar = max([num for ls in lst for num in ls]) # Find max in flattened list
# print(lar)
# OR
#print(max([num for ls in lst for num in ls]))

max_num = max([num for ls in lst for num in ls])
max_pair = [n for n in lst if max_num in n]
print(max_pair)