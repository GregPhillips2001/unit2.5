#Greg Phillips
#9/20/17
#germanFlag.py - german flag

from ggame import * 

red = Color(0xff0000,1)
black = Color(0x000000,1)
yellow = Color(0xffff00,1)

blackOutline = LineStyle(1,black) #(pixels thick,color)

blackRectangle = RectangleAsset(800,160,blackOutline,black)
redRectangle = RectangleAsset(800,160,blackOutline,red)
yellowRectangle = RectangleAsset(800,160,blackOutline,yellow)

Sprite(blackRectangle)
Sprite(redRectangle, (0,160))
Sprite(yellowRectangle, (0,320))

App().run()
