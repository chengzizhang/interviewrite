a='aaabbbbbbbbbabababab'
b='baaabb'
counta=0
c=len(a)-len(b)+1
d=0
for i in b:

    for k in a[d:d+c]:
        if d+c>len(a):
            break
        elif i!=k:
            counta=counta+1
    d=d+1

print(counta)