#python code
#military time(24-hour)
#code for only main logic function part

def timeConversion(s):
    # Write your code here
    ap=s[8:]
    time=int(s[:2])
    if(ap=="PM" and 1<=time<=11):
        time+=12
        new_time=str(time)+s[2:8]
        return new_time
    elif(ap=="AM" and time==12):
        time="00"
        new_time=(time)+s[2:8]
        return new_time
    else:
        return s[:8]
