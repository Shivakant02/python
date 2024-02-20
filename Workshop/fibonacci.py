def fibbo(n):
        if n==0: return 0
        elif n==1 or n==2 : return 1
        return  fibbo(n-1)+fibbo(n-2)

                
print(fibbo(5))

def fib(n):
        dp=[0,1]
        for i in range(2,n+1):
                dp.append(dp[i-1]+dp[i-2])
                if(dp[i]%2==0):dp[i]=dp[i]**dp[i]

        
        return dp
        

arr=fib(5)
print(arr[3])
