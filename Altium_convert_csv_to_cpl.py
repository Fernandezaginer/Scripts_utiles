# Convert Altium CPL Script to JLCPCB CPL File
# For PCBA & JLCPCB
# © AFM 2023


import io
import os


# Input file name
INPUT_FILE = "pp.csv"
OUTPUT_BOM = "bom.csv"
OUTPUT_CPL = "cpl.csv"




def insert (source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]


def add_mm(string):
    add = False
    for i in range(len(string)):
        if string[i] == ".":
            add = True
        if string[i] == "," and add == True:
            string = insert(string, "mm", i-1)
            add = False
    string = string.replace("mmmm", "mm")
    return string


def csv_bom_line(string):
    if ";" in string:
        char = ";"
    else:
        char = ","
    component = string[0:(string.index(char)-1)]
    component = component.replace(" ", "")
    component = component.replace("'", "")
    component = component.replace('"', "")
    return component + ";"
    


# Read input file
file = open(INPUT_FILE, "r")
s = file.read()
with open(INPUT_FILE, 'r') as fi:
    lines = fi.readlines()
nl = []
for i in lines:
    if '"' in i:
        nl.append(i)
lines = nl
file.close()



# Generate cpl
s = s[s.index('"'):]
cpl_s = ""
for i in lines:
    cpl_s = cpl_s + add_mm(i)
cpl_s = cpl_s.replace("TopLayer", "Top")
cpl_s = cpl_s.replace("BottomLayer", "Bottom")
cpl_s = cpl_s.replace("Center-X(mm)", "Mid X")
cpl_s = cpl_s.replace("Center-Y(mm)", "Mid Y")
cpl_s = cpl_s.replace("'", "")
cpl_s = cpl_s.replace('"', "")
f = open(OUTPUT_CPL, "w")
f.write(cpl_s)
f.close()



# Generate bom
f = open(OUTPUT_BOM, "w")
for line in lines:
    f.write(csv_bom_line(line) + "\n")
f.close()


print("Successfully finished")
os.system("PAUSE")





