import numpy as np
import shutil
import cv2
import os

base = 'Difference/'
folders = os.listdir(base)

for folder in folders:

	make = 90
	base = ''
	folder = 'Difference'
	shutil.rmtree('Base')
	os.mkdir('Base')

	images = os.listdir(base + folder)
	for j in range(0, len(images), make):
		output = cv2.imread(base + folder + '/' + images[j])
		image1 = cv2.imread(base + folder + '/' + images[j + 1])
		cv2.addWeighted(image1, 1.0/min(make, len(images)-j), output, 1.0/min(make, len(images)-j), 0, output)

		for i in range(j + 2,j + min(make, len(images)-j)):
			# load the image
			image1 = cv2.imread(base + folder+ '/' + images[i])
			cv2.addWeighted(image1, 1.0/min(make, len(images)-j), output, 1, 0, output)
		cv2.imwrite("Base/OutputComb" + str(j) + ".jpg", output)


	base = 'Base/'
	images = os.listdir(base)
	output 	= cv2.imread(base + images[0])
		
	if(len(images)>1):
		image1 	= cv2.imread(base + images[1])

		cv2.addWeighted(image1, 1.0/len(images) , output, 1.0/len(images), 0, output)

		for i in range(2, len(images)):

			image1 = cv2.imread(base + images[i])
			cv2.addWeighted(image1, 1.0/len(images), output, 1, 0, output)

	cv2.imwrite('Combines/Difference/' + folder + '.jpg', output)
	break