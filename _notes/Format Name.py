####### Format name #######
def format_name(f_name, l_name):
    return f_name.title() + " " + l_name.title()

name = input("What is your full name?\n").split()
print(format_name(name[0], name[1]))



