def print_formatted(num):
    space = len(str(bin(num)[2:]))
    for i in range(1,num+1):
        print(str(i).rjust(space,' '),str(oct(i)[2:]).rjust(space,' '),str(hex(i)[2:]).upper().rjust(space,' '),str(bin(i)[2:]).rjust(space,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
