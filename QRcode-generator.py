import qrcode

data = input("Enter URL: ")

qr = qrcode.QRCode(border=2)
qr.add_data(data)
qr.make(fit=True)


qr.print_ascii(invert=True)