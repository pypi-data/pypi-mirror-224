# spalette

spalette breaks down the colors that comprise a digital image and generates a color palette based on those colors. Each pixel in a digital image is assigned a specific red, green, and blue value which, when combined, displays a particular color. These RGB values are commonly represented in hexadecimal form, eg '#121212' in photo editing and graphic design contexts. When you provide spalette with an image the program quantizes it to simplify the number of colors available while maintaining accuracy. Each pixel of the quantized image is read into RGB form, then converted to hexadecimal. These hex colors are then ordered by occurrence and sampled to generate a color palette.

## How to run:

spalette is intended to be as simple as possible. The only requirement from the user is a filepath. In a terminal or CLI, type 'spalette path/to/imagefile.jpg'. A color palette will be generated, and ten hex color codes will be returned in the terminal. For a visual representation of the palette in addition, pass flag '-cw' before or after the filepath like so: 'spalette -cw path/to/imagefile.jpg'. A new window will open with the ten palette colors plotted onto a color wheel, courtesy of matplotlib. 

## Requirements/Installation:

spalette is available for pip installation via PyPI. If installed via pip: 'pip install spalette' the requirements will be installed for you.

This program utilizes pandas for data manipulation, opencv to read image data,
and matplotlib to generate a visual output. These need to be installed for the program to work.

These libraries can be installed by running the following commands:

* pip3 install pandas

* pip3 install opencv-python

* pip3 install matplotlib

These requirements are also listed in requirements.txt, which is prepared should you want to run this program in a virtual environment. 

## Primary Features:

Reading Image Color Data
- Reads RGB values from digital image files into an array (ndarray).

Cleaning and Manipulating Image Color Data
- The read image file is quantized to simplify the color data available while maintaining accuracy to the colors present in the image. The program creates a pandas dataframe of this data by extracting it from an ndarray and putting it into R, G, and B columns. Each row of this dataframe contains one pixel's color values. This dataframe is then converted to hexadecimal. The hexadecimal is added as an additional column, preserving the R G B values, and creating a master dataframe of all useful color data pixel by pixel. 

Sorting Image Data by Occurence
- This dataframe is then sorted into a pandas series, with the values that occur more often than others at the top and the values that occur least often at the bottom. This sort is then broken up into 10 equally sized sections for sampling. From these sections, the most often occuring color in each is selected and included in the palette.
 
Visualizing the Occurence of Certain Colors
- These ten colors are always output to the terminal for you to use as you see fit. They may also be visualized as a color wheel (matplotlib pie chart with each color being given equal space) if so desired by passing the -cw flagat runtime.

![alt text](https://i.imgur.com/hrVCxEi.png)
