RSA-Oracle
==========
# math background
in RSA public key, we have (e,n), in real world, we have c:  
thus, we can use these info to build a chain:  
c\*(2^e) mod n == (m^e\*2^e) mod n = (2m)^e mod n
# what to do
if we send a c\*2^e to server  
thus, in the server, it will check whether 2m is even or odd  
trick:  
2m can be odd?  
the answer is yes, because if 2m>n,the result will be:  
2m%n==2m-n  
in other word, n = p\*q , n is odd  
so in conclusion:  
`1. result == odd , 2n>2m>n`  
`2. result == even , n>2m>0`
# what to do next
in our trick, we can only know the range of 2m  
thus ,we can imagine what will happen if we send c\*4^e?  
we have 2m%n == 2m - n just know  
2*(2m-n) == 4m - 2n , the result must be even  
so the result doesn't affect the next step  
if `result1 == odd , 2n>2m>n`   
we send `c*4^e`, we can have that:  
`1. result == odd , 4n>4m>3n`  
`2. result == even , 3n>2m>2n`  
the result of `result1 == even` you can imagine  
# result
if we send c\*(2^k)`k=1,2,...,len(bin(n))` to server, thus we can have the result:  
`high*n>=2^len(bin(n))*m>=low*n`  
subject to high-low == 1  
thus n is nearly 2^len(bin(n))  
we can test what is m easily