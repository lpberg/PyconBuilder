#Creates PNG images from text (string) input.
#Use: For multiple lines, seperate words with spaces
#FONT: Arimo - http://www.google.com/webfonts/specimen/Arimo
import ImageFont, ImageDraw, Image

def createIconImageFromText(txt):
	# split text input into multiple words in a list
	txt = txt.split()
	#open background image
	image = Image.open('base.png')
	#create a drawable image
	draw = ImageDraw.Draw(image)
	#set initial font size to 1 (smallest)
	fontsize = 1
	# set the precentage of base image text should occupy - .9 provides good border
	img_fraction = 0.90
	#creat intial font using fontsize of 1
	font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
	#set up image width and height variables to be used later
	img_w, img_h = image.size
	#how large can the text
	max_width = img_fraction*image.size[0]
	max_height = img_fraction*(image.size[1]/len(txt)+1)
	#if statement - first block for single words
	if len(txt) < 2:
		#set text to be the first element in txt list
		txt = txt[0]
		#while the font fits the width of the image space - increase font
		while font.getsize(txt)[0] < max_width:
			fontsize += 1
			font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
		#reduce fontsize by 1 to ensure it fits nicely in space
		fontsize -= 1
		#create the font with new found fontsize
		font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
		#create variables for text width and height
		text_w, text_h = font.getsize(txt)
		#draw the text on the image, place it at the center vertically and horizontally
		draw.text(((img_w - text_w)/2, (img_h/2-text_h/2)), txt, font=font,fill ="#000000")
		#save image
		image.save(txt+'.png')
		#print out confirmation to cmdline
		print(txt+'.png created successfully')
	# else block assumes multiline text (space delineated) 
	else:
		#a list to collect font sizes of each word in txt
		fontsizes = []
		# for every word, find the max font size given image constraints
		for item in txt:
			fontsize = 1
			font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
			while (font.getsize(item)[0] < max_width) and (font.getsize(item)[1] < max_height):
				fontsize += 1
				font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
			#reduce fontsize by 1 to ensure it fits nicely in space
			fontsize -= 1
			#append 'found' font size to list to find min (next)
			fontsizes.append(fontsize)
		#set the font to a font with the smallest (largest) possible for all words in txt
		font = ImageFont.truetype("fonts/Arimo-Bold.ttf", min(fontsizes))
		# set the variables for the width and height of the smallest (largest) word
		text_w, text_h = font.getsize(txt[fontsizes.index(min(fontsizes))])
		# draw each word in a specific place
		for item in range(len(txt)):
			text_w, t = font.getsize(txt[item])
			w = (img_w - text_w)/2
			h = (item+1)*(img_h/(len(txt)+1))-(text_h/2)
			draw.text((w, h), txt[item], font=font,fill ="#000000")
		#save image
		image.save("".join(txt)+'.png') 
		#print out confirmation to cmdline
		print("".join(txt)+'.png created successfully')

def createFlashCardImageFromText(txt):
	# split text input into multiple words in a list
	txt = txt.split("*")
	#open background image
	image = Image.open('flash_base.png')
	#create a drawable image
	draw = ImageDraw.Draw(image)
	#set initial font size to 1 (smallest)
	fontsize = 1
	# set the precentage of base image text should occupy - .9 provides good border
	img_fraction = 0.90
	#creat intial font using fontsize of 1
	font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
	#set up image width and height variables to be used later
	img_w, img_h = image.size
	#how large can the text
	max_width = img_fraction*image.size[0]
	max_height = img_fraction*(image.size[1]/len(txt)+1)
	#if statement - first block for single words
	if len(txt) < 2:
		#set text to be the first element in txt list
		txt = txt[0]
		#while the font fits the width of the image space - increase font
		while font.getsize(txt)[0] < max_width:
			fontsize += 1
			font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
		#reduce fontsize by 1 to ensure it fits nicely in space
		fontsize -= 1
		#create the font with new found fontsize
		font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
		#create variables for text width and height
		text_w, text_h = font.getsize(txt)
		#draw the text on the image, place it at the center vertically and horizontally
		draw.text(((img_w - text_w)/2, (img_h/2-text_h/2)), txt, font=font,fill ="#000000")
		#save image
		image.save(txt+'.png')
		#print out confirmation to cmdline
		print(txt+'.png created successfully')
	# else block assumes multiline text (space delineated) 
	else:
		#a list to collect font sizes of each word in txt
		fontsizes = []
		# for every word, find the max font size given image constraints
		for item in txt:
			fontsize = 1
			font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
			while (font.getsize(item)[0] < max_width) and (font.getsize(item)[1] < max_height):
				fontsize += 1
				font = ImageFont.truetype("fonts/Arimo-Bold.ttf", fontsize)
			#reduce fontsize by 1 to ensure it fits nicely in space
			fontsize -= 1
			#append 'found' font size to list to find min (next)
			fontsizes.append(fontsize)
		#set the font to a font with the smallest (largest) possible for all words in txt
		font = ImageFont.truetype("fonts/Arimo-Bold.ttf", min(fontsizes))
		# set the variables for the width and height of the smallest (largest) word
		text_w, text_h = font.getsize(txt[fontsizes.index(min(fontsizes))])
		# draw each word in a specific place
		for item in range(len(txt)):
			text_w, t = font.getsize(txt[item])
			w = (img_w - text_w)/2
			h = (item+1)*(img_h/(len(txt)+1))-(text_h/2)
			draw.text((w, h), txt[item], font=font,fill ="#000000")
		#save image
		image.save("".join(txt)+'.png') 
		#print out confirmation to cmdline
		print("".join(txt)+'.png created successfully')