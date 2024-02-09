chai_types={
    "Masala":"Spicy", 
    "Ginger":"Zesty",
    "GreenTea":"Mild"        
            }

print(chai_types)
print(chai_types["Ginger"])
chai_types["GreenTea"]="Fresh"
print(chai_types)

#For printing keys
for chai in chai_types:
    print(chai)

#for printing Keys and values
for chai in chai_types:
    print(chai,chai_types[chai])


#for operaitons on keys and values
    
    for key, value in chai_types.items():
        print(key,value);


if "Masala" in chai_types:
    print("I have masala chai")

    #Add some keys and values
    chai_types["Earl grey"]="Citrus"

    print(chai_types)


#pop method
    
    chai_types.pop("Ginger")
    print(chai_types)
    chai_types.popitem();
print(chai_types)

#delete method
del chai_types["GreenTea"]
print(chai_types)

#.copy() -> for copying the data

#we can define dictionary inside the dictionary

squared_num={x:x**2 for x in range(6)}
print(squared_num)