if __name__ == '__main__':
    a = int(input())
    if a % 2 != 0:
        print('Weird')
    elif a % 2 == 0:
        if a in range(2,6):
            print('Not Weird')
        elif a in range(6,21):
            print('Weird')
        else:
            print('Not Weird')
