if __name__ == "__main__":
    n = int(input())
    average = {}

    for i in range(n):
        info = input().split()

        average[info[0]] = "%.2f" % ((float(info[1])+float(info[2])+float(info[3]))/3.0)
        

    name = input()
    print(average[name])
