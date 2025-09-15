myTuple = ()
row = int(input("Row: "))
col = int(input("Col: "))

for x in range(row):
    print(f"Row {x+1}")
    innerList = ()
    for y in range(col):
        num = float(input(f"Enter Number {y+1}: "))
        innerList += (num,)
    myTuple += (innerList,)

print()
search = float(input("Search: "))
print()
print("The Numbers Are: ")

for x in range(len(myTuple)):
    for y in range(len(myTuple[x])):
        print(f"{myTuple[x][y]}", end = " ")
    print()

found = ()

for x in range(row):
    for y in range(col):
        if myTuple[x][y] == search:
            found += ((x, y),)

if found:
    for pos in found:
        print(f"\nNumber {search} found at Row {pos[0]} and Col {pos[1]}")
else:
    print(f"\nNumber {search} not found.")