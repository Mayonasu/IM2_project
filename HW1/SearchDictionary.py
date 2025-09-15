myDict = {}

row = int(input("Row: "))
col = int(input("Col: "))

for x in range(row):
    print(f"Row {x+1}")
    for y in range(col):
        num = float(input(f"Enter Number {y+1}: "))
        myDict[(x, y)] = num

print()
search = float(input("Search: "))
print()
print("The Numbers Are: ")

for x in range(row):
    for y in range(col):
        print(f"{myDict[(x, y)]}", end =" ")
    print()

found = []

for key, value in myDict.items():
    if value == search:
        found.append(key)

if found:
    for pos in found:
        print(f"\nNumber {search} found at Row {pos[0]} and Col {pos[1]}")
else:
    print(f"\nNumber {search} not found.")