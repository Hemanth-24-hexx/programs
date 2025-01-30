#to add element in a nested list

#the given list
list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list[2][2].append(7000)

print(list)
