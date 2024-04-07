s = "a good   example"

s = " ".join( s.strip().split()[::-1])

print(s,s.strip().split(" "))