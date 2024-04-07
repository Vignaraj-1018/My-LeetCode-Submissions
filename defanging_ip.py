str = input()

# str = str.replace('.','[.]')
output =''
for i in range(len(str)):
    if str[i] == '.':
        output  += '[.]'
    else:
        output += str[i]

print(output)