##################
#For Range
##################

for number in range(1,10): #does not include last number
    print(number)


#Print sum of even numbers in range (A)
total = 0
for number in range(1, 101):
    if (number%2) == 0:
        total += number
print(total)


# Prim sum of even numbers in range (B)
total = 0
for number in range(2, 101, 2): #third parameter is the step size, or interval. How many steps, including current, before the next item is selected
    total += number
print(total)




##################
#For IN
##################

#Highest Number
numbers = input("Enter a list of numbers:\n").split()
print(max(numbers))


# Average Heights
heights = input("enter heights:\n").split()
total = 0 
    
for height in heights:
    total += int(height)


print(f"Average Height: {total/len(heights)}")

