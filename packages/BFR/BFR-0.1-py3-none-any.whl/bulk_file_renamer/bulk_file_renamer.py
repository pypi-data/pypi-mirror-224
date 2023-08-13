import os, re

class BulkFileRenamer():

    def __init__(self,file_naming_format:str, extension:str, debug_mode = False):
        self.fileNamingFormat = file_naming_format
        self.extension = extension
        self.debugMode = debug_mode

    def RenameFiles(self, folder_path:str):
        files = os.listdir(folder_path)
        pattern = re.compile(f'{self.fileNamingFormat}\\d+{self.extension}')

        for file in files:
            if not pattern.match(file):
                new_name = self.get_next_filename(folder_path)
                old_path = os.path.join(folder_path, file)
                new_path = os.path.join(folder_path, new_name)

                os.rename(old_path, new_path)
                if self.debugMode:
                    print(f'Renamed {file} to {new_name}')

    def get_next_filename(self,folder_path):
    
        files = os.listdir(folder_path)

        # Dynamically create the regex pattern based on the configuration
        pattern = re.compile(f'{self.fileNamingFormat}(\\d+){self.extension}')
        numbers = [int(pattern.match(file).group(1)) for file in files if pattern.match(file)]

        next_number = max(numbers, default=-1) + 1
        return f'{self.fileNamingFormat}{next_number}{self.extension}'