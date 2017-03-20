if __name__ == '__main__':
    n = int(input())
    my_list = input().split()
    my_ar = []
    for i in my_list:
        my_ar.append(int(i))
        
    print(hash(tuple(my_ar)))
