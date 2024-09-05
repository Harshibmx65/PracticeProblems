#only main logic part
def plusMinus(arr):
    # Write your code here
    plus=0
    minus=0
    zero=0
    l=len(arr)
    for i in arr:
        if(i>0):
            plus+=1
        elif(i<0):
            minus+=1
        else:
            zero+=1
    print(plus/l)
    print(minus/l)
    print(zero/l)
