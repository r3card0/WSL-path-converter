import sys
from pathlib import Path, PureWindowsPath, PurePosixPath
from logging import Logger


def convert_path(file:str, logger : Logger | None = None) -> str:
    """
    Validates the incoming file path

    This function starts by normalize the file path, then runs a process to 
    identify the current operating system (OS) and select the correct file path. Returns a   
    validated file path in a string format.

    It has the option to add a logger when it's required apply obserability

    Parameters:
        file(str): Path of a file
        logger (logging.Logger, optional). logging instance to track
            events (info, errors). Default value (None)

    Return:
        An OS validated file path (str) 

    Raise:
        ValueError: file must be a non-empty string
    """

    # Validate the file must be a non-empty string
    if not isinstance(file,str) or not file.strip():
        msg = "❌ Error: file must be a non-empty string"
        if logger: logger.error(msg)
        raise ValueError(msg)
    
    # Identify the current OS
    operating_system = sys.platform
    if logger: logger.info(f"The current operating system is: {operating_system}")

    # define the parent path of this file
    parent_path = Path(__file__).parent
    if logger : logger.info(f"The parent path: {parent_path}")

    # evaluate if file is a windows format
    possible_drive = PureWindowsPath(file).drive
    is_windows_format = possible_drive != '' or '\\' in file
    if logger : logger.info(f"Is Windows format: {is_windows_format}")

    # --- WSL / Linux -------------------------
    if operating_system == 'linux':

        if is_windows_format:
            if logger : logger.info("Scenario: Windows path running on Linux/WSL")

            if possible_drive != '':
                # Absolute Windows path
                drive_letter = possible_drive[0].lower()
                windows_parts = PureWindowsPath(file).parts
                wsl_path = Path(f"/mnt/{drive_letter}").joinpath(*windows_parts[1:])
            else:
                # Relative Windows path
                windows_parts = PureWindowsPath(file).parts
                wsl_path = parent_path.joinpath(*windows_parts)

            return str(wsl_path.resolve()) # cast to str
        
        else:
            if logger : logger.info("Scenario: Unix path running on Linux/WSL")
            return str(Path(file).resolve()) # cast to str
    
    # --- Windows -------------------------
    elif operating_system == 'win32':
        if is_windows_format:
            # Native Windows path on Windows
            if logger : logger.info("Scenario: Windows path running on Windows")
            return str(Path(file).resolve()) # cast to str
        else:
            # Unix format path on Windows - not compatible 
            if logger : logger.info("Scenario: Unix path on Windows - convertig to relative")
            unix_parts = PurePosixPath(file).parts
            # Strip leading '/' if absolute Unix path
            parts_clean = [p for p in unix_parts if p != '/']
            return parent_path.joinpath(*parts_clean).resolve()

    # --- macOS -------------------------
    elif operating_system == "darwin":
        
        if is_windows_format:
            if logger : logger.info("Scenario: Windows path running on macOS")

            if possible_drive != '':
                windows_parts = PureWindowsPath(file).parts
                mac_path = parent_path.joinpath(*windows_parts[1:])
            else:
                windows_parts = PureWindowsPath(file).parts
                mac_path = parent_path.joinpath(*windows_parts)

            return str(mac_path.resove())
        else:
            if logger : logger.info("Scenario: Unix path running on macOS")
            return str(Path(file).resolve())

    else:
        if logger: 
            logger.warning(
                f"⚠️: Unknown operating system '{operating_system}', attempting generic resolution"
                )
        return Path(file).resolve()