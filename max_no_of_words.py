sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]

def count_words(input):
    return len(input.split(' '))

print(sentences, len(sentences))
out = 0
for i in sentences:
    max = count_words(i)
    if max  > out:
        out = max

print(out)