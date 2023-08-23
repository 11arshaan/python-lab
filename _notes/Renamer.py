import os



# RENAME PREPEND

directory = input('Enter the directory path: ')
directory = directory.replace('\\', '/')

# Check if the string starts and ends with quotes
if directory.startswith('"') and directory.endswith('"'):
    # Remove the quotes
    directory = directory[1:-1]

for filename in os.listdir(directory):
    if filename.startswith('-'):
        os.rename(os.path.join(directory, filename), os.path.join(directory, filename[2:]))





# RENAME FILES OF EXTENSION

# define your target directory
target_dir = "D:/VFX/Houdini Training/geo/flametornado1"
# iterate over each file in the target directory
for i, file_name in enumerate(sorted(os.listdir(target_dir))):
    # make sure this is a vdb file
    if file_name.endswith(".vdb"):
        # create the new file name
        new_file_name = "frame_{:03d}.vdb".format(i)

        # get the full paths for the old and new file names
        old_file_path = os.path.join(target_dir, file_name)
        new_file_path = os.path.join(target_dir, new_file_name)

        # rename the file
        os.rename(old_file_path, new_file_path)
