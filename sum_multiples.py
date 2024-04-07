num = 9
sum = 0
for i in range(num+1):
    if i%3==0 or i%5==0 or i%7==0:
        sum += i

# arr = sum([i for i in range(num) if i%3==0 or i%5==0 or i%7==0])

print(sum)