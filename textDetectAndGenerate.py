import io
import os
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()



def generaPics(paths):
	pathName = paths	
	paths = "pics/"+paths
	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    paths)
	print(paths)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations
	#str1=" ".join(str(x.description) for x in labels )

	    

	font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 30)

	imageFile=paths
	im1=Image.open(imageFile)

	draw=ImageDraw.Draw(im1)
	i=0
	for label in labels:
		draw.text((0,i),label.description,(255,255,0),font=font)
		i+=30
	draw=ImageDraw.Draw(im1)

	im1.save("./labeledPics/"+pathName)

dirs=os.listdir("./pics/")
dirs.sort()

for filesDir in dirs:
	generaPics(filesDir)

#generate video
command="ffmpeg -framerate 5 -i ./labeledPics/pic%03d.jpg outputLabed.mp4"
p=os.popen(command)
p.close()
