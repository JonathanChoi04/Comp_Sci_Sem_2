x = int(input("How many items are you purchasing? "))

total = 0
for i in range (0, x):
    y = input("What item are you purchasing? ")
    z = float(input("How much is the item? "))
    print("Thank you for purchasing " + y + "!")
    total = total + z 
    
print("Your total is: " + str(total))