from pyqrcode import QRcode
import png
link="https://www.instagram.com/cristiano/"
qr_code=QRcode.create(link)
qr_code.png("instagram.png"scale=8)