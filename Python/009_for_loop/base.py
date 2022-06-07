x = int(input("Please enter the line length: "))
y = input("Do you want a horizontal or vertical line? ")

for a in range(0,x):
    if "vertical" == y:
        print(x)
    elif "horizontal" == y:
        print(x, end=" ")
