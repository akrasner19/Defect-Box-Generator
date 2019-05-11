import numpy as np
import drawSvg as draw
import random as rand

def cart2pol(x, y):
	rho = np.sqrt(x**2 + y**2)
	phi = np.arctan2(y, x)
	return(rho, phi)

def pol2cart(rho, phi):
	x = rho * np.cos(phi)
	y = rho * np.sin(phi)
	return(x, y)

class DotGenerator:
	
	def __init__(self, dotRadius, canvasWidth, canvasHeight, dotColor, boxColor, boxThickness):
		self.dotRadius = dotRadius
		self.canvasWidth = canvasWidth
		self.canvasHeight = canvasHeight
		self.canvasLeft = canvasWidth/(-2)
		self.canvasRight = canvasWidth/(2)
		self.canvasTop = canvasHeight/(2)
		self.canvasBottom = canvasHeight/(-2)
		self.leftBound = None
		self.rightBound = None
		self.topBound = None
		self.bottomBound = None
		self.dotColor = dotColor
		self.boxColor = boxColor
		self.boxThickness = boxThickness

	def adjustBounds(self,x,y):
		if self.leftBound is None:
			self.leftBound = x
		if self.rightBound is None:
			self.rightBound = x
		if self.topBound is None:
			self.topBound = y
		if self.bottomBound is None:
			self.bottomBound = y

		if self.leftBound > x-(self.boxThickness/2):
			self.leftBound = x-(self.boxThickness/2)
		if self.rightBound < x+(self.boxThickness/2):
			self.rightBound = x+(self.boxThickness/2)
		if self.topBound < y+(self.boxThickness/2):
			self.topBound = y+(self.boxThickness/2)
		if self.bottomBound > y-(self.boxThickness/2):
			self.bottomBound = y-(self.boxThickness/2)

	def generateDot(self):
		#determine angle
		angle = 2 * np.pi * rand.random()

		#determine the distance from the center
		#distance must place the whole dot within the canvas
		#should have greater likelihood to place near the center as controlled by some kind of parameter
		multiplier = abs(rand.gauss(0,0.2))
		if multiplier > 1:
			multiplier = 1
		magnitude = multiplier * ((self.canvasWidth/2)-self.dotRadius-(self.boxThickness/2))

		#convert to cartesian
		(cx,cy) = pol2cart(magnitude,angle)

		#adjust bounds
		self.adjustBounds(cx,cy)

		#create circle
		return draw.Circle(cx, cy, self.dotRadius, fill=self.dotColor, stroke_width=0)

	def generateBoundingBox(self):
		boxWidth = self.rightBound - self.leftBound + self.boxThickness
		boxHeight = self.topBound - self.bottomBound + self.boxThickness

		return draw.Rectangle(self.leftBound-(self.boxThickness/2),
			self.bottomBound-(self.boxThickness/2),
			boxWidth,
			boxHeight,
			fill_opacity=0,stroke_width=self.boxThickness, stroke=self.boxColor)