longest = current = s[0]

length = len(s)
for i in range(1, length):
    if s[i] >= s[i - 1]:
        current += s[i]
    else:
        current = s[i]

    if len(current) > len(longest):
        longest = current

print("Longest substring in alphabetical order is: " + longest)