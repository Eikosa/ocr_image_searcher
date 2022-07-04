import subprocess

def ocr(konum): 
    return subprocess.Popen(
        f'python ocr_master.py "{konum}"', 
        shell=True, stdout=subprocess.PIPE).communicate()[0].strip().decode("UTF-8")

#a = ocr(r"C:\Users\Arda\Pictures\72_1.png")

from jql import *

import glob

db = jql("my_database.db", "?")

db.read("eiko")

for i in db.get_all():
    i = i["key"]
    if not os.path.exists(i):
        db.delete_key(i)
        print(i," silindi.")

for filename in glob.iglob("C:\\" + '**/*.png', recursive=True):
    if db.read(filename+"?ocr") == {}:
        db.write(filename+"?ocr", ocr(filename))
        print(filename)
    #ekle.append(filename)
    #if len(ekle) % 500 == 0:
    #    print(len(ekle))

for filename in glob.iglob("C:\\" + '**/*.jpg', recursive=True):
    if db.read(filename+"?ocr") == {}:
        db.write(filename+"?ocr", ocr(filename))
        print(filename)

# print(len(ekle))