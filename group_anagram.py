from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

res=defaultdict(list)
for s in strs:
    key = [0]*26
    for ch in s:
        key[ord(ch)-ord("a")] += 1
    print(key)
    res[tuple(key)].append(s)

print(res.values())