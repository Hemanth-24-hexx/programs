list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

common= []

for item in list_a:
    if item in list_b:
        common.append(item)

print("Common elements:", common)

