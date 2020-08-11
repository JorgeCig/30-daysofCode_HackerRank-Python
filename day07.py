def arra(n,arr):
    arrn = " ".join(map(str, arr[::-1]))
    return arrn 


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(arra(n,arr))