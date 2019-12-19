from PIL import Image, ImageDraw, ImageFont

image = Image.open('certificate.png')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('font.ttf', size=45)


(x, y) = (50, 50)
message =
color = 'rgb(0, 0, 0)'  # black color

# draw the message on the background

draw.text((x, y), message, fill=color, font=font)
(x, y) = (150, 150)
name = 'Vinay'
color = 'rgb(255, 255, 255)'  # white color
draw.text((x, y), name, fill=color, font=font)

# save the edited image

image.save('greeting_card.png')
