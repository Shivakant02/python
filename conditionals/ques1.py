# Age group categorization , Classify a person's age grp : Child(<13),teenager(13-19) , Adult (20-59), Senior(60+);


age=int(input("provide an age : "));

if age<13:
            print("Child")
elif age<20:
            print("Teenager")
elif age<60:
            print("Adult")
else :
        print("Senior")