s ="chris alan"

word_s = s.split(" ")

for i in range(len(word_s)):
    word_s[i] = word_s[i].capitalize()

s = " ".join(word_s)
print(s)
