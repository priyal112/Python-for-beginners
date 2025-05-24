import pyqrcode

content = "This is my content"

url = pyqrcode.create(content)

url.png("myqr.png", scale = 5)

print("QR is generated successfully")