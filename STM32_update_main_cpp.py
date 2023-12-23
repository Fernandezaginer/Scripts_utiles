# Script to update main.c to main.cpp
# Program STM32 in C++ !!!
# © AFM 2023

import io
import os

# STM32CubeIDE Strings:
file_name = "main.c"
s1 = "/* USER CODE BEGIN Includes */"
a1 = "#include \"mainProgram.h\"\n"
s2 = "/* USER CODE BEGIN WHILE */"
a2 = "  setup();\n"
s3 = "/* USER CODE BEGIN 3 */"
a3 = "    loop();\n"


# File name not found error:
if os.path.exists(file_name) == False:
    print(file_name, "not found")
    os.system("pause")
    exit()

indice = lambda file_raw, string : file_raw.index(string) + len(string) + 2


try:
    # Copy functions:
    file = open(file_name, "r")
    raw = file.read()
    file.close()
    i = indice(raw, s1)
    raw = raw[:i] + a1 + raw[i:]
    i = indice(raw, s2)
    raw = raw[:i] + a2 + raw[i:]
    i = indice(raw, s2)
    raw = raw[:i] + a3 + raw[i:]

    # write main.cpp
    file = open("main.cpp", "w")
    file.write(raw)
    file.close()

    # delete main.c
    os.remove("main.c")

except Exception as e:
    print(e)

os.system("PAUSE")

