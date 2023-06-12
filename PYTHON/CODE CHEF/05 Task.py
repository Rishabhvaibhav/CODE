#Update the code below to solve this problem

t = int(input())
for i in range(t):
    N, M, K = map(int, input().split())
#    M = expiry
#    N = number of bread
#    K = number of breads to be eaten


   
    if (N % ex) == 0:
        print('Yes')
    
    elif (ex%N ) == 1:
        print('No')
    else :
        print('invalid')
