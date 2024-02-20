#****************Attendence management system*****************

t_username="pradip@limat.com"
t_password=12345
t_attendance=90


while 1:
    print("MAIN MENU")
    print("Enter 1 to teacher section")
    print("Enter 2 to teacher student")
    print("Enter 3 to exit")

    ch=int(input("Enter the choice: "))

    if ch==1:
            uname=str(input("Enter the username : "))
            upass=int(input("Enter the password : "))
            if uname==t_username and upass==t_password:
                print("Welcome to the teacher saction")
            while 1:
                    print("Enter 1 to view the attendance")
                    print("Enter 2 to update the attendance")
                    print("Enter 3 to logout")
                    cho=int(input("Enter the choice"))
                    if cho==1:
                          print(f"Attendance is {t_attendance}")

                    elif cho==2:
                          upAtt=int(input("Enter the updated att: "))
                          t_attendance=upAtt
                          print(f"updated att is {t_attendance}")

                    elif cho== 3:break
                    else:
                          print("Invalid choice , Enter the right choice : ")
    elif ch==2:
          pass
    elif ch==3:break



    
