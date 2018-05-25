

def divides(l, r):
    m = l
    n = r
    suma = 0
    sumb = 0
    sumc = 0
    count = 0
    while n >= 0:
        sumb = sumb + (r - n) * 10 ** (n)
        n = n - 1
    while m >= 0:
        suma = suma + (l - m) * 10 ** (m)
        m = m - 1
    if suma / 3 == 0:
        count = count + 1

    j = l
    c = r - l
    while c > 0:
        k = j
        while k >= 0:
            sumc = sumc + (j - k) * 10 ** (k)

            k = k - 1
        sumc=0
        if sumc / 3 == 0:
            count = count + 1
        c = c - 1
        j = j + 1
    print(count)
if __name__=="__main__":

   l=int(input('ds'))
   r=int(input('as'))
   divides(l, r)