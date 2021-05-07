import requests


def main(bName,im):
	print("**********Reached Python**************")
	API_ENDPOINT = "http://192.168.43.61:5000/conImage"
	data = {'image':im,
			'book_name':bName,
			}
	# sending post request and saving response as response object
	r = requests.post(url = API_ENDPOINT, data = data)

	# extracting response text
	resurl = r.text
	print("Received Response")

	return resurl





