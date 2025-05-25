from pyzbar.pyzbar import decode
from PIL import Image

#reading
img = Image.open("myqr.png")

cont = decode(img)

print(cont[0].data.decode())
