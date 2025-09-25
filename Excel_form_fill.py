# Python Script to fill an excel form
# Usefull for recurrent polls
# © AFM 2025


import os
import win32com.client as win32

excel_file = list(filter(lambda x : ".XLSX" in x.upper(), os.listdir()))[0]


dict = {
    "B15" : "23",
    "D16" : "x",
    "N25" : "Madrid",
    "D24" : "x",
    "N22" : "x",
    "N30" : "x",
    "N35" : "x",
    "D47" : "x",
    "N45" : "x",
    "N53" : "x",
    "N54" : "x",
    "N56" : "x",
    "N57" : "x",
    "N59" : "x",
    "N60" : "x",
    
    "I63" : "x",
    "I64" : "x",
    "N63" : "x",
    "N64" : "x",

    "N66" : "x",
    "N67" : "x",

    "N69" : "x",
    "N70" : "x",

    "N72" : "x",
    "N73" : "x",

    "N76" : "x",
    "N77" : "x",

    "L80" : "x",
    "L81" : "x",
    "L82" : "x",
    "L83" : "x",
    "L84" : "x",
    
    "M86" : "x",
    "L87" : "x",
}



excel = win32.Dispatch("Excel.Application")
excel.Interactive = False
excel.Visible = False
excel.ScreenUpdating = False
excel.DisplayAlerts = False
excel.EnableEvents = False
wb = excel.Workbooks.Open(os.path.abspath(excel_file))
ws = wb.Sheets("Cuestionario")

for key, value in dict.items():
    ws.Range(key).Value = value

wb.Save()
wb.Close()
excel.Quit()






