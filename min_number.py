def find_min(my_list):
  min = my_list[0]

  for i in range(len(my_list)):
    if my_list[i] < min:
      min = my_list[i]

  return min


x = 10
list1 = [110, 14, 52, 33, x, 74]
print(find_min(list1))

list2=[1,2,67,665,65,32,54,4353,452354,-423,0]
print(find_min(list2))


