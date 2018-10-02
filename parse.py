list_of_values = []

file1 = open('file1.txt', 'r')
for line in file1:
    list_of_values.append(line[:-1])
file1.close()

list_of_lists = []
for i in range(len(list_of_values)):
    list_of_lists.append(list_of_values[i].split(' '))
    
print(list_of_lists)
