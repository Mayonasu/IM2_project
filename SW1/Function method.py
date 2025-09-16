def currency(dollars):
    peso = 57.17
    yen = 146.67

    convertedPeso = dollars*peso
    convertedYen = dollars*yen

    return convertedPeso, convertedYen

dollars = float(input("Enter currency in $: "))

convertedPeso, convertedYen = currency(dollars)

print(f"Dollars: {dollars}")
print(f"Dollars in peso is {convertedPeso:,.2f}")
print(f"Dollars in yen is {convertedYen:,.2f}")