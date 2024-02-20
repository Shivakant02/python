# a=10
# b=10

# # print(a=b)  gives error

# # loops

# for i in range(10,20):
#         print(i)


# for i in (20,30,-1):
#      print(i)    # to print reverse , we can use


                   
            
s="Hello 100 567 123 abcd 789 "
count =0
for i in s:
    if(i.isnumeric()):
        count+=1

print(count)

#******************List************************
myList=['india',23, True, 'python',1947]

print(myList[0:4])
#[st:end:step]

myList[1:3]=['manipur',100]
print(myList)

# to update the list the data type must be list 
#eg: myList[1:3]=111 gives error bcoz 111 is intiger
#String is a list of character


#to insert at any point
myList.insert(3,[3,5,6,7])


myList[2:2]=["many",3,4,5]
print(myList)

#deleting multiple elements 

new_list=[1,3,4,5,6,7,8]

# del new_list[1:4]
print(new_list)



