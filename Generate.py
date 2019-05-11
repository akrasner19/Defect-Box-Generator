import drawSvg as draw
from Process import *
import random as rand

#declare process wide, constant variables
CANVASWIDTH = 300
CANVASHEIGHT = 300
DOTCOLOR = '#000000'
DOTRADIUS = 2
DOTNUMBER = 100
SEED = "testingseed1"
BOXCOLOR = 'red'
BOXTHICKNESS = 4

drawing = draw.Drawing(CANVASWIDTH,CANVASHEIGHT,origin='center')

rand.seed(SEED)

dg = DotGenerator(DOTRADIUS,CANVASWIDTH,CANVASHEIGHT,DOTCOLOR,BOXCOLOR,BOXTHICKNESS)

for i in range(DOTNUMBER):
	drawing.append(dg.generateDot())

drawing.append(dg.generateBoundingBox())

drawing.setPixelScale(2)
drawing.saveSvg('test.svg')
#drawing.savePng('test.png')