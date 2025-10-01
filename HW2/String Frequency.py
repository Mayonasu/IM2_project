def frequency(text):
    freq = {}
    display = {}

    for ch in text:
        if ch.isalpha():
            key = ch.lower()
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
                display[key] = ch
    return freq, display

word = input("Enter string: ")

words = word.replace(",", " ").split()

for word in words:
    freq, display = frequency(word)
    
    output = []
    for key, value in freq.items():
        output.append(f"{display[key]}={value}")
    print(", ".join(output))