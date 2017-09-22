#Greg Phillips
#9/20/17
#germanFlag.py - german flag

from ggame import * 

red = Color(0xff0000,1)
black = Color(0x000000,1)
yellow = Color(0xffff00,1)

blackOutline = LineStyle(1,black) #(pixels thick,color)

blackRectangle = RectangleAsset(100,20,blackOutline,black)
redRectangle = RectangleAsset(100,20,blackOutline,red)
yellowRectangle = RectangleAsset(100,20,blackOutline,yellow)

Sprite(blackRectangle)
Sprite(redRectangle, (0,20))
Sprite(yellowRectangle, (0,40))

App().run()
