import cv2
import matplotlib.pyplot as plt
import os.path
import pandas as pd
import numpy as np
from . import color_module as clr_m
import argparse

# parser configuration
parser = argparse.ArgumentParser(
	description='simple color palette generation from an image file')
parser.add_argument('-cw', '--colorwheel', 
	help='present color palette as colorwheel/graph',
	action="store_true")
parser.add_argument('filepath', 
	help='the filepath of an image from which to generate a palette',)
args = parser.parse_args()

def main():
	# assign filepath to var for operation
	filepath = args.filepath
	file_exists = os.path.exists(filepath)

	# if file exists, operate, otherwise, tell the user and close
	if file_exists:
		"""
		Reading data (image) in
		"""
		# read user image into ndarray with cv2.
		pic = cv2.imread(filepath)
	
		"""
		Cleaning the data
		"""
		# quantize the image, reducing the number of colors for a more
		# aesthetically useful palette
		qpic = clr_m.quantizer(pic)
	
		# Shrink the quantized image, so gathering RGB data doesn't use so
		# much memory.
		scale_percent = 50
		width = int(qpic.shape[1] * scale_percent / 100)
		height = int(qpic.shape[0] * scale_percent / 100)
		dim = (width, height)
	
		qzd_rzd_pic = cv2.resize(qpic, dim, interpolation = cv2.INTER_AREA)
	
		# create dataframe of the rgb values of every pixel in the image
		# using extract_rgb from color_module.
		df_rgb = pd.DataFrame(clr_m.extract_rgb(qzd_rzd_pic))
	
		# create dataframe df_hex from df_rgb, adding hex value column to 
		# df_rgb. This is converted from r,g,b columns using a lambda and  
		# rgb2hex from color_module.
		df_hex = df_rgb.assign(hex=df_rgb.astype(int).apply(
		lambda x: clr_m.rgb2hex(*x), axis=1))

		"""
		Analyzing the data
		"""
		# create srs_hex_byoccur series: hexes are ordered from those 
		# occurring most often to least often in the image. RGB values are
		# removed to make working with this series easier.
		series_hex_byoccur = df_hex.drop(['R', 'G', 'B'], axis=1).value_counts(
		ascending=False)
	
		# split the hex color data series into 10 equal parts
		df_10color_sample = np.array_split(series_hex_byoccur, 10)
		# define lists to build palette dataframe
		occurrence_list = []
		hex_list_sampled = []
	
		# populate lists with sampled color hex codes and # of times they occur in the image
		for i in range(0, 10): 
			hex_list_sampled.append(df_10color_sample[i].index[0]) # the ten hex codes that compose the palette
			occurrence_list.append(df_10color_sample[i][0]) # the number of times each hex code occurs
	
		# create palette dataframe (10 color palette, with occurrence count)
		df_palette = pd.DataFrame(hex_list_sampled, columns=['hex'])  
		df_palette['occurrences'] = occurrence_list
	
		# prepare palette dataframe for visualization/output
		df_palette=df_palette.set_index('hex') # set index of df_palette to the hex codes, for coloring matplotlib
		colors=df_palette.index.tolist() # define colors for matplotlib, flattening df to list
		df_palette['false_y_axis']=1 # append a false y axis to the dataframe, matplotlib will make a colorwheel inst of a typical pie chart
	
		"""
		Color data visualization options
		"""
		# cli output (default, constant output)
		print(', '.join(colors))
	
		# create pie chart of a color palette (colorwheel) if -cw is passed
		if args.colorwheel:
			df_palette.plot(kind='pie', y='false_y_axis', colors=colors, legend=None) # plot the palette as an arbitrarily sized pie chart
			title_piechart='Palette from colors in ' + filepath # define the title for the palette chart
			plt.ylabel(None) # disable labeling of the ys, false data
			plt.title(label=title_piechart) # tell matplotlib to use our defined title
			plt.show() # plot the palette


	# if the image filepath provided didn't point to an image, end with msg	
	else: 
		print("File not found.")
		
if __name__ == "__main__":
    main()
