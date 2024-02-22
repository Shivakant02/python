#****************Attendence management system*****************
from Login import login
from Login import studentlogin
t_username="pradip@limat.com"
t_password=12345
t_attendance=90
student={
1:{
      "Name":"Naresh",
      "userName":"Naresh@gmail.com",
      "Password":12345678,
      "Attendance":90,
      "roll no":1
},
2:{
      "Name":"Gokul",
      "userName":"gokul@gmail.com",
      "Password":12345678,
      "Attendance":90,
      "roll no":2
},
3:{
      "Name":"Mohit",
      "userName":"mohit@gmail.com",
      "Password":12345678,
      "Attendance":90,
      "roll no":3
},
}




while 1:
    print("MAIN MENU")
    print("Enter 1 to teacher section")
    print("Enter 2 to teacher student")
    print("Enter 3 to exit")

    ch=int(input("Enter the choice: "))

    if ch==1:
            login(t_username,t_password)
           
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
            studentlogin(student)
            while 1:
                    print("Enter 1 to view the attendance")
                  
                    print("Enter 2 to logout")
                    cho=int(input("Enter the choice"))
                    if cho==1:
                          print(f"Attendance is {t_attendance}")

                  #   elif cho==2:
                  #         upAtt=int(input("Enter the updated att: "))
                  #         t_attendance=upAtt
                  #         print(f"updated att is {t_attendance}")

                    elif cho== 2:break
                    else:
                          print("Invalid choice , Enter the right choice : ")
    elif ch==3:break
    else : print("Invalid choice. Enter the choice")





    
