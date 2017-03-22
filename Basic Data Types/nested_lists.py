if __name__ == '__main__':
    n  = int(input())
    d = {}
    data = []
    
    for i in range(n):
        name = input()
        num = float(input())
        d[name] = num
        data.append(num)
   
    s = list(set(data))
    s.sort()
    second = s[1]
    
    final_name = []
    for k,v in d.items():
        if v == second:
            final_name.append(k)

    final_name.sort()
    for xx in final_name:
        print(xx)
            
    
