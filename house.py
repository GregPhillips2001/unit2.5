#Greg Phillips
#9/20/17
#house.py - displays a picture of a house

from ggame import * 

black = Color(0x000000,1)
white = Color(0xffffff,1)
blackOutline = LineStyle(1,black) #(pixels thick,color)

whiteRectangle = RectangleAsset(200,100,blackOutline,white) #(width,height,outline,fill)
whiteTriangle =PolygonAsset([(100,0), (0,100), (200,100)], blackOutline, white)

Sprite(whiteTriangle)
Sprite(whiteRectangle, (0,100))
App().run()
