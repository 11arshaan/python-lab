import os

directory = input('Enter the directory path: ')
directory = directory.replace('\\', '/')

# Check if the string starts and ends with quotes
if directory.startswith('"') and directory.endswith('"'):
    # Remove the quotes
    directory = directory[1:-1]

for filename in os.listdir(directory):
    if filename.startswith('-'):
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename[2:]))
