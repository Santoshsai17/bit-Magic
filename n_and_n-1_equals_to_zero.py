n=int(input())
c=0
while n:
    n=n>>1
    c+=1
print(1<<c)
print(1<<(c-1))
