sen ="A man, a pln, a canal: Panama"

# f_s = ''.join([char.lower() for char in sen if char.isalnum()])
# print(f_s)


# print(f_s[::-1]==f_s)

# print(f_s)
import re

f_s=re.sub('[^a-z0-9]','',sen.lower())
l = 0
r = len(f_s)-1

while l < r:
    if f_s[l] != f_s[r]:
        print("Not a palindrome")
        break
    l += 1
    r -= 1

print("palindrome")

