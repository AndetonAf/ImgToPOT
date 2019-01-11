from tkinter import filedialog
from tkinter import *
import os
from PIL import Image

def ReturnProxPOT(x):
	pot = 8
	while 1:
		pot = pot * 2
		if pot >= x :
			print(pot)
			return pot
			break;

try:  
    os.mkdir("POT")
except OSError:
	print("Error")
	
root = Tk()
root.filename = filedialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("all files","*.*")))

for filenam in root.filename:
	img = Image.open(filenam, 'r')
	img_w, img_h = img.size
	x = ReturnProxPOT(img_w)
	y = ReturnProxPOT(img_h)
	background = Image.new('RGBA', (x,y), (255, 0, 0, 0))
	bg_w, bg_h = background.size
	offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
	background.paste(img, offset)
	background.save('pot/'+filenam.split("/")[-1].split(".")[0]+'.png', 'PNG')
			
