heights = input("enter heights:\n").split()
total = 0 
    
for height in heights:
    total += int(height)


print(f"Average Height: {total/len(heights)}")