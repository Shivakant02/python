chai="Lemon tea"


# replace a word or sentance

print(chai.replace("Lemon","Ginger"))

newChai="Lemon, Ginger, Masala, Mint"

#String to list

print(newChai.split(", "))#Converts in list

#find the word

print(chai.find("tea"))

# .count()->for counting the occurance



chai_type="Masala"
quantity=2
order="I ordered {} cup of {} chai."
print(order.format(quantity,chai_type))


#List to String

chai_variety=["Lemon", "Masala", "Ginger", "Mint"]
print(" ".join(chai_variety))



for letter in chai :
        print(letter)

chai_name ="He said, \"Masala chai is awesome\" "
print(chai_name)

#or we can use raw string tag

chai_name=r"ginger\ntea"
print(chai_name)