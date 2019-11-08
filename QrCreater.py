##Create Qr according to given content

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

#add data with given format and parse them accordingly in scanner.py and open image
qr.add_data('Name:Tree ')
qr.add_data('Date:01.01.2019 ')
qr.add_data('Size:5Mb ')
qr.add_data('Format:PNG ')
qr.add_data('Path:C:/Users/yigit/Desktop/QR/runner.JPG')


qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("QR.png")