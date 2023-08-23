
try:
    file1 = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["apple"])
except FileNotFoundError:
    file1 = open("a_file.txt", "w")
except KeyError as error_key:
    print(f"the key {error_key} does not exist")
else:  # else is executed if no exception is raised
    content = file1.read()
    print(content)
finally:  # finally is executed no matter what
    file1.close()
    print("file was closed")


fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Index is out of range.")


make_pie(4)


word = ""
while word == "":
    try:
        user_input = input("Type a word: ")
        if any([char.isdigit() for char in user_input]):
            raise ValueError("You typed a number.")
        if user_input == "":
            raise ValueError("You didn't type anything.")
    except ValueError as error_message:
        print(error_message)
    else:
        word = user_input
    finally:
        pass
print(word)