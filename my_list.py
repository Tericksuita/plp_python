# creating an empty list
my_list = []

#Appending the values 10, 20, 30 and 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting 15 at the second position
my_list.insert(1, 15)

#extending my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])

#removing the last item in my_list
my_list.pop()

#sorting list in ascending order
my_list.sort()

#Finding and printing the index of 30 in my_list
index_of_30 = my_list.index(30)
print(f'The index of 30 in my_list is: {index_of_30}')