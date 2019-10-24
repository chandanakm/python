import random
username="ckm"
pwd="ckm05*"
count=0
count1=0
flag=0

while(count1<3):
    print("hi")
    if(flag==1):
        break
    else:
        uname=input("enter user name:\n")
        password=input("enter pwd:\n")
        count1+=1
        if((uname==username)&(password==pwd)):
            while(count<3):
                n=random.randrange(1000,10000)
                print(n)
                count+=1
                otp=int(input("enter the otp which u received\n"))
                if(otp==n):
                    print("login successful!")
                    flag=1
                    break
                elif(count<3):
                    print("resend otp\n")
                    continue
                else:
                    print("your attempt is timed out!")
            else:
                print("illi?")
                break
                
        else:
            if(count1<3):
                print("invalid username or pwd, please enter valid input")
            else:
                print("your attempt is timed out")

    

            
             
    
