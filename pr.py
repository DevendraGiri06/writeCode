def swap(list,a1,a2):
    temp =list[a1]
    list[a1]= list[a2]
    list[a2] = temp
    return list
list = [23,56,45,65]
a1,a2 =1,3
print(swap(list,a1-1,a2-2))

