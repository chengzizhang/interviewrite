import sys


def count(n, k, list1):
    i = 0
    a = 0
    b = 0
    count1 = 0
    for i in range(0, len(list1) - 2):
        if list1[i] == list1[i + 1]:
            list1.remove(list[i])
    for a in range(0, len(list1) - 2):
        b = a + 1
        while b < len(list1):
            if list1[a] - list1[b] == k or list1[b] - list1[a] == k:
                count1 =count1+1
    print(count1)


if __name__ == "__main__":
    b = sys.stdin.readline().strip()
    list2 = list(map(int, b.split()))
    n = list2[0]
    k = list2[1]
    a = sys.stdin.readline().strip()
    list1 = list(map(int, a.split()))
    count(n, k, list1)

