from pathlib import PureWindowsPath, PurePosixPath

class PathConverter:
    def __init__(self, filepath:str):
        self.filepath = filepath.strip()

    # Convert Windows path to WSL path
    def to_wsl(self):
        try:
            # if filepath is wsl then pass
            if PureWindowsPath(self.filepath).is_absolute() == False:
                return self.filepath
            else:
                # else convert to wsl
                windows_path = PureWindowsPath(self.filepath).parts
                wsl_path = PurePosixPath("/mnt/c",*windows_path[1:])
                return wsl_path
        
        except SyntaxError:
            print("Syntax Error, windows file path format, adding 'r'")