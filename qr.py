import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


link = "https://github.com/Emeika"

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(link)
qr.make()
img = qr.make_image(fill_color = 'black', back_color = 'white')
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="image.png")
img_4 = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

img.save('default.png')
img_1.save('round.png')
img_2.save('colored.png')
img_3.save('embeded.png')
img_4.save('git.png')
