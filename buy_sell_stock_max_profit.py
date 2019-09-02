import numpy as np
import pandas as pd 
def max_profit(Prices):
    n=len(Prices)
    S=np.zeros((n,n))
    #boundary conditions
    S[n-1][0]=0
    S[n-1][1]=Prices[n-1]
    k=n-2
    while(k>=0):
        for i in range(0,min(k,n-k)+1):
            if i==0:
                S[k][i]=max(S[k+1][i], S[k+1][i+1]-Prices[k])
            if 1<=i and i<=n-k-2:
                S[k][i]=max(max(S[k+1][i], S[k+1][i+1]-Prices[k]),
                            S[k+1][i-1]+Prices[k])
            if i==n-k-1:
                S[k][i]=max(S[k+1][i],S[k+1][i-1]+Prices[k])
            if i==n-k:
                S[k][i]=S[k+1][i-1]+Prices[k]
        k=k-1
    return S[0][0]
