## \package setup
#  Script for building the R2C_Basestation executable using cx_Freeze.
from cx_Freeze import setup, Executable

## \var build_exe_options
#  Dictionary containing options for building the executable.
#  - packages: List of required Python packages.
#  - include_files: List of non-Python files to include in the build.
build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["assets"],
}

## \fn setup()
#  Calls cx_Freeze.setup with metadata and build configuration.
setup(
    name="R2C_Basestation",
    version="1.0",
    description="R2C_Basestation",
    options={"build_exe": build_exe_options},
    executables=[Executable("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/Main.py", icon="/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/icon.ico", base="Win32GUI")]
)
