import os

directory_name = "."
os.makedirs(directory_name, exist_ok=True)

file_names = [
    "SampleTxt.txt",
    "SamplePy.py",
    "SampleSh.sh",
    "SampleJava.java"
]

for file_name in file_names:
    with open(os.path.join(directory_name, file_name), 'w') as file:
        pass

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

files = os.listdir(current_directory)

for file in files:
    file_path = os.path.join(current_directory, file)
    permissions = os.stat(file_path).st_mode
    print(f"File: {file}, Permissions: {permissions:o}")
