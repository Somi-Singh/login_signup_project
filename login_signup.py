import json

name=input("Please Enter Your Name\n--")
print("Hello",name)

user=input("Enter what you want :)\n1.signup\n2.login\n--")
if user=="1" or user=="signup":
    userName=input("Enter your userName:)\n--")
    password1=input("Enter password\n")
    password2=input("Enter the confirm password\n--")
    dob=input("enter your date of birth\n--")
    Gender=input("enter male or female\n--")
    Hobby=input("enter your hobby\n--")



    dic={"userName":userName,"password":password1,"Profile":{"DOB":dob,"gender":Gender,"hobby":Hobby}}
    
    if len(password1)>=8 and "a" in password1 or "b" in password1 or "c" in password1 or "d" in password1 or "e" in password1 or "f" in password1 or "g" in password1 or "h" in password1 or "i" in password1 or "j" in password1 or "k" in password1 or "l" in password1 or "m" in password1 or "n" in password1 or "o" in password1 or "p" in password1 or "q" in password1 or "r" in password1 or "s" in password1 or "t" in password1 or "u" in password1 or "v" in password1 or "w" in password1 or "x" in password1 or "y" in password1 or "z" in password1 and "A" in password1 or "B" in password1 or "C" in password1 or "D" in password1 or "E" in password1 or "D" in password1 or "E" in password1 or "F" in password1 or "G" in password1 or "H" in password1 or "I" in password1 or "J" in password1 or "K" in password1 or "L" in password1 or "M" in password1 or "N" in password1 or "O" in password1 or "P" in password1 or "Q" in password1 or "R" in password1 or "S" in password1 or "T" in password1 or "U" in password1 or "V" in password1 or "W" in password1 or "X" in password1 or "Y" in password1 or "Z" in password1 and "0" in password1 or "1" in password1 or "2" in password1 or "3" in password1 or "4" in password1 or "5" in password1 or "6" in password1 or "7" in password1 or "8" in password1 or "9" in password1 and "@" in password1 or "#" in password1 or "$" in password1 or "&" in password1:
            

    

            if password1==password2:
                # user existing checking here...
                with open('userDetails.json','r') as f:
                    userData=json.load(f)
                    for i in userData["allUserDetails"]:
                        if i['userName']==userName and i['password']==password1:
                            print("User already Exist :)")
                            break
                    else:
                # -----SignUp Section----
                        with open('userDetails.json') as json_file: 
                            data = json.load(json_file) 

                            temp = data["allUserDetails"] 

                            temp.append(dic)

                        
                        with open("userDetails.json","w") as data1:
                            json.dump(data, data1,indent=4)

                        print("congurlation",userName,"you account succesfully created....")
            # <------->
            else:
                print("your password not same please enter same password--")
    else:
        print("in your password no special character at least put 1 special character ")


else:
    if user=="2" or user=="login": 


        # ----Login Section---
        print('Hey:',name, 'Welcome To Login Page :)')
        userName=input("enter the userName:) ")
        loginPassword=input('enter the password:)')
     
        with open('userDetails.json','r') as f:
            userData=json.load(f)
            for i in userData['allUserDetails']:
                if i['userName']==userName and i['password']==loginPassword:
                    print("Login Successfully :)")
                    break
                    
            else:
                print("\n\n\tpassword/userName is wrong")
                
    else:
        print('Please Enter The C0rrect Input')

