import re

def count_substring(string, sub_string):
    count = 0
    for i in re.finditer(sub_string, string):
        count +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
