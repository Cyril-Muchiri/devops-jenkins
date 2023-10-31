import os

def check_files_exist(directory):
    readme_exists = os.path.exists(os.path.join(directory, 'README.md'))
    license_exists = os.path.exists(os.path.join(directory, 'LICENSE'))
    
    return readme_exists, license_exists

if __name__ == "__main__":
    directory = "."  
    
    readme_exists, license_exists = check_files_exist(directory)
    
    if readme_exists:
        print("README.md exists in the directory.")
    else:
        print("README.md does not exist in the directory.")
    
    if license_exists:
        print("LICENSE exists in the directory.")
    else:
        print("LICENSE does not exist in the directory.")
