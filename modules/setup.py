from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pygame"],
    "include_files": ["assets"],
}

setup(
    name="R2C_Basestation",
    version="1.0",
    description="R2C_Basestation",
    options={"build_exe": build_exe_options},
    executables=[Executable("/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/Main.py", icon="/home/joan/Downloads/BASESTATION - R2C - WARRIOR (coba)/assets/icon.ico", base="Win32GUI")]
)
