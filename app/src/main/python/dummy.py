from PIL import Image
import re
from io import BytesIO
import cv2
import requests
import base64
from os.path import dirname, join
#from com.chaquo.python import Python

def main(bName,im):
	files_dir=str(Python.getPlatform().getApplication().getFilesDir())
	fileimg1=join(dirname(files_dir),"input.jpg")
	fileimg2=join(dirname(files_dir),"output.jpg")
	print("**********Reached Python**************")
	text = bName
	pattern = list(text.split(" "))
	print(pattern)
	imgb = bytes(im, 'ascii')
	img_bytes = base64.decodebytes(imgb)
	with open(fileimg1, 'wb') as ip:
		ip.write(img_bytes)
	image = cv2.imread(fileimg1)
	API_ENDPOINT = "http://127.0.0.1:5000/conImage"
	data = {'image':im,
			'book_name':bName,
			}

	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)

	# extracting response text
	resurl = r.text

	return resurl


def main1():
	API_ENDPOINT = "http://127.0.0.1:5000/"
	data = {'book_name':'pyhton programming'}

	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)

	# extracting response text
	resurl = r.text

	return resurl


