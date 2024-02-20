def fib(n):
        dp=[0,1]
        for i in range(2,n+1):
                dp.append(dp[i-1]+dp[i-2])
                if(dp[i]%2==0):dp[i]=dp[i]**dp[i]

        
        return dp
        

arr=fib(5)
print(arr[3])

