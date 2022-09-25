import qrcode
from PIL import Image

link = input('send the link')

qr_code = qrcode.make(link)

name_qr = input('Name the img from qr') + '.png'
file_img = open(name_qr, 'wb')
qr_code.save(file_img)
file_img.close()

path_img = './'+name_qr
Image.open(path_img).show()