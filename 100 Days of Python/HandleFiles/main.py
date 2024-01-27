with open("file.txt") as file:
    content = file.read()
    letters = content.splitlines()
    print(letters)
    for letter in letters:
        new_file = open(f"{letter}.txt", "w")
        new_file.write(f"{letter} is {letter}")
        new_file.close
    file.close()
