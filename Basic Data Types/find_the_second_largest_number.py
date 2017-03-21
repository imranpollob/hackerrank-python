if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    ar = []
    for i in arr:
        ar.append(int(i))
    
    ar.sort()
    maximum = max(ar)
    
    for j in ar[::-1]:
        if j < maximum:
            second = j
            break

    print(second)
