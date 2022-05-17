from time import sleep
from tkinter import N
import os


name = input(("App name: "))
version = input(("App Version: "))
icon = input(("App Icon Link: "))
download = input(("iPA Download Link: "))
description = input(("Apps Description: "))
bundleID = input(("Whats the Bundle ID ?: "))
banner = input(("Whats the banner?: "))

os.system("cls")

end = '{\n    "name": "'+name+'",\n    "version": "'+version+'",\n    "icon": "'+icon+'",\n    "down": "'+download+'",\n    "dev": "7z",\n    "category": "Tweaked Apps",\n    "description": "'+description+'",\n    "bundleID": "'+bundleID+'",\n    "appstore": "'+bundleID+'",\n    "banner": "'+banner+'",\n"contact":  {\n        "web": "https://7zz.shop/discord",\n        "twitter": "https://twitter.com/7z_henry"}}'

print(end)

sleep(120)