from PIL import Image
import pytesseract
import cv2
import os
 
def ocr(image_path, preprocess="thresh"):
	image = cv2.imread(image_path)
	gray = preprocess_image(image, preprocess)
	tmp_filename = create_tmp_file(gray)
	config = ('-l eng+nor --oem 1 --psm 3')
	text = pytesseract.image_to_string(Image.open(tmp_filename), config=config)
	os.remove(tmp_filename)
	return text

def preprocess_image(image, preprocess):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	if preprocess == "thresh":
		gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)

	return gray

def create_tmp_file(gray):
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)
	return filename
