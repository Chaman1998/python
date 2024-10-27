import os

# Specify the directory I wat to list
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)