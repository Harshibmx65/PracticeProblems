
def lonelyinteger(a):
    # Write your code here
    # dict1={}
    # for i in a:
    #     if(i not in dict1):
    #         dict1[i]=1
    #     else:
    #         dict1[i]+=1
    # for i in dict1:
    #     if(dict1[i]==1):
    #         return i
    
    # approach-2
    res=0
    for i in a:
        res^=i
    return res
