from functions.decrypt import *
import json
import base64
import time

isfile = False
ld = 0
cfgpth = 'config/config.json'

with open(cfgpth, 'r') as file:
    cfg = json.load(file)

sellang = cfg['DefaultLanguage']

langpth = 'config/lang/'+ sellang + '.json'
with open(langpth, 'r') as file:
    lang = json.load(file)

def loadlang():
    global lang, sellang
    langpth = 'config/lang/'+ sellang + '.json'
    with open(langpth, 'r') as file:
        lang = json.load(file)

for i in range(51):
    print(lang['ui.startup.load'] + ": " + str(ld) + "%")
    ld = ld + 2
    time.sleep(0.01)

print("<--- " + cfg['ToolName'] + " --->")

print("\n"+"© " + cfg['Credits'])
print("Version " + cfg['Version'])

if cfg['AllowFile'] == "true":
    print(lang['ui.files.wip'] + "...")
else:
    print("🛈 " + lang['ui.files.deny'])

if input(lang['ui.lang.startchange'] + " Y/N: ").lower() == "y":
    sellang = input(lang['ui.lang.avb'] + " " + cfg['Languages'] + ": ")
    loadlang()
    ld = 0
    for i in range(51):
        print(lang['ui.startup.load'] + ": " + str(ld) + "%")
        ld = ld + 2
        time.sleep(0.01)