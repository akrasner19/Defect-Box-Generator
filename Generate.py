import drawSvg as draw
from Process import DotGenerator
import random as rand

#declare process wide, constant variables
CANVASWIDTH = 300
CANVASHEIGHT = 300
DOTCOLOR = '#000000' #can be implemented as a set to pull from
DOTRADIUS = 2 #this can also be dynamic
DOTNUMBER = 100 #add variable dotnumber as a range in future
BOXCOLOR = 'red'
BOXTHICKNESS = 4
SEEDLIST = ["testingseed1",
	"testingseed2",
	"testingseed3",
	"weirdseed"]

for SEED in SEEDLIST:
	drawing = draw.Drawing(CANVASWIDTH,CANVASHEIGHT,origin='center')

	rand.seed(SEED)

	dg = DotGenerator(DOTRADIUS,CANVASWIDTH,CANVASHEIGHT,DOTCOLOR,BOXCOLOR,BOXTHICKNESS)

	for i in range(DOTNUMBER):
		drawing.append(dg.generateDot())

	drawing.setPixelScale(1)
	drawing.saveSvg(SEED + "_defect.svg")

	drawing = draw.Drawing(CANVASWIDTH,CANVASHEIGHT,origin='center')
	
	drawing.append(dg.generateBoundingBox())

	drawing.setPixelScale(1)
	drawing.saveSvg(SEED + "_box.svg")
	#drawing.savePng('test.png')