
import os
import sys
from PIL import Image
import asyncio
import winocr

async def f(dosya, dil = "tr"):
    img = Image.open(dosya)
    return (await winocr.recognize_pil(img, dil)).text

if __name__ == "__main__":
    try:  
        konum = sys.argv[1]
    except IndexError: 
        print("Lütfen konum giriniz.")
        sys.exit(0)

    print(asyncio.run(f(konum)))
