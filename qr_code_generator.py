import qrcode
from PIL import Image
scanner = qrcode.QRCode(version = 1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=15,border=6)
scanner.add_data("https://www.linkedin.com/in/ayesha-fatima-7118602b7/")
scanner.make(fit=True)
img = scanner.make_image(fill_color = "green",back_color =  "black" )
img.save("linkedin_scanner.png")
