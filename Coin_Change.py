def cp(D,n):
    '''This is a function which takes two inputs, a
       set/list of denominations D and an amount n
       and returns the minimum number of coins required
       to get the amount n. It returns -1 if the amount
       can't be achieved'''
    try:
        m=min(D)#smallest denomination
        N=dict()
        '''This variable act as an array storing solution
           for cp(D,i) for i <= n, if not possible give infinity '''
        for i in range(n+1):
            if i==0: ## for zero amount no coins are required
                N[i]=0
            elif i<m: # if amount entered is less than smallest denomination gives infinity.
                N[i]=float('inf')
            else:
                S=set()
                for d in D:
                    if i>=d:# for i<d it is not possible to achieve i using d.
                        S.add(N[i-d])# S = {N(i-d)| d in D, i>=d}
                N[i]=1+min(S)# N[i] = 1+ min{N(i-d)| d in D, i>=d}
        if N[n]==float('inf'):
            return -1#if not possible give value -1
        return N[n]
    except:
        print("Error")
    
