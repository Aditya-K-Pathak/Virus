"""
This Module performs oprations like finding files in directory, readin and writing a file
"""
import os

class Folder:
    """
    A class that use os to list all the files in the current directory
    """
    def __init__(self) -> None:
        pass
    
    def list_files(self, location: str) -> list[str]:
        """
        :params - location -> Takes the location of current directory in string format
        :return -list -> a list of strings conatining all the files with their location
        """
        files, i = os.listdir(), 0

        while i < len(files):
            if files[i] in ("__pycache__", "Rebuilder.py", "Files.py", "key.key", "main.py", ".git"):files.pop(i)
            elif os.path.isdir(files[i]):
                for j in os.listdir(files[i]):files.append(f"{files[i]}/{j}")
                files.pop(i)
            else:i += 1

        return files
    
class FileOperations:
    """
    A class to perform action like read and write
    """
    def __init__(self) -> None:
        return
    
    def read_file(self, location: str) -> bytes:
        """
        Read the data of file in read-binary mode
        :params - location -> location of file (directory + file name)
        :return - returns a binary string
        """
        with open(location, "rb") as file:
            return file.read()
        
    def write_file(self, location: str, content: str) -> None:
        """
        Write the binary-data to file in string format
        :params - location -> location of file (directory + file name)
        :return - returns a binary string
        """
        with open(location, "w")as file:
            file.write(content)