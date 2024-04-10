string = 'stressed'
string1 = ''

for i in range(len(string) - 1, -1, -1):
    string1 = string1 + string[i]

print(string1)
