import random
#username=["ckm","mkm","snk","ubr"]
#pwd=["ckm05*","mkm05","snk21","ubr02"]
d={"ckm":"ckm05*","mkm":"mkm05","snk":"snk21"}
otpcount=0
upcount=0
flag=0

while(upcount<3):
    if(flag==1):
        break
    else:
        uname=input("enter user name:\n")
        password=input("enter pwd:\n")
        upcount+=1
        
        for i,j in d.items():
            if (uname==i) & (password ==j):
                while(otpcount<3):
                    n=random.randrange(1000,10000)
                    print(n)
                    otpcount+=1
                    otp=int(input("enter the otp which u received\n"))
                    if(otp==n):
                        print("login successful!")
                        flag=1
                        break
                    elif(otpcount<3):
                        print("resend otp\n")
                        continue
                    else:
                        print("your attempt is timed out!")
                        break
                else:
                    break
                break
                
        else:
            if(upcount<3):
                print("invalid username or pwd, please enter valid input")
            else:
                print("your attempt is timed out")

    

            
             
    
