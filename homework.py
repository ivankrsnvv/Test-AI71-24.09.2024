import random
list = [[random.randint(1,10)for i in range(3)] for j in range(3)]
for row in list:
    for element in row:
        print(element, end='\t')  # tab on end of line
    print()  # break line
print()
print()
count = 1  # reset counter
for row in list:
    if count != 2:
        row.reverse()  # reverse all line except 2
    for element in row:
        print(element, end='\t')  # tab on the rnd of line
    print()  # line break
    count += 1  # counter