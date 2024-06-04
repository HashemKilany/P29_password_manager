import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = 8
nr_symbols = 4
nr_numbers = 8

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
p1 = []

for i in range(0, nr_letters):
    r = random.randint(0, len(letters) - 1)
    p1.append(letters[r])

for i in range(0, nr_symbols):
    s = random.randint(0, len(symbols) - 1)
    p1.append(symbols[s])

for i in range(0, nr_numbers):
    n = random.randint(0, len(numbers) - 1)
    p1.append(numbers[n])

random.shuffle(p1)
list_as_string = ''.join(p1)
print(list_as_string)