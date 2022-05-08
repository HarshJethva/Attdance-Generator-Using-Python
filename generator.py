# import MyQR
# from MyQR import myqr
# import os
# import base64


# print(lines)

# for i in range(0, len(lines)):
#     data = lines[i].encode()
#     name = base64.b64encode(data)
#     version, level, qr_name = MyQR.myqr.run(
#         str(name),
#         level='H',
#         colorized=True,
#         version=1,
#         contrast=1.0,
#         brightness=1.0,
#         save_name=str(lines[i] + '.bmp'),
#         save_dir=os.getcwd()
#     )

# import pyqrcode
# import png
# from pyqrcode import QRCode
  
  
# # String which represents the QR code
# s = "www.geeksforgeeks.org  "
  
# # Generate QR code
# url = pyqrcode.create(s)
  
# # Create and save the svg file naming "myqr.svg"
# url.svg("myqr.svg", scale = 8)
  
# # Create and save the png file naming "myqr.png"
# url.png('myqr.png', scale = 6)

import qrcode
import os.path

f = open('1.csv', 'r')
lines = f.read().split('\n')
for i in lines:
    s = i + '.png'
    
    file_exists = os.path.exists(s)
    if file_exists:
        pass

    else:
        img=qrcode.make(i)
        img.save(s)