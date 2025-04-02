count = 0
length = len(s) - 2
for i in range(length):
    if s[i:i+3] == "bob":
        count += 1
print("Number of times bob occurs is: " + str(count))