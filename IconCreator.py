import ImageFont, ImageDraw, Image

def createIconImageFromText(txt):
	txt = txt.split()
	image = Image.open('base.png')
	draw = ImageDraw.Draw(image)
	fontsize = 1
	img_fraction = 0.90
	font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
	img_w, img_h = image.size
	if len(txt) < 2:
		txt = txt[0]
		while font.getsize(txt)[0] < img_fraction*image.size[0]:
			fontsize += 1
			font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
		fontsize -= 1
		font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
		text_w, text_h = font.getsize(txt)
		draw.text(((img_w - text_w)/2, (img_h/2-text_h/2)), txt, font=font,fill ="#000000")
		image.save(txt+'.png') # save it
		print(txt+'.png created successfully')
	else:
		fontsizes = []
		max_width = img_fraction*image.size[0]
		max_height = img_fraction*(image.size[1]/len(txt)+1)
		for item in txt:
			fontsize = 1
			while (font.getsize(item)[0] < max_width) and (font.getsize(item)[1] < max_height):
				fontsize += 1
				font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
			fontsize -= 1
			fontsizes.append(fontsize)
		print fontsizes, min(fontsizes)
		font = ImageFont.truetype("fonts/Arimo-Bold.ttf", min(fontsizes))
		text_w, text_h = font.getsize(txt[fontsizes.index(min(fontsizes))])
		for item in range(len(txt)):
			text_w, t = font.getsize(txt[item])
			w = (img_w - text_w)/2
			h = (item+1)*(img_h/(len(txt)+1))-(text_h/2)
			draw.text((w, h), txt[item], font=font,fill ="#000000")
		image.save("".join(txt)+'.png') # save it
		print("".join(txt)+'.png created successfully')

# createIconImageFromText("folder name")