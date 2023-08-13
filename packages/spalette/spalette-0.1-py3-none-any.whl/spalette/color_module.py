from itertools import product
import pandas as pd

"""
extract_rgb() returns dictionary of all 
rgb values in an image by pixel, given an ndarray of rgb values
"""
def extract_rgb(image_as_ndarray):
	i = 0 
	r_vals=[]
	g_vals=[]
	b_vals=[]
	coordinates = list(product(range(image_as_ndarray.shape[0]), 
	range(image_as_ndarray.shape[1])))
	
	while i < len(coordinates):
		r_vals.append(format(image_as_ndarray[coordinates[i][0], coordinates[i][1], 2]))
		g_vals.append(format(image_as_ndarray[coordinates[i][0], coordinates[i][1], 1]))
		b_vals.append(format(image_as_ndarray[coordinates[i][0], coordinates[i][1], 0]))
		i += 1
	rgb_data = {'R': r_vals, 'G': g_vals, 'B': b_vals}	
	return rgb_data
	
"""
rgb2hex() converts rgb values to hexadecimal values, given RGB input
(three int values)
"""
def rgb2hex(red, green, blue):
	return '#%02x%02x%02x' % (red, green, blue)

"""
quantizer quantizes the given image file for better color output
"""
def quantizer(cv2image_as_input):
	div = 64
	cv2image_quantized = cv2image_as_input // div * div + div // 2
	return cv2image_quantized

# add_one for pypi
def add_one(number):
    return number + 1
