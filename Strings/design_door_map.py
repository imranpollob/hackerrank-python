n, m = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.

out = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print('\n'.join(out+['WELCOME'.center(m,'-')]+out[::-1]))
