myList = []
row = int(input("Row: "))
col = int(input("Col: "))

for x in range(row):
    print(f"Row {x+1}")
    innerList = []
    for y in range(col):
        num = float(input(f"Enter Number {y+1}: "))
        innerList.append(num)
    myList.append(innerList)

print()
search = float(input("Search: "))
print()
print("The numbers are:")

for x in range(len(myList)):
    for y in range(len(myList[x])):
        print(f"{myList[x][y]}", end = " ")
    print()

found = []

for x in range(row):
    for y in range(col):
        if myList[x][y] == search:
            found.append((x, y))

if found:
    for x in found:
        print(f"\nNumber {search} found at Row {x[0]} and Col {x[1]}")
else:
    print(f"\nNumber {search} not found.")