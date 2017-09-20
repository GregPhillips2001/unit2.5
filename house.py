#Greg Phillips
#9/20/17
#house.py - displays a picture of a house

from ggame import * 

white = Color()xffffff,1)
blackOutline = LineStyle(1,black) #(pixels thick,color)

whiteRectangle = RectangleAsset(200,100,blackOutline,red) #(width,height,outline,fill)

App().run()
